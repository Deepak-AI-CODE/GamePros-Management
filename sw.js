// Tournament Manager - Service Worker
// Enables offline use and installability

const CACHE_NAME = "tournament-manager-v2";
const ASSETS = [
  "/GamePros-Management/",
  "/GamePros-Management/index.html",
  "/GamePros-Management/manifest.json",
  "/GamePros-Management/icons/icon-192.png"
];

// Install: cache all assets
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

// Activate: clean old caches
self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch: serve from cache, fallback to network
self.addEventListener("fetch", event => {
  event.respondWith(
    fetch(event.request)
      .then(response => {
        const clone = response.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        return response;
      })
      .catch(() => {
        return caches.match(event.request).then(res => {
          return res || caches.match("/GamePros-Management/index.html");
        });
      })
  );
});

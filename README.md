# 🏏 Tournament Manager — Complete Setup Guide

## What This App Is
A Progressive Web App (PWA) that works like a native app on both Android and iOS.
No app store needed. Completely FREE to host and use.

---

## 📁 File Structure
```
tournament-app/
├── index.html          ← Main app (all code inside)
├── manifest.json       ← Makes it installable as an app
├── sw.js               ← Service worker (offline support)
├── generate_icons.py   ← Run once to create icons
└── icons/
    ├── icon-72.png
    ├── icon-96.png
    ├── icon-128.png
    ├── icon-144.png
    ├── icon-152.png
    ├── icon-192.png
    ├── icon-384.png
    └── icon-512.png
```

---

## 🚀 FREE Hosting Options (Choose One)

### Option 1: GitHub Pages (RECOMMENDED — Easiest)
**Cost: Free forever**

1. Create account at https://github.com
2. Click "New Repository" → name it `tournament-app` → Public → Create
3. Upload all files (drag & drop on GitHub)
4. Go to Settings → Pages → Source: Deploy from branch → main → / (root) → Save
5. Your app URL: `https://YOUR-USERNAME.github.io/tournament-app`
6. Done! Share this URL with everyone.

### Option 2: Netlify (Easiest drag & drop)
**Cost: Free forever**

1. Go to https://netlify.com → Sign up free
2. Drag your entire `tournament-app/` folder onto the dashboard
3. Gets a URL like: `https://random-name.netlify.app`
4. Optional: Set custom domain name in settings

### Option 3: Vercel
**Cost: Free forever**

1. Go to https://vercel.com → Sign up free
2. Click "Add New Project" → Upload folder
3. Gets URL like: `https://tournament-app.vercel.app`

### Option 4: Cloudflare Pages
**Cost: Free forever**

1. Go to https://pages.cloudflare.com
2. Connect GitHub repo or upload directly
3. Very fast, global CDN included free

---

## 📱 Installing on Android Phone

1. Open Chrome browser on Android
2. Go to your hosted URL (e.g. `https://yourname.github.io/tournament-app`)
3. Chrome shows a banner: **"Add Tournament Manager to Home Screen"** → Tap it
4. OR: Tap the 3-dot menu (⋮) → "Add to Home Screen" → "Install"
5. App icon appears on home screen — works like a native app!
6. Opens fullscreen, no browser bar, works offline too

---

## 🍎 Installing on iPhone / iPad (iOS)

1. Open **Safari** browser (must be Safari, not Chrome)
2. Go to your hosted URL
3. Tap the **Share button** (□ with arrow at bottom)
4. Scroll down → Tap **"Add to Home Screen"**
5. Give it a name → Tap **"Add"**
6. App icon appears on home screen!

> ⚠️ iOS Note: Always use Safari for installation. Chrome on iOS doesn't support PWA install.

---

## 💬 WhatsApp Integration Notes

The app opens `wa.me` links which:
- On mobile: Opens WhatsApp directly to the captain's chat with a pre-filled message
- On desktop: Opens WhatsApp Web
- Captain just needs to tap SEND — message is already typed

**Pre-filled message includes:**
- Tournament name
- Match date & ground
- Teams & scores
- Winner
- Amount to pay

---

## 📊 Excel Export

The "Download CSV" button exports all matches to a `.csv` file.
Open it in Microsoft Excel or Google Sheets.

**Columns exported:**
ID, Date, Tournament, Ground, Type, Team A, Team B,
Score A, Score B, Winner, Amount/Team, Total Amount, Status,
Captain A Phone, Captain B Phone

---

## 💾 Data Storage

All data is stored in your phone's browser `localStorage`.
- No server, no database needed
- Data stays on the device
- To back up: use the CSV export regularly

> To share data between multiple phones, use the CSV export and re-import manually,
> or consider upgrading to a free Firebase backend (ask for that version if needed).

---

## 🔧 Steps to Go Live (Quick Start)

```
Step 1: Generate icons
  python3 generate_icons.py

Step 2: Upload to GitHub Pages (free)
  - Create GitHub account
  - New repo → upload all files
  - Enable GitHub Pages in settings

Step 3: Share URL with your team
  - Everyone installs it from their phone via Safari/Chrome

Step 4: Start adding matches!
```

---

## 📞 Support
Built with HTML + CSS + JavaScript. No frameworks, no dependencies.
Works 100% offline after first load.

const CACHE_NAME = 'kdoryung-v2';
const STATIC_ASSETS = [
  '/k-doryung/',
  '/k-doryung/index.html',
  '/k-doryung/icon-192.png',
  '/k-doryung/icon-512.png',
  '/k-doryung/marker-doryung.png',
  '/k-doryung/marker-baekgu.png',
  '/k-doryung/manifest.json',
  '/k-doryung/cheap-data.json',
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(STATIC_ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(res => {
        if (res.ok && new URL(e.request.url).origin === self.location.origin) {
          const clone = res.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(e.request, clone));
        }
        return res;
      });
    })
  );
});

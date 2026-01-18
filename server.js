const http = require('http');
const fs = require('fs');
const path = require('path');
const https = require('https');

const PORT = 8080;
const ROOT = __dirname;

const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'text/javascript',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.json': 'application/json',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff'
};

const server = http.createServer((req, res) => {
  console.log(`Request: ${req.url}`);

  // CORS Proxy for webassets.linear.app
  if (req.url.startsWith('/proxy/webassets/')) {
    const upstreamPath = req.url.replace('/proxy/webassets/', '/');
    const upstreamUrl = 'https://webassets.linear.app' + upstreamPath;

    console.log(`Proxying to: ${upstreamUrl}`);

    https.get(upstreamUrl, (proxyRes) => {
      // Forward status and headers
      res.writeHead(proxyRes.statusCode, proxyRes.headers);
      proxyRes.pipe(res);
    }).on('error', (e) => {
      console.error(`Proxy error: ${e.message}`);
      res.writeHead(500);
      res.end(`Proxy error: ${e.message}`);
    });
    return;
  }

  let reqPath = req.url.split('?')[0];
  if (reqPath === '/') reqPath = '/index.html';

  // Redirect /homepage to serve index.html with AI
  if (reqPath === '/homepage') reqPath = '/index.html';

  // Prevent directory travel
  const safePath = path.normalize(reqPath).replace(/^(\.\.[\/\\])+/, '');
  let filePath = path.join(ROOT, safePath);

  // Check if file exists direclty
  fs.stat(filePath, (err, stats) => {
    if (err) {
      // If not found, check if it's a directory and has index.html ? 
      // Or maybe it's just missing
      res.writeHead(404);
      res.end('404 Not Found');
      return;
    }

    if (stats.isDirectory()) {
      // Try index.html inside directory
      const indexPath = path.join(filePath, 'index.html');
      fs.stat(indexPath, (err, indexStats) => {
        if (!err && indexStats.isFile()) {
          serveFile(indexPath, 'text/html', res);
        } else {
          // Directory listing or 403? let's 404 for now
          res.writeHead(404);
          res.end('404 Not Found (Directory without index)');
        }
      });
      return;
    }

    // It is a file
    const ext = path.extname(filePath).toLowerCase();

    // Logic for extensions
    let contentType = MIME_TYPES[ext] || 'application/octet-stream';

    // If no extension, assume it IS an html file (as seen in the directory listing: 'homepage', 'login')
    if (ext === '') {
      contentType = 'text/html';
    }

    serveFile(filePath, contentType, res);
  });
});

function serveFile(filePath, contentType, res) {
  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(500);
      res.end('Server Error');
      return;
    }
    res.writeHead(200, { 'Content-Type': contentType });
    res.end(data);
  });
}

server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}/`);
});

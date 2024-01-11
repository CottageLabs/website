server {
    listen 80;
    listen [::]:80;
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name next.cottagelabs.com;

    root /var/www/next.cottagelabs.com/output;
    index index.html;

    # Block .git and other hidden files (except .well-known for SSL)
    location ~ /\.(?!well-known).* {
        deny all;
        access_log off;
        log_not_found off;
    }

    location / {
        try_files $uri $uri/ /src/$uri /src/$uri/ =404;
    }

    access_log /var/log/nginx/next.access.log;
    error_log /var/log/nginx/next.error.log;

    ssl_certificate /etc/letsencrypt/live/next.cottagelabs.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/next.cottagelabs.com/privkey.pem;

    if ($scheme != "https") {
        return 301 https://$host$request_uri;
    }
}

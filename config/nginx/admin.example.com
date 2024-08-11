server {
    listen 80;
    server_name admin.example.com www.admin.example.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name admin.example.com www.admin.example.com;
    ssl_certificate /home/main/rapidforge/config/ssl/server_combined_ssl.cer;
    ssl_certificate_key /home/main/rapidforge/config/ssl/server_ssl.key;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        error_log /var/log/nginx/error.log debug;
    }
}
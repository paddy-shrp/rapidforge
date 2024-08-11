sudo cp config/nginx/example.com /etc/nginx/sites-available
sudo cp config/nginx/admin.example.com /etc/nginx/sites-available
sudo nginx -t
sudo systemctl restart nginx





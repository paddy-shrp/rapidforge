sudo cp config/nginx/example.com /etc/nginx/sites-available
sudo cp config/nginx/admin.example.com /etc/nginx/sites-available
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/admin.example.com /etc/nginx/sites-enabled/
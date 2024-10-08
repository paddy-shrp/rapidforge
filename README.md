# Build a Startup in One Week - RapidForge

RapidForge is a streamlined and scalable backend framework designed to help startups quickly establish and deploy a robust backend infrastructure. Whether you’re launching a new product or iterating on an existing one, RapidForge provides the essential components to get your backend up and running with minimal effort.

## Features

RapidForge includes an intuitive Admin Center for managing backend operations, with automated server performance logging to monitor system health in real time. The framework’s modular core architecture ensures easy maintenance and scalability, while pre-configured NGINX and SSL setups guarantee secure and optimized performance.

An internal API handles efficient routing within the infrastructure, and new services can be easily introduced in the file structure and managed through the Admin Center. For critical error notifications, Pushover integration (account required) provides real-time alerts directly to your phone.

### Overview

![RapidForge](https://github.com/user-attachments/assets/a4eea0b4-fb2d-4507-bd00-a3d37220e8db)

# Installation

## Setup the repo
1. Create a private repo that should inherit rapidforge
2. Clone the repo to your local machine
3. Add the original rapidforge repo as an remote upstream
```bash 
git remote add upstream https://github.com/paddy-shrp/rapidforge.git
```
4. [REPEAT ON UPGRADE] Merge the upstream with the origin branch
```bash
git fetch upstream
git merge upstream/main
```

## Setup the Python Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e rapidforge_core
```
__Run the "startup.py" File__

## Setup the Modules

### MongoDB
1. Create a MongoDB-Account
2. Create a free database
3. Copy the URI and Password into the __settings.json__

### Pushover
1. Create a Pushover-Account
2. Create a Pushover-Application
3. Copy the UserID and Application Token into the __settings.json__
4. Download the Pushover-App on IOS or Android
5. Log in using your Account and Register the Device

## Setup the Services

### NGINX

1. Run the ```config/nginx/setup.sh``` File
2. Create domain sites in the config/nginx/sites Folder
3. To use the SSL Certificates of your domain follow the Instructions in the SSL Folder
4. Link SSL with NGINX
5. Run the ```config/nginx/patch.sh``` File

### Controller

```bash
cd hub/controller
npm install
```

For Authentication using Auth0
1. Create an Auth0-Account (https://auth0.com/de/signup)
2. Create an Auth0-Application
3. Copy the required settings in the __config.json__ in the hub/controller folder
4. Add Users using Auth0 and Test the Controller using Authentication by change the state in the __config.json__ to "PRODUCTION"

# File Structure

```
rapidforge/
├── config/
│   ├── nginx/
│   │   ├── admin.example.com
│   │   ├── example.com
│   │   └── setup.sh
│   └── ssl
├── core/
│   ├── modules
│   └── utils
├── hub/
│   ├── controller
│   ├── dlogger
│   └── internal
├── systemd/
│   ├── controller/
│   │   └── forge-controller.service
│   ├── dlogger/
│   │   └── forge-dlogger.service
│   └── internal/
│       └── forge-internal.service
└── startup.py
```

# Additional

### Update Requirements (Optional)
```bash
.venv/bin/pip freeze > requirements.txt
```

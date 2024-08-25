# Build a Startup in One Week? - RapidForge

RapidForge is a streamlined and scalable backend framework designed to help startups quickly establish and deploy a robust backend infrastructure. Whether you’re launching a new product or iterating on an existing one, RapidForge provides the essential components to get your backend up and running with minimal effort.

## Features

RapidForge includes an intuitive Admin Center for managing backend operations, with automated server performance logging to monitor system health in real time. The framework’s modular core architecture ensures easy maintenance and scalability, while pre-configured NGINX and SSL setups guarantee secure and optimized performance.

An internal API handles efficient routing within the infrastructure, and new services can be easily introduced in the file structure and managed through the Admin Center. For critical error notifications, Pushover integration (account required) provides real-time alerts directly to your phone.

### How your will server look like


# Installation

## Repository

Fork the repistory and clone it

```bash
git clone {repo_link.git}
git checkout -b startup_branch
cd rapidforge
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


# Additional

### Update Requirements (Optional)
```bash
.venv/bin/pip freeze > requirements.txt
```
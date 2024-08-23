# Setup the Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e rapidforge_core
```
### Run the "startup.py" File

# Additional

### Update Requirements
```bash
.venv/bin/pip freeze > requirements.txt
```
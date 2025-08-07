cd /app/tester

node index.js

echo "Activating venv"
source /venv/env/bin/activate && python3 tester.py

cd /app/proxy_server

source /venv/env/bin/activate && python3 app.py

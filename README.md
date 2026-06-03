Monitoring Dashboard

Features

- View monitoring logs
- Filter logs by candidate name
- Filter logs by violation type
- FastAPI backend API
- HTML/JavaScript frontend dashboard

Project Structure

monitoring-dashboard/

├── backend/

│ └── main.py

├── frontend/

│ └── index.html

├── requirements.txt

├── sample_logs.json

└── README.md

Installation

pip install -r requirements.txt

Run Backend

cd backend
uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

Open Frontend

Open:

frontend/index.html

in a browser.

API Endpoints

GET /

Returns API status.

GET /logs

Returns monitoring logs.

Handling Large Log Volumes

For 1000+ logs, the dashboard can be improved using:

- Pagination
- Server-side filtering
- Database storage
- Lazy loading

to improve performance.

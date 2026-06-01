from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logs = [
    {
        "candidate": "Rahul",
        "violation": "Tab Switch",
        "timestamp": "2026-05-31 10:15"
    },
    {
        "candidate": "Priya",
        "violation": "Multiple Faces",
        "timestamp": "2026-05-31 10:20"
    }
]

@app.get("/")
def home():
    return {"message": "Monitoring Dashboard API Running"}

@app.get("/logs")
def get_logs():
    return logs

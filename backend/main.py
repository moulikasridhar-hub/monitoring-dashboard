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
    },
    {"candidate": "Rahul", "violation": "Tab Switch", "timestamp": "2026-05-31 10:15"},
    {"candidate": "Priya", "violation": "Multiple Faces", "timestamp": "2026-05-31 10:20"},
    {"candidate": "Amit", "violation": "No Face Detected", "timestamp": "2026-05-31 10:25"},
    {"candidate": "Sneha", "violation": "Tab Switch", "timestamp": "2026-05-31 10:30"},
    {"candidate": "Arjun", "violation": "Multiple Faces", "timestamp": "2026-05-31 10:35"},
    {"candidate": "Neha", "violation": "No Face Detected", "timestamp": "2026-05-31 10:40"},
    {"candidate": "Rohit", "violation": "Tab Switch", "timestamp": "2026-05-31 10:45"},
    {"candidate": "Ananya", "violation": "Multiple Faces", "timestamp": "2026-05-31 10:50"},
    {"candidate": "Vikram", "violation": "No Face Detected", "timestamp": "2026-05-31 10:55"},
    {"candidate": "Pooja", "violation": "Tab Switch", "timestamp": "2026-05-31 11:00"},
    {"candidate": "Karan", "violation": "Multiple Faces", "timestamp": "2026-05-31 11:05"},
    {"candidate": "Meera", "violation": "No Face Detected", "timestamp": "2026-05-31 11:10"}
]
    
    

@app.get("/")
def home():
    return {"message": "Monitoring Dashboard API Running"}

@app.get("/logs")
def get_logs():
    return logs

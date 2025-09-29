from fastapi import FastAPI
from pydantic import BaseModel # Used for defining data structures

# Initialize the FastAPI application
app = FastAPI(
    title="AI-Powered Train Traffic Control API",
    description="API for real-time train status, optimization, and conflict resolution."
)

# --- 1. Define Data Models (for Request/Response) ---
# This schema represents a single train's status report
class TrainStatus(BaseModel):
    train_id: str
    current_location: str # e.g., "Station A", "Milepost 105"
    speed_kmh: float
    status: str # e.g., "On Time", "Delayed", "Idle"
    delay_minutes: int = 0 # Default value for no delay

# This schema will be used to respond with an optimization decision
class OptimizationDecision(BaseModel):
    train_id: str
    action: str # e.g., "Maintain Speed", "Reduce Speed", "Hold at Signal"
    reason: str
    estimated_impact_minutes: float


# --- 2. Define API Endpoints (Routes) ---

# Root Endpoint: Simple health check
@app.get("/")
def read_root():
    return {"message": "System is operational! API Version 1.0"}

# Endpoint to report a train's real-time status (POST)
@app.post("/api/v1/train_status")
def receive_train_status(status_report: TrainStatus):
    """
    Receives real-time status updates from a specific train.
    This is where the input data for the AI model will arrive.
    """
    # Placeholder for saving to database and feeding to AI/ML model
    print(f"Received status for Train {status_report.train_id}: {status_report.status}")
    
    # In the future, this will trigger the AI model inference
    # For now, just return a confirmation
    return {"message": "Status received successfully", "train_id": status_report.train_id}

# Endpoint to request an optimization decision (GET)
# The AI/ML logic will eventually be placed here
@app.get("/api/v1/optimize/{train_id}", response_model=OptimizationDecision)
def get_optimization_decision(train_id: str):
    """
    Requests a real-time traffic control decision from the AI model
    for a specified train.
    """
    # !!! Placeholder for AI/ML Logic !!!
    # The complex AI-ML model will run here to determine the best action.
    
    # Simple placeholder logic:
    if train_id == "T-101":
        action = "Hold at Signal 12"
        reason = "Conflict detected with Express T-205"
        impact = 5.0
    else:
        action = "Maintain Speed"
        reason = "Route is clear and on schedule"
        impact = 0.0
        
    return OptimizationDecision(
        train_id=train_id,
        action=action,
        reason=reason,
        estimated_impact_minutes=impact
    )
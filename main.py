from fastapi import FastAPI

app = FastAPI(title="Asset Appraisal Agent")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run")
def run(payload: dict):
    asset = payload.get("asset", "property")
    base_value = 100000
    adjustment = 1.1 if "villa" in asset.lower() else 0.9 if "land" in asset.lower() else 1.0
    est_value = base_value * adjustment
    confidence = 0.9
    return {"estimated_value": est_value, "confidence": confidence}

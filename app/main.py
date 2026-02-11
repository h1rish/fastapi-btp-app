from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI running on SAP BTP Cloud Foundry 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

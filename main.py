from fastapi import FastAPI

app = FastAPI()

@app.get("/shipment")
def get_shipment():
    return {
        "message": "Xin chào!",
        "status": "intransit"    
    }
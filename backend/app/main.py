from fastapi import FastAPI 

app = FastAPI(title="ServiceOps Core")

@app.get("/health")
def health():
    return {"Status": "Ok"}
from fastapi import FastAPI
from routes import auth
from database.mongodb import MongoDB
import uvicorn
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await MongoDB.connect_to_mongo()
    print("Server started")

@app.on_event("shutdown")
async def shutdown_event():
    await MongoDB.close_mongo_connection()
    print("Server closed")

@app.get("/")
def test() :
    return "Working"

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
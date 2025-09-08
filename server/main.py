
# Imports the FastAPI class to create the server, and HTTPException to handle errors that we will return to the user, and UploadFile, File, Form – allow sending files and data in a form.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.user_router import router as user_router
from api.production_router import router as production_router

# Creating an instance of the server.
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router, prefix="/user")
app.include_router(production_router,prefix="/production")

@app.get("/")
def root():
    return {"message": "API is running"}


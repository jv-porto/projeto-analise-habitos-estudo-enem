# importing libraries and functions
import uvicorn
from fastapi import FastAPI
from routes import routes


# instantiating the FastAPI application
app = FastAPI()

# connecting the routers to the main application
app.include_router(routes.router)


# running the application
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

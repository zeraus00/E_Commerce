from fastapi import FastAPI
import uvicorn

from ecm.routes.auth_routes import auth_router

app = FastAPI()



app.include_router(auth_router)

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)
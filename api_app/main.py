from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import auth,predict,generate_plan



app = FastAPI(title="Employee Retention IA Plateforme ")


# Création des tables
Base.metadata.create_all(bind=engine)

#  Routes
app.include_router(auth.router)
app.include_router(predict.router)
app.include_router(generate_plan.router)


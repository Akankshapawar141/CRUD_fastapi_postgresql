from fastapi import FastAPI
from app.product.endpoints import product_route
from app.partner.endpoints import partner_route
from app.micro_svc.endpoints import micro_svc_route
from app.partner import models
from app.database import engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

print("postgreSQL connected")



app.include_router(partner_route,tags=["PARTNERS"])
app.include_router(product_route,tags=["PRODUCTS"])
app.include_router(micro_svc_route,tags=["MICRO_SVC"])

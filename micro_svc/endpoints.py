import json
import uuid

from fastapi import APIRouter
from fastapi import UploadFile,File
from fastapi import status,HTTPException
from app.micro_svc.models import Micro_SVC_schema
from typing import List
from app.database import SessionLocal
from app.micro_svc import models
from app.product.models import Products
import pandas as pd


micro_svc_route = APIRouter()

db = SessionLocal()

#Upload CSV file
@micro_svc_route.post(
    "/Upload_file"
)
def upload_file(product_id:str , Micro_svc : Micro_SVC_schema ,csv_file: UploadFile = File(...)):
    df = pd.read_csv(csv_file.file)
    request_data = df.to_dict(orient="records")
    return request_data


#Get All Micro-services Data
@micro_svc_route.get(
    "/partners/products/{products_id}/micro_svc",
    response_description="",
    response_model=List[Micro_SVC_schema],
    status_code=status.HTTP_200_OK
)
def Get_All_Micro_Svc(limit: int = 100):

    # if limit is less than 0 raise exception
    if limit > 0:
        posts = db.query(models.Micro_SVC).limit(limit).all()
        return posts
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Data Not found"
    )


#Create New Micro-service
@micro_svc_route.post(
    "/partners/products/micro_svc",
    response_description="Created new Micor-Service",
    response_model=Micro_SVC_schema,
    status_code=status.HTTP_201_CREATED
)
def Create_Micro_Svc(product_id: str, micro_svc: Micro_SVC_schema):

    # if product_id exists
    query_data = db.query(Products).filter(Products.id == product_id).first()

    if query_data is not None:
        new_micro_svc = models.Micro_SVC(
            product_id=product_id,
            name=micro_svc.name,
            shape=micro_svc.shape,
            size=micro_svc.size,
            bust=micro_svc.bust,
            waist=micro_svc.waist,
            hip=micro_svc.hip,
        )

        db.add(new_micro_svc)
        db.commit()

        return micro_svc

    raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="product_id does not exists ."
        )


#Get Micro-service by ID
@micro_svc_route.get(
    "/partners/products/micro_svc/{_id}",
    response_description="Get data by ID",
    response_model=Micro_SVC_schema,
    status_code=status.HTTP_200_OK
)
def Get_Micro_Svc_By_Id(id: str):

    if(posts := db.query(models.Micro_SVC).filter(models.Micro_SVC.id == id).first()) is not None:
        return posts
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{id} ID not found."
    )


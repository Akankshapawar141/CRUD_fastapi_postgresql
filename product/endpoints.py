from fastapi import APIRouter
from fastapi import status, HTTPException
from app.database import SessionLocal
from app.product import models
from app.product.models import Product_schema
from typing import List
from app.partner.models import Partners


product_route = APIRouter()

db = SessionLocal()


#Get All Prodyucts Data
@product_route.get(
    "/partners/products/",
    response_description="Get all data of Products",
    response_model=List[Product_schema],
    status_code=status.HTTP_200_OK
)
def Get_All_Products(limit: int = 100):
    # if limit is less than 0 raise exception
    if limit > 0:
        posts = db.query(models.Products).limit(limit).all()
        return posts
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Data Not found"
    )


#Create New Products
@product_route.post(
    "/partners/{partner_id}/products/",
    response_description="Created new Products ",
    response_model=Product_schema,
    status_code=status.HTTP_201_CREATED
)
def Create_Product(partner_id: str, products: Product_schema):

    # if partner_id exists
    query_data = db.query(Partners).filter(Partners.id == partner_id).first()

    if query_data is not None:
        new_product = models.Products(
            partner_id=partner_id,
            name=products.name,
            code=products.code,
            URL=products.URL,
            handle=products.handle
        )

        db.add(new_product)
        db.commit()

        return products

    raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="partner_id does not exists ."
        )


#Get Product by ID
@product_route.get(
    "/partners/products/{product_id}",
    response_description="Get data by Product Id",
    response_model=Product_schema,
    status_code=status.HTTP_200_OK
)
def Get_Products_By_Id(product_id:str):
    if (posts := db.query(models.Products).filter(models.Products.id == product_id).first()) is not None:
        return posts
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{id} not found."
    )

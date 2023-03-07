from fastapi import  HTTPException, status, APIRouter
from passlib.context import CryptContext
from app.database import SessionLocal
from typing import List
from app.partner import models
from app.partner.models import Partner_schema


partner_route = APIRouter()

db = SessionLocal()

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

def get_password_hash(password):
    return pwd_context.hash(password)

#Get All Partner Data
@partner_route.get(
    "/partners/",
    response_description="Get all Partners Data ",
    response_model=List[Partner_schema],
    status_code=status.HTTP_200_OK
)
def Get_All_Partners(limit: int = 100):
    if limit > 0:
        posts = db.query(models.Partners).limit(limit).all()
        return posts
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Data Not found"
    )

#Create New Partner
@partner_route.post(
    "/partners/",
    response_description="New Partner Created ",
    status_code=status.HTTP_201_CREATED
)
def Create_Partner(Partners :Partner_schema ):
    # if partner with same email-ID exists
    find_email = db.query(models.Partners).filter(models.Partners.email == Partners.email).first()

    if find_email is not None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Email ID already exists .Please try with another Email ID."
        )
    else:
        new_partner = models.Partners(
            name=Partners.name,
            code=Partners.code,
            url=Partners.url,
            email=Partners.email,
            password=get_password_hash(Partners.password)
        )

        db.add(new_partner)
        db.commit()

        return Partners


#Get Partner by ID
@partner_route.get(
    "/partners/{_id}",
    response_description="Get data by Partner Id",
    response_model=Partner_schema,
    status_code=status.HTTP_200_OK
)
def Get_Partner_By_Id(partner_id:str):
    if (posts := db.query(models.Partners).filter(models.Partners.id == partner_id).first()) is not None:
        return posts
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{id} not found."
    )



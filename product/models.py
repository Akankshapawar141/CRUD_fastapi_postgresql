from pydantic import BaseModel, Field
import uuid
from app.database import Base
from sqlalchemy import Column,String



class Products(Base):
    __tablename__ = "PRODUCTS"
    id = Column(String, primary_key=True, nullable=False, default=uuid.uuid4)
    partner_id = Column(String,nullable=False, default=uuid.uuid4)
    name = Column(String(50),nullable=False)
    code = Column(String(50),nullable=False)
    handle = Column(String(50),nullable=False)
    URL = Column(String(100),nullable=False)


class OurBasemodel(BaseModel):
  class Config:
        orm_mode = True


class Product_schema(OurBasemodel):
    id: str = Field(default_factory=uuid.uuid4, alias="id")
    partner_id: str = Field(default_factory=uuid.uuid4)
    name: str = Field(...)
    code: str = Field(...)
    handle: str = Field(...)
    URL: str = Field(...)

    class Config:
        allow_population_field_by_name = True
        schema_extra = {
            "example": {
                "name": "Low Of Motion",
                "code": "LOM",
                "handle": "xyz",
                "URL": "partner/product/",
        }
    }

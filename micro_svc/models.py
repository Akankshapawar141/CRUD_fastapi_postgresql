import uuid
from pydantic import BaseModel,Field
from app.database import Base
from sqlalchemy import Column,String,FLOAT



class Micro_SVC(Base):
    __tablename__ = "MICRO_SVC"
    id = Column(String, primary_key=True, nullable=False, default=uuid.uuid4)
    product_id = Column(String,nullable=False, default=uuid.uuid4)
    name = Column(String(50),nullable=False)
    shape = Column(String(50),nullable=False)
    size = Column(String(50),nullable=False)
    bust = Column(FLOAT,nullable=False)
    waist = Column(FLOAT,nullable=False)
    hip = Column(FLOAT,nullable=False)


class OurBasemodel(BaseModel):
  class Config:
        orm_mode = True


class Micro_SVC_schema(OurBasemodel):
    id : str =Field(default_factory=uuid.uuid4,alias="id")
    product_id: str = Field(default_factory=uuid.uuid4)
    name: str = Field(...)
    shape: str = Field(...)
    size:str = Field(...)
    bust: float = Field(...)
    waist: float = Field(...)
    hip: float = Field(...)

    class Config:
        allow_population_field_by_name = True
        schema_extra = {
            "example":{
                "name": "Merry",
                "shape": "P",
                "size": "M",
                "bust": "30",
                "waist": "30",
                "hip":"30",
            }
        }
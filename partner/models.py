from pydantic import BaseModel, Field
import uuid
from app.database import Base
from sqlalchemy import Column,String,VARCHAR


class Partners(Base):
    __tablename__ = "PARTNERS"
    id = Column(String, primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String(50),nullable=False)
    code = Column(String(50),nullable=False)
    url = Column(String(100),nullable=False)
    email = Column(VARCHAR(100),nullable=False)
    password = Column(String(255),nullable=False)


class OurBasemodel(BaseModel):
  class Config:
        orm_mode = True


class Partner_schema(OurBasemodel):
    id : str =Field(default_factory=uuid.uuid4,alias="id")
    name: str = Field(...)
    code: str = Field(...)
    url: str = Field(...)
    email: str = Field(...)
    password : str = Field(...)

    class Config:
        allow_population_field_by_name =True
        schema_extra = {
            "example": {
                "name": "Low of Motion",
                "code": "LOM",
                "url": "/student/",
                "email": "hello@gmail.com",
                "password": "password",
            }
        }







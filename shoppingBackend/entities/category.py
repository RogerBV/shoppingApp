from .common.base import Base
from .common.baseEntity import BaseEntity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Category(Base, BaseEntity):
    __tablename__ = "Category"
    name = Column(String(50), nullable=False)
    
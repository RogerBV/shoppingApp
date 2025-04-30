from sqlalchemy import Column, String, Numeric, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .common.base import Base
from .common.baseEntity import BaseEntity
from models.product.registeredProductModel import RegisteredProductModel

class Product(Base, BaseEntity):
    __tablename__="Product"
    name = Column(String(50), nullable=False)
    price = Column(Numeric(18,2), nullable=False)
    categoryId = Column(Integer, ForeignKey('Category.id'), nullable=False)
    category = relationship('Category', backref= 'products', lazy='joined')
    
    def getRegisteredProductModel(self) -> RegisteredProductModel:
        return RegisteredProductModel(
            id=self.id,
            name=self.name,
            price = self.price,
            categoryId=self.category.id,
            categoryName=self.category.name,
            status=1
        )
    
    
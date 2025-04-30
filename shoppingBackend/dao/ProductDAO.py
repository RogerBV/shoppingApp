from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from entities.common.config import DATABASE_URI
from entities.product import Product
from models.product.newProductModel import NewProductModel
from models.product.registeredProductModel import RegisteredProductModel

class ProductDAO():
    async def getProducts(self) -> list[RegisteredProductModel]:
        engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        products = session.query(Product).options(joinedload(Product.category)).all()
        
        result = []
        
        for product in products:
            result.append(
                product.getRegisteredProductModel()
            )
        
        session.close()
        return result
    
    async def insertProduct(self, newProductModel: NewProductModel) -> RegisteredProductModel:
        engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        objProduct = Product()
        objProduct.name = newProductModel.name
        objProduct.price = newProductModel.price
        objProduct.categoryId = newProductModel.categoryId
        session.add(objProduct)
        session.commit()
        session.refresh(objProduct)
        
        session.close()
        return objProduct.getRegisteredProductModel()
        
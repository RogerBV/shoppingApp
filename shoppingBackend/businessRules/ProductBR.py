from dao.ProductDAO import ProductDAO
from models.product.newProductModel import NewProductModel
from models.product.registeredProductModel import RegisteredProductModel

class ProductBR():
    async def getProducts(self) -> list[RegisteredProductModel]:
        productDAO = ProductDAO()
        return await productDAO.getProducts()
    
    async def insertProduct(self, newProductModel: NewProductModel) -> RegisteredProductModel:
        productDAO = ProductDAO()
        return await productDAO.insertProduct(newProductModel)
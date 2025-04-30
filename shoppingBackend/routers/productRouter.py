from fastapi import APIRouter
from businessRules.ProductBR import ProductBR
from models.product.newProductModel import NewProductModel
from models.product.registeredProductModel import RegisteredProductModel

productRouter = APIRouter(
    prefix='/products',
    tags=['Products']
)

@productRouter.get('/', description='API that returns a list of products', response_description='List of Products')
async def getProducts() -> list[RegisteredProductModel]:
    productBR = ProductBR()
    return await productBR.getProducts()

@productRouter.put('/', description='API that create a new product and return this', response_description= 'created product')
async def insertProduct(newProductModel: NewProductModel):
    productBR = ProductBR()
    return await productBR.insertProduct(newProductModel)

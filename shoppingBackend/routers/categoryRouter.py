from fastapi import APIRouter
from businessRules.CategoryBR import CategoryBR
from models import RegisteredCategoryModel, NewCategoryModel, UpdateCategoryModel

categoryRouter = APIRouter(
    prefix='/categories',
    tags=["Categories"]
)

@categoryRouter.get('')
async def getCategories() -> list[RegisteredCategoryModel]:
    categoryBR = CategoryBR()
    return await categoryBR.getCategories()

@categoryRouter.get('/{categoryId}')
async def getCategoryById(categoryId: int) -> RegisteredCategoryModel:
    categoryBR = CategoryBR()
    return await categoryBR.getCategoryById(categoryId)

@categoryRouter.put('')
async def insertCategory(categoryModel: NewCategoryModel) -> RegisteredCategoryModel:
    categoryBR = CategoryBR()
    return categoryBR.insertCategory(categoryModel)

@categoryRouter.post('')
async def updateCategory(updateCategoryModel: UpdateCategoryModel) -> RegisteredCategoryModel:
    categoryBR = CategoryBR()
    return categoryBR.updateCategory(updateCategoryModel)
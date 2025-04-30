from dao.CategoryDAO import CategoryDAO
from models.newCategoryModel import NewCategoryModel
from models.registeredCategoryModel import RegisteredCategoryModel
from models.updateCategoryModel import UpdateCategoryModel

class CategoryBR():
    async def getCategories(self) -> list[RegisteredCategoryModel]:
        categoryDAO = CategoryDAO()
        return  await categoryDAO.getCategories()
    
    async def getCategoryById(self, categoryId: int) -> RegisteredCategoryModel:
        categoryDAO = CategoryDAO()
        return  await categoryDAO.getCategoryById(categoryId)
    
    async def insertCategory(self, newCategoryModel: NewCategoryModel):
        categoryDAO = CategoryDAO()
        return await categoryDAO.insertCategory(newCategoryModel)
    
    async def updateCategory(self, updateCategoryModel: UpdateCategoryModel) -> RegisteredCategoryModel:
        categoryDAO = CategoryDAO()
        return await categoryDAO.updateCategory(updateCategoryModel)
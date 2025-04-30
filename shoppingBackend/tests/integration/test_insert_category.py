import pytest
from businessRules.CategoryBR import CategoryBR
from models.newCategoryModel import NewCategoryModel

async def test_insertCategory():
    categoryName = "CATEGORY 1000"
    
    categoryBR = CategoryBR()
    result = await categoryBR.insertCategory(NewCategoryModel(name=categoryName))
    categoryId = result.id
    
    categoryFounded = await categoryBR.getCategoryById(categoryId)
    
    assert categoryFounded.id > 0
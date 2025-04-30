from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entities.common.config import DATABASE_URI
from .SQLAlchemyModels import Category
from models import NewCategoryModel, RegisteredCategoryModel

class CategoryDAO():
    async def getCategories(self):
        engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        categories = session.query(Category).all()
        session.close()
        return categories
    
    async def getCategoryById(self, categoryId: int):
        engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        category = session.query(Category).filter_by(id = categoryId).first()
        session.close()
        return category
    
    async def insertCategory(self, objCategoryModel: NewCategoryModel) -> RegisteredCategoryModel:
        engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        objCategory = None
        try:
            objCategory = Category()
            objCategory.name = objCategoryModel.name
            session.add(objCategory)
            session.commit()
            session.refresh(objCategory)
        except:
            print("Error while we are trying to insert data")
            session.rollback()
        finally:
            session.close()
        return objCategory
    
    async def updateCategory(self, objCategoryModel: RegisteredCategoryModel):
        engine = create_engine(DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            objCategory = session.query(Category).filter_by(id=objCategoryModel.id).first()
            if objCategory:
                objCategory.name = objCategoryModel.name
                session.commit()
            else:
                print("Category couldn't be found")
        except:
            session.rollback()
        finally:
            session.close()
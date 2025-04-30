from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.categoryRouter import categoryRouter
from routers.productRouter import productRouter
from middlewares.exceptionMiddleare import ExceptionMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(categoryRouter)
app.include_router(productRouter)
app.add_middleware(ExceptionMiddleware)
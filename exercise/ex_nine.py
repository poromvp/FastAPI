# Exercise 7 8 9

from fastapi import FastAPI, Path

app = FastAPI()

#a)
@app.get("/")
async def read_root():
    return {"message" : "TechMart API"}

#b)
@app.get("/products/{product_id}")
async def get_product_by_id(product_id:int = Path(..., ge=1, le=100000)):
    return {"message" : f"lấy thành công sản phẩm có mã là {product_id}"}

#c)
@app.get("/produc")
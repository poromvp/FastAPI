# Exercise 7 8 9

from fastapi import FastAPI, Path, Query

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
@app.get("/categories/{category_slug}/products")
async def get_products_by_category(category_slug:str = Path(..., min_length=3, max_length=30, regex='^[a-z0-9-]+$')):
    return {"message" : f"Danh sách sản phẩm có category id là: {category_slug}"}

#d)
@app.get("/products/")
async def get_products(keyword: str | None = Query(None, max_length=50), skip: int = Query(0, ge=0), limit: int=Query(10, le=100)):
    limit = limit + skip
    return {"message" : f"Danh sách sản phẩm từ {skip} tới {limit}"}             
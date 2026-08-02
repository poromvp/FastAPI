from fastapi import FastAPI

app = FastAPI()

product = [
    {"rau": "10 cái"},
    {"chén": "1 cái"},
    {"đồ chơi": "2 cái"},
    {"quần áo": "0 cái"}
]

@app.get("/product")
async def get_product(skip:int = 0, limit:int =20):
    return product[skip:skip+limit]

@app.get("/search") #querry params không gắn giá trị mặc định thì nghĩa là bắt buộc
async def get_search(keyword:str, is_active:bool | None = None): 
    return {"search key word" : keyword, "is_active" : is_active, "message" : f"đây là kết quả tìm kiếm cho {keyword}, trạng thái active: {is_active}"}
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
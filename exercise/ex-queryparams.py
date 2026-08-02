from fastapi import FastAPI

app = FastAPI()

product = [
    {"rau": "10 cái"},
    {"chén": "1 cái"},
    {"đồ chơi": "2 cái"},
    {"quần áo": "0 cái"},
]


@app.get("/product")
async def get_product(skip: int = 0, limit: int = 20):
    return product[skip : skip + limit]


@app.get("/search")  # querry params không gắn giá trị mặc định thì nghĩa là bắt buộc
async def get_search(keyword: str, is_active: bool | None = None):
    return {
        "search key word": keyword,
        "is_active": is_active,
        "message": f"đây là kết quả tìm kiếm cho {keyword}, trạng thái active: {is_active}",
    }


@app.get("/items")
async def get_items(min_price: float = 0.0, max_price: float | None = None):
    return {
        "min_price": min_price,
        "max_price": max_price,
        "message": "Đã lọc sản phẩm theo giá.",
    }

@app.get("/authors/{author_id}/posts/")
async def get_posts_by_author(author_id:int, published_only: bool = True):
    return {"author_id": author_id, "published_only": published_only}

@app.get("/users/{user_id}/orders/{order_id}")
async def get_orders_users_by_id(user_id:int, order_id:int, show_details:bool=False):
    if show_details:
        return {"user_id": user_id, "order_id": order_id,"details": "Áo thun đỏ, size M"}
    return {"user_id": user_id, "order_id": order_id}
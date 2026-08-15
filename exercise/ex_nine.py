# Exercise 7 8 9

from fastapi import FastAPI, Path, Query, Body

from pydantic import BaseModel, Field
app = FastAPI()

#a)
@app.get("/")
async def read_root():
    return {"message" : "TechMart API"}

#h)
@app.get("/products/filter")
async def filter_products_by_tags(tags:list[str] = Query([])):
    return {"tags" : tags, "count" : len(tags)}

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
    return {"message" : f"Danh sách sản phẩm từ {skip} tới {limit}", "keyword": keyword}     

#e)
class ProductCreate(BaseModel):
    name:str
    price:float
    stock:int
    is_available:bool = True

@app.post("/products/")
async def create_product(product: ProductCreate = Body(...)):
    return product

#f)
@app.put("/products/{product_id}")
async def update_product(product_id:int = Path(..., ge=1), product: ProductCreate = Body(...)):
    return {"message" : f"cap nhat thanh cong sp {product_id} co thong tin nhu sau {product}"}

#g)
@app.get("/promotions/verify")
async def verify_promotion_code(promo_code: str = Query(None, alias="promo-code", pattern=r"^TECH[0-9]{4}$")):
    return {"promo-code": promo_code, "is_valid" : True}

#i)
@app.put("/orders/{order_id}/items/{item_id}")
async def update_order_item_quantity(order_id:int = Path(..., ge=1), item_id:int = Path(..., ge=1), notify_customer: bool = False, quantity: int = Body(..., ge=1, le=99)):
    return {"messsage" : f"chinh sua thanh cong don hang {order_id} san pham {item_id}", "quantity" : quantity, "notify_customer" : notify_customer}

#j)
class CustomerProfile (BaseModel):
    full_name : str
    email: str
@app.post("/customers/")
async def create_customer_profile(customer: CustomerProfile = Body(..., embed=True)):
    return {"message" : "tao thanh con khach hang", "customer" : customer}

#k)
class VendorInfo(BaseModel):
    vendor_name: str
    tax_code:str
@app.post("/products/with-vendor")
async def create_product_with_vendor(product: ProductCreate, vendor: VendorInfo, priority: int = Body(1, ge=1, le=5)):
    return {"message" : f"tao san pham thanh cong do nha cung cap la {vendor.vendor_name} , ", "priority" : priority, "product" : product}

#l)
class VoucherCreate(BaseModel):
    code: str = Field(..., min_length=5, max_length=15, pattern="^[A-Z]+$")
    discount_percent: int = Field(..., ge=0, le=100)
    max_usage: int = Field(..., gt=0)
    description: str | None = Field(None, max_length=200)
@app.post("/vouchers/")
async def create_voucher(voucher: VoucherCreate):
    return {"message" :"tao voucher thanh cong", "voucher" : voucher}

#m)

#n)
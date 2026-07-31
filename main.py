from fastapi import FastAPI

app = FastAPI()

@app.get('/', description="This is the ours first route")
async def base_get_route():
    return {
        "message" : "hello world"
    }


@app.post('/')
async def post():
    return {
        "message" : "hello from the post route"
    }

@app.put('/')
async def put():
    return {
        "message" : "hello from the put route"
    }

@app.get("/items")
async def list_items():
    return {
        "message" : "list items route"
    }

@app.get("/items/{items_id}")
async def get_items(items_id):
    return {
        "item_id" : "items_id"
    }
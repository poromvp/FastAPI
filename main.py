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

@app.get("/users")
async def list_users():
    return {
        "message" : "list users route"
    }

@app.get("/users/me")
async def get_current_user(): 
    return {
        "message" : "this is the current user"
    }

@app.get("/users/{users_id}")
async def get_users(users_id: str): 
    return {
        "users_id" : users_id
    }

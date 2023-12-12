from fastapi import FastAPI

app = FastAPI()


items = []


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/items")
def get_items(item: str):
    items.append(item)
    return items

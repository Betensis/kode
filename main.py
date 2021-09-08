from fastapi import FastAPI

app = FastAPI(debug=True)


@app.on_event("startup")
def startup():
    pass


@app.on_event("shutdown")
def startup():
    pass


@app.get("/")
def index():
    return {"hello": "world"}

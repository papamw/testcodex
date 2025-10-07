from fastapi import FastAPI

app = FastAPI(title="Hello World API")


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a basic greeting."""
    return {"message": "Hello, World!"}

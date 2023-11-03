from fastapi import FastAPI
from langserve import add_routes
from t00_llm import chain as t00_llm

app = FastAPI()

# Edit this to add the chain you want to add
add_routes(app, t00_llm, path="/t00-llm")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

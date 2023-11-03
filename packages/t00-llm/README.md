# T00: LLM

Large Language Models (LLMs) are the core of the current AI revolution.


## Setup Models

There are lots of models to choose from while OpenAI's GPT series would be the go-to ones.


## Run Locally

```shell
# inside this directory
langchain serve
```

This will start the FastAPI app with
- A server running locally at [http://localhost:8000](http://localhost:8000)
- API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- A playground at [http://127.0.0.1:8000/playground](http://127.0.0.1:8000/playground)


## Serve at an endpoint

Add the following code to your [`server.py` file](../../app/server.py):
```python
from t00_llm import chain as t00_llm_chain

add_routes(app, t00_llm_chain, path="/t00-llm")
```


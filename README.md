# LangChain Tutorial

Practical guides of [LangChain](https://github.com/langchain-ai/langchain).

## Chapters

- [x] [T00: LLM](./packages/t00-llm/README.md)
- [ ] T01: Prompt
- [ ] T02: Memory
- [ ] ...



## Run Locally

```bash
git clone https://github.com/xleven/langchain-tutorial.git

cd langchain-tutorial
python3 -m venv .venv && source .venv/bin/activate
pip install -U "langchain-cli[serve]"
for dir in packages/t*; do pip install -e "$dir"; done

# set OpenAI API key
export OPENAI_API_KEY=<your-api-key>

# serve all chapters
langchain serve

# or serve specific chapter
cd packages/t00-llm && langchain serve
```

Now go to [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redoc) to see all the available API. Those ended with `playground` can be used to play with the API.


from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI

gen_model = OpenAI()  # defaults to `text-davinci-003`
chat_model = ChatOpenAI()  # defaults to `gpt-3.5-turbo`

mode = "chat"  # or "gen"

if mode == "chat":
    chain = chat_model
else:
    chain = gen_model

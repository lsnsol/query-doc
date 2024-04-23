from indexify import IndexifyClient
client = IndexifyClient()

from indexify_langchain import IndexifyRetriever
params = {"name": "minilm-em.embedding", "top_k": 15}
retriever = IndexifyRetriever(client=client, params=params)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(openai_api_key="<OpenAI API Key Goes Here>")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

print(chain.invoke("What are the results on MT-Bench?"))
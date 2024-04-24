
from flask import Flask, flash, request, redirect, url_for, make_response, jsonify
from flask_cors import cross_origin

app = Flask(__name__)

# Hello API for testing purposes
@app.route('/hello', methods=['GET'])
@cross_origin()
def hello_api():
  print ('Hello World Flask API')
  response = jsonify({'message': 'Hello from Query-Doc'})
  return response

# Upload PDF API
@app.route('/uploadpdf', methods=['POST'])
@cross_origin()
def uploadpdf():
  from indexify import IndexifyClient
  client = IndexifyClient()
  client.add_extraction_policy(extractor='tensorlake/pdf-extractor', name="pdf-extraction")
  client.add_extraction_policy(extractor='tensorlake/chunk-extractor', name="chunks", content_source="pdf-extraction", input_params={"chunk_size": 512, "overlap": 150})
  client.add_extraction_policy(extractor='tensorlake/minilm-l6', name="minilm-em", content_source="chunks")

  client.upload_file(path="sample.pdf")

# Query PDF API
@app.route('/querypdf', methods=['POST'])
@cross_origin()
def querypdf():
  question_asked = 'What are the results on MT-Bench?'
  
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

  response = jsonify({'result': chain.invoke(question_asked)})
  return response


if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=8080)

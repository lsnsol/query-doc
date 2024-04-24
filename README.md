# Query Doc

## Query your PDF documents and get more insights from them

### Dependencies
1. Flask (flask)
2. Flask Cors (flask_cors)
3. Indexify (indexify)
4. Indexify Langchain (indexify-langchain)
5. Indexify Extractor SDK (indexify-extractor-sdk)
6. Virtual Env (virtualenv)
7. Transformers (transformers)
8. Poppler-utils (poppler-utils)
9. Torch (torch)
10. PDF2Image (pdf2image)
11. Torch Vision (torchvision)
12. Easy OCR (easyocr)
13. Py PDF (pypdf)
14. Utils (utils)
15. Langchain OpenAI (langchain_openai) or Langchain Google VertexAI (langchain-google-vertexai)

### Note: Google Vertex AI will require following setup as well
1. gcloud SDK - download and install
2. run ```gcloud init``` - initialize the gcloud
3. select project with VertexAI API enabled - can be done via ```gcloud config set project **name of project**```
4. run ```gcloud auth application-default login``` - this will enable all libraries being called to use the auth of the accouint used in gcloud init


### Steps to Run and Stop:
1. ```curl https://www.tensorlake.ai | sh```
2. ```sh init.sh```

If killing init.sh terminal and running again use ```run.sh```

To completely stop all services use ```sh stop.sh```
It should show the message - "No Sockets found in /run/screen/S-**username**"


### Reference

[Indexify Examples](https://getindexify.io/examples/Scientific_Journals/)


### Special Thanks

[Rishiraj Acharya](https://rishiraj.github.io/) for making this and helping me out

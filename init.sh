#!/bin/bash
# Install all Dependencies
pip install indexify-extractor-sdk indexify-langchain indexify flask flask_cors virtualenv transformers torch pdf2image torchvision easyocr pypdf langchain_openai

# Install Poppler Utils
sudo apt-get install -y poppler-utils

# Start Indexify Servers for Chunking, Embeddings and PDF Extractor
screen -dmS Indexify-Server scripts/server.sh
screen -dmS Indexify-Chunking scripts/chunking.sh
screen -dmS Indexify-Embedding scripts/embedding.sh
screen -dmS Indexify-PDF scripts/pdf.sh
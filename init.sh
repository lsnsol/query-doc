#!/bin/bash
# Install all Dependencies
pip install indexify-extractor-sdk indexify-langchain indexify flask flask_cors virtualenv transformers torch pdf2image torchvision easyocr pypdf langchain_openai utils

# Install Poppler Utils
sudo apt-get install -y poppler-utils

# Start Indexify Servers for Chunking, Embeddings and PDF Extractor
screen -dmS Indexify-Server sh scripts/server.sh
screen -dmS Indexify-Chunking sh scripts/chunking.sh
screen -dmS Indexify-Embedding sh scripts/embedding.sh
screen -dmS Indexify-PDF sh scripts/pdf.sh

# show screens
screen -ls

# Run main.py
python3 main.py

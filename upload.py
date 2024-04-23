
# from flask import Flask, flash, request, redirect, url_for, make_response, jsonify
# from flask_cors import cross_origin

from indexify import IndexifyClient
client = IndexifyClient()
client.add_extraction_policy(extractor='tensorlake/pdf-extractor', name="pdf-extraction")
client.add_extraction_policy(extractor='tensorlake/chunk-extractor', name="chunks", content_source="pdf-extraction", input_params={"chunk_size": 512, "overlap": 150})
client.add_extraction_policy(extractor='tensorlake/minilm-l6', name="minilm-em", content_source="chunks")

client.upload_file(path="sample.pdf")

# Results on MT-Bench show that ZEPHYR-7B surpasses LLAMA 2-CHAT-70B, the best open-access RLHF-based model.

# app = Flask(__name__)
# app.secret_key = 'k8smashers'

# @app.route('/hello', methods=['GET'])
# @cross_origin()
# def hello_api():
#   print ('Get call recieved')
#   response = jsonify({'message': 'hello from cloud run'})
#   return response

# @app.route('/uploadpdf', methods=['POST'])
# @cross_origin()
# def uploadpdf():


# if __name__ == "__main__":
#   app.run(debug=False, host="0.0.0.0", port=8080)

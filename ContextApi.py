from flask import Flask, request, jsonify
from reverso_context_api import Client
import itertools 

app = Flask(__name__)

@app.route('/get_translation_samples', methods=['GET'])
def get_translation_samples():
    word = request.args.get('word')
    source = request.args.get('source_language')
    target = request.args.get('target_language')

    if not word:
        return jsonify({"error": "Missing 'word' parameter"}), 400
    c = Client(source, target)

    return list(itertools.islice(c.get_translation_samples(word, cleanup=False), 15))

@app.route('/get_translation', methods=['GET'])
def get_translation():
    word = request.args.get('word')
    source = request.args.get('source_language')
    target = request.args.get('target_language')

    if not word:
        return jsonify({"error": "Missing 'word' parameter"}), 400
    c = Client(source, target)

    return list(Client(source, target).get_translations(word))


  

if __name__ == '__main__':
    app.run(debug=True)

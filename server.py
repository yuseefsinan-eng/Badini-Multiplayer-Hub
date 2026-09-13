import os
from flask import Flask, jsonify, request

app = Flask(__name__)

badini_lang = {
    "server_name": "سێرڤەرا کوردییا بادینی - SAMP",
    "status": "سێرڤەر کاردکەت و ب خێر هاتن!"
}

@app.route('/')
def home():
    return jsonify(badini_lang)

@app.route('/settings/language', methods=['POST'])
def change_language():
    data = request.json
    selected_lang = data.get('lang', 'badini')
    return jsonify({"message": f"زمان هاتە گوهۆڕین بۆ: {selected_lang}"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

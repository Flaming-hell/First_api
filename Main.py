from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/me', methods=['GET'])
def get_creator_info():
    creator_info = {
        "name": "anto",  
        "age": 17,           
        "profession": "-"  
    }
    return jsonify(creator_info)


if __name__ == '__main__':
    app.run(debug=True)
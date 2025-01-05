from flask import Flask, jsonify

# Inisialisasi Flask
app = Flask(__name__)

# Endpoint untuk menampilkan informasi pembuat
@app.route('/creator', methods=['GET'])
def get_creator_info():
    creator_info = {
        "name": "anto",  
        "age": 17,           
        "profession": "-"  
    }
    return jsonify(creator_info)


if __name__ == '__main__':
    app.run(debug=True)
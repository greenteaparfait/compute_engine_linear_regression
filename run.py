from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        firstname = request.json['first_name']
        lastname = request.json['last_name']
        return jsonify(result1=firstname, result2=lastname[1])
    else:
        return "<h1> This is Index Page</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)

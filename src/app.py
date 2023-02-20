from flask import Flask, request, jsonify
from executer import trailinit

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
api_alive = 'Im alive'


@app.route('/api/test', methods=['GET', 'POST'])
def test_application():
    if request.method == 'GET':
        return api_alive
    else:
        info_input = request.json
        result = trailinit()
        return jsonify(result)
    

if __name__ == '__main__':
    app.run("0.0.0.0", port=8000)

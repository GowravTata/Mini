from flask import Flask, request
from app.services.insert_data import all_tools

app = Flask(__name__)


@app.route('/enter', methods=['POST'])
def route():
    data = request.json
    if 'brand' in data and 'model' in data and 'year' in data:
        response = all_tools(data=data)
    else:
        response = 'More keys are required'
    return response


if __name__ == '__main__':
    app.run(port=5001,debug=True)

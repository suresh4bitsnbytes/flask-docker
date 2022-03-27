from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def get_users():

    return jsonify([{
        "firstName":"Suresh",
        "lastName":"Kumar"
        },
        {
        "firstName":"Steve",
        "lastName":"Jobs"
        }])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
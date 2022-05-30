from flask import Flask,jsonify

app = Flask(__name__)


tasks = {
    {
        "id":1,
        "title": u'buy groceries',
        "description": U'Milk,cheese,bread,butter',
        "done": False
     },
    {
        "id":2,
        "title": u'Rentting',
        "description": U'We are renting ec2 server from aws cloud',
        "done": False
    }
}

@app.route("/Login", methods=["POST", "GET"])

def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == "__main__":
    app.run(debug=True)

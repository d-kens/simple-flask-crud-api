from flask import Flask 

# create a flask application instance
app = Flask(__name__)

# Define a route and its associated view function
@app.route('/')
def hello():
    return 'Hello, World!'


from controller import * 


if __name__ == '__main__':
    app.run(debug=True)
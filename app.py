from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    m= 'Hello, World and beatiful'
    n="somthing"
    k=m.upper()
    return k


@app.route('/home')
def home():
    return 'Home Page!!'

if __name__ == '__main__':
    # Run the app in local network
    app.run()
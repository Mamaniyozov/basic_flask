from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    m= 'Hello, World and beatiful'
    n="somthing"
    k=m.upper()
    return n , k


@app.route('/home')
def home():
    return 'Home Page!!'

if __name__ == '__main__':
    # Run the app in local network
    app.run(host='0.0.0.0', port=8000,debug=True)
from flask import Flask,request


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    r=request.args
    a=int(r['a'])
    b=int(r['b'])
    # data = {
    #     'a': 15,
    #     'b': 2,
    #     'c': 5,
    #     'g': 10
    # }
   
    s=a+b
    return {"summa":s}
def home():
    return 'Home Page!!;)'
@app.route('/about')
def about():
    return ("welcome to my web sayt:)").title()


    # or just {{ table }} from within a Jinja template
    # Observe the result    

    



if __name__ == '__main__':
    # Run the app in local network
    app.run()
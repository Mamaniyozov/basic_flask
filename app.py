from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    m= 'Hello, World and beatiful'
    n="somthing"
    k=m.upper()
    return k


@app.route('/home')
def home():
    return 'Home Page!!;)'
@app.route('/about')
def about():
    return ("welcome to my web sayt:)").title()
@app.route('/table')
def table():
    # Import pandas package


# Define a dictionary containing Students data
    data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
            'Height': [5.1, 6.2, 5.1, 5.2],
            'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)

    # Declare a list that is to be converted into a column
    address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']

    # Using 'Address' as the column name
    # and equating it to the list
    df['Address'] = address

# Observe the result
    return df



if __name__ == '__main__':
    # Run the app in local network
    app.run()
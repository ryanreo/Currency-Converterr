from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '***REMOVED***'
BASE_URL = "https://v6.exchangerate-api.com/v6/***REMOVED***/latest/USD"

@app.route('/')
def home():
    return render_template('index.html')

#Convert currency (POST request)
@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.get_json()
    amount = float(data['amount'])
    from_currency = data['from']
    to_currency = data['to']
    
    response = requests.get(f"https://v6.exchangerate-api.com/v6/***REMOVED***/latest/{from_currency}")
    rates = response.json()["conversion_rates"]
    
    #Convert currency
    if to_currency in rates:
        converted_amount = amount * rates[to_currency]
        return jsonify({'converted_amount': converted_amount})
    else:
        return jsonify({'error': 'Invalid currency'}), 400
    
if __name__ == '__main__':
    app.run(debug=True)
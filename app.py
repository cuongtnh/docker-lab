from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_price = None
    error = None
    
    if request.method == 'POST':
        ticker = request.form.get('ticker', '').strip()
        if ticker:
            try:
                stock = yf.Ticker(ticker)
                stock_price = stock.history(period='1d')['Close'].iloc[-1]
            except Exception as e:
                error = f"Error fetching data: {str(e)}"
        else:
            error = "Please enter a valid stock ticker."
    
    return render_template('index.html', stock_price=stock_price, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

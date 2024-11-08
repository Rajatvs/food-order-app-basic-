from flask import Flask, render_template, request

app = Flask(__name__)

# Sample menu data with images
menu = {
    "Burger": {"price": 5.99, "image": "https://www.bing.com/th?id=OIP.ydNry8zoLz4BzraMRDhvXwHaF-&w=146&h=120&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2"},
    "Pizza": {"price": 8.99, "image": "https://www.bing.com/th?id=OIP.PyD2FPss2X99L71KPv4XkwHaE8&w=222&h=150&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2"},
    "Soda": {"price": 1.99, "image": "https://th.bing.com/th/id/OIP.RdQH1zNJCM8qJB6rjgvtOQHaHa?w=189&h=189&c=7&r=0&o=5&dpr=1.3&pid=1.7"},
    "Fries": {"price": 2.49, "image": "https://th.bing.com/th/id/OIP.9MM9v7VZhiUSGon_EapRuwHaFj?w=252&h=189&c=7&r=0&o=5&dpr=1.3&pid=1.7"},
    "Salad": {"price": 4.99, "image": "https://th.bing.com/th/id/OIP.jevUF8toFBsTCfqvRcuIRQHaLH?w=204&h=306&c=7&r=0&o=5&dpr=1.3&pid=1.7"}
}

# Route to display the menu and buying option
@app.route('/')
def index():
    return render_template('index.html', menu=menu)

# Route to handle purchasing an item
@app.route('/buy', methods=['POST'])
def buy():
    item = request.form.get('item')
    if item and item in menu:
        price = menu[item]["price"]
        return f"Thank you for buying {item} for ${price:.2f}!"
    else:
        return "Invalid item selected.", 400

if __name__ == '__main__':
    app.run(debug=True)

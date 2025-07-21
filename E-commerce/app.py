from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample product catalog
products = [
    {
        "id": 1,
        "name": "Smartphone",
        "price": 15000,
        "image": "smartphone.jpg",
        "description": "Latest 5G smartphone with 64MP camera."
    },
    {
        "id": 2,
        "name": "Laptop",
        "price": 45000,
        "image": "laptop.jpg",
        "description": "Powerful laptop for developers and designers."
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2000,
        "image": "headphones.jpg",
        "description": "Noise-cancelling over-ear headphones."
    }
]

# Home page
@app.route("/")
def home():
    return render_template("home.html", products=products)

# Product details page
@app.route("/product/<int:id>")
def product_details(id):
    product = next((p for p in products if p["id"] == id), None)
    return render_template("product.html", product=product)

# Add to cart (form POST)
@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    product_id = request.form.get("product_id")
    quantity = request.form.get("quantity")
    return redirect(url_for('cart', id=product_id, qty=quantity))

# Cart page
@app.route("/cart")
def cart():
    product_id = int(request.args.get("id", 0))
    qty = int(request.args.get("qty", 1))

    product = next((p for p in products if p["id"] == product_id), None)
    total = product["price"] * qty if product else 0

    return render_template("cart.html", product=product, qty=qty, total=total)

if __name__ == "__main__":
    app.run(debug=True,port=8007)

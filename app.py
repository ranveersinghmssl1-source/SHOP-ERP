from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
    
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'shoperp123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop_erp.db'

db = SQLAlchemy(app)

# --------------------------
# MODELS
# --------------------------

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(50), unique=True)
    product_name = db.Column(db.String(200))
    category = db.Column(db.String(100))
    purchase_price = db.Column(db.Float)
    sale_price = db.Column(db.Float)
    stock_qty = db.Column(db.Integer)
    min_stock = db.Column(db.Integer)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_code = db.Column(db.String(50), unique=True)
    customer_name = db.Column(db.String(200))
    mobile = db.Column(db.String(20))
    address = db.Column(db.String(300))

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_code = db.Column(db.String(50), unique=True)
    supplier_name = db.Column(db.String(200))
    mobile = db.Column(db.String(20))
    address = db.Column(db.String(300))

# --------------------------
# ROUTES
# --------------------------

@app.route("/")
def dashboard():

    product_count = Product.query.count()
    customer_count = Customer.query.count()
    supplier_count = Supplier.query.count()

    return render_template(
        "dashboard.html",
        product_count=product_count,
        customer_count=customer_count,
        supplier_count=supplier_count
    )

# --------------------------
# PRODUCT MASTER
# --------------------------

@app.route("/products")
def products():

    products = Product.query.all()

    return render_template(
        "products.html",
        products=products
    )

@app.route("/add_product", methods=["POST"])
def add_product():

    product = Product(
        product_code=request.form["product_code"],
        product_name=request.form["product_name"],
        category=request.form["category"],
        purchase_price=request.form["purchase_price"],
        sale_price=request.form["sale_price"],
        stock_qty=request.form["stock_qty"],
        min_stock=request.form["min_stock"]
    )

    db.session.add(product)
    db.session.commit()

    return redirect("/products")

# --------------------------
# CUSTOMER MASTER
# --------------------------

@app.route("/customers")
def customers():

    customers = Customer.query.all()

    return render_template(
        "customers.html",
        customers=customers
    )

@app.route("/add_customer", methods=["POST"])
def add_customer():

    customer = Customer(
        customer_code=request.form["customer_code"],
        customer_name=request.form["customer_name"],
        mobile=request.form["mobile"],
        address=request.form["address"]
    )

    db.session.add(customer)
    db.session.commit()

    return redirect("/customers")

# --------------------------
# SUPPLIER MASTER
# --------------------------

@app.route("/suppliers")
def suppliers():

    suppliers = Supplier.query.all()

    return render_template(
        "suppliers.html",
        suppliers=suppliers
    )

@app.route("/add_supplier", methods=["POST"])
def add_supplier():

    supplier = Supplier(
        supplier_code=request.form["supplier_code"],
        supplier_name=request.form["supplier_name"],
        mobile=request.form["mobile"],
        address=request.form["address"]
    )

    db.session.add(supplier)
    db.session.commit()

    return redirect("/suppliers")

# --------------------------

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)

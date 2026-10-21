class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(200))
    product_name = db.Column(db.String(200))
    qty = db.Column(db.Integer)
    rate = db.Column(db.Float)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(200))
    product_name = db.Column(db.String(200))
    qty = db.Column(db.Integer)
    rate = db.Column(db.Float)

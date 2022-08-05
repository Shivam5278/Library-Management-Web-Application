from app import db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(40))
    publisher = db.Column(db.String(40))
    quantity = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'{self.title}'

class Members(db.Model):
    id_m = db.Column(db.Integer, primary_key=True)
    name_m = db.Column(db.String(255), nullable=False)
    memid_m = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'{self.name_m}'

class Transactions(db.Model):
    id_t = db.Column(db.Integer, primary_key=True)
    name_t = db.Column(db.String(255), nullable=False)
    memid_t = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'{self.name_m}'



db.create_all()

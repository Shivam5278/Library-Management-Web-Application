from app import db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(40))
    publisher = db.Column(db.String(40))
    quantity = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'{self.title} {self.author}'

class Members(db.Model):
    id_m = db.Column(db.Integer, primary_key=True)
    name_m = db.Column(db.String(255), nullable=False)
    memid_m = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'{self.name_m} {self.memid_m}'

class Transactions(db.Model):
    id_t = db.Column(db.Integer, primary_key=True)
    name_t = db.Column(db.String(255), nullable=False)
    memid_t = db.Column(db.Integer, nullable=False)
    title_t = db.Column(db.String(100), nullable=False)
    issue_t = db.Column(db.Date, nullable=False)
    due_t = db.Column(db.Date, nullable=False)
    rent_t = db.Column(db.Integer, nullable=False)
    type_t = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'{self.name_m}'



db.create_all()

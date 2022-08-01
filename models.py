from app import db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255))
    quantity = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'{self.title}'

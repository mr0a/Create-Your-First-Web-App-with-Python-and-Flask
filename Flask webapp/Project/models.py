from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    date = db.Column(db.Date, nullable = False)

    #A method to represent its instance of this datamodel
    def __repr__(self):
        return f'{self.title} created on {self.date}'

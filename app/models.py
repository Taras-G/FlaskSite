from app import db

class Score(db.Model):
    id = db.Column(db.String(3), primary_key=True)
    score = db.Column(db.Integer())

    def __repr__(self):
        return '<Score %r>' % (self.id)
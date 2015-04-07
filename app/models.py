from app import db

class Score(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    initials = db.Column(db.String(3))
    score = db.Column(db.Integer())

    def __repr__(self):
        return '<Score %r>' % (self.id)
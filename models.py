from init_setup import db_global


db = db_global.db
ma = db_global.ma


# Define a base model for other database tables to inherit
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class Match(Base):
    opponent = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    link = db.Column(db.String(250))

    def __init__(self, opponent, rating, link):
        self.opponent = opponent
        self.rating = rating
        self.link = link


class MatchSchema(ma.ModelSchema):
    class Meta:
        model = Match

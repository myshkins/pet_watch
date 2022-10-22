from project import db

class Temps(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'temperature'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    temperature = db.Column(
        db.Float,
        unique=False,
        nullable=False
    )
    time = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)

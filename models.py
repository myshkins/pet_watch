"""database table models"""
from project import db

class Temp(db.Model):
    """Data model for temperature data point."""

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
        index=True,
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return f'temp:{self.temperature}, time:{self.time}'

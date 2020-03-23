from app import db


class Candle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candle_currency = db.Column(db.String)
    candle_end_date = db.Column(db.DateTime)
    candle_high = db.Column(db.Float)
    candle_low = db.Column(db.Float)
    candle_open = db.Column(db.Float)
    candle_close = db.Column(db.Float)
    candle_volume = db.Column(db.Float)

    def __repr__(self):
        return f"Candle start = {self.candle_start_date}"


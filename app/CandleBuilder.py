from datetime import datetime

from app.models import Candle
from app import db


class CandleBuilder:
    def __init__(self, high=0, low=0, date=None, open=0, close=0, volume=0, minute=0):  # noqa: E501
        self.high = high
        self.low = low
        self.date = date
        self.open = open
        self.close = close
        self.volume = volume
        self.minute = minute

    def receive_trade(self, trade):
        validation = []
        if type(trade) == type(validation):
            print(trade)
            timestamp = float(trade[1][0][2])
            time_object = datetime.fromtimestamp(timestamp)
            minute = time_object.minute
            price = round(float(trade[1][0][0]), 2)
            volume = round(float(trade[1][0][1]), 8)
            currency = trade[3]

            if minute <= self.minute + 5:
                self.volume += volume
                self.date = time_object
                if price > self.high:
                    self.high = price
                if price < self.low:
                    self.low = price
                if self.open == 0:
                    self.open = price
                self.close = price
            else:
                # call method to add candle to DB
                self.add_candle(time_object, currency)
                # call method to reset all properties to 0\
                print(
                    f"Candle added.\
                    High: {self.high}\
                    Low: {self.low}\
                    Open: {self.open}\
                    Close: {self.close}\
                    Volume: {self.volume}"
                )
                self.reset()
                self.date = time_object
                self.minute = minute
                self.low = price
                self.high = price
                self.open = price
                self.close = price
                self.volume += volume

    def reset(self):
        try:
            self.high = 0
            self.low = 0
            self.high = 0
            self.open = 0
            self.close = 0
            self.volume = 0
            self.minute = None
        except TypeError as identifier:
            pass

    def add_candle(self, time_object, currency):
        new_candle = Candle(
            time_object, currency, self.high, self.low, self.open, self.close, self.volume  # noqa: E501
        )
        db.session.add(new_candle)
        db.session.commit()




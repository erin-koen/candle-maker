from datetime import datetime
import json
import csv
import sqlite3

from kraken_wsclient_py import kraken_wsclient_py as kraken_client


class CandleBuilder:
    def __init__(self, db_name):
        self.trade_table = db_name
        # self.candle_size = candle_size
        # self.units = unit

    def add_candle(self, candle_size, unit):
        # pull from self.everything to send to db
        pass

    def initialize_db(self):
        try:
            db = sqlite3.connect(self.trade_table)
            print('db connection open')
            cursor = db.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS trades
                (year int,
                month int,
                day int,
                hour int,
                minute int,
                price float,
                volume float,
                currency string)''')
            db.commit()
            print('Trade table created.')
            cursor.close()

        except sqlite3.Error as error:
            print('Error while creating the trade table.', error)

        finally:
            if (db):
                db.close()
                print('DB connection closed.')

    def add_trade(self, message):
        validation = []
        if type(message) == type(validation):
            print(message)
            try:
                db = sqlite3.connect(self.trade_table)

                timestamp = float(message[1][0][2])
                time_object = datetime.fromtimestamp(timestamp)
                year = time_object.year
                month = time_object.month
                day = time_object.day
                hour = time_object.hour
                minute = time_object.minute
                price = round(float(message[1][0][0]), 2)
                volume = round(float(message[1][0][1]), 8)
                currency = message[3]

                cursor = db.cursor()

                cursor.execute("INSERT INTO trades (year, month, day, hour, minute, price, volume, currency) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
                    year, month, day, hour, minute, price, volume, currency))

                db.commit()
                print('Succesfully inserted trade.')
                cursor.close()

            except sqlite3.Error as error:
                print('Failed to insert trade into table', error)

            finally:
                if (db):
                    db.close()
                    print("SQLite connection closed successfully")

    def open_connection(self):
        kraken = kraken_client.WssClient()
        kraken.subscribe_public(
            subscription={
                'name': 'trade'
            },
            pair=['ETH/USD', 'BTC/USD'],
            callback=self.add_trade
        )

        kraken.start()


test = CandleBuilder('trades.db')
test.initialize_db()
test.open_connection()

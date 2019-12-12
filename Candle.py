from datetime import datetime
import time
import json
import csv
import sqlite3

from kraken_wsclient_py import kraken_wsclient_py as kraken_client


class CandleBuilder:
    def __init__(self, db_name):
        self.db_name = db_name
        self.last_query = None
        self.trades = []
        # self.units = unit

    def retrieve_trades(self):
        # pull from self.everything to send to db
        try:
            db = sqlite3.connect(self.db_name)
            ts = time.time()
            # query trades between self.last_query and timestamp inclusive
            query = f'SELECT * FROM trades WHERE timestamp BETWEEN {self.last_query} AND {ts}'
            cursor = db.cursor()
            cursor.execute(query)
            # return all trades since last query (or query all then delete?) track time in
            trades = cursor.fetchall()
            self.trades = trades
            # set self_last_query to current ts for next round
            self.last_query = ts

            # assemble candles based on returned array
            # insert candles into candle table
        except sqlite3.Error as error:
            e = error
            print('Error while retrieving trades, ', error)
        finally:
            if trades:
                return 'Trades were fetched successfully.'
            elif e:
                return 'There was an error retrieving the trades, see message.'
            else:
                return 'There were no trades since the last fetch.'

    def build_candles(self):
        if len(self.trades):
            # check that these trades are newer than your
            # last candles
            # build five minute candles 
            # insert into db
        else:
            pass

    def initialize_db(self):
        try:
            db = sqlite3.connect(self.db_name)
            print('DB connection open')
            cursor = db.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS trades
                (year int,
                month int,
                day int,
                hour int,
                minute int,
                price float,
                volume float,
                currency string,
                timestamp float)''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS candles
                (year int,
                month int,
                day int,
                hour int,
                minute int,
                timestamp float,
                high float, 
                low float, 
                open float,
                close float)''')

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
                db = sqlite3.connect(self.db_name)

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

                cursor.execute("INSERT INTO trades (year, month, day, hour, minute, price, volume, currency, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
                    year, month, day, hour, minute, price, volume, currency, timestamp))

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

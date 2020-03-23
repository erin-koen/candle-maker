from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models, Kraken, CandleBuilder  # noqa: E731 F401 type:ignore

new_candle = CandleBuilder.CandleBuilder
exchange = Kraken.Kraken

exchange.open_connection(exchange, new_candle.receive_trade)

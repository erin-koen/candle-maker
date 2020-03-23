from kraken_wsclient_py import kraken_wsclient_py as kraken_client


class Kraken:
    def __init__(self):
        pass

    def open_connection(self, func):
        kraken = kraken_client.WssClient()
        kraken.subscribe_public(
            subscription={"name": "trade"},
            pair=["ETH/USD"],
            callback=func
        )
        kraken.start()
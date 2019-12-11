from datetime import datetime
import json
import csv


def from_csv():
    with open('trades.csv') as prices:
        price_list = [
            line.rstrip().split(',')[0:3]
            for line in prices
            if line.rstrip().split(',')[0] != ''
        ]
        return price_list[1:]


def candle_maker(trades):
    candle_array = []
    candle = {
        'high': None,
        'low': None,
        'open': None,
        'close': None,
        'volume': 0,
        'hour': 0
    }

    current_hour = 0
    with open('candles.csv', 'w') as candles_csv:
        fieldnames = candle.keys()
        writer = csv.DictWriter(candles_csv, fieldnames=fieldnames)
        writer.writeheader()

        for trade in trades:
            price = float(trade[0])
            size = float(trade[1])
            timestamp = float(trade[2])
            time_object = datetime.fromtimestamp(timestamp)
            hour = time_object.hour

            if hour == current_hour:
                candle['close'] = price

                if candle['open'] is None:
                    candle['open'] = price
                if candle['high'] is None or price > candle['high']:
                    candle['high'] = price
                if candle['low'] is None or price < candle['low']:
                    candle['low'] = price
                candle['volume'] += size
            else:
                print(f'FALSE. Hour: {hour}, current_hour: {current_hour}')
                print(candle)
                # candle_array.append(candle)
                writer.writerow(candle)
                current_hour = hour
                # print(f'NEW CURRENT HOUR: {current_hour}')
                candle['high'] = price
                candle['low'] = price
                candle['open'] = price
                candle['close'] = price
                candle['volume'] = size
                candle['hour'] = current_hour

    # with open('candles.json', 'w') as candle_json:
    #     json.dump(candle_array, candle_json)

    return "SUCCESS"


def main():
    print(f'Starting script')
    trades = from_csv()
    print(f'Trades generated {trades[0]}')
    candles = candle_maker(trades)
    return candles


main()

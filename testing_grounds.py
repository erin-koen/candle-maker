from datetime import datetime

array = [1, [['7174.70000', '0.03624754',
              '1576097380.650025', 's', 'l', '']], 'trade', 'XBT/USD']
time_object = datetime.fromtimestamp(float(array[1][0][2]))
heartbeat = {'event': 'heartbeat'}
print(
    type(array) == type(heartbeat)
)

def fake():
    try:
        something = [1,2,3,3,3]
    except expression as identifier:
        pass
    finally:
        return something

print(fake())
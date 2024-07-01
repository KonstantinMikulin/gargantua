from datetime import datetime

test = '04-01-1988'

print(bool(datetime.strptime(test, "%d-%m-%Y")))
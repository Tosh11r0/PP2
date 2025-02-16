import datetime
from datetime import datetime, timedelta

#I will write a programm to find a difference between today and tomorrow

x = datetime.now()
y = x + timedelta(days=1)

their_difference = y - x

ans = their_difference.total_seconds()

print (ans)
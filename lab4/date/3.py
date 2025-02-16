import datetime
from datetime import datetime, timedelta

x = datetime.now()

ans = x.replace(microsecond=0)

print (ans)
import datetime

date = datetime.date(*map(int,input().split()))
d = int(input())
res = date + datetime.timedelta(days=d)
print(res.year, res.month, res.day)

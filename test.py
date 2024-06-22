import datetime


startTime = datetime.datetime.strptime('07:00:00.750000', '%H:%M:%S.%f').time()
print(startTime)
actualTime = datetime.datetime.now().time()
print(actualTime)
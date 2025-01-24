import random
import time
def getRandomdate(startDate,endDate):
    print("printing random date between",startDate,"and",endDate)
    randomGenerator = random.random
    dateformat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate,dateformat))
    endtime = time.mktime(time.strptime(endDate,dateformat))
    
    randomTime = startTime + randomGenerator *(endtime-startTime)
    randomDate = time.strftime(dateformat,time.localtime(randomTime))
    return randomDate
    
print("random Date",getRandomdate("1/1/2016","12/12/2018"))

#! python3

import pyautogui
import csv
import time
import os
import re

#max_iter = 3000
#start_time = time.time()
#freq = 1/1000
#max_file_size = 30
#max_file_size_unit = 'KB'
#file_name = 'file_0.csv'

def csv_write(file, x, y):
    log_file = open(file, 'a', newline='')
    #print(str(x), str(y))
    data = [x , y,]
    #print(data)
    wr = csv.writer(log_file)#, quoting=csv.QUOTE_ALL)
    wr.writerow(data)
    return

def sizer(file):
    size = os.path.getsize(file)
    #print(size)
    return size

def max_file_sizer(max_file_size):
    if 'KB' in max_file_size:
        #print(re.findall('\d+',max_file_size))
        x = int(re.findall('\d+',max_file_size)[0])*1024
        #print(x)
    elif 'MB' in max_file_size:
        x = int(re.findall('\d+',max_file_size)[0])*1048576
    elif 'GB' in max_file_size:
        x = int(re.findall('\d+',max_file_size)[0])*1073741824
    elif 'TB' in max_file_size:
        x = int(re.findall('\d+',max_file_size)[0])*1099511627776
    else:
        x = int(re.findall('\d+',max_file_size)[0])
    return x

def logger(file_name, max_file_size, sec):
    print('Logger Started: ' + str(time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())))
    start_time = time.time()
    csv_write(file_name, 'x', 'y')
    x, y = pyautogui.position()
    count = 1
    #positionStr = 'x: ' + str(x).rjust(4) + ' y: ' + str(y).rjust(4)
    next_step = (start_time + (count -1.0) * sec) - time.time()
    if next_step > 0.0:
        time.sleep(next_step)
    #print(positionStr)
    #print(count)
    #print(time.time())
    csv_write(file_name, x, y)    
    #while sizer(file_name) <= max_file_size:
    while count <= 30:
        x, y = pyautogui.position()
        #positionStr = 'x: ' + str(x).rjust(4) + ' y: ' + str(y).rjust(4)
        next_step = (start_time + (count -1.0) * sec) - time.time()
        if next_step > 0.0:
            time.sleep(next_step)
        #print(positionStr)
        #print(count)
        print(time.time())
        count += 1
        csv_write(file_name, x, y)
        #sizer(file_name)
    print ('Logger Stopping...')
    return

freq = float(input('Enter Logging Frequency in Hz: '))
max_file_size = str(input('Enter Max File Size: '))
file_name = input('Enter Filename:') + '.csv'
print('Logger Starting...')
logger(file_name, max_file_sizer(max_file_size), (1/freq))
print('Logger Stop: ' + str(time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime())))





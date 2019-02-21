import os
import time
from datetime import datetime 
import speedtest   
    
hostnames = ['1.1.1.1','213.191.128.8','213.191.128.9','8.8.8.8']    
counter=0    
    
def Ping(hostname):
    print('Starting Ping')
    response = os.system('ping -n 4 ' + hostname)
    if response != 0:
        with open("down.txt", "a") as myfile:
            myfile.write(str(datetime.now())+'    -->Ping: '+hostname+'-->pad veze \n')
        TestSpeed()

def TestSpeed():
    try:
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        with open("speed.txt", "a") as myfile:	
            myfile.write(str(datetime.now())+'\n')					
            myfile.write('  Ping:      '+str(res["ping"])+'ms \n')
            myfile.write('  Download:  '+str(res["download"]/1024)+'Kb/s \n')
            myfile.write('  Upload:    '+str(res["upload"]/1024)+'Kb/s \n\n\n')
            myfile.write('\n\n')  
        print 'Speedtest Complete'				
       
    except:
        print 'speedtest failed'
        with open("down.txt", "a") as myfile:
            myfile.write(str(datetime.now())+'    -->Speedtest-->pad veze \n')
            time.sleep(5)
        TestSpeed()
          

while True:    
    print 'Starting Speedtest'	       
    for hostname in hostnames:
        Ping(hostname)
    print 'Ping ok\n Sleeping 1 minute'
    counter+=1
    if counter>60:
        TestSpeed()
        counter=0
    time.sleep(60)
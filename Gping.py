import os
import time
from datetime import datetime 
import speedtest   
    
hostnames = ['1.1.1.1','213.191.128.8','213.191.128.9','8.8.8.8']    
 #8.8.8.8-Google 
    #192.168.1.1-Lokalni ruter    

while True:   
    print str(datetime.now())
    time.sleep(10) 
    print 'Starting Speedtest'	
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
        print 'retesting'
        
        
    for hostname in hostnames:
        response = os.system('ping -n 4 ' + hostname)
        if response == 0:
            with open("ok.txt", "a") as myfile:
                myfile.write(str(datetime.now())+'    --> Ping: '+hostname+'-->up\n')
            if hostname == '8.8.8.8':
				with open("ok.txt", "a") as myfile:
					myfile.write('\n\n')  
				print str(datetime.now())				
				time.sleep(4*60)
        else:
            print hostname, 'DOWN'
            with open("down.txt", "a") as myfile:
                myfile.write(str(datetime.now())+'    -->Ping: '+hostname+'-->pad veze \n')
                if hostname == '8.8.8.8':
                    myfile.write('\n\n')
		time.sleep(30)
		   
 
			
	

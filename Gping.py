import os
import time
from datetime import datetime 
import speedtest   
    
    
    

while True:   
    #8.8.8.8-Google 
    #192.168.1.1-Lokalni ruter 
    hostnames = [
        '8.8.8.8',
        '192.168.1.1']

    for hostname in hostnames:
        response = os.system('ping -n 2 ' + hostname)
        if response == 0:
            if hostname == '8.8.8.8':
                s = speedtest.Speedtest()
                s.get_servers()
                s.get_best_server()
                s.download()
                s.upload()
                res = s.results.dict()
                     
            print hostname, 'ok'
            with open("ok.txt", "a") as myfile:
                myfile.write(str(datetime.now())+'\n    -->'+hostname+'-->up\n')
                if hostname == '8.8.8.8' :              
                    myfile.write('  Ping:      '+str(res["ping"])+'ms \n')
                    myfile.write('  Download:  '+str(res["download"]/1024)+'Kb/s \n')
                    myfile.write('  Upload:    '+str(res["upload"]/1024)+'Kb/s \n\n\n')
            print 'sleeping 5 minutes'
            time.sleep(5*60)
        else:
            print hostname, 'DOWN'
            with open("down.txt", "a") as myfile:
                myfile.write(str(datetime.now())+'\n    -->'+hostname+'-->pad veze \n')
            print 'sleeping 0,5 minutes'
            time.sleep(30)
	

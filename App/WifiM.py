import os
import subprocess
from time import sleep


Version='022.008.001.001'

def GetVersion():
    return(str(Version))

def ChangeWifi(WIFIN,WIFIP):
    WIFIN=WIFIN.strip()
    WIFIP=WIFIP.strip()

    print(os.system("sudo ifconfig wlan0 up"))
    sleep(3)

    msj=subprocess.check_output("iw dev wlan0 link|grep SSID|awk '{print $2}'",shell=True).decode('utf8')
    red=msj.strip()
    
    if WIFIN in red:
        return True



    file=open("red.mc",'w')
    file.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev'+'\n')
    file.write('update_config=1'+'\n')
    file.write('country=AR'+'\n')
    file.write('\n')
    file.write('network={'+'\n')
    file.write('    ssid="'+str(WIFIN)+'"'+'\n')
    file.write('    psk="'+str(WIFIP)+'"'+'\n')
    file.write('    key_mgmt=WPA-PSK'+'\n')
    file.write('}')
    file.flush()
    file.close()

    print(os.system("sudo rm /etc/wpa_supplicant/wpa_supplicant.conf"))
    print(os.system("sudo cp red.mc /etc/wpa_supplicant/wpa_supplicant.conf"))
    print(os.system("sudo ifconfig wlan0 up"))
    print(os.system("sudo wpa_cli -i wlan0 reconfigure"))
    
    sleep(7)
    veces=0
    while veces<3:
        sleep(7)
        msj=subprocess.check_output("iw dev wlan0 link|grep SSID|awk '{print $2}'",shell=True).decode('utf8')
        red=msj.strip()
        veces+=1
        if red[:5]==WIFIN[:5]:
            return True
    print(os.system("sudo rm red.mc"))    
    return False
    
    
    
    #print('Ahora esta conectado a '+red)

#print(ChangeWifi('MagneticashAP','5050505050'))





import json
import os
import sys
from time import sleep

#------IMPORTO DE ACUERDO AL MODULO ACTIVO--------------------
sys.path.append('/home/pi/CheckBalance/')


 #importa aplicacion y vista actual
rutaPrincipal='/home/pi/CheckBalance/App/'
sys.path.append(rutaPrincipal)
#-------------------------------------------------------------


#import ViewM
#primer punto Soft
#segundo punto Modulo
#tercer modificaciones de app
Version='0.1'

JsonSetup=""
FirstStart=True

def GetJsonSetup():
    global JsonSetup
    if not JsonSetup:
        JsonSetup=Read_SetupJson()
    return JsonSetup

def SetJsonSetup(q):
    global JsonSetup
    if q:
        JsonSetup=q


def SaveSetup():
    global JsonSetup
    try:
        
        filename=rutaPrincipal +'setup.json'      
        if JsonSetup:
            data = JsonSetup#Read_Setup()
        else:
            return False
        

        data['Setup'] = 0

        #os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        return(True)


    except Exception as error:
        print(str(error) + ' Error to reset partial start counter')
        return False   

def CloseSetup():
    global JsonSetup
    try:
        
        filename=rutaPrincipal +'setup.json'      
        if JsonSetup:
            data = JsonSetup#Read_Setup()
        else:
            return False
        

        data['Setup'] = 0

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        return(True)


    except Exception as error:
        print(str(error) + ' Error to reset partial start counter')
        return False   


def GetVersion():
    return(str(Version))

def Read_SetupJson():
    global JsonSetup
    try:
        with open(rutaPrincipal +'setup.json') as json_file:
            JsonSetup = json.loads(json_file.read())        
        #print(mijson)
        return JsonSetup
    #Total_Start=mijson["Total_Start"]

    except Exception as error:
        print(error)
        return None

def Read_Setup():
    global JsonSetup
    try:
        with open('setup.json') as json_file:
            mijson = json.loads(json_file.read())
            r=Read_SetupJson()
            if r:
                JsonSetup=r #actualizo JsonGral        
        
        return mijson['Setup']
    

    except Exception as error:
        print(error)
        return('')


Read_SetupJson()


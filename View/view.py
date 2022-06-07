import webview
import os
from furl import furl #para la url en python
import sys
import os, signal
import json
from time import sleep
import time
from datetime import datetime, timedelta
import threading
from pynput import keyboard

#importo modulos
sys.path.append('/home/pi/CheckBalance/App/') #importa aplicacion y vista actual
import magnetic
import SetupM
import WifiM

#variables
listener=None
orientation = 'right'
Tarjeta=''
entrada=''
window=''
cerrarApp=False
entroConsulta=False
FueraDeServicio=False
timeoutSetup=False
canceloSetup=False
guardoSetup=False
pasoInicio=False

class Api:
    global canceloSetup
    global guardoSetup
    global timeoutSetup

    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def init(self):
        response = {
            'message': 'ok'
        }
        
        return response

    def saveSetup(self,resultJson):
        global guardoSetup
        j=SetupM.GetJsonSetup()
        j['System_url']=resultJson['ip_master']
        j['SSID']=resultJson['wifi']['ssid']
        j['Password']=resultJson['wifi']['password']
        j['orientation']=resultJson['orientation']
        SetupM.SetJsonSetup(j)
        SetupM.SaveSetup()
        print(resultJson)

        guardoSetup=True

    def cancelSetup(self):
        global canceloSetup
        print('cancelo')    
        canceloSetup=True

    def timeOutSetup(self):
        global timeoutSetup
        print('timeout')
        timeoutSetup=True

def CargoInicio():
    #cargo Defectos:----------------------
     #chargeInfo
    pa='false'

    m='false'
    


             
    amarillo="false"  

    rojo="false"  
    
    
    purpura="false"  
                        

    vv="""masterFunction(`[
    {"obj":"checkBalanceSetup","is_visible":"false","text":"null","value":"null"},
    {"obj":"progressBar","is_visible":"false","text":"null","value":"null"},
    {"obj":"checkBalanceWait","is_visible":"false","text":"null","value":"null"},
    {"obj":"backgroundImage","is_visible":"true","text":"null","value":"null"},
    {"obj":"logo","is_visible":"true","text":"null","value":"null"},
    {"obj":"balance","is_visible":"false","text":"null","value":"$"},
    {"obj":"promociones","is_visible":"false","text":"null","value":"null"},
    {"obj":"btnTarjeta","is_visible":"false","text":"null","value":"null"},
    {"obj":"btnAyuda","is_visible":"false","text":"null","value":"null"},
    {"obj":"btnConsultaSaldo","is_visible":"false","text":"null","value":"null"},
    {"obj":"btnNewCard","is_visible":"false","text":"null","value":"$2"},
    {"obj":"ilustraciones","is_visible":"false","text":"null","value":"null"},
    {"obj":"nfc","is_visible":"false","text":"null","value":"null"},
    {"obj":"swipeCard","is_visible":"false","text":"null","value":"null"},
    {"obj":"scanApp","is_visible":"false","text":"null","value":"null"},
    {"obj":"yellowWarning","is_visible":"false","text":"null","value":"null"},
    {"obj":"redWarning","is_visible":"false","text":"null","value":"null"},
    {"obj":"purpleWarning","is_visible":"false","text":"null","value":"null"},
    {"obj":"orangeWarning","is_visible":"false","text":"null","value":"null"},
    {"obj":"messageBox","is_visible":"false","text":"null","value":"null"},
    {"obj":"messageBoxError","is_visible":"false","text":"null","value":"null"},
    {"obj":"messageBoxNewCard","is_visible":"false","text":"null","value":"null"},
    {"obj":"messageBoxSlideCard","is_visible":"false","text":"null","value":"null"},
    {"obj":"messageBoxBalance","is_visible":"false","text":"null","value":"null"},
    {"obj":"finTransaccionError","is_visible":"false","text":"null","value":"null"},
    {"obj":"finTransaccionSuccess","is_visible":"false","text":"null","value":"null"},
    {"obj":"finTransaccionErrorMessage","is_visible":"false","text":"null","value":"null"},
    {"obj":"consultaSaldo","is_visible":"false","text":"null","value": "null"},
    {"obj":"consultaStandBy","is_visible":"true","text":"null","value": "null"},
    {"obj":"arrowDown","is_visible":"true","text":"null","value": "null"},
    {"obj":"finTransaccionSuccessMessage","is_visible":"false","text":"null","value":"null"},
    {"obj":"charged","is_visible":"false","text":"null","value":"null"},
    {"obj":"chargedLabel","is_visible":"false","text":"null","value":"null"},
    {"obj":"promoWonLabel","is_visible":"false","text":"null","value":"null"},
    {"obj":"promoWon","is_visible":"false","text":"null","value":"null"},
    {"obj":"modal","is_visible":"false","text":"null","value":"null"},
    {"obj":"modalTitle","is_visible":"false","text":"null","value":"null"},
    {"obj":"modalText","is_visible":"false","text":"null","value":"null"},
    {"obj":"btnModal","is_visible":"false","text":"null","value":"null"},
    {"obj":"value1","is_visible":"false","text":"null","value":"null"},
    {"obj":"value2","is_visible":"false","text":"null","value":"null"},
    {"obj":"value3","is_visible":"false","text":"null","value":"null"},
    {"obj":"value4","is_visible":"false","text":"null","value":"null"},
    {"obj":"valuePersonalizado","is_visible":"false","text":"null","value":"null"},
    {"obj":"btnBack","is_visible":"false","text":"null","value":"null"},
    {"obj":"btnBack","is_visible":"false","text":"Atras","value":"null"},
    {"obj":"itemSelected","is_visible":"false","text":"null","value":"null"},
    {"obj":"posnetIlustration","is_visible":"false","text":"null","value":"null"},
    {"obj":"posnetPersonalizado","is_visible":"false","text":"null","value":"null"},
    {"obj":"confirmBtn","is_visible":"false","text":"null","value":"null"},
    {"obj":"outOfService","is_visible":"false","text":"null","value":"null"},
    {"obj":"consultaSaldo","is_visible":"false","text":"null","value": "null"},
        {"obj":"chargeInfo","is_visible":"false","text":"null","value": "null"},
        {"obj":"chargeInfoTable","is_visible":"false","text":"null","value": "null"},
    {"obj":"outOfOrderTitle","is_visible":"false","text":"null","value":"null"}]` );"""


        
    #print(vv)
    window.evaluate_js(vv)
  
def CargoVacio():
    #cargo Defectos:----------------------
     #chargeInfo
    pa='false'

    m='false'
    


             
    amarillo="false"  

    rojo="false"  
    
    
    purpura="false"  
                        

    vv="""masterFunction(`[
        {"obj":"consultaStandBy","is_visible":"false","text":"null","value":"null"},
        {"obj":"arrowDown","is_visible":"false","text":"null","value":"null"},
        {"obj":"backgroundImage","is_visible":"true","text":"null","value":"null"},
        {"obj":"logo","is_visible":"true","text":"null","value":"null"},
        {"obj":"balance","is_visible":"false","text":"null","value":"$"""+str(0)+""""},
        {"obj":"promociones","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnTarjeta","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnAyuda","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnConsultaSaldo","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnNewCard","is_visible":"false","text":"null","value":"$2"},
        {"obj":"ilustraciones","is_visible":"false","text":"null","value":"null"},
        {"obj":"nfc","is_visible":"false","text":"null","value":"null"},
        {"obj":"swipeCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"scanApp","is_visible":"false","text":"null","value":"null"},
        {"obj":"yellowWarning","is_visible":"""+str(amarillo)+""","text":"null","value":"null"},
        {"obj":"redWarning","is_visible":"""+str(rojo)+""","text":"null","value":"null"},
        {"obj":"purpleWarning","is_visible":"""+str(purpura)+""","text":"null","value":"null"},
        {"obj":"orangeWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBox","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxError","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxNewCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxSlideCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxBalance","is_visible":"true","text":"Por favor, espere...","value":"null"},
        {"obj":"finTransaccionError","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccess","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionErrorMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccessMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"charged","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargedLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWonLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWon","is_visible":"false","text":"null","value":"null"},
        {"obj":"modal","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalTitle","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalText","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnModal","is_visible":"false","text":"null","value":"null"},
        {"obj":"value1","is_visible":"false","text":"null","value":"null"},
        {"obj":"value2","is_visible":"false","text":"null","value":"null"},
        {"obj":"value3","is_visible":"false","text":"null","value":"null"},
        {"obj":"value4","is_visible":"false","text":"null","value":"null"},
        {"obj":"valuePersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnBack","is_visible":"false","text":"null","value":"null"},
        {"obj":"itemSelected","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetIlustration","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetPersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargeInfo","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargeInfoTable","is_visible":"false","text":"null","value":"null"},
        {"obj":"outOfService","is_visible":"false","text":"null","value":"null"},
        {"obj":"outOfOrderTitle","is_visible":"false","text":"null","value":"null"},
        {"obj":"outOfOrderMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"helpScreen","is_visible":"false","text":"null","value":"null"},
        {"obj":"confirmBtn","is_visible":"false","text":"null","value":"null"}]`);"""


        
    #print(vv)
    window.evaluate_js(vv)

def TiempoEntrada():
    global t
    global entrada
    global Tarjeta
    while 1:
        if cerrarApp:
            return
        return
        if 1:#'help' not in page and 'newCardBtnActivado' not in page and 'modalTarjeta' not in page:
            if entrada !='':
                if len(entrada)>=14:
                    p=entrada.find(';')
                    if p+14==len(entrada):
                        Tarjeta=entrada[p:p+14]

                    #functions.LeerFiat=False
                        print('llego '+str(Tarjeta))
                        entrada=''
                
            
        sleep(0.001)    

def on_release(key):
    global entrada
    global t
    global Tarjeta
    global pasoInicio
    try:
        #if entrada=='':
        #    t=datetime.now() + timedelta(milliconds=300)
        #if t> datetime.now():
        if  not entroConsulta and not FueraDeServicio:#'help' not in page and 'newCardBtnActivado' not in page and 'newCardBtnActivado' not in page:#and 'consultaSaldo=true' in page  or 'help' not in page and 'newCardBtnActivado' not in page and 0>0  or 'aceptarNoComprar=true' in page or DispenserM.Estado_Tarjetero['statusTarjetas']!='red' and page.find('newCardBtnActivado=true')==-1 or 'consultaSaldo=' in page:
            entrada+=key.char
            #print('ACAAA ->'+ str(entrada))
            if entrada.find(';')<0:
                entrada=''
            if len(entrada)==15 and not entrada[14:].isnumeric():
                p=entrada.find(';')
                #if entrada.find('?'):
                
                Tarjeta=entrada[p:p+14]
                if  pasoInicio:
                    CargoVacio()
                print('llego '+str(Tarjeta))
                entrada=''
            elif len(entrada)>=17:
                Tarjeta=entrada#[p:p+17]
                
                if  pasoInicio:
                    CargoVacio()
                print('llego '+str(Tarjeta))
                entrada=''
            

        #functions.LeerFiat=False
            
        else:
            entrada=''
        
            

    except Exception as e:
        #print(e)
        a=1

def EscuchoTeclas():
    global listener
    #listener=None
    while 1:
        try:
            #if cerrarApp:
            #    return
            
            if not listener:
                
            #else:
            
                with keyboard.Listener(
                #on_press=on_press,
                on_release=on_release)as listener:
                    def terminar():
                        global cerrarApp
                        while 1:
                            if cerrarApp:
                                listener.stop()
                                #break
                            #else:
                            #    listener.join()

                            sleep(0.2)
                        

                    #threading.Thread(target=terminar).start()
                    listener.join()
            
                    break
        except Exception as e:
            print(e)
            continue

def PingMagnetic():
    global ruta
    global FueraDeServicio
    while 1:
        try:
            
            if 1:#Tarjeta:
                r=magnetic.ping()

                rr=json.loads(r)

                if rr['status']=='pong':
                    
                    print('ping OK')
                    FueraDeServicio=False
                    sleep(3)
                
                else:# 'Timeout' in rr['msg'] or '[Errno 111] Connection refused' in rr['msg']:
                    FueraDeServicio=True
                    sleep(0.1)
                
                
                

        except Exception as e:
            print("error en ping -->")
            print(e)
            continue

def software():
    global Tarjeta
    global FueraDeServicio
    global timeoutSetup
    global canceloSetup
    global guardoSetup
    global pasoInicio
    
    try:

        
        
        tf=datetime.now()+timedelta(seconds=5)
        while tf>datetime.now():
            if Tarjeta:
                CargoSetup()
                while 1:
                    if canceloSetup:
                        break
                    elif guardoSetup:
                        break
                    sleep(0.1)

                #CargoWait()
                
                #cuando sale del setup levanto datos actualizados
                JsonLeido=SetupM.GetJsonSetup()

                #paso orientacion de aplicacion
                orientation=JsonLeido['orientation']
                os.system('DISPLAY=:0 xrandr --output HDMI-1 --rotate '+ orientation)
                CargoWait2()

            elif timeoutSetup:
                break
            sleep(0.1)
        
        #configura WIFI
        data=SetupM.GetJsonSetup()
        r=WifiM.ChangeWifi(data['SSID'],data['Password'])
        if r:
            print('conecto al wifi seleccionado')
        else:
            print('NO conecto al wifi seleccionado')
            FueraDeServicio=True
            CargoFueraServicio()

        


        magnetic.Host=data['System_url']#'192.168.1.158'#158
        magnetic.Port=int(str(data['System_port']))
            

        Tarjeta=''
        pasoInicio=True

        #genero ping a magnetic:
        h=threading.Thread(target=PingMagnetic)
        h.setDaemon=False
        h.start()


        while 1:

            if FueraDeServicio:
                CargoFueraServicio()
            elif not Tarjeta:            
                CargoInicio()
            else:
                ConsultaEspecial()

            time.sleep(0.1)
    except Exception as e:
        print(e)
        CargoFueraServicio()


def change_pages(window):
    print('ok')


def CargoInicioCargando():
    #cargo Defectos:----------------------
     #chargeInfo
    pa='false'

    m='false'
   
    amarillo="false"  

    
    rojo="false"  
    
    
    purpura="false"  
                        

    vv="""masterFunction(`[
        {"obj":"checkBalanceSetup","is_visible":"false","text":"null","value":"null"},
        {"obj":"consultaStandBy","is_visible":"false","text":"null","value":"null"},
        {"obj":"arrowDown","is_visible":"false","text":"null","value":"null"},
        {"obj":"backgroundImage","is_visible":"true","text":"null","value":"null"},
        {"obj":"logo","is_visible":"true","text":"null","value":"null"},
        {"obj":"balance","is_visible":"false","text":"null","value":"$"""+str(0)+""""},
        {"obj":"promociones","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnTarjeta","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnAyuda","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnConsultaSaldo","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnNewCard","is_visible":"false","text":"null","value":"$2"},
        {"obj":"ilustraciones","is_visible":"false","text":"null","value":"null"},
        {"obj":"nfc","is_visible":"false","text":"null","value":"null"},
        {"obj":"swipeCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"scanApp","is_visible":"false","text":"null","value":"null"},
        {"obj":"yellowWarning","is_visible":"""+str(amarillo)+""","text":"null","value":"null"},
        {"obj":"redWarning","is_visible":"""+str(rojo)+""","text":"null","value":"null"},
        {"obj":"purpleWarning","is_visible":"""+str(purpura)+""","text":"null","value":"null"},
        {"obj":"orangeWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBox","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxError","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxNewCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxSlideCard","is_visible":"false","text":"null","value":"..."},
        {"obj":"messageBoxBalance","is_visible":"false","text":"Cargando sistema, Por favor, espere...","value":"null"},
        {"obj":"finTransaccionError","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccess","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionErrorMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccessMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"charged","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargedLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWonLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWon","is_visible":"false","text":"null","value":"null"},
        {"obj":"modal","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalTitle","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalText","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnModal","is_visible":"false","text":"null","value":"null"},
        {"obj":"value1","is_visible":"false","text":"null","value":"null"},
        {"obj":"value2","is_visible":"false","text":"null","value":"null"},
        {"obj":"value3","is_visible":"false","text":"null","value":"null"},
        {"obj":"value4","is_visible":"false","text":"null","value":"null"},
        {"obj":"valuePersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnBack","is_visible":"false","text":"null","value":"null"},
        {"obj":"itemSelected","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetIlustration","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetPersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargeInfo","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargeInfoTable","is_visible":"false","text":"null","value":"null"},
        {"obj":"outOfService","is_visible":"false","text":"null","value":"null"},
        {"obj":"outOfOrderTitle","is_visible":"false","text":"null","value":"null"},
        {"obj":"outOfOrderMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"helpScreen","is_visible":"false","text":"null","value":"null"},
        {"obj":"confirmBtn","is_visible":"false","text":"null","value":"null"}]`);"""


        
    #print(vv)
    window.evaluate_js(vv)



def CargoMovimientos(mov):
    #cargo Defectos:----------------------
     #chargeInfo
    
    #posnet
    pa='false' 
    
    #tarjeta nueva
    m='false'
    
    #window.evaluate_js("CargaInicio('"+str(pa)+"','"+str(m)+"','"+str(newCardPrice)+"')")

    
    ht='"Insert Money"'

    vv="""masterFunction(`[
        {"obj":"consultaStandBy","is_visible":"false","text":"null","value":"null"},
        {"obj":"arrowDown","is_visible":"false","text":"null","value":"null"},
        {"obj":"backgroundImage","is_visible":"true","text":"null","value":"null"},
        {"obj":"logo","is_visible":"true","text":"null","value":"null"},
        {"obj":"balance","is_visible":"false","text":"null","value":"$"""+str(0)+""""},
        {"obj":"promociones","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnTarjeta","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnAyuda","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnConsultaSaldo","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnNewCard","is_visible":"false","text":"null","value":"$2"},
        {"obj":"ilustraciones","is_visible":"false","text":"null","value":"null"},
        {"obj":"nfc","is_visible":"false","text":"null","value":"null"},
        {"obj":"swipeCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"scanApp","is_visible":"false","text":"null","value":"null"},
        {"obj":"yellowWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"redWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"purpleWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"orangeWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBox","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxError","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxNewCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxSlideCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxBalance","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionError","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccess","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionErrorMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"consultaSaldo","is_visible":"true","text":"null","value":"""+mov+"""},
        {"obj":"finTransaccionSuccessMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"charged","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargedLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWonLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWon","is_visible":"false","text":"null","value":"null"},
        {"obj":"modal","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalTitle","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalText","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnModal","is_visible":"false","text":"null","value":"null"},
        {"obj":"value1","is_visible":"false","text":"null","value":"null"},
        {"obj":"value2","is_visible":"false","text":"null","value":"null"},
        {"obj":"value3","is_visible":"false","text":"null","value":"null"},
        {"obj":"value4","is_visible":"false","text":"null","value":"null"},
        {"obj":"valuePersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnBack","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnBack","is_visible":"false","text":"Volver","value":"null"},
        {"obj":"itemSelected","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetIlustration","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetPersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"confirmBtn","is_visible":"false","text":"null","value":"null"}]`);"""
    window.evaluate_js(vv)

def CargoError(Error):
    #cargo Defectos:----------------------
     #chargeInfo

    #posnet
    pa='false' 
    
    #tarjeta nueva
    m='false'
    


    

    #window.evaluate_js("CargaInicio('"+str(pa)+"','"+str(m)+"','"+str(newCardPrice)+"')")

    
    ht='"Insert Money"'
    
    if Error=='Aplicacion':
        appV='true'
    else:
        appV='false'

    

    if appV=='false':
        vv="""masterFunction(`[
            {"obj":"consultaStandBy","is_visible":"false","text":"null","value":"null"},
            {"obj":"arrowDown","is_visible":"false","text":"null","value":"null"},
            {"obj":"backgroundImage","is_visible":"true","text":"null","value":"null"},
            {"obj":"logo","is_visible":"true","text":"null","value":"null"},
            {"obj":"balance","is_visible":"false","text":"null","value":"$"""+str(0)+""""},
            {"obj":"promociones","is_visible":"false","text":"null","value":"null"},
            {"obj":"btnTarjeta","is_visible":"""+str(pa)+""","text":"null","value":"null"},
            {"obj":"rejectedScreen","is_visible":"""+str(appV)+""","text":"null","value":"null"},
            {"obj":"btnAyuda","is_visible":"false","text":"null","value":"null"},
            {"obj":"btnConsultaSaldo","is_visible":"false","text":"null","value":"null"},
            {"obj":"btnNewCard","is_visible":"false","text":"null","value":"$2"},
            {"obj":"ilustraciones","is_visible":"false","text":"null","value":"null"},
            {"obj":"nfc","is_visible":"false","text":"null","value":"null"},
            {"obj":"swipeCard","is_visible":"false","text":"null","value":"null"},
            {"obj":"scanApp","is_visible":"false","text":"null","value":"null"},
            {"obj":"yellowWarning","is_visible":"false","text":"null","value":"null"},
            {"obj":"redWarning","is_visible":"false","text":"null","value":"null"},
            {"obj":"purpleWarning","is_visible":"false","text":"null","value":"null"},
            {"obj":"orangeWarning","is_visible":"false","text":"null","value":"null"},
            {"obj":"messageBox","is_visible":"false","text":"null","value":"null"},
            {"obj":"messageBoxError","is_visible":"false","text":"null","value":"null"},
            {"obj":"messageBoxNewCard","is_visible":"false","text":"null","value":"null"},
            {"obj":"messageBoxSlideCard","is_visible":"false","text":"null","value":"null"},
            {"obj":"messageBoxBalance","is_visible":"false","text":"null","value":"null"},
            {"obj":"finTransaccionError","is_visible":"true","text":"null","value":"null"},
            {"obj":"finTransaccionSuccess","is_visible":"false","text":"null","value":"null"},
            {"obj":"finTransaccionErrorMessage","is_visible":"true","text":"null","value":\""""+Error+"""\"},
            {"obj":"finTransaccionSuccessMessage","is_visible":"false","text":"null","value":"null"},
            {"obj":"charged","is_visible":"false","text":"null","value":"null"},
            {"obj":"chargedLabel","is_visible":"false","text":"null","value":"null"},
            {"obj":"promoWonLabel","is_visible":"false","text":"null","value":"null"},
            {"obj":"promoWon","is_visible":"false","text":"null","value":"null"},
            {"obj":"modal","is_visible":"false","text":"null","value":"null"},
            {"obj":"modalTitle","is_visible":"false","text":"null","value":"null"},
            {"obj":"modalText","is_visible":"false","text":"null","value":"null"},
            {"obj":"btnModal","is_visible":"false","text":"null","value":"null"},
            {"obj":"value1","is_visible":"false","text":"null","value":"null"},
            {"obj":"value2","is_visible":"false","text":"null","value":"null"},
            {"obj":"value3","is_visible":"false","text":"null","value":"null"},
            {"obj":"value4","is_visible":"false","text":"null","value":"null"},
            {"obj":"valuePersonalizado","is_visible":"false","text":"null","value":"null"},
            {"obj":"btnBack","is_visible":"false","text":"null","value":"null"},
            {"obj":"itemSelected","is_visible":"false","text":"null","value":"null"},
            {"obj":"posnetIlustration","is_visible":"false","text":"null","value":"null"},
            {"obj":"posnetPersonalizado","is_visible":"false","text":"null","value":"null"},
            {"obj":"confirmBtn","is_visible":"false","text":"null","value":"null"}]`);"""
    else:
            vv="""masterFunction(`[
        {"obj":"consultaStandBy","is_visible":"false","text":"null","value":"null"},
        {"obj":"arrowDown","is_visible":"false","text":"null","value":"null"},
        {"obj":"backgroundImage","is_visible":"true","text":"null","value":"null"},
        {"obj":"logo","is_visible":"true","text":"null","value":"null"},
        {"obj":"balance","is_visible":"false","text":"null","value":"$"""+str(0)+""""},
        {"obj":"promociones","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnTarjeta","is_visible":"""+str(pa)+""","text":"null","value":"null"},
        {"obj":"rejectedScreen","is_visible":"""+str(appV)+""","text":"null","value":"null"},
        {"obj":"btnAyuda","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnConsultaSaldo","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnNewCard","is_visible":"false","text":"null","value":"$2"},
        {"obj":"ilustraciones","is_visible":"false","text":"null","value":"null"},
        {"obj":"nfc","is_visible":"false","text":"null","value":"null"},
        {"obj":"swipeCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"scanApp","is_visible":"false","text":"null","value":"null"},
        {"obj":"yellowWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"redWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"purpleWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"orangeWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBox","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxError","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxNewCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxSlideCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxBalance","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionError","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccess","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionErrorMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccessMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"charged","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargedLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWonLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWon","is_visible":"false","text":"null","value":"null"},
        {"obj":"modal","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalTitle","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalText","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnModal","is_visible":"false","text":"null","value":"null"},
        {"obj":"value1","is_visible":"false","text":"null","value":"null"},
        {"obj":"value2","is_visible":"false","text":"null","value":"null"},
        {"obj":"value3","is_visible":"false","text":"null","value":"null"},
        {"obj":"value4","is_visible":"false","text":"null","value":"null"},
        {"obj":"valuePersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnBack","is_visible":"false","text":"null","value":"null"},
        {"obj":"itemSelected","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetIlustration","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetPersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"confirmBtn","is_visible":"false","text":"null","value":"null"}]`);"""
    #print(vv)
    window.evaluate_js(vv)

    #\""""+Error+"""\"

def CargoSetup():
    #cargo Defectos:----------------------
     #chargeInfo
    pa='false'

    m='false'
    


    

    #window.evaluate_js("CargaInicio('"+str(pa)+"','"+str(m)+"','"+str(newCardPrice)+"')")

    
    ht='"Insert Money"'

    """ document.getElementById('outOfService').style.display = 'flex';
    document.getElementById('outOfOrderTitle').innerHTML = title;
    document.getElementById('outOfOrderMessage').innerHTML = message; """

    vv="""masterFunction(`[
        {"obj":"checkBalanceSetup","is_visible":"true","text":"null","value":"null"},
        {"obj":"progressBar","is_visible":"false","text":"null","value":"null"},
        {"obj":"checkBalanceWait","is_visible":"false","text":"null","value":"null"},
        {"obj":"consultaStandBy","is_visible":"false","text":"null","value":"null"},
        {"obj":"arrowDown","is_visible":"false","text":"null","value":"null"},
        {"obj":"backgroundImage","is_visible":"true","text":"null","value":"null"},
        {"obj":"logo","is_visible":"false","text":"null","value":"null"},
        {"obj":"outOfService","is_visible":"false","text":"null","value":"null"},
        {"obj":"outOfOrderTitle","is_visible":"false","text":"","value":"null"},
        {"obj":"outOfOrderMessage","is_visible":"false","text":"","value":"null"},
        {"obj":"balance","is_visible":"false","text":"null","value":"null"},
        {"obj":"promociones","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnTarjeta","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnAyuda","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnConsultaSaldo","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnNewCard","is_visible":"false","text":"null","value":"$2"},
        {"obj":"ilustraciones","is_visible":"false","text":"null","value":"null"},
        {"obj":"nfc","is_visible":"false","text":"null","value":"null"},
        {"obj":"swipeCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"scanApp","is_visible":"false","text":"null","value":"null"},
        {"obj":"yellowWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"redWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"purpleWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"orangeWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBox","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxError","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxNewCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxSlideCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxBalance","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionError","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccess","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionErrorMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccessMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"charged","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargedLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWonLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWon","is_visible":"false","text":"null","value":"null"},
        {"obj":"modal","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalTitle","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalText","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnModal","is_visible":"false","text":"null","value":"null"},
        {"obj":"value1","is_visible":"false","text":"null","value":"null"},
        {"obj":"value2","is_visible":"false","text":"null","value":"null"},
        {"obj":"value3","is_visible":"false","text":"null","value":"null"},
        {"obj":"value4","is_visible":"false","text":"null","value":"null"},
        {"obj":"valuePersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnBack","is_visible":"false","text":"null","value":"null"},
        {"obj":"itemSelected","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetIlustration","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetPersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"confirmBtn","is_visible":"false","text":"null","value":"null"}]`);"""
    #print(vv)
    window.evaluate_js(vv)

    JsonLeido=SetupM.GetJsonSetup()
    j={}
    j['ip_master']=JsonLeido['System_url']
    j['wifi']={}
    j['wifi']['ssid']=JsonLeido['SSID']
    j['wifi']['password']=JsonLeido['Password']
    j['orientation']=JsonLeido['orientation']
    j=json.dumps(j)
    window.evaluate_js("chargeSetup('"+ j +"')")


def CargoWait():
    #cargo Defectos:----------------------
     #chargeInfo
    pa='false'

    m='false'
    


    

    #window.evaluate_js("CargaInicio('"+str(pa)+"','"+str(m)+"','"+str(newCardPrice)+"')")

    
    ht='"Insert Money"'

    """ document.getElementById('outOfService').style.display = 'flex';
    document.getElementById('outOfOrderTitle').innerHTML = title;
    document.getElementById('outOfOrderMessage').innerHTML = message; """

    vv="""masterFunction(`[
        {"obj":"progressBar","is_visible":"true","text":"null","value":"null"},
        {"obj":"checkBalanceWait","is_visible":"true","text":"null","value":"null"},
        {"obj":"consultaStandBy","is_visible":"false","text":"null","value":"null"},
        {"obj":"arrowDown","is_visible":"false","text":"null","value":"null"},
        {"obj":"backgroundImage","is_visible":"true","text":"null","value":"null"},
        {"obj":"logo","is_visible":"true","text":"null","value":"null"},
        {"obj":"outOfService","is_visible":"false","text":"null","value":"null"},
        {"obj":"outOfOrderTitle","is_visible":"false","text":"","value":"null"},
        {"obj":"outOfOrderMessage","is_visible":"false","text":"","value":"null"},
        {"obj":"balance","is_visible":"false","text":"null","value":"null"},
        {"obj":"promociones","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnTarjeta","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnAyuda","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnConsultaSaldo","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnNewCard","is_visible":"false","text":"null","value":"$2"},
        {"obj":"ilustraciones","is_visible":"false","text":"null","value":"null"},
        {"obj":"nfc","is_visible":"false","text":"null","value":"null"},
        {"obj":"swipeCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"scanApp","is_visible":"false","text":"null","value":"null"},
        {"obj":"yellowWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"redWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"purpleWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"orangeWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBox","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxError","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxNewCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxSlideCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxBalance","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionError","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccess","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionErrorMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccessMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"charged","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargedLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWonLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWon","is_visible":"false","text":"null","value":"null"},
        {"obj":"modal","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalTitle","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalText","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnModal","is_visible":"false","text":"null","value":"null"},
        {"obj":"value1","is_visible":"false","text":"null","value":"null"},
        {"obj":"value2","is_visible":"false","text":"null","value":"null"},
        {"obj":"value3","is_visible":"false","text":"null","value":"null"},
        {"obj":"value4","is_visible":"false","text":"null","value":"null"},
        {"obj":"valuePersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnBack","is_visible":"false","text":"null","value":"null"},
        {"obj":"itemSelected","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetIlustration","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetPersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"confirmBtn","is_visible":"false","text":"null","value":"null"}]`);"""
    #print(vv)
    window.evaluate_js(vv)

    window.evaluate_js("fillProgressBar(4)")

def CargoWait2():
    #cargo Defectos:----------------------
     #chargeInfo
    pa='false'

    m='false'
    


    

    #window.evaluate_js("CargaInicio('"+str(pa)+"','"+str(m)+"','"+str(newCardPrice)+"')")

    
    ht='"Insert Money"'

    """ document.getElementById('outOfService').style.display = 'flex';
    document.getElementById('outOfOrderTitle').innerHTML = title;
    document.getElementById('outOfOrderMessage').innerHTML = message; """

    vv="""masterFunction(`[
        {"obj":"checkBalanceSetup","is_visible":"false","text":"null","value":"null"},
        {"obj":"progressBar","is_visible":"false","text":"null","value":"null"},
        {"obj":"checkBalanceWait","is_visible":"true","text":"null","value":"null"},
        {"obj":"consultaStandBy","is_visible":"false","text":"null","value":"null"},
        {"obj":"arrowDown","is_visible":"false","text":"null","value":"null"},
        {"obj":"backgroundImage","is_visible":"true","text":"null","value":"null"},
        {"obj":"logo","is_visible":"true","text":"null","value":"null"},
        {"obj":"outOfService","is_visible":"false","text":"null","value":"null"},
        {"obj":"outOfOrderTitle","is_visible":"false","text":"","value":"null"},
        {"obj":"outOfOrderMessage","is_visible":"false","text":"","value":"null"},
        {"obj":"balance","is_visible":"false","text":"null","value":"null"},
        {"obj":"promociones","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnTarjeta","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnAyuda","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnConsultaSaldo","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnNewCard","is_visible":"false","text":"null","value":"$2"},
        {"obj":"ilustraciones","is_visible":"false","text":"null","value":"null"},
        {"obj":"nfc","is_visible":"false","text":"null","value":"null"},
        {"obj":"swipeCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"scanApp","is_visible":"false","text":"null","value":"null"},
        {"obj":"yellowWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"redWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"purpleWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"orangeWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBox","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxError","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxNewCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxSlideCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxBalance","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionError","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccess","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionErrorMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccessMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"charged","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargedLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWonLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWon","is_visible":"false","text":"null","value":"null"},
        {"obj":"modal","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalTitle","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalText","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnModal","is_visible":"false","text":"null","value":"null"},
        {"obj":"value1","is_visible":"false","text":"null","value":"null"},
        {"obj":"value2","is_visible":"false","text":"null","value":"null"},
        {"obj":"value3","is_visible":"false","text":"null","value":"null"},
        {"obj":"value4","is_visible":"false","text":"null","value":"null"},
        {"obj":"valuePersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnBack","is_visible":"false","text":"null","value":"null"},
        {"obj":"itemSelected","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetIlustration","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetPersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"confirmBtn","is_visible":"false","text":"null","value":"null"}]`);"""
    #print(vv)
    window.evaluate_js(vv)

    #window.evaluate_js("fillProgressBar(4)")


def CargoFueraServicio():
    #cargo Defectos:----------------------
     #chargeInfo
    pa='false'

    m='false'
    


    

    #window.evaluate_js("CargaInicio('"+str(pa)+"','"+str(m)+"','"+str(newCardPrice)+"')")

    
    ht='"Insert Money"'

    """ document.getElementById('outOfService').style.display = 'flex';
    document.getElementById('outOfOrderTitle').innerHTML = title;
    document.getElementById('outOfOrderMessage').innerHTML = message; """

    vv="""masterFunction(`[
        {"obj":"consultaStandBy","is_visible":"false","text":"null","value":"null"},
        {"obj":"arrowDown","is_visible":"false","text":"null","value":"null"},
        {"obj":"backgroundImage","is_visible":"true","text":"null","value":"null"},
        {"obj":"logo","is_visible":"true","text":"null","value":"null"},
        {"obj":"outOfService","is_visible":"true","text":"null","value":"null"},
        {"obj":"outOfOrderTitle","is_visible":"true","text":"","value":"null"},
        {"obj":"outOfOrderMessage","is_visible":"true","text":"","value":"null"},
        {"obj":"balance","is_visible":"false","text":"null","value":"null"},
        {"obj":"promociones","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnTarjeta","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnAyuda","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnConsultaSaldo","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnNewCard","is_visible":"false","text":"null","value":"$2"},
        {"obj":"ilustraciones","is_visible":"false","text":"null","value":"null"},
        {"obj":"nfc","is_visible":"false","text":"null","value":"null"},
        {"obj":"swipeCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"scanApp","is_visible":"false","text":"null","value":"null"},
        {"obj":"yellowWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"redWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"purpleWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"orangeWarning","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBox","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxError","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxNewCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxSlideCard","is_visible":"false","text":"null","value":"null"},
        {"obj":"messageBoxBalance","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionError","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccess","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionErrorMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"finTransaccionSuccessMessage","is_visible":"false","text":"null","value":"null"},
        {"obj":"charged","is_visible":"false","text":"null","value":"null"},
        {"obj":"chargedLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWonLabel","is_visible":"false","text":"null","value":"null"},
        {"obj":"promoWon","is_visible":"false","text":"null","value":"null"},
        {"obj":"modal","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalTitle","is_visible":"false","text":"null","value":"null"},
        {"obj":"modalText","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnModal","is_visible":"false","text":"null","value":"null"},
        {"obj":"value1","is_visible":"false","text":"null","value":"null"},
        {"obj":"value2","is_visible":"false","text":"null","value":"null"},
        {"obj":"value3","is_visible":"false","text":"null","value":"null"},
        {"obj":"value4","is_visible":"false","text":"null","value":"null"},
        {"obj":"valuePersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"btnBack","is_visible":"false","text":"null","value":"null"},
        {"obj":"itemSelected","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetIlustration","is_visible":"false","text":"null","value":"null"},
        {"obj":"posnetPersonalizado","is_visible":"false","text":"null","value":"null"},
        {"obj":"confirmBtn","is_visible":"false","text":"null","value":"null"}]`);"""
    #print(vv)
    window.evaluate_js(vv)

  
def ConsultaEspecial():
    global entroConsulta
    global volverAtras
    global Tarjeta
    global aceptarNoComprar
    global FueraDeServicio
    
    try:
        

        entroConsulta=True
        volverAtras=False
        t=''
        cr=0
        bn=0
        qty=0
        tks=0
        data={}
        if Tarjeta :
            
            print("antes de consultar saldo "+ str(datetime.now()))
            r=magnetic.balance(Tarjeta[-14:])
            print("desp de consultar saldo "+ str(datetime.now()))
            #r.json.dumps(r)
            r=json.loads(r)
            data=''
            if r['status']==True:
                if r['exists']==True:
                    cr=str(r['Balances']['saldo'])
                    bn=str(r['Balances']['bonus'])
                    qty=str(r['Balances']['quantity'])
                    tks=str(r['Balances']['tickets'])
                    data=magnetic.movements(Tarjeta[-14:])#database.GetHistory(Tarjeta)
                    t=Tarjeta
                else:
                    #if r['msg']=='card is not in database':
                        #r['msg']='Su tarjeta no esta en el sistema'

                    #ruta=rutaSin+'&btnBackFromConsultaDeSaldo=true&finTransaccionError=true&msjError='+str(r['msg'])#'index.html?&noIlustraciones=true&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&swipeCard='+swipeCard+'&scanApp='+scanApp+'&saldo='+ str(0) +'&simbolo=$&newCardPrice='+ str(newCardPrice)+'&finTransaccionError=true&msjError='+str(r['msg'])
                    #Tarjeta=''
                    #CambioVentana(window)
                    #sleep(2) 
                    #LeerConsulta=False
                    #print('no esta o error')
                    #window.evaluate_js("setFinTransaccion('finTransaccionError','true','"+r['msg']+"')")
                    CargoError(r['msg'])
                    sleep(2)
                    #window.evaluate_js("setFinTransaccion('finTransaccionError','false','"+r['msg']+"')")
                    vence=datetime.now()

            else:
                if r['msg']=='Rejected card!!!':
                        #r['msg']='Tarjeta restringida !'                                                
                        #ruta=rutaSin+'&btnBackFromConsultaDeSaldo=true&finTransaccionError=true&msjError='+str(r['msg'])#'index.html?&noIlustraciones=true&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&swipeCard='+swipeCard+'&scanApp='+scanApp+'&saldo='+ str(0) +'&simbolo=$&newCardPrice='+ str(newCardPrice)+'&finTransaccionError=true&msjError='+str(r['msg'])
                        #Tarjeta=''
                        #CambioVentana(window)
                        #window.evaluate_js("setFinTransaccion('finTransaccionError','true','"+r['msg']+"')")
                        CargoError(r['msg'])
                        sleep(2)
                        #window.evaluate_js("setFinTransaccion('finTransaccionError','false','"+r['msg']+"')")
                        vence=datetime.now()

                        
                        #LeerConsulta=False
                else:#if 'Timeout' in r['msg'] or '[Errno 111] Connection refused' in r['msg']:
                    
                    m="Can't connect to Server<br>Thank you!"
                    CargoFueraServicio()
                    FueraDeServicio=True
                    
                    while FueraDeServicio:#PingMagneticCarga()==False:
                        sleep(0.5)
                        
                    LeerConsulta=False
                    Tarjeta=''

                    #ruta=rutaSin#'index.html?outOfService=true&msjOutOfService=<p>Can't connect to Server<br>Thank you!'
                    #CambioVentana(window)
                    #m="Can't connect to Server<br>Thank you!"
                    #window.evaluate_js("setOutOfService('"+m+"', 'false')")
                    


        
        
            if data !='' and 'Error' not in data:
                
                data=data.replace('"',"'")
                #OcultoInicio()
                
                m='{"chargeInfoTable":"'+str(data)+'","card_number":"'+str(Tarjeta)+'","credits_value":"'+str(cr)+'","bonus_value":"'+str(bn)+'","tks_value":"'+str(tks)+'","qty_value":"'+str(qty)+'"}'
                CargoMovimientos(m)
                print("desp de mostrar saldo "+ str(datetime.now()))
                #window.evaluate_js("setChargeInfoTable('"+str(data)+"','"+str(Tarjeta)+"','$"+str(cr)+"','$"+str(bn)+"','"+str(tks)+"','"+str(qty)+"');")
                
                vence2=datetime.now() + timedelta(seconds=5)
                #sleep(3)
                while 1:
                    sleep(0.01)
                    if vence2 < datetime.now() or not entroConsulta:
                        vence=datetime.now()
                        entroConsulta=False
                        volverAtras=False
                        break
        entroConsulta=False        
        Tarjeta=''
        
        
    except Exception as e:
        print(e)
        Tarjeta=''
        entroConsulta=False

def on_loaded():
    sleep(4)
    CargoWait()
    window.show()
    software()

def CreoVentana():
    global window
    #levanto json de config
    while 1:
        try:
            sleep(5)
            print('Leo Json')
            JsonLeido=SetupM.GetJsonSetup()

            #paso orientacion de aplicacion
            orientation=JsonLeido['orientation']
            os.system('DISPLAY=:0 xrandr --output HDMI-1 --rotate '+ orientation)

            #escucho lectoras:
            try:
                th=threading.Thread(target=TiempoEntrada).start()

                if not listener:
                    pteclas=threading.Thread(target=EscuchoTeclas)#.start()
                    #pteclas=multiprocessing.Process(target=EscuchoTeclas)
                    if pteclas:
                        #pteclas.setDaemon=True
                        pteclas.start()

            except Exception as e:    
                print(e)

            

            api=Api()
            window = webview.create_window('Consulta de saldo test', 'Cajero-UI/index.html', fullscreen=True,js_api=api,hidden=True)
            window.loaded += on_loaded
            webview.start(change_pages, window, http_server=True)
            break
        except Exception as e:
            print(e)
            continue

CreoVentana()
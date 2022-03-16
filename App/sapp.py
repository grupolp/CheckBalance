
Version='1.0'

import sys
#----------------------------------------------------------------------------------

#importo puntero
try:
    
    sys.path.append('/home/pi/CheckBalance/App/')
    sys.path.append('/home/pi/CheckBalance/View/')
    #from View import *
    #from View import view
    #import view
    
    
    from time import sleep
    from datetime import datetime
    import threading
    
except Exception as e:
    print(e)


def GetVersion():
    return(str(Version))






def Start():
    
    #read current Divise
    try:

        print('VA A ABRIR APP')
        view.CreoVentana()
    except Exception as e:
        print(e)
    """ while 1:

        ruta='index.html?nfc=1&mercadoPago=1?insertCash=1&swipeCard=1&card=1&scanApp=1&newCard=1&saldo='+ str(functions.SALDO) +'&simbolo=$'#'C:\\Users\\LP\\Documents\\Interface_2020\\CajeroNuevo\\setup.html?t='+str(t)+'&p='+str(p)+'&r='+str(r)+'&spacs='+str(spacs)+'&appacs='+str(appacs)+'&vacs='+str(vacs)+'&spacv='+str(spacv)+'&appacv='+str(appacv)+'&vacv='+str(vacv)+'&c='+str(customer)
        sview.CambioVentana(ruta)
        functions.LeerFiat=True
        functions.LeerIngresoFiat()
        sleep(0.1) """
#if sys.argv[0]=='startApp' or sys.argv[1]=='startApp':
print('llego start en APP')
#Start()


import socket
import time
import json
from time import sleep
from datetime import datetime

import sys
import re
#----------------------------------------------------------------------------------
#importo puntero

sys.path.append('/home/pi/CheckBalance//App/') #importa aplicacion y vista actual
import SetupM

rutaVista='/home/pi/CheckBalance//View/'
sys.path.append(rutaVista)











Host=''
Port=0

date_open=''
terminal=''
card_price=0
JsonPromociones=''
def client_program(data1):
    try:
        host = Host  # as both code is running on same pc
        port = Port  # socket server port number
        
        client_socket = socket.socket()  # instantiate
        if 'ping' in json.dumps(data1):
            client_socket.settimeout(1)
        else:
            client_socket.settimeout(5)
        client_socket.connect((host, port))  # connect to the server
        if 'ping' in json.dumps(data1):
            client_socket.settimeout(1)
        else:
            client_socket.settimeout(5)

        

        
        client_socket.send(data1.encode())  # send message
        data =b''
        d=b''
        while not d:
            try:
                d= client_socket.recv(2048)  # receive response
                data=data + d
                d=b''
                r=data.decode()
                if r:
                    rr=json.loads(r)
                    break
                else:
                    data =b''
                    rr={}    
            except socket.timeout:
                    print('sale por time out')
                    return '{"status":"Error","msg":"time out"}' 
            except socket.error:
                    print('sale por error')
                    return '{"status":"Error","msg":"error"}' 
            except Exception as e:
                print(e)
                
                if  not client_socket:
                    print('sale por time out')
                    return '{"status":"Error","msg":"time out"}' 
                elif 'ping' in json.dumps(data1):
                    data =b''
                    rr={} 
                    return '{"status":"Error","msg":"error"}' 
                else:
                    #sigue escuchando para rellenar json
                    continue
            
        data=data.decode()



        client_socket.close()  # close the connection

        if data:
            return data
        else:
            return '{"status":"Error","msg":"error"}'
    except Exception as e:
        return '{"status":"Error","msg":"'+str(e)+'"}'

    

    

    

def opencash(name,device):
    global Host
    global Port
    global date_open
    global card_price
    #Host=h
    #Port=p
    data='{"transaction_type": "opencash","cashier_name": "'+str(name)+'","cashier_id": 0,"device_name": "'+str(device)+'","datetime_device": datetime.now()}'
    r=client_program(data)
    rr=json.loads(r)    
    if rr['status']=='ok':
        date_open=rr['dateopen']
        card_price=rr['card_price']

    return r

def balance(mpl):
    #ts=time.time()
    #ts=str(ts)[:8]
    data='{"transaction_type": "balance","mpl": "'+str(mpl)+'"}'
    data=json.dumps(data)
    data=json.loads(data)
    r=client_program(str(data))
    return r

def getBonus(promo):
    return (promo.get('total_gift_value'))

def getPrecio(promo):
    return (promo.get('precio','total_gift_value'))

def GetPromotions():
    global JsonPromociones
    #ts=time.time()
    #ts=str(ts)[:8]
    data='{"transaction_type": "promotions"}'
    data=json.dumps(data)
    data=json.loads(data)
    r=client_program(str(data))
    if r==']':
        r='[]'
    if r:
        rj=json.loads(r)
        #rj.sort(key=getBonus,reverse=True)
        promociones=[]
        precioAnt=0
        PromocionesFinal=[]
        rj.sort(key=getPrecio,reverse=True)
        for promo in rj:
            if precioAnt==0 or precioAnt==promo['precio']:
                promociones.append(promo)
                precioAnt=promo['precio']
                #PromocionesFinal.append(promo)
            else:
                #primero ordeno iguales
                
                #agrego distinto
                x=0
                for p in promociones:
                    if PromocionesFinal:
                        if p['precio']==PromocionesFinal[len(PromocionesFinal)-1]['precio'] or p['total_gift_value']==PromocionesFinal[len(PromocionesFinal)-1]['total_gift_value']:
                            #if p['tipopromo']=='Free Card' and  PromocionesFinal[len(PromocionesFinal)-1]['tipopromo']!='Free Card' or p['tipopromo']!='Free Card' and  PromocionesFinal[len(PromocionesFinal)-1]['tipopromo']=='Free Card':
                            #    PromocionesFinal.append(p)
                            print('No agrega por mismo precio  menor/igual premio')
                        else:
                            PromocionesFinal.append(p)
                    else:
                        PromocionesFinal.append(p)
                    #if len(PromocionesFinal)==2:
                    #    break
                    
                
                if promo not in promociones:
                    promociones.append(promo)
                    precioAnt=promo['precio']
                #promociones=[]
                

        # Agregue esto para que si hay mismo precio con mayor beneficio deje la que es mayor
        if not PromocionesFinal:
            x=0
            promociones.sort(key=getBonus,reverse=True)
            for p in promociones:
                if PromocionesFinal:
                    if p['precio']==PromocionesFinal[len(PromocionesFinal)-1]['precio'] or p['total_gift_value']==PromocionesFinal[len(PromocionesFinal)-1]['total_gift_value']:
                        #if p['tipopromo']=='Free Card' and  PromocionesFinal[len(PromocionesFinal)-1]['tipopromo']!='Free Card' or p['tipopromo']!='Free Card' and  PromocionesFinal[len(PromocionesFinal)-1]['tipopromo']=='Free Card':
                        #    PromocionesFinal.append(p)
                        print('No agrega por mismo precio  menor/igual premio')
                    else:
                        PromocionesFinal.append(p)
                else:
                    PromocionesFinal.append(p)
                #if len(PromocionesFinal)==2:
                #    break
                
            if PromocionesFinal:
                promociones=PromocionesFinal
        #------------------1
        #     
        if promo not in promociones:
            promociones.append(promo)
            precioAnt=promo['precio']

        if promociones:
            PromocionesFinal=promociones
        rj=PromocionesFinal
        for promo in rj:
            s=promo['nombrepromo']            
            ns=re.sub(r"[^a-zA-Z0-9., ]","",s)
            if ns=='':
                ns='Promo'
            print(ns)
            promo['nombrepromo']=ns
        color=1

        rj.sort(key=getPrecio)
        #elimina mayor precio/menor beneficio
        vanterior=0
        panterior=0
        borre=True
        while borre==True:
            borre=False
            for promo in rj:
                if panterior==0:
                    promoanterior=promo
                    panterior=promo['precio']
                    vanterior=promo['total_gift_value']
                    tpanterior=promo['tipopromo']
                else:
                    if panterior<=promo['precio'] and vanterior>promo['total_gift_value'] and tpanterior!='Charge+':
                        rj.remove(promo)
                        borre=True
                    elif   panterior == promo['precio'] and vanterior<promo['total_gift_value']:# todo este elif lo agregue para que verifique si tiene q borrar mismo precio mayor ganancia
                        rj.remove(promoanterior)
                        promoanterior=promo
                        panterior=promo['precio']
                        vanterior=promo['total_gift_value']
                        tpanterior=promo['tipopromo']
                        borre=True
                    else:
                        promoanterior=promo
                        panterior=promo['precio']
                        vanterior=promo['total_gift_value']
                        tpanterior=promo['tipopromo']
            



        
        for promo in rj:
            promo['color']=color
            color+=1
            if color>6:
                color=1
        r=json.dumps(rj)
    

        
    JsonPromociones=r
    return r

def ping():
    #ts=time.time()
    #ts=str(ts)[:8]
    data='{"status": "ping"}'
    data=json.dumps(data)
    data=json.loads(data)
    r=client_program(str(data))
    return r

def movements(mpl):
    #ts=time.time()
    #ts=str(ts)[:8]
    data='{"transaction_type": "movements","mpl": "'+str(mpl)+'"}'
    #data=json.dumps(data)
    data=json.loads(data)
    r=client_program(str(data))
    return r

def Charge(mpl,vmpl,amount,name,device,cp,oc,buy,promotions):
    #ts=time.time()
    #ts=str(ts)[:8]
    if promotions:
        if buy=='0' and promotions[0]['tipopromo']=='Free Card':
            promotions='[]'#json.dumps(promotions)
        else:
            promotions=json.dumps(promotions)
    else:
        promotions='[]'
    
    
    data='{"opencash":"'+str(oc)+'","transaction_type": "charge","mpl": "'+str(mpl)+'","vmpl": "'+str(vmpl)+'","msj": "","transaction_id": "0123456786","charge": [{"balance_type": "Pesos","amount": '+str(amount)+',"cashier_name": "'+str(name)+'","cashier_id": 0,"device_name": "'+str(device)+'","datetime_device":"'+ str(datetime.now())+'","payments": [{"currency": "Pesos","payment_method": "efectivo","Amount": '+str(amount)+',"rate": 1.0 }],"total_payment_local_currency": '+str(amount)+',"promotions": '+str(promotions)+'}],"card_price":'+str(cp) + ',"buycard":'+str(buy) +'}'
    data=json.dumps(data)
    data=json.loads(data)
    r=client_program(str(data))
    return r


#revisar timeout cuando saca tarjeta

data=SetupM.GetJsonSetup()


Host=data['System_url']#'192.168.1.158'#158
Port=int(str(data['System_port']))#r=Charge(';9999999999999','',15.50,'CajeroEze','Autocashier',1.0,'10/08/21 12:05:08')


#r=Posnet_Init(Host,Port)
#r=Posnet_Config()
#print(r)
""" while 1:
    r=Posnet_Status()
    r=json.loads(r)
    r=r['Resultado']['Status']
    if r!='Ocupado':
        break
    sleep(1)
#r=Posnet_Config()
#print(r)
r=Posnet_Pay(20,1)
r=json.loads(r)
Charge(';9999999999999','',15.50,'CajeroEze','Autocashier',1.0,'10/08/21 12:05:08')esultado']['Cod']==15:
    r=Posnet_Config()
    print(r) """

#r=Posnet_Pay(20,1)
#r=json.loads(r)
#print(r)



#now = str(time.ctime((time.time()+40000000000)))
#print("t,"opencash":"'+str(oc)+'"he now time is " + str(now))
#r=GetPromotions()
#r=Charge(';6140011477687','',15.50,'CajeroEze','Autocashier',1.0,'10/08/21 12:05:08',0,r)
#r=balance(';6230012703787')
#print(r)
#sleep(1)
"""r=GetPromotions()
#print(r)
mj=json.loads(r)
s=10
promociones=[]
promoPagada=[]
for x in range(len(mj)):
    if 1:#len(promociones)<5:
        if s<=mj[x]['precio']:
            promociones.append(mj[x])
        else:
            promoPagada=[]
            promoPagada.append(mj[x])
    else:
        break
if len(promociones)>5:
    while len(promociones)>5:
        promociones.remove(promociones[len(promociones)-1])
else:
    p=promociones
    promociones=[]
    promociones.append(promoPagada[0])
    for pr in p:
        promociones.append(pr)
pmostrar=[]
for promo in promociones:

    armo=[]
    parmo=[]
    parmo.append(promo['bonus'])
    parmo.append(promo['credits'])
    parmo.append(promo['tickets'])
    tipo=''
    if s<promo['precio']:
        #falta
        tipo=''
        falta='$'+str((s-promo['precio'])*-1)
    elif s==promo['precio']:
        tipo='igual'
        #carga exacta
        falta='$0'
    else :
        tipo='mayor'    
        falta='$0'
        #more than
    
    armo.append(promo['nombrepromo'])
    armo.append(promo['precio'])
    armo.append(parmo)
    armo.append(str(falta))
    #verifico si tengo que mostrar
    if tipo=='igual' and promo['tipopromo']=='Charge+' or tipo=='igual' and promo['tipopromo']=='Free Card':
        pmostrar.append(armo)
    elif tipo=='mayor' and promo['tipopromo']=='Charge++' or tipo=='igual' and promo['tipopromo']=='Free Card':
        pmostrar.append(armo)
    elif tipo=='':
        pmostrar.append(armo)
#promociones=[["10%20da%201",10,[10,0,0],"$0"]]
#print(promociones)
print(pmostrar)"""
#for x in range(len(mj)):
#    print(mj[x]['precio'])

#promos=json.loads(GetPromotions())
#p=sorted(promos,key=lambda x:(x[1],x[7]))

#p=sorted(promos.items(),key=lambda x:(x[1],x[7]))
#print(promos)
#print(GetPromotions())
""" promociones=json.loads(GetPromotions())
s=50
puseEstrella=False
color=1
for promo in promociones:
    if promo['precio']==s:
        promo['estrella']=True
        promo['habilitada']=True
        puseEstrella=True
    promo['color']=color
    color+=1
    if color >6:
        color=1
promociones.sort(key=getBonus,reverse=True)#invierto para ver mayor a menor
for promo in promociones:
    if promo['precio']>s:
        promo['habilitada']=True
        
        for promoMenor in promociones:
            if promoMenor['tipopromo']!='Charge+' and promoMenor['precio']<=s and not puseEstrella:
                promoMenor['estrella']=True
                promoMenor['habilitada']=True
                puseEstrella=True
                
if not puseEstrella:
    promociones.sort(key=getBonus,reverse=True)#invierto para ver mayor a menor
    for promoMenor in promociones:
        if promoMenor['tipopromo']!='Charge+' and promoMenor['precio']<=s and not puseEstrella:
            promoMenor['estrella']=True
            promoMenor['habilitada']=True
            puseEstrella=True
promociones.sort(key=getPrecio)#invierto para ver mayor a menor
while len(promociones)>5:
    promociones.remove(promociones[len(promociones)-1])

pmostrar=[]
PromocionAPagar=[]
falta='$0'
promociones.sort(key=getPrecio)
for promo in promociones:

    armo=[]
    armo.append(promo['nombrepromo'])
    armo.append(promo['precio'])
    parmo=[]
    
    parmo.append(promo['bonus'])
    parmo.append(promo['credits'])
    parmo.append(promo['tickets'])
    tipo=''
    if s<promo['precio']:
        #falta
        tipo=''
        falta='$'+str(round((s-promo['precio'])*-1,2))
    elif s==promo['precio'] or 'estrella' in promo:                
        falta='$0'
    armo.append(parmo)
    armo.append(falta)
    if 'habilitada' in promo:
        pmostrar.append(armo)
promociones.sort(key=getBonus)
for promo in promociones:
    if 'estrella' in promo:
        PromocionAPagar.append(promo)

print(pmostrar)
print('paga ' + str(PromocionAPagar) )"""
#print(GetPromotions())


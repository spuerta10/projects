import random #modulo para sacar los numeros aleatorios
import time #modulo para retraso de ejecuciones
import os #modulo para generar el reporte diario
from chemicals import colector
import statistics #modulo para hallar la media
import requests
from ploting import graphs
from db import to_DB


TOKEN = "" #Ubidots token here
DEVICE_LABEL = "water-station"


def percentage(capacity): #hallar porcentaje capacidad tanque
    # 100% -> 250000 
    # capacity -> x 
    capacity = round(((100*capacity)/200000),2)
    return capacity

                               
def capture(percentage, turb, chemicals): #captura de la informacion
    #time.sleep(0.3)#captura de datos cada .3 segundos
    sensors = {
    'water-level' : percentage, #nivel agua en los tanques
    'turbidity' : turb, #turbidez del agua entrante a los tanques
    'aluminum_sulfate' : chemicals['coagulant'], #cantidad actual de quimicos
    'limestone' : chemicals['flocculant'],
    'chlorine' : chemicals['chlorine'],
    }
    return sensors


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        #time.sleep(1)

    # Processes results
    #print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def send_IoT(percentage, turb, chemicals):
    payload = capture(percentage, turb, chemicals)
    post_request(payload)
    

def low_chemicals(chemicals, chemicals_used): #aviso de que me quedan pocos quimicos
    if chemicals_used['coagulant']*1.5 >= chemicals['coagulant'] or chemicals_used['flocculant']*1.5 >= chemicals['flocculant'] or chemicals_used['chlorine']*1.5 >= chemicals['chlorine']:
        #alguno de los quimicos no alcanza para los sgtes 1.5 dias
        return True
    else:
        #todo bien los quimicos dan abasto
        return False


def turbidity():
    turb = random.randint(250,800) #turbidez del agua 250 - 800
    return turb


def daily_report(day, chemicals_used, turb, tank,prices, day1 = {}, day2 = {}, day3 = {},low=None): #generar archivo del resumen del dia
    #inex 1 -> coagulant, idex 2 -> flocculant, index 3 -> chlorine
    tdays = int(day) 

    day1 = day1
    day2 = day2
    day3 = day3

    if tdays %4 == 0: #cada 4 dias sacar reportes de los 3 previos
        path = f'C:\\Users\\Admin\\Desktop\\output\\dia-{tdays}'
        os.mkdir(path)
        file = open(path+f"\\dia-{int(day)}.txt", "w")
        if low == True:
            file.write('¡ALERTA! Bajo nivel de quimicos')
        file.write(f'\nQuimicos usados en el dia: {int(day)}')
        file.write('\nCoagulant : '+(str(chemicals_used['coagulant']))+' mg')
        file.write('\nFlocculant : '+(str(chemicals_used['flocculant']))+' mg')
        file.write('\nChlorine : '+(str(chemicals_used['chlorine']))+ ' ml')
        file.write('\nPrecios de los quimicos: ')
        file.write('\nCoagulant : '+str(int((chemicals_used['coagulant']*prices[0])))+'$')
        file.write('\nFlocculant : '+str(int((chemicals_used['flocculant']*prices[1])))+'$')
        file.write('\nChlorine : '+str((chemicals_used['chlorine']*prices[2]))+'$')
        file.write('\nInformacion sobre turbidez del agua: ')
        if max(turb) > 780:
            file.write('\n¡ALERTA! Maxima turbidez del agua: '+str(max(turb)))
        else:
            file.write('\nMaxima turbidez del agua: '+str(max(turb)))
        file.write('\nTurbidez del agua media: '+str(statistics.mean(turb)))
        file.write('\nMinima turbidez del agua encontrada: '+str(min(turb)))
        file.write('\nInformacion sobre niveles de los tanques:')
        file.write('\nMaximo almacenamiento del tanque: '+str(max(tank)))
        file.write('\nMedia de almacenamiento del tanque: '+str(statistics.mean(tank)))
        file.write('\nMinimo almacenamiento del tanque: '+str(min(tank)))
        graphs(day1, day2, day3, path)
        tdays= 0
    
    else:
        file = open(f'C:\\Users\\Admin\\Desktop\\output\\dia-{int(day)}.txt', "w")
        if low == True:
            file.write('¡ALERTA! Bajo nivel de quimicos')
        file.write(f'\nQuimicos usados en el dia: {int(day)}')
        file.write('\nCoagulant : '+(str(chemicals_used['coagulant']))+' mg')
        file.write('\nFlocculant : '+(str(chemicals_used['flocculant']))+' mg')
        file.write('\nChlorine : '+(str(chemicals_used['chlorine']))+ ' ml')
        file.write('\nPrecios de los quimicos: ')
        file.write('\nCoagulant : '+str(int((chemicals_used['coagulant']*prices[0])))+'$')
        file.write('\nFlocculant : '+str(int((chemicals_used['flocculant']*prices[1])))+'$')
        file.write('\nChlorine : '+str((chemicals_used['chlorine']*prices[2]))+'$')
        file.write('\nInformacion sobre turbidez del agua: ')
        if max(turb) > 780:
            file.write('\n¡ALERTA! Maxima turbidez del agua: '+str(max(turb)))
        else:
            file.write('\nMaxima turbidez del agua: '+str(max(turb)))
        file.write('\nTurbidez del agua media: '+str(statistics.mean(turb)))
        file.write('\nMinima turbidez del agua encontrada: '+str(min(turb)))
        file.write('\nInformacion sobre niveles de los tanques:')
        file.write('\nMaximo almacenamiento del tanque: '+str(max(tank)))
        file.write('\nMedia de almacenamiento del tanque: '+str(statistics.mean(tank)))
        file.write('\nMinimo almacenamiento del tanque: '+str(min(tank)))


def tank(stime):
    chemicals = {
        'coagulant': 10000000,#mg
        'flocculant': 8000000,#mg
        'chlorine': 20000, #mL
    }
    day1 = {}
    day2 = {}
    day3 = {}
    prices = colector()
    sdays = 0
    tlevels = [] #porcentaje de niveles del tanque
    wturb = []
    info = {}
    
    chemicals_used = { #quimicos usados
    'coagulant' : 0,
    'flocculant' : 0,
    'chlorine' : 0,
    }

    less_70 = False
    less_15 = False
    capacity = 200000
    demand = 5000#random.uniform(0.2, 2)
    turb = turbidity()
    #agua entrante al tanque
    incoming = 1000 #1.2
    #intime -> tiempo de ejecucion que lleva el programa
    for intime in range(1,stime+1):
        sdays+=1

        turb = turbidity()
        wturb.append(turb)

        if percentage(capacity) < 70:
            if percentage(capacity) < 15:
                less_15 = True
                entered = 1000
                print('Baja demanda')
                demand = 200#random.uniform(0.2, 0.6)
            else:
                if less_15 and percentage(capacity) <= 60:
                    print('Baja de demanda') 
                    demand = 200#random.uniform(0.2, 0.6)
                else:
                    demand = 1000#random.uniform(0.2, 2)

            less_70 = True
            #print('Agua entrando al tanque')
            capacity += incoming #1.2
            chemicals_used['coagulant'] += (25 * incoming)#mg
            chemicals_used['flocculant'] += (15 * incoming)#mg
            chemicals_used['chlorine'] += (0.05 * incoming)#ml
        else:
            if less_70 and percentage(capacity) <= 95:
                #print('Agua entrando al tanque')
                capacity += incoming #1.2
                chemicals_used['coagulant'] += (25 * incoming)#mg
                chemicals_used['flocculant'] += (15 * incoming)#mg
                chemicals_used['chlorine'] += (0.05 * incoming)#ml
            else:
                print('Deja de entrar agua al tanque')
                capacity += 0    
        print(f'Capacidad del tanque: {percentage(capacity)}')
        tlevels.append(percentage(capacity))
        #send_IoT(percentage(capacity), turb, chemicals)
        #time.sleep(0.7)#Demanda de agua cada segundo
        capacity-=demand
        print(f'Tanque - {demand}')
        if sdays/480 == 1: #86400
            day1 = {
                'coagulant' : int(chemicals_used['coagulant']),
                'flocculant' : int(chemicals_used['flocculant']),
                'chlorine' : int(chemicals_used['chlorine']),
                'coagulant_price' : int((chemicals_used['coagulant']*prices[0])), 
                'flocculant_price' : int((chemicals_used['flocculant']*prices[1])),
                'chlorine_price' : (chemicals_used['chlorine']*prices[2]),
                'avg_tanks' : statistics.mean(tlevels),
                'max_tanks' : max(tlevels),
                'min_tanks' : min(tlevels),
                'avg_turb' : statistics.mean(wturb),
                'max_turb' : max(wturb),
                'min_turb' : min(wturb),
                'dia' : int(intime/480), #86400
            }
        if sdays /480 == 2:
            day2 = {
                'coagulant' : int(chemicals_used['coagulant']),
                'flocculant' : int(chemicals_used['flocculant']),
                'chlorine' : int(chemicals_used['chlorine']),
                'coagulant_price' : int((chemicals_used['coagulant']*prices[0])), 
                'flocculant_price' : int((chemicals_used['flocculant']*prices[1])),
                'chlorine_price' : (chemicals_used['chlorine']*prices[2]),
                'avg_tanks' : statistics.mean(tlevels),
                'max_tanks' : max(tlevels),
                'min_tanks' : min(tlevels),
                'avg_turb' : statistics.mean(wturb),
                'max_turb' : max(wturb),
                'min_turb' : min(wturb),
                'dia' : int(intime/480), #86400
            }
        if sdays /480 == 3:
            day3 = {
                'coagulant' : int(chemicals_used['coagulant']),
                'flocculant' : int(chemicals_used['flocculant']),
                'chlorine' : int(chemicals_used['chlorine']),
                'coagulant_price' : int((chemicals_used['coagulant']*prices[0])), 
                'flocculant_price' : int((chemicals_used['flocculant']*prices[1])),
                'chlorine_price' : (chemicals_used['chlorine']*prices[2]),
                'avg_tanks' : statistics.mean(tlevels),
                'max_tanks' : max(tlevels),
                'min_tanks' : min(tlevels),
                'avg_turb' : statistics.mean(wturb),
                'max_turb' : max(wturb),
                'min_turb' : min(wturb),
                'dia' : int(intime/480), #86400
            }
        chemicals['coagulant'] -= chemicals_used['coagulant']
        chemicals['flocculant'] -= chemicals_used['flocculant']
        chemicals['chlorine'] -= chemicals_used['chlorine']
        #termina un dia; 1 dia -> 480s
        if intime % 480 == 0: #86400
            low = low_chemicals(chemicals, chemicals_used)
            if low == True:
                chemicals['coagulant'] = 10000000
                chemicals['flocculant'] = 8000000
                chemicals['chlorine'] = 20000
            daily_report((intime/86400),chemicals_used, wturb, tlevels,prices, day1,day2,day3,low)
            #to_DB((int(intime/480)),max(wturb),max(tlevels),min(wturb),min(tlevels),(statistics.mean(tlevels)),(statistics.mean(wturb)))
            chemicals_used['coagulant'] = 0
            chemicals_used['floacculant'] = 0
            chemicals_used['chlorine'] = 0
            wturb = []
            tlevels = []
            
        if sdays /480 == 4: #cuando se llega al dia 4 #86400
            #Limpio el almacenamiento de los dias anteriores  
            for key in day1.keys():   
                day1[key] = 0
                day2[key] = 0
                day3[key] = 0
            sdays = 0


def run():
    days = int(input('Digite el numero de dias ->'))
    stime = 480 * days #86400
    tank(stime)


if __name__ == '__main__':
    run()

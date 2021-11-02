import random
import matplotlib.pyplot as plt #graficas para el report
from matplotlib.backends.backend_pdf import PdfPages


""" day1 = {'coagulant': 12000000, 
'flocculant': 7200000, 
'chlorine': 24000, 
'coagulant_price': 4411764705, 
'flocculant_price': 82056904, 
'chlorine_price': 67.55555555555556, 
'avg_tanks': 55.94716666666667, 
'max_tanks': 100.0, 
'min_tanks': 15.07, 
'avg_turb': 506.9166666666667, 
'max_turb': 777, 
'min_turb': 275,
'dia':1,}

day2 = {'coagulant': 12000000, 
'flocculant': 14400000, 
'chlorine': 24000, 
'coagulant_price': 4411764705, 
'flocculant_price': 164113809, 
'chlorine_price': 67.55555555555556, 
'avg_tanks': 63.045291666666664, 
'max_tanks': 67.27, 
'min_tanks': 58.67, 
'avg_turb': 498.4583333333333, 
'max_turb': 796, 
'min_turb': 291,
'dia': 2,}

day3 = {'coagulant': 12000000, 
'flocculant': 21600000, 
'chlorine': 24000, 
'coagulant_price': 4411764705, 
'flocculant_price': 246170713, 
'chlorine_price': 67.55555555555556, 
'avg_tanks': 63.0050625, 
'max_tanks': 67.75, 
'min_tanks': 58.97, 
'avg_turb': 566.125, 
'max_turb': 780, 
'min_turb': 266, 
'dia': 3,} """


def graphs(day1, day2, day3, path): #funcion para realizar las graficas del daily report
    colors =  ['blue','green','red','cyan','magenta']
    fig1 = plt.figure()
    x1 = ['sulfato\n'+str(day1['coagulant'])+' mg'+f" dia{day1['dia']}", 'piedra caliza\n'+str(day1['flocculant'])+' mg'+f" dia{day1['dia']}", 'cloro\n'+str(day1['chlorine'])+' mL'+f" dia{day1['dia']}",
        'sulfato\n'+str(day2['coagulant'])+' mg'+f" dia{day2['dia']}", 'piedra caliza\n'+str(day2['flocculant'])+' mg'+f" dia{day2['dia']}", 'cloro\n'+str(day2['chlorine'])+' mL'+f" dia{day2['dia']}",
        'sulfato\n'+str(day3['coagulant'])+' mg'+f" dia{day3['dia']}", 'piedra caliza\n'+str(day3['flocculant'])+' mg'+f" dia{day3['dia']}", 'cloro\n'+str(day3['chlorine'])+' mL'+f" dia{day3['dia']}"]
    y1 = [day1['coagulant_price'], day1['flocculant_price'], day1['chlorine_price'],
        day2['coagulant_price'], day2['flocculant_price'], day2['chlorine_price'],
        day3['coagulant_price'], day3['flocculant_price'], day3['chlorine_price']]
    plt.barh(x1,y1,color=colors[random.randint(0,len(colors)-1)])
    plt.xlabel('Precio')
    plt.title("Quimicos y precio")
    plt.tight_layout()
    fig1.savefig(path+f"\\quimicos-precio-dias{day1['dia']},{day2['dia']},{day3['dia']}.pdf",dpi=300)
    fig2 = plt.figure()
    x2 = [f'avg almacenamiento dia{day1["dia"]}', f'min almacenamiento dia{day1["dia"]}', f'max almacenamiento dia{day1["dia"]}',
        f'avg almacenamiento dia{day2["dia"]}', f'min almacenamiento dia{day2["dia"]}', f'max almacenamiento dia{day2["dia"]}',
        f'avg almacenamiento dia{day3["dia"]}', f'min almacenamiento dia{day3["dia"]}', f'max almacenamiento dia{day3["dia"]}']
    y2 = [day1['avg_tanks'],day1['min_tanks'], day1['max_tanks'],
        day2['avg_tanks'],day2['min_tanks'], day2['max_tanks'],
        day3['avg_tanks'],day3['min_tanks'], day3['max_tanks']]

    plt.barh(x2,y2,color =colors[random.randint(0,len(colors)-1)])
    plt.ylabel('')
    plt.title("Informacion tanques")
    plt.tight_layout()
    fig2.savefig(path+f"\\info-tanques-dias{day1['dia']},{day2['dia']},{day3['dia']}.pdf",dpi=300)

    fig3 = plt.figure()
    x3 = [f'avg turbidez dia{day1["dia"]}', f'min turbidez dia{day1["dia"]}', f'max turbidez dia{day1["dia"]}',
    f'avg turbidez dia{day2["dia"]}', f'min turbidez dia{day2["dia"]}', f'max turbidez dia{day2["dia"]}',
    f'avg turbidez dia{day3["dia"]}', f'min turbidez dia{day3["dia"]}', f'max turbidez dia{day3["dia"]}']

    y3 = [day1['avg_turb'],day1['min_turb'], day1['max_turb'],
    day2['avg_turb'],day2['min_turb'], day2['max_turb'],
    day3['avg_turb'],day3['min_turb'], day3['max_turb']]

    plt.barh(x3,y3,color =colors[random.randint(0,len(colors)-1)])
    plt.ylabel('')
    plt.title("Turbidez del agua")
    plt.tight_layout()
    fig3.savefig(path+f"\\turbidez-dias{day1['dia']},{day2['dia']},{day3['dia']}.pdf",dpi=300)

    
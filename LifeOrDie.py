import os
from tqdm import tqdm
from time import sleep

print('''
       ---------------------------------------------
                 ╔╗──╔═╗───────────╔╗
                 ║║──║╔╝───────────║║
                 ║║╔╦╝╚╦══╗╔══╦═╗╔═╝╠╦══╗
                 ║║╠╬╗╔╣║═╣║╔╗║╔╝║╔╗╠╣║═╣   
                 ║╚╣║║║║║═╣║╚╝║║─║╚╝║║║═╣
                 ╚═╩╝╚╝╚══╝╚══╩╝─╚══╩╩══╝
       ---------------------------------------------

       
       estamos preparando el juego..

''')
for i in tqdm(range(50)):
    sleep(.1)

run = os.system
run('clear')

print(''' 

        Desde el 2020 se presento un viruz en cual iba a hacer erradicado por 'la vacuna'
        pero no estabamos preparados para lo que se venia...

''')

jugador = input("digite nombre del jugador: ")

run('clear')

print(f'''

        Hola! {jugador},en este momento estudias en el colegio guanenta en la ciudad llamada San Gil, 
        estas iniciando un nuevo año de clases nada fuera de lo normal, al pasar el tiempo debes ir 
        tomando desiciones para poder sobrevivir y crear tu propio destino asi que
        Life Or Die

''')
print('''
        presiona la tecla 'Enter' para continuar
''')
input()
run('clear')
run('python3 cap1-1.py')

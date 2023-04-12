import os
import time
run=os.system

print('''
    vas corriendo en busca de la puerta trasera de la institucion, Afortunadamnete esta el portero en la
    salida con la puerta abierta, el portero te dice que no puedes salir hasta que den la orden.

    Ahora tienes que decidir...

    1) esperar hasta que den la orden de salida      /       2) escaparse sin importar que

''')
      
cap13 = float(input())

if cap13 == 1:
    print('''

    un grupo de infectados  viene corriendo hacia ti y te conviertes en uno de ellos... 

    ''')

    print('''
        presiona la tecla 'Enter' para continuar
    ''')
      
    input()

    run('clear') 

    print('''

    has escojido mal tu destino... estas muerto

    lo quieres intentar denuevo? si o no

    ''')
    rep1 = input()
    if rep1 == 'no':
        print('''
                        GAME OVER
        ''')
        time.sleep(2)
        run('exit')
    elif rep1 == 'si':
        run('clear && python3 cap1-3.py')

elif cap13 == 2:
    run('clear && python3 cap1-4.py')
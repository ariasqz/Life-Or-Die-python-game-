import os
import time
run = os.system

print('''

        El profesor evacua rapidamente a los estudiantes del salon y nos ubican en la salida del colegio 
        con los demas estudiantes, el rector del colegio dijo que no iban a abrir la puerta hasta que todos
        estuvieramos en la salida.

''')

print('''
        presiona la tecla 'Enter' para continuar
''')
      
input()

run('clear') 

print('''

        derrepente se escuchan unos gritos que provienen de la enfermeria, algunos estudiantes y profesores
        salen corriendo de ese sector.

        Ahora tienes que decidir...

        1)buscar otra salida rapidamente       /       2) ir a investigar que está pasando en la enfermería

''')
      
cap12 = int(input())

if cap12 == 2:
        print(''''

                Al llegar a la enfermeria un grupo de infectados te atacan y mueres al instante

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

        if rep1 == 'si':
                run('clear && python3 cap1-2.py')

elif cap12 == 1:
        run('clear && python3 cap1-3.py')
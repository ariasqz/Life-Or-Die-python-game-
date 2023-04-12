import os
import time
run=os.system

print('''

        Al salir del colegio, buscas rapidamente tu telefono para llamar a tus padres y contarles 
        lo que está pasando en el colegio, pero tu telefono está sin batería. pero afortunadamente a 
        pocos metros puedes ver a un profesor que está en el parqueadero del colegio y a un policia 
        hablando por telefono.

    1) ir al parqueadero para hablar con el profesor      2) ir con el policia a pedir ayuda

''')

cap4 =int(input())
run('clear')
if cap4 == 1:
    print('''

        llegas a donde está el profesor y le cuentas lo que esta pasando en el colegio, el profesor 
        se rie y no te cree nada de lo que estas diciendo, pero a los pocos minutos se escucha un estruendo 
        que proviene de la puerta principal del colegio.
    
    ''')
    print('''
            presiona la tecla 'Enter' para continuar
    ''')
      
    input()

    run('clear && python3 cap1-5.py') 

elif cap4 == 2:
    print('''
    
        te dirijes hacia el policia y le cuentas la situacion, te dice que te quedes en este mismo sitio mientras que
        el se dirije a la puerta principal del colegio a investigar. 
    
    ''')
    print('''
            presiona la tecla 'Enter' para continuar
    ''')
      
    input()

    run('clear') 

    print('''

        al llegar a la puerta principal, esta se abre bruscamente saliendo todos los estudiantes que se infectaron 
        atacando al policia. al ver esto sales corriendo tratando de que no te alcancen, pero ellos son mas rapidos que tu...

        Estas muerto, has tomando la desidicion incorrecta.

    ''')

    print('''
            presiona la tecla 'Enter' para continuar
    ''')
      
    input()

    run('clear') 

    print('''
        Lo quieres intentar de nuevo? si o no 
    ''')

rep1 = input()
if rep1 == 'no':
    print('''
                    GAME OVER
    ''')
    time.sleep(2)
    run('exit')

elif rep1 == 'si':
    run('clear && python3 cap1-4.py')




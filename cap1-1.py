import time
import os
run=os.system

print('''

        capitulo 1: un dia muy especial

''')
print('''
        te encuentras ingresando al colegio, hoy es tu primer dia presencial, porfin te pudiste
        reencontrar con tus amigos despues de 1 año de cuarentena debido a la pandemia y 
        la vacunacion. te ubican en tu respectivo salon y comienza tu primera clase.
''')
print('''
        presiona la tecla 'Enter' para continuar
''')
input()

run('clear')


print('''

        al tomar tu asiento, notas que al lado tuyo hay un compañero que al parecer tiene sintomas
        de algun tipo de alergia.

        ahora tienes que decidir...

        1) acercarse y preguntarle que le sucede      /    2) avisarle al profesor discretamente

''')
cap11 = int(input("elige una opcion de tu destino: "))

if cap11 == 2:
    print('''

            te acercas al profesor y le informas sobre el estado en el que se encuentra un compañero
            de tu salon, El profesor inmediatamente lo retira de la clase y lo envia a la enfermeria del colegio. 
    
    ''')
    print('''
        presiona la tecla 'Enter' para continuar
    ''')
    input()
    run('clear')
   
    print('''
                despues el profesor continua su clase, Al pasar una hora anunciaron por el sonido del colegio
                sobre una evacuacion inmediata debido a un alumno con un tipo de virus desconocido muy peligroso

    ''')
    print('''
                presiona la tecla 'Enter' para continuar
    ''')
    input()
    run('clear')


    run('python3 cap1-2.py')

elif cap11 == 1:
    print('''

            te acercas y te dice que se ha sentido muy mal desde que lo vacunaron, al terminar
            la conversacion accidentalmente tose en frente tuyo y a lo pocos minutos te empiezas
            a sentir con los mismos sintomas
            
    ''')

    print('''
        presiona la tecla 'Enter' para continuar
    ''')
    input()
    run('clear')

    print(f'''

            has escojido mal tu destino... estas muerto
    
    ''')
    print('''

            lo quieres intentar denuevo? si o no
    
    ''')
    rep1 = input()
    if rep1 == 'si':
        run('clear && python3 cap1-1.py')
        

    elif rep1 == 'no':
       print('''
                GAME OVER        
       ''')
       time.sleep(2)
       run('exit')








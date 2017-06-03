# -*- coding: utf-8 -*-
import random


def run():
    number_found = True
    random_number = random.randint(0, 20)

    while number_found:
        number = int(raw_input('Intenta un Numero: '))
        if number == random_number:
            print('Felicidades. Encontraste el numero')
            number_found = False
        elif number > random_number:
            print('El numero es mas pequeño')
        else:
            print('El numero es mas grande')
if __name__ == '__main__':
    run()
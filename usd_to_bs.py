# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
    usd_to_bs = 6112.88
    return usd_to_bs * ammount

def run():
    print('C A L C U L A D O R A   D E   D I V I S A S')
    print('Convierte Dolares a Bolivares')
    print('')

    ammount = float(raw_input('Ingresa la cantidad de dolares que quieres convertir a bolivares: '))
    result = foreign_exchange_calculator(ammount)

    print('{} dolares son Bs {}'. format(ammount, result))
    print('')

if __name__ == '__main__':
    run()
# -*- coding: utf-8 -*-

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def run():
    number = int(raw_input('Escribe un numero: '))
    result = fact(number)
    print("{}! es {}".format(number, result))

if __name__ == '__main__':
    run()
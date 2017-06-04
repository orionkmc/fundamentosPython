# -*- coding: utf-8 -*-

def protected(func):
    def wrapper(password):
        if password == '123':
            return func()
        else:
            print('Contraseña incorrecta.')
    return wrapper


@protected
def protected_func():
    print('Tu contraseña es correcta.')

if __name__ == '__main__':
    password = str(raw_input('Ingresa tu contraseña: '))

    protected_func(password)
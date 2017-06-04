# -*- coding: utf-8 -*-
import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    make_square(dave)
    turtle.mainloop()

def make_square(dave):
    length = int(raw_input('Tamaño del cuadrado: '))

    for i in range(4):
        make_line_and_turn(dave, 100)
        dave.left(90)

def make_line_and_turn(dave, length):
    dave.forward(length)

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
    
    def update_contact(self, contact):
        name = str(raw_input('Escribe el nuevo nombre del contacto: '))
        phone = str(raw_input('Escribe el nuevo teléfono del contacto: '))
        email = str(raw_input('Escribe el nuevo email del contacto: '))

        contact.name = name
        contact.phone = phone
        contact.email = email
        print('*********')
        print('Contacto Guardado')
        print('*********')
        self._save()

    def update(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self.update_contact(contact)
                break
        else:
            self._not_found()

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _save(self):
        with open('contact.csv', 'w')as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('*********')
        print('no encontramos el contacto')
        print('*********')

def run():
    contact_book = ContactBook()

    with open('contact.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(raw_input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el telefono del contacto: '))
            email = str(raw_input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(raw_input('Escribe el nombre del contacto que quiere actualizar: '))
            contact_book.update(name)

        elif command == 'b':
            name = str(raw_input('Escribe el nombre del contacto que quiere buscar: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(raw_input('Escribe el nombre del contacto que quiere eliminar: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()

#coding=utf8
import sys, shelve
#基于shelve的简单数据库

def store_person(db):
    """
    Query user for data and store it in the shelf object
    """
    pid = raw_input('Enter unique ID number: ')
    person = {}
    person['name'] = raw_input('Enter name: ')
    person['age'] = raw_input('Enter age: ')
    person['phone'] = raw_input('Enter phone number: ')
    db[pid] = person

def lookup_person(db):
    """
    Query user for ID and desired field, and fetch the corresponding data from the shelf object
    """
    pid = raw_input('Enter ID number: ')
    field = raw_input('What would you like to know? (name, age, phone) ')
    field = field.strip().lower()
    print field.capitalize() + ':', db[pid][field]

def print_help():
    print 'The available commons are: '
    print 'store :Stores information about a person'
    print 'lookup :Looks up a person from ID number'
    print 'quit  :Save changes and exit'
    print '?   :Print this message'

def enter_command():
    cmd = raw_input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:         #return之前finally中的代码会被执行噢
        database.close()



if __name__ == '__main__':
    main()

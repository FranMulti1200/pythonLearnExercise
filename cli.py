#from functions import get_todos, write_todos
from modules import functions
import time
text = """ Multilines coment
Principles of productivity:
Managing your inflow.
Systemizing everything that repeats 
"""
now = time.strftime("%b %d, %Y %W:%M:%S")
print("It is", now)
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        #file = open('files/subfiles/todos.txt', 'r')
        #todos = file.readlines()
        #file.close()

        todos = functions.get_todos()

        todos.append(todo+'\n')

        #file = open('files/subfiles/todos.txt', 'w' )
        #file.writelines(todos)
        #file.close()

        functions.write_todos(todos)



    elif user_action.startswith('show'):
        #file = open('files/subfiles/todos.txt', 'r')
        #todos = file.readlines()
        #file.close()a

        todos = functions.get_todos()

        # new_todos = []
        # for item in todos:
            #new_item = item.strip('\n')
            #new_todos.append(new_item)
        # Bucle for en una linea
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            # item = item.title()
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
        #print(f"Lenght is {index+1}")
        #print(len(todos))
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos()
            print('Here is todos existing', todos)

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number-1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todos_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
        #case _:
            #print("Hey, you entered an unknown command")
    else:
        print("Command is not valid!")


print('Bye!')
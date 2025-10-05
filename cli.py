from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    if user_action.startswith('add'):
        todo = user_action[4:].strip()

        todos = get_todos()

        todos.append(todo.capitalize() + "\n")

        write_todos(todos, 'todos.txt')

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos, 'todos.txt')

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = get_todos()

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos, 'todos.txt')

            message = f"{todo_to_remove} was removed from list"
            print(message)

        except IndexError:
            print("There is no item with that number")
            continue

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid!")
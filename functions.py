def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list
    of to do items.
    """
    with open(filepath, 'r') as todos_file:
        fetched_todos = todos_file.readlines()
        print("Fetched todos:", fetched_todos)
        return fetched_todos

def write_todos(new_todos, filepath="todos.txt"):
    """ Write the to do items list in a text file """
    with open(filepath, 'w') as todos_file:
        todos_file.writelines(new_todos)
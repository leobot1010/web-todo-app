FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns list of todo items  """
    with open(filepath, 'r') as file_local:
        return file_local.readlines()


def write_todos(todos_write, filepath=FILEPATH):
    """ Writes the updated todo items to the text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_write)


if __name__ == '__main__':
     print("hello from functions")






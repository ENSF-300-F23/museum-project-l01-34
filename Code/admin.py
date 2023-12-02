from print_tables import *

def get_command_or_check_select(string, delimiter, index):
    return string.partition(delimiter)[index]

def get_column_names(command):
    cur.execute(command)
    return list(cur.column_names)

def sql_commands():
    command = input("\n0-Return\nEnter Command:\n")
    select_checker = get_command_or_check_select(command, " ", 0)
    if command == 0:
        return
    elif select_checker == 'SELECT':
        From = get_command_or_check_select(command, "FROM ", 2)
        column_names = get_column_names(command)
        cur.execute(command)
        get_columns(From, column_names, " ")
        cur.execute(command)
        get_table(From, column_names)
    else:
        cur.execute(command)
    sql_commands()

def open_sql_file():
    file_name = input("Enter file path and name: ")
    fd = open(file_name, 'r')
    sqlfile = fd.read()
    fd.close()
    sqlCommands = sqlfile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cur.execute(command)
        except (IOError):
            print("Command skipped")
    return
            
while True:
    print("\n1-SQL Commands\n2-Run SQL File\n0-Exit")
    dir_index = int(input("\nEnter the number corresponding to your choice: "))
    if dir_index == 0:
        break
    elif dir_index == 1:
        sql_commands()
    elif dir_index == 2:
        open_sql_file()
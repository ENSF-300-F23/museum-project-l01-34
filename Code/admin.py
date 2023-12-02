import mysql.connector
cnx = mysql.connector.connect(
                            user ='root', 
                            password ='password here',
                            host ='127.0.0.1',
                            port = 3306)

cur = cnx.cursor(buffered=True)
cur.execute('USE artobject')

def find_column_size(Attribute_name, From):
    cur.execute("SELECT max(length(" + Attribute_name + ")) FROM " + From)
    Column_size = cur.fetchone()[0]
    if Column_size < len(Attribute_name):
        Column_size = len(Attribute_name)
    return Column_size

def get_columns(From, col_names, title_name):
    print("\n"+title_name+"\n")
    att_size = len(col_names)
    for i in range(att_size):
        sizer = find_column_size(col_names[i], From)
        print(f'{col_names[i]:<{sizer}}', end='  ')
    print("\n"+265*"-")
    return

def get_table(From, col_names):
    not_app = 'N/A'
    rows = cur.fetchall()
    size = len(rows)
    for i in range(size):
        for x in range(len(rows[i])):
            sizer = find_column_size(col_names[x], From)
            print(f'{f"{not_app:<{sizer}}" if rows[i][x] == None else f"{str(rows[i][x]):<{sizer}}"}', end='  ')
        print()
    return

def get_column_names(command):
    cur.execute(command)
    return list(cur.column_names)

def sql_commands():
    pass

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
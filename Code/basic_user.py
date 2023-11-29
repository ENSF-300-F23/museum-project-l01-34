import mysql.connector
cnx = mysql.connector.connect(
                            user ='root', 
                            password ='PASSWORD HERE',
                            host ='127.0.0.1',
                            port = 3306)

cur = cnx.cursor(buffered=True)
cur.execute('USE artobject')

def find_column_size(Dir_index, Attribute_name):
    cur.execute("SELECT max(length(" + Attribute_name + ")) FROM " + (tables[Dir_index-1]))
    Column_size = cur.fetchone()[0]
    if Column_size < len(Attribute_name):
        Column_size = len(Attribute_name)
    return Column_size

def get_columns(Dir_index):
    col_names = cur.column_names
    print("\n"+(tables[Dir_index-1]) + " Attribute List:\n")
    att_size = len(col_names)
    for i in range(att_size):
        sizer = find_column_size(Dir_index, col_names[i])
        print(f'{col_names[i]:<{sizer}}', end='  ')
    print("\n"+180*"-")
    return

def get_table(Dir_index):
    Not_app = 'N/A'
    col_names = cur.column_names
    rows = cur.fetchall()
    size = len(rows)
    for i in range(size):
        for x in range(len(rows[i])):
            sizer = find_column_size(Dir_index, col_names[x])
            print(f'{f"{Not_app:<{sizer}}" if rows[i][x] == None else f"{str(rows[i][x]):<{sizer}}"}', end='  ')
        print()
    return

def menu_options():
    print("1-Art Objects\n2-Artists\n3-Exhibitions\n4-Paintings\n5-Sculptures\n6-Other\n7-Permanent Collection\n8-Borrowed Items\n9-Borrowed Collections")
    Dir_index = int(input("Please enter the number correspoding to the table of your choice: "))
    cur.execute("SELECT * FROM " + (tables[Dir_index-1]))
    get_columns(Dir_index)
    cur.execute("SELECT * FROM " + (tables[Dir_index-1]))
    get_table(Dir_index)
    return
    

tables = ["Art_object","Artist","Exhibition","Painting","Sculpture_or_Statue","Other","Permanent_Collection","Borrowed","Collection"]
print("Welcome to the Art_object database.")
menu_options()

cnx.close()
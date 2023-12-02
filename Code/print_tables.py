import mysql.connector
cnx = mysql.connector.connect(
                            user ='root', 
                            password ="PASSWORD HERE!",
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
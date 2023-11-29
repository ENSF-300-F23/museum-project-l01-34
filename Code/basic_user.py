import mysql.connector
cnx = mysql.connector.connect(
                            user ='root', 
                            password ='PASSWORD HERE!',
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
    Not_app = 'N/A'
    rows = cur.fetchall()
    size = len(rows)
    for i in range(size):
        for x in range(len(rows[i])):
            sizer = find_column_size(col_names[x], From)
            print(f'{f"{Not_app:<{sizer}}" if rows[i][x] == None else f"{str(rows[i][x]):<{sizer}}"}', end='  ')
        print()
    return

def execute_basic_query(Select, From, col_names, title_name):
    cur.execute("SELECT " + Select + " FROM "+ From)
    get_columns(From, col_names, title_name)
    cur.execute("SELECT " + Select + " FROM " + From)
    get_table(From, col_names)
    return

def select_art(From):
    cur.execute("SELECT * FROM "+ From[0])
    art_columns = list(cur.column_names)
    art_columns.pop(0)
    
    cur.execute("SELECT * FROM "+ From[1])
    other_columns = list(cur.column_names)
    other_columns.pop(0)
    
    combined_columns = art_columns + other_columns
    return combined_columns

def select_exhibit(From):
    cur.execute("SELECT * FROM "+ From)
    exhibit_columns = list(cur.column_names)
    return exhibit_columns
    
def submenu_art_object():
    print("\n1-Paintings\n2-Sculptures\n3-Other\n4-Permanent Collection\n5-Borrowed Items\n0-Return")
    Dir_index = int(input("\nPlease enter the number corresponding to the table of your choice: "))
    if Dir_index == 0:
        return
    if Dir_index == 1:
        column_names = select_art(["art_object", "painting"])
        execute_basic_query((','.join(column_names)), "art_object join painting on art_object.Id_no = painting.Id_no", column_names, "Paintings")
    if Dir_index == 2:
        column_names = select_art(["art_object", "sculpture_or_statue"])
        execute_basic_query((','.join(column_names)), "art_object join sculpture_or_statue on art_object.Id_no = sculpture_or_statue.Id_no", column_names, "Sculptures")
    if Dir_index == 3:
        column_names = select_art(["art_object", "other"])
        execute_basic_query((','.join(column_names)), "art_object join other on art_object.Id_no = other.Id_no", column_names, "Other")
    if Dir_index == 4:
        column_names = select_art(["art_object", "permanent_collection"])
        execute_basic_query((','.join(column_names)), "art_object join permanent_collection on art_object.Id_no = permanent_collection.Id_no", column_names, "Permanent Collection")
    if Dir_index == 5:
        column_names = select_art(["art_object", "borrowed"])
        execute_basic_query((','.join(column_names)), "art_object join borrowed on art_object.Id_no = borrowed.Id_no", column_names, "Borrowed Collection")
    submenu_art_object()


def submenu_exhibition():
    print("\n1-Exhibition Archive\n2-The Tudors: Art and Majesty in Renaissance England\n3-Cubism and the Trompe l’Oeil Tradition\n4-Hear Me Now: The Black Potters of Old Edgefield, South Carolina\n5-Van Gogh's Cypresses\n6-The Rediscovery of The Baroque Period\n7-Masterpieces of the Louvre\n0-Return")
    Dir_index = int(input("\nPlease enter the number corresponding to the table of your choice: "))
    From = "art_object"
    column_names = select_exhibit(From)
    column_names.remove('Exhibit_name')
    column_names.pop(0)
    if Dir_index == 0:
        return
    if Dir_index == 1:
        column_names = select_exhibit("exhibition")
        execute_basic_query("*", "Exhibition", column_names, "Exhibition Archive")
    if Dir_index == 2:
        execute_basic_query((','.join(column_names)), From + " WHERE art_object.Exhibit_name = \"The Tudors: Art and Majesty in Renaissance England\"", column_names, "The Tudors: Art and Majesty in Renaissance England")
    if Dir_index == 3:
        execute_basic_query((','.join(column_names)), From + " WHERE art_object.Exhibit_name = \"Cubism and the Trompe l\’Oeil Tradition\"", column_names, "Cubism and the Trompe l’Oeil Tradition")
    if Dir_index == 4:
        execute_basic_query((','.join(column_names)), From + " WHERE art_object.Exhibit_name = \"Hear Me Now: The Black Potters of Old Edgefield, South Carolina\"", column_names, "Hear Me Now: The Black Potters of Old Edgefield, South Carolina")
    if Dir_index == 5:
        execute_basic_query((','.join(column_names)), From + " WHERE art_object.Exhibit_name = \"Van Gogh\'s Cypresses\"", column_names, "Van Gogh's Cypresses")
    if Dir_index == 6:
        execute_basic_query((','.join(column_names)), From + " WHERE art_object.Exhibit_name = \"The Rediscovery of The Baroque Period\"", column_names, "The Rediscovery of The Baroque Period")
    if Dir_index == 7:
        execute_basic_query((','.join(column_names)), From + " WHERE art_object.Exhibit_name = \"Masterpieces of the Louvre\"", column_names, "Masterpieces of the Louvre")
    submenu_exhibition()

print("\nWelcome to the Art_object database.")

while True:
    print("\n1-Art Objects\n2-Exhibitions")
    Dir_index = int(input("\nPlease enter the number corresponding to the table of your choice: "))
    if Dir_index == 0:
        break
    elif Dir_index == 1:
        submenu_art_object()
    elif Dir_index == 2:
        submenu_exhibition()

cnx.close()
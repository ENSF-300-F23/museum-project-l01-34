def Insert(curr):
    curr.execute("SHOW TABLES")
    print("Tables: ")
    for x in curr:
        print(x)
    tableName = input("Choose Table:\n")
    curr.execute("SELECT * FROM " + tableName)
    columns = curr.column_names
    
    print("Provide entries for the following values: ")
    for i in range(len(columns)):
        print(columns[i] + "\t", end="")
    print(" ")
    
    data = [input() for _ in range(len(columns))]
    curr.execute("INSERT INTO " + tableName + " VALUES (" + ",".join(["%s" for _ in range(len(columns))]) + ")", data)

def Delete():
    pass

def Update():
    pass

def CreateTable():
    pass

def CreateView():
    pass

operations = {
    "1" : Insert,
    "2" : Delete,
    "3" : Update,
    "4" : CreateTable,
    "5" : CreateView
}
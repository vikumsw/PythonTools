import sqlalchemy as db


CHOICE_SUMMARY = -1
CHOICE_2 = -1
CHOICE_EXIT = -1


global conn
global db_engine
db_engine = None
conn = None

def initChoices():
    i = 1
    global CHOICE_SUMMARY
    CHOICE_SUMMARY = i
    i = i+1
    global CHOICE_2
    CHOICE_2 = i
    i = i+1
    global CHOICE_EXIT
    CHOICE_EXIT = i

def insertInitial(conn,engine):
    metadata = db.MetaData()
    ent = db.Table('Entities', metadata,
              db.Column('Entity_Name', db.String(30), nullable=False, primary_key = True),
              db.Column('Instance_Table', db.String(30), nullable=False)
              )
    metadata.create_all(engine)
    
    query = db.insert(ent).values(Entity_Name='Market', Instance_Table='markets') 
    ResultProxy = conn.execute(query)

    s = ent.select()
    result = conn.execute(s)

    for row in result:
        print (row)


def ConnectToDB():
    db_engine = db.create_engine('sqlite:///refdataDB.db')
    conn = db_engine.connect()
    return conn, db_engine

def displaySummary():
    print('''Displaying Summary\n
    | Entity \t| Instance count \t|''')
    global conn
    global db_engine

    #s = db.select([Entities])

    s = db.text("SELECT * FROM Entities")
    result = conn.execute(s)

    for row in result:
        print(type(result))
        print (row)

if __name__ == "__main__":
    print("Starting System")
    
    initChoices()
    conn,db_engine = ConnectToDB()
    #insertInitial(conn,db_engine)


    while(True):
        #str = input("Enter your input: ")
        #print( "Received input is : ", str)
        menustr = """ ----------------------------\n
            Menu            \n
        {}. Summary
        {}. CHOICE_2
        {}. CHOICE_EXIT
        """.format(CHOICE_SUMMARY,CHOICE_2,CHOICE_EXIT)

        print(menustr)

        inputChoice = int(input("Enter your input: "))
        
        
        if inputChoice == CHOICE_EXIT:
            break
        elif inputChoice == CHOICE_SUMMARY:
            displaySummary()
            

    print("Exiting System")


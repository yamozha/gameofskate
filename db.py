from idCounter import idCount
import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
        
def createCont(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Contestant(name, phone, instagram)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def addCont(user,phone,ig):
    database = "sqlite.db"

    conn = create_connection(database)
    with conn:
        user = (user,phone,ig)
        user_id = createCont(conn, user)

def viewCont(name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    database = "sqlite.db"

    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Contestant;")

    rows = cur.fetchall()
    for row in rows:
        if row[0] == name:
            return row



# def addUser(name, phone, idCount=idCount):
    # db = open("database.txt", "a")
    # dictObj = {"name":name, "phone":phone, "id":idCount}
    # db.write(f"{dictObj}\n")
    # db.close()
    # 
# def viewUser(user=None):
    # db = open("database.txt", "r")
    # if not user:
        # for line in db:
            # print
        # 


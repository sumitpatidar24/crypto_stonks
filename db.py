import sqlite3
conn = sqlite3.connect('data/crypto.db')

def createtable():
    conn.execute('''CREATE TABLE DogeCoin
                (ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                PRICE REAL NOT NULL,
                GL REAL NOT NULL,
                MAXP REAL NOT NULL,
                MINP REAL NOT NULL,
                TIME TEXT NOT NULL, 
                DATE TEXT NOT NULL
                );
            ''')
    conn.execute('''CREATE TABLE BitCoin
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            PRICE REAL NOT NULL,
            GL REAL NOT NULL,
            MAXP REAL NOT NULL,
            MINP REAL NOT NULL,
            TIME TEXT NOT NULL,
            DATE TEXT NOT NULL);
        ''')
    conn.execute('''CREATE TABLE Ethereum
                (ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                PRICE REAL NOT NULL,
                GL REAL NOT NULL,
                MAXP REAL NOT NULL,
                MINP REAL NOT NULL,
                TIME TEXT NOT NULL,
                DATE TEXT NOT NULL);
            ''')
    

def inserttable(crypto,id, name, price, gl,maxp, minp, time,date):
    info_string= f"INSERT INTO {crypto} (ID, NAME, PRICE, GL,MAXP, MINP, TIME, DATE) VALUES({id}, '{name}', '{price}', '{gl}',{maxp}, {minp}, '{time}', '{date}')"
    
    conn.execute(info_string)
    conn.commit()

def closeit():
    conn.close()
def getapricefromid(crypto, ids):
    da = f"SELECT * FROM {crypto} WHERE ID = {ids}; "
    datat = conn.execute(da)
    lst = []
    for i in datat:
        lst.append(i)
    return lst[0]

def getapricefromdate(crypto, date):
    da = f"SELECT ID FROM {crypto} WHERE DATE ='{date}';"
    datat = conn.execute(da)
    lst = []
    for i in datat:
        lst.append(i[0])
    for i in lst:
        print(getapricefromid(crypto, i))
    return lst

def getapricefromiddiff(crypto, id1, id2):
    da = f"SELECT ID FROM {crypto} WHERE ID BETWEEN {id1} AND {id2}; "
    datat = conn.execute(da)
    lst = []
    for i in datat:
        lst.append(i[0])
    for i in lst:
        print(getapricefromid(crypto, i))
    return lst
def getlastid(crypto):
    query = F"SELECT ID FROM {crypto} ORDER BY ID DESC LIMIT 1"
    datat = conn.execute(query)
    lst = []
    for i in datat:
        lst.append(i)
    return int(lst[0][0])
def getcryptofrommaxprice(crypto):
    query = f"SELECT MAX(MAXP) FROM {crypto};"
    datat = conn.execute(query)
    lst = []
    
    for i in datat:
        lst.append(i)
    m = lst[0][0]
    query2 = f"SELECT ID FROM {crypto} WHERE MAXP= {m};"
    da = conn.execute(query2)

    lst2 = []
    for i in da:
        lst2.append(i[0])
        print(getapricefromid(crypto,i[0]))
    return lst2
    
def getcryptofromminprice(crypto):
    query = f"SELECT MIN(MINP) FROM {crypto};"
    datat = conn.execute(query)
    lst = []
    
    for i in datat:
        lst.append(i)
    m = lst[0][0]
    query2 = f"SELECT ID FROM {crypto} WHERE MINP= {m};"
    da = conn.execute(query2)

    lst2 = []
    for i in da:
        lst2.append(i[0])
        print(getapricefromid(crypto,i[0]))
    return lst2
    

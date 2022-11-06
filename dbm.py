import pymysql as p

def connection():
    return p.connect(host="localhost",user="root",password="",database="jarvis",port=3306)

# USER DATABASE

def uinsert(d):
    con = connection()
    cur = con.cursor()
    sql = "insert into userbook values(%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,d)
    con.commit()
    con.close()

def showudata():
    con = connection()
    cur = con.cursor()
    sql = "select * from userbook"
    cur.execute(sql)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data

def ueditdetails(e):
    con = connection()
    cur = con.cursor()
    sql = "select * from userbook where email=%s"
    cur.execute(sql,e)
    userdetails = cur.fetchall()
    con.commit()
    con.close()
    return userdetails

def uupdate(t):
    con=connection()
    cur = con.cursor()
    sql = "update userbook set fname=%s,lname=%s,email=%s,password=%s,mobile=%s,city=%s where email=%s"
    cur.execute(sql,t)
    con.commit()
    con.close()

def udrop(e):
    con=connection()
    cur = con.cursor()
    sql = "delete from userbook where email=%s"
    cur.execute(sql,e)
    con.commit()
    con.close()

def uloginbyemail(email):
    con=connection()
    cur = con.cursor()
    sql = "select email,password from userbook where email=%s"
    cur.execute(sql,email)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data



# AUTHOR DATABASE

def ainsert(da):
    con = connection()
    cur = con.cursor()
    sql = "insert into authorbook values(%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,da)
    con.commit()
    con.close()

def showadata():
    con = connection()
    cur = con.cursor()
    sql = "select * from authorbook"
    cur.execute(sql)
    adata = cur.fetchall()
    con.commit()
    con.close()
    return adata

def aeditdetails(e):
    con = connection()
    cur = con.cursor()
    sql = "select * from authorbook where email=%s"
    cur.execute(sql,e)
    userdetails = cur.fetchall()
    con.commit()
    con.close()
    return userdetails

def aupdate(t):
    con=connection()
    cur = con.cursor()
    sql = "update authorbook set fname=%s,lname=%s,email=%s,password=%s,mobile=%s,city=%s where email=%s"
    cur.execute(sql,t)
    con.commit()
    con.close()

def adrop(e):
    con=connection()
    cur = con.cursor()
    sql = "delete from authorbook where email=%s"
    cur.execute(sql,e)
    con.commit()
    con.close()

def aloginbyemail(email):
    con=connection()
    cur = con.cursor()
    sql = "select email,password from authorbook where email=%s"
    cur.execute(sql,email)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data


# BLOG

def binsert(db):
    con = connection()
    cur = con.cursor()
    sql = "insert into blogbook1 values(%s,%s,%s)"
    cur.execute(sql,db)
    con.commit()
    con.close()

def showbdata():
    con = connection()
    cur = con.cursor()
    sql = "select * from blogbook1"
    cur.execute(sql)
    bdata = cur.fetchall()  
    con.commit()
    con.close()
    return bdata

def showbdata1():
    con = connection()
    cur = con.cursor()
    sql = "select * from blogbook1"
    cur.execute(sql)
    bdata = cur.fetchall()  
    con.commit()
    con.close()
    return bdata

def beditdetails(e):
    con = connection()
    cur = con.cursor()
    sql = "select * from blogbook1 where name=%s"
    cur.execute(sql,e)
    blogdetails = cur.fetchall()
    con.commit()
    con.close()
    return blogdetails

def bupdate(t):
    con=connection()
    cur = con.cursor()
    sql = "update blogbook1 set name=%s,title=%s,blog=%s where name=%s"
    cur.execute(sql,t)
    con.commit()
    con.close()

def bdrop(e):
    con=connection()
    cur = con.cursor()
    sql = "delete from blogbook1 where name=%s"
    cur.execute(sql,e)
    con.commit()
    con.close()
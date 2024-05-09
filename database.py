import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from flask import Flask, request, send_file
import io

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="newpro")
    c = _conn.cursor()

    return c, _conn



# -------------------------------Registration-----------------------------------------------------------------


    


def inc_reg(username,password,email,mobile):
    try:
        c, conn = db_connect()
        print(username,password,email,mobile)
        id="0"
        status = "pending"
        j = c.execute("insert into user (id,username,password,email,mobile,status) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+mobile+"','"+status+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    



def ins_loginact(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from user where username='" +
                      username+"' and password='"+password+"' "  )
        c.fetchall()
        
        conn.close()
        return j
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(db_connect())

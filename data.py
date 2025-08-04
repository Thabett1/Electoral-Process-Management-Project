import sqlite3
import cv2
from pyzbar.pyzbar import decode
class voter:
        def __init__(self,db):
                self.con=sqlite3.connect('Database.db')
                self.cur=self.con.cursor()
                self.db=db
                if self.db=="candidate":
                        sql=f"""
                        CREATE TABLE IF NOT EXISTS {self.db}(
                        name text,
                        number text
                )
                """
                elif self.db=="voter":
                        sql=f"""
                        CREATE TABLE IF NOT EXISTS {self.db}(
                        name text,
                        id text,
                        voter_t text
                )
                """
                self.cur.execute(sql)
                self.con.commit()

        def updet(self,number,name):
                self.cur.execute(f"update {self.db} set number=? where name=?",(number,name,))
                self.con.commit()
        def updet_v(self,voter_t,name):
                self.cur.execute(f"update {self.db} set voter_t=? where name=?",(voter_t,name,))
                self.con.commit()
        def serch(self,x):
                self.cur.execute(f"SELECT {x} FROM {self.db}")
                row=self.cur.fetchall()
                return row
        def serch_all(self,x,r,id):
                self.cur.execute(f"SELECT {x} FROM {self.db} where {r}=?",(id,))
                row=self.cur.fetchone()
                return row
        def serch_alll(self):
                self.cur.execute(f"SELECT * FROM {self.db}")
                row=self.cur.fetchall()
                return row
        
        
try:    
        class Camra: 
                def __init__(self) :
                        self.cop=cv2.VideoCapture(0)
                def camra_get(self):
                        try:
                                while True:
                                        success,frame=self.cop.read()
                                        cv2.imshow('tgufusg',frame)
                                        for code in decode(frame):
                                                if (code.data.decode('utf-8'))!="":
                                                        self.cop.release()
                                                        cv2.destroyAllWindows()
                                                        return (code.data.decode('utf-8'))
                                                
                                        if cv2.waitKey(1) & 0xFF==ord('q'):
                                                break
                                self.cop.release()
                                cv2.destroyAllWindows()
                                return ""
                        except:
                                print('error')


except cv2.error:
    cv2.waitKey() 
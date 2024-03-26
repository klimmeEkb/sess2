import PyQt6
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QWidgets
import pyodbc
import sqlite3
from sqlalchemy import create_engine, select
import random
import sys

# from sqlachemy.orm import Session
# from PyQt6.QtSql import QSqlDatabase
# from tables import Base, User,

user = password = db = "wsrprbj-04"
driver = "ODBC+Driver+17+for+SQL+Server"
server = "SERV-PRB/MSSQL"
engine = create_engine(f"mssql://@{server}/{db}?driver={driver}&trusted_connection=yes")


# Base.metadata.create_all(engine)
# con = sqlite3.connect("dbo.pacient")
# cur = con.cursor()
# eng = 'as5rtg'
# for i in range(100):
#     result = cur.execute("INSERT INTO pacient(name) VALUES(" + eng + ")" +
#     "\nINSERT INTO pacient(surname) VALUES(" + eng + ")" +
#     "\nINSERT INTO pacient(fathername) VALUES(" + eng + ")" +
#     "\nINSERT INTO pacient(num&ser) VALUES(" + eng + ")"
#     "\nINSERT INTO pacient(birthday) VALUES(" + eng + ")"
#     "\nINSERT INTO pacient(sex(male, female)) VALUES(" + eng + ")"
#     "\nINSERT INTO pacient(adress) VALUES(" + eng + ")"
#     "\nINSERT INTO pacient(phone) VALUES(" + eng + ")"
#     "\nINSERT INTO pacient(mail) VALUES(" + eng + ")"
#     "\nINSERT INTO pacient(medcard) VALUES(" + eng + ")"
#     "\nINSERT INTO pacient(medcard start) VALUES(" + eng + ")"
#     "\nINSERT INTO pacient(last visit) VALUES(" + eng + ")"
#     "\nINSERT INTO pacient(next visit) VALUES(" + eng + ")"
#     "\nINSERT INTO pacient(strax polis) VALUES(" + eng + ")"
#    "\nINSERT INTO pacient(lose strax polis) VALUES(" + eng + ")"
#    "\nINSERT INTO pacient(diagnoz) VALUES(" + eng + ")"
#    "\nINSERT INTO pacient(history ill) VALUES(" + eng + ")"
#    )
#    con.commit()
# con.close()
# "print("Hello world")
# cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                      "Server=serv-prb/mssql;"
#                      "Database=wsrprbj-04;"
#                      "Trusted_Connection=no;"
##                      "UID=wsrprbj-04;"
#                     "PWD=wsrprbj-04;")
# "

class PacientOut(QWidgets):
    def __init__(self, doc):
        super().__init__()
        self.doc = doc
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect("dbo.medic-diagnostic-meropr")
        self.cur = self.con.cursor()
        self.pacientes = self.cur.execute("SELECT name, surname, fathername FROM medic-diagnostic-meropr WHERE doctor = ?", (self.doc)).fecthall()
        self.setFixedSize(350, 350)
        self.setWindowTitle("pacient out")
        self.name_pac = QLineEdit(self)
        self.find = QPushButton("искать", self)
        self.find.move(100, 0)
        self.find.clicked.connect(self.finder)
        self.medcard = QLineEdit(self)
        self.medcard.move(10, 50)
        self.medcardstart = QLineEdit(self)
        self.medcardstart.move(10, 85)
        self.lastvisit = QLineEdit(self)
        self.lastvisit.move(10, 120)
        self.nextvisit = QLineEdit(self)
        self.nextvisit.move(10, 155)
        self.straxpolis = QLineEdit(self)
        self.straxpolis.move(10, 190)
        self.losestraxpolis = QLineEdit(self)
        self.losestraxpolis.move(10, 225)
        self.diagnoz = QLineEdit(self)
        self.diagnoz.move(10, 260)
        self.historyill = QLineEdit(self)
        self.historyill.move(10, 295)

    def finder(self):
        con = sqlite3.connect("dbo.pacient")
        cur = con.cursor()
        self.info = ""
        for i in range(len(self.pacientes)):
            info = cur.execute("SELECT medcard, medcatdstart, lastvisit, nextvisit, straxpolis, losestraxpolis, diagnoz, historyill FROM pacient WHERE name = ? AND surname = ? AND fathername = ?", (self.pacientes[0], self.pacientes[1], self.pacientes[2])).fetchall()
            if info:
                self.info = info
                break
        if self.info:
            self.medcard.setText(self.info[0])
            self.medcardstart.setText(self.info[1])
            self.lastvisit.setText(self.info[2])
            self.nextvisit.setText(self.info[3])
            self.straxpolis.setText(self.info[4])
            self.losestraxpolis.setText(self.info[5])
            self.diagnoz.setText(self.info[6])
            self.historyill.setText(self.info[7])


class DocEnter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(350, 280)
        self.setWindowTitle("Doc Enter")
        self.btn = QPushButton("войти", self)
        self.btn.clicked.connect(self.enter)
        self.btn.move(10, 200)
        self.btn.resize(330,50)
        self.uz = QLineEdit(self)
        self.uz.move(10, 10)
        self.uz.resize(330, 50)
        self.pass_field = QLineEdit(self)
        self.pass_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_field.move(10, 100)
        self.pass_field.resize(330, 50)
        pass

    def enter(self):
        con = sqlite3.connect("dbo.UZDoc")
        cur = con.cursor()
        dano = self.uz.text()
        password = self.pass_field.text()
        need = cur.execute("SELECT passwordUZ FROM UZDoc WHERE UZ = ?", (dano)).fetchall()
        if password == need:
            pacout = PacientOut(dano)
            pacout.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DocEnter()
    ex.show()
    sys.exit(app.exec())
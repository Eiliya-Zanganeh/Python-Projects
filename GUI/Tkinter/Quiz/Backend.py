import sqlite3


def connect():
    conct = sqlite3.connect("Quiz Word's Book.db")
    cur = conct.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Words (ID INTEGER PRIMARY KEY, Word text, Main text )")
    conct.commit()
    conct.close()

def insert(word, main):
    conct = sqlite3.connect("Quiz Word's Book.db")
    cur = conct.cursor()
    cur.execute("INSERT INTO Words VALUES (NULL, ?, ?) ", (word, main))
    conct.commit()
    conct.close()

def view():
    conct = sqlite3.connect("Quiz Word's Book.db")
    cur = conct.cursor()
    cur.execute("SELECT * FROM Words")
    rows = cur.fetchall()
    conct.close()
    return rows

def serch(word="", main=""):
    conct = sqlite3.connect("Quiz Word's Book.db")
    cur = conct.cursor()
    cur.execute("SELECT * FROM Words WHERE word=? OR main=? ", (word, main))
    rows = cur.fetchall()
    conct.close()
    return rows

def delete(id):
    conct = sqlite3.connect("Quiz Word's Book.db")
    cur = conct.cursor()
    cur.execute("DELETE FROM words WHERE id=?", (id,))
    conct.commit()
    conct.close()

def update(id, word, main):
    conct = sqlite3.connect("Quiz Word's Book.db")
    cur = conct.cursor()
    cur.execute("UPDATE words SET word=?, main=? WHERE id=?", (word, main, id))
    conct.commit()
    conct.close()

connect()

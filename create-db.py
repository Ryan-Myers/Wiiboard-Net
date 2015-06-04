#!/usr/bin/env python

import sqlite3

sqlConn = sqlite3.connect('w8.db')

def main():
    cur = sqlConn.cursor()
    cur.execute("CREATE TABLE w8upd8 IF NOT EXISTS (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, weight REAL)")
    sqlConn.commit()
    cur.close()
    sqlConn.close()

if __name__ == "__main__":
    main()

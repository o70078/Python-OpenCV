#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from os import getenv
import pyodbc

conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=shenfenzheng;UID=sa;PWD=0000;charset="utf8"')

cursor = conn.cursor()
'''
cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])
# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()
'''

cursor.execute('SELECT * FROM kfjl WHERE id=25')
row = cursor.fetchone()
while row:
    #print("ID=%d, Name=%s" % (row[0], row[1]))
    print(row)
    print(row[7])
    print(row.Address)
    row = cursor.fetchone()
# encoding: utf-8
print(u'\u6d77\u4e0a\u5e02'.encode('gb2312'))#
conn.close()
# from Python Pocket Reference page-223
from sqlite3 import connect
conn = connect(r'C:\Data\temp.db') # create a folder named 'Data'
curs = conn.cursor()

curs.execute('create table emp (who, job, pay)')
prefix = 'insert into emp values '
curs.execute(prefix + "('Bob', 'dev', 100)")
curs.execute(prefix + "('Sue', 'dev', 120)")

##curs.execute("select * from emp where pay > 100")
##for (who, job, pay) in curs.fetchall():
##    print(who, job, pay)

# store it in 'result'
result = curs.execute("select who, pay from emp")
result.fetchall()

query = "select * from emp where job = ?"
curs.execute(query, ('dev', )).fetchall()


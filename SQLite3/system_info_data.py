
## connect with SQL Server
import psutil
import time
import pyodbc
con = pyodbc.connect('Driver={SQL Server};'
                     'Server=HP2024\SQLEXPRESS;'
                     'Database=System_info;'
                     'Trusted_Connection=yes;')
## remove the space in lines above
cursor = con.cursor()

## produce data

while 1 == 1:
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory()[2]
    disk_usage = psutil.disk_usage('/')[3]
    cursor.execute('insert into Performance values (GETDATE(),'
                   + str(cpu_usage) + ','
                   + str(memory_usage) + ','
                   + str(disk_usage) + ')'
                   )
    print(cpu_usage)
    con.commit()
    time.sleep(1)

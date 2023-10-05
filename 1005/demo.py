import pymysql

# Connect to the database
conn, cursor = None, None
try :
    conn = pymysql.connect(host='43.201.116.29', 
                             port=3306,
                             user='root',
                             password='pythonmysql')
    
#2.cursor
    cursor = conn.cursor()
#3.SQL statement 쿼리 날리기
    sql = "SELECT NOW()"
    cursor.execute(sql)
#4.결과 가져오기, fetchone또는 fetchall
    result = cursor.fetchone()
    print(result)

except Exception as err :
    print(err)
finally : 
#5.close
    conn.close()
    cursor.close()
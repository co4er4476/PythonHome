import pymysql

#1.데이터베이스 연결을 위해 pymysql의 connect 함수 사용
host='ec2-43-201-116-29.ap-northeast-2.compute.amazonaws.com'
port=3306
user='root'
password='pythonmysql'
database='mycompany'

conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
   
#2.cursor
cursor = conn.cursor()
#3.SQL statement 쿼리 날리기
sql = "SELECT EMPNO, ENAME, JOB, SAL, DEPTNO FROM EMP WHERE DEPTNO = 20"
cursor.execute(sql)
#4.결과 가져오기, fetchone(한명만 가져옴) 또는 fetchall
results = cursor.fetchall() #결과가 튜플로 들어옴
for emp in results:
    print(emp[1], emp[3], sep='\t')
#5.close
conn.close()
cursor.close()
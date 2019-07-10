import pymysql

db = pymysql.connect(host="rm-uf6gw23j409s5ui7qmoo.mysql.rds.aliyuncs.com", user="maxpr_mysql",
                     password="COFdjwD*$*m8bd!HtMLP4+Az0eE9m", database="zj_live")
cursor = db.cursor()

sql1 = "select message_uuid,comment_count from zj_live.dt where comment_count>0"
sql2 = "select * from zj_live.pl where message_uuid={}"
cursor.execute(sql1)

results = cursor.fetchall()
for row in results:
    print(row[0])
    cursor1 = db.cursor()
    cursor1.execute(sql2.format(row[0]))
    # cursor.execute(sql2.format(row[0]))
    comments = cursor1.fetchall()
    for com in comments:
        if len(com[0]) > 0:
            print(com[0])

# cursor = conn.cursor().execute(sql1)
# for i in cursor:
#     print(i[1])


"""
MYSQL_HOST = "rm-uf6gw23j409s5ui7qmoo.mysql.rds.aliyuncs.com"
# MYSQL_DBNAME = "sp_spider"
MYSQL_DBNAME = "zj_live"
MYSQL_USER = "maxpr_mysql"
MYSQL_PASSWORD = "COFdjwD*$*m8bd!HtMLP4+Az0eE9m"
MYSQL_PORT = 3306
"""

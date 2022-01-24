import pymysql

# DB_HOST=127.0.0.1
# DB_PORT=3306
# DB_DATABASE=homestead
# DB_USERNAME=homestead
# DB_PASSWORD=secret

db = None
try:
    db = pymysql.connect(host='JoSoJeongui-MacBookPro.local', user='root', password='0719', charset='utf8')
    print("DB 연결 성공")

    # sql = '''
    # CREATE TABLE mysql.tb_student (
    # id int primary key auto_increment not null,
    # name varchar(32),
    # age int,
    # address varchar(32)
    # ) ENGINE = InnoDB DEFAULT CHARSET = utf8
    # '''

    # sql = '''
    # INSERT mysql.tb_student(name, age, address) values('sojeong', 24, 'korea')
    # '''

    id = 1
    # sql = '''
    # UPDATE mysql.tb_student set name ='sojeong', age=25, where id = %d
    # ''' % id

    sql = '''
    DELETE FROM mysql.tb_student where id = %d
    '''% id

    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()


except Exception as e:
    print("에러",  e)

finally:
    if db is not None:
        db.close()
        print("DB 연결 닫기 성공")
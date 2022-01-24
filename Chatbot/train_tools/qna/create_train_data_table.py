import pymysql
from Chatbot.config.DatabaseConfig import *

db = None

try:
    db = pymysql.connect(host= DB_HOST, user= DB_USER, password=DB_PASSWORD, db= DB_NAME, charset= 'utf8')
    print("DB 연결 성공")

    sql = '''
        CREATE TABLE IF NOT EXISTS `chatbot_train_data` (
        `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
        `intent` VARCHAR(45) NULL,
        `ner` VARCHAR(1024) NULL,
        `query` TEXT NULL,
        `answer` TEXT NOT NULL,
        `answer_image` VARCHAR(2048) NULL,
        PRIMARY KEY (`id`))
    ENGINE = InnoDB DEFAULT CHARSET=utf8
    '''

    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print("에러" , e)

finally:
    if db is not None:
        db.close()
        print("DB 연결 닫기 성공")
import os
import pymysql
import pymysql.cursors
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# docker 접속용
def mysql_create_session():
    mysql_host = os.environ.get('MYSQL_HOST', 'db')  # Docker Compose에서 정의한 서비스 이름
    mysql_port = int(os.environ.get('MYSQL_PORT', 3306))  # MySQL의 기본 포트
    mysql_user = os.environ['MYSQL_USER']
    mysql_pw = os.environ['MYSQL_PASSWORD']  # Docker Compose에서 정의한 환경 변수 이름과 일치
    mysql_db = os.environ['MYSQL_DATABASE']  # Docker Compose에서 정의한 환경 변수 이름과 일치

    # MYSQL에 생성한 DB와 연결
    conn = pymysql.connect(
        host=mysql_host,
        port=mysql_port,
        user=mysql_user,
        password=mysql_pw,
        db=mysql_db,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )

    cur = conn.cursor()

    return conn, cur

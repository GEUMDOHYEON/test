# import os
# import pymysql
# import pymysql.cursors
# from dotenv import load_dotenv

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, ".env"))

# # docker 접속용
# def mysql_create_session():
#     mysql_host = os.environ.get('MYSQL_HOST', 'db')  # Docker Compose에서 정의한 서비스 이름
#     mysql_port = int(os.environ.get('MYSQL_PORT', 3306))  # MySQL의 기본 포트
#     mysql_user = os.environ['MYSQL_USER']
#     mysql_pw = os.environ['MYSQL_PASSWORD']  # Docker Compose에서 정의한 환경 변수 이름과 일치
#     mysql_db = os.environ['MYSQL_DATABASE']  # Docker Compose에서 정의한 환경 변수 이름과 일치

#     # MYSQL에 생성한 DB와 연결
#     conn = pymysql.connect(
#         host=mysql_host,
#         port=mysql_port,
#         user=mysql_user,
#         password=mysql_pw,
#         db=mysql_db,
#         charset='utf8',
#         cursorclass=pymysql.cursors.DictCursor
#     )

#     cur = conn.cursor()

#     return conn, cur

import os
import pymysql
import pymysql.cursors

# docker 접속용
def mysql_create_session():
    # .env 파일 대신, 환경 변수를 직접 가져옴
    mysql_host = os.environ.get('MYSQL_HOST', 'db')  # Docker Compose에서 정의한 서비스 이름
    mysql_port = int(os.environ.get('MYSQL_PORT', 3306))  # MySQL의 기본 포트
    mysql_user = os.environ.get('MYSQL_USER')  # GitHub Secrets 또는 Docker Compose 환경 변수
    mysql_pw = os.environ.get('MYSQL_PASSWORD')  # GitHub Secrets 또는 Docker Compose 환경 변수
    mysql_db = os.environ.get('MYSQL_DATABASE')  # GitHub Secrets 또는 Docker Compose 환경 변수

    if not all([mysql_user, mysql_pw, mysql_db]):
        raise ValueError("Required environment variables are missing.")

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

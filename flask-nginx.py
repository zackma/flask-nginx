# -*- coding: UTF-8 -*-

from flask import Flask, render_template, json
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/goUserList')
def goUserList():
    return render_template('user/user_list.html')


@app.route('/userList', methods=['POST'])
def userList():
    rst = {}
    userList = []
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '***',
        'db': 'flask',
        'charset': 'utf8'
    }
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = "select * from user where 1=1"

    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            user = {}
            user['name'] = row[1]
            user['email'] = row[2]
            userList.append(user)
    except:
        msg = r'Error: unable to fetch data'
        print(msg)
        rst['success'] = False
        rst['msg'] = msg
        rst['data'] = []
        return json.dumps(rst, ensure_ascii=False)

    conn.close()
    msg = r'fetch data successfully'
    rst['success'] = True
    rst['msg'] = msg
    rst['data'] = userList
    return json.dumps(rst, ensure_ascii=False)


if __name__ == '__main__':
    app.run()

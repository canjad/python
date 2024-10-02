import pymysql

db_conn = None


def conn_database():
    global db_conn
    try:
        db_conn = pymysql.connect(
            host='172.16.67.128',
            port=3306,
            user='root',
            password='123456',
            db='bank'
        )
        print("连接成功")
        return 1
    except:
        print("连接失败")
        return -1


def close_database():
    global db_conn
    if db_conn:
        db_conn.close()
        print("关闭数据库连接")


def print_menu():
    print("1.查询账号信息")
    print("2.新建账号")
    print("3.修改账户")
    print("4.删除账户")
    print("5.退出系统")


def query_acct():
    acc_no = input("请输入账号:")
    if acc_no and acc_no != "":
        sql = "select * from acct where acct_no=%s" % acc_no
    else:
        sql = "select * from acct"
    global db_conn
    cursor = db_conn.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            user_info = "账号:%s,户名:%s, 余额:%s" % (row[0], row[1], row[6])
            print(user_info)
    except Exception as e:
        print(e)


def new_acct():
    acct_no = input("请输入账号:")
    acct_name = input("请输入户名:")
    acct_type = input("请输入账户类型: 1-存款账号 2-贷款账号")
    balance = float(input("请输入余额:"))
    if acct_type != "1" and acct_type != "2":
        print("账户类型输入有误")
        return
    if balance > 0.0001:
        sql = """insert into acct(acct_no, acct_name, cust_no,acct_type,reg_date,acct_state, balance) \
        values(\'%s\',\'%s\',\'%s\',%s,date(now()),%s,%s) """ % (acct_no, acct_name, "C008", acct_type, "1", balance)
        print(sql)
        global db_conn
        cursor = db_conn.cursor()
        try:
            cursor.execute(sql)
            db_conn.commit()
            print("新建账户成功：%s" % acct_no)
        except Exception as e:
            print(e)
            db_conn.rollback()


def update_acct():
    try:
        acct_no = input("请输入账号:")
        acct_name = input("请输入户名:")
        balance = float(input("请输入余额:"))
        if balance > 0.0001:
            sql = "update acct set balance=%s where acct_name=\'%s\' and acct_no=\'%s\'" % (balance, acct_name, acct_no)
            global db_conn
            cursor = db_conn.cursor()
            cursor.execute(sql)
            db_conn.commit()
            print("修改成功,影响行数", cursor.rowcount)
        else:
            print('金额不合法')
    except Exception as e:
        print(e)
        db_conn.rollback()


def delete_acct():
    try:
        acct_no = input("请输入账号:")
        sql = "delete from acct where acct_no=\'%s\'" % acct_no
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)
        db_conn.commit()
        print("删除成功,影响行数", cursor.rowcount)
    except Exception as e:
        print(e)
        db_conn.rollback()
        return


if __name__ == "__main__":
    # 连接数据库
    if conn_database() < 0:
        exit(0)
    # 对菜单进行操作
    while True:
        print_menu()
        option = input("请输入您要操作的选项:")
        if option == "1":
            query_acct()
        elif option == "2":
            new_acct()
        elif option == "3":
            update_acct()
        elif option == "4":
            delete_acct()
        elif option == "5":
            break
        else:
            print("您输入的选项有误,请重新输入")
    # 关闭数据库
    close_database()

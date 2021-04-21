import sqlite3

class Sql:
    def __init__(self):
        super(Sql, self).__init__()
        try:
            db = sqlite3.connect("user_data.db")
            cursor = db.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT UNIQUE PRIMARY KEY,password TEXT)")
        except Exception as e:
            print("数据库创建失败！")
        else:
            print("数据库创建成功！")
        finally:
            db.close()

    def add_user(self, input_name, input_password):
        try:
            db = sqlite3.connect("user_data.db")
            cursor = db.cursor()
            cursor.execute("INSERT INTO users(name,password) VALUES(?,?)", (input_name, input_password))
            db.commit()
        except Exception as e:
            db.rollback()
            print("用户名已存在！")
        else:
            print("添加成功")
        finally:
            db.close()  # 关闭数据库

    def show_all_data(self):
        db = sqlite3.connect("user_data.db")
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute('''SELECT name, password FROM users''')
        all_rows = cursor.fetchall()
        users=[]
        passwords=[]
        for row in all_rows:
            print("show_all_data", '{0} : {1}'.format(row[0], row[1]))
            users.append(row[0])
            passwords.append(row[1])
        print(users)
        print(passwords)
        db.close()
        return users,passwords

    def get_first_user(self):
        db = sqlite3.connect("user_data.db")
        cursor = db.cursor()
        cursor.execute('''SELECT name, password FROM users''')
        row = cursor.fetchone()
        db.close()
        if row is None:
            return row
        else:
            return row[0]

    def get_password(self, user_name):
        db = sqlite3.connect("user_data.db")
        cursor = db.cursor()
        cursor.execute("SELECT password FROM users WHERE name=?", [user_name])
        row = cursor.fetchone()
        db.close()
        if row is None:
            return row
        else:
            return row[0]

    def update_user_info(self, user_name, user_password):
        db = sqlite3.connect("user_data.db")
        cursor = db.cursor()
        cursor.execute("UPDATE users SET password=? WHERE name=?", (user_password, user_name))
        db.commit()
        db.close()

    def delete_user(self, user_name):
        db = sqlite3.connect("user_data.db")
        cursor = db.cursor()
        cursor.execute("DELETE FROM users WHERE name=?", [user_name])
        db.commit()
        db.close()


if __name__ == '__main__':
    database = Sql()
    database.get_first_user()
    database.show_all_data()
    print("add")
    database.add_user("asdf", "123456")
    database.add_user("asa", "12356")
    database.add_user("q", "2345")
    database.show_all_data()
    print("get")
    database.get_first_user()
    print(database.get_password("asdf"))
    print(database.get_password("qq"))
    print("update")
    database.update_user_info("asdf", "789")
    database.show_all_data()
    print("delete")
    database.delete_user("as")
    database.show_all_data()

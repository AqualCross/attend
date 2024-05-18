#import databasetest

# 创建或连接数据库
#conn = sqlite3.connect("test.db")
# 创建 user 数据库
#conn.execute('''CREATE TABLE user
# (
#     user_id   int,
#     user_name text,
#     password  text
# )
#''')
# 写入数据
#conn.execute("INSERT INTO user (user_id,user_name,password) VALUES(1,'zmister','123456')")
#conn.execute("INSERT INTO user (user_id,user_name,password) VALUES(2,'mrdoc','234323')")
#conn.execute("INSERT INTO user (user_id,user_name,password) VALUES(2,'python','hahaheheh')")
#conn.commit()
# # 更新数据
# conn.execute("UPDATE user SET password = '888888' WHERE user_id = 1;")
# conn.commit()
# # 删除数据
# conn.execute("DELETE FROM user WHERE user_name = 'python'")
# conn.commit()

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d
#
#
# # 指定字典类型
# conn.row_factory = dict_factory
#
# # 查询数据
# cursor = conn.execute("SELECT * FROM user")
# for row in cursor.fetchall():
#     print(row)
#
# conn.close()

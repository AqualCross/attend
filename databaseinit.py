# 学生信息管理：录入、修改、删除学生信息，包括姓名、学号、班级等。
# 教师信息管理：录入、修改、删除教师信息，包括姓名、工号等。
# 初始化:读取表格文件一次性导入大量学生信息和教师信息
# 修改单个学生/教师信息需要修改表格文件，然后重新初始化
import pandas as pd

students = pd.read_excel('students.xlsx')
teachers = pd.read_excel('teachers.xlsx')


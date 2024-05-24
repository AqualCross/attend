
class User:
    """
    uid String          学号/工号
    name String         姓名
    password String     密码
    """
    def __init__(self, uid, name, password):
        self.uid = uid
        self.name = name
        self.password = password


class Student(User):
    def __init__(self, uid, name, password, major, classname):
        super().__init__(uid, name, password)
        self.major = major
        self.classname = classname


class Teacher(User):
    def __init__(self, uid, name, password):
        super().__init__(uid, name, password)


class attend:
    """
    latel   迟到时间线
    final   旷课时间线
    time    实际签到时间
    location签到地点
    """
    def __init__(self):
        self.name = None
        self.lateline = None
        self.finalline = None
        self.time = None
        self.location = None

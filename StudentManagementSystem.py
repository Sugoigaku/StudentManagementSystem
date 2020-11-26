from Student import *
from Template import *
from DbcSbc import *


class System(object):
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    def start_up(self):
        op_list = ["1.添加学员", "2.删除学员", "3.修改学员信息", "4.查询学员信息", "5.显示学员所有信息", "6.退出系统"]
        print("+{0:{0}^12}+".format('―', '―'))
        print("|{0:{1}^12}|".format("学员管理系统", chr(12288)))
        print("+{0:{0}^12}+".format('―', '―'))
        for op in op_list:
            print("|{1}{0:{1}<12}|".format(op, chr(12288)))
        print("+{0:{1}^12}+".format('―', '―'))

    def add_stu(self):
        name = sbc2dbc(input("请输入学员姓名："))
        number = sbc2dbc(input("请输入学员学号："))
        age = sbc2dbc(input("请输入学员年龄："))
        student = Student(number, name, age)
        self.data.append(student)

    def delete_stu(self):
        num = sbc2dbc(input("请输入要删除学生的学号："))
        for s in self.data:
            if s.number == num:
                self.data.remove(s)
                print("删除成功！")
                break
            else:
                print("删除失败，未找到该学号学生。")

    def modify_stu(self):
        num = sbc2dbc(input("请输入要修改学生的学号："))
        for s in self.data:
            if s.number == num:
                s.name = sbc2dbc(input("请输入学员姓名："))
                s.number = sbc2dbc(input("请输入学员学号："))
                s.age = sbc2dbc(input("请输入学员年龄："))
                print("修改成功！")
                break
            else:
                print("修改失败，未找到该学号学生。")

    def query(self):
        num = sbc2dbc(input("请输入要查询学生的学号："))
        temp = []
        for s in self.data:
            if s.number == num:
                temp.append(s)
        table = Template(['学号', '姓名', '年龄'])
        for t in temp:
            r = [t.number, t.name, t.age]
            table.add_row(r)
        table.print_table()

    def show_all(self):
        table = Template(['学号', '姓名', '年龄'])
        for d in self.data:
            r = [d.number, d.name, d.age]
            table.add_row(r)
        table.print_table()

    def quit(self):
        print("再见~")

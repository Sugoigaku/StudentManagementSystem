from StudentManagementSystem import *


if __name__ == '__main__':
    s = System()
    s.start_up()
    while True:
        op = input("请输入指令：")
        if op == '1':
            s.add_stu()
        elif op == '2':
            s.delete_stu()
        elif op == '3':
            s.modify_stu()
        elif op == '4':
            s.query()
        elif op == '5':
            s.show_all()
        elif op == '6':
            s.quit()
            break

import random
# class Computer:
#     def __init__(self, brand, type, color):
#         self.brand = brand
#         self.type = type
#         self.color = color
#     def online(self):
#         print("正在使用电脑上网。。。。")
#     def __str__(self):
#         return self.brand + "---" + self.type + "---" + self.color
#
# class Book:
#     def __init__(self, bname, author, number):
#         self.bname = bname
#         self.author = author
#         self.number = number
#     def __str__(self):
#         return self.bname + "---" + self.author + "---" + self.number
# class Student:
#     def __init__(self, name, computer, book):
#         self.name = name
#         self.computer = computer
#         self.books = []
#         self.books.append(book)
#     def borrow_book(self, book):
#         for book1 in self.books:
#             if book1.bname == book:
#                 print("已经借过吃书")
#                 break
#         else:
#             self.books.append(book)
#     def show_book(self):
#         for book in self.books:
#             print(book.bname)
#
#     def __str__(self):
#         return self.name + "--" + str(self.computer) + "---" + str(self.books)
#
# computer = Computer("mac", "mac pro2018", "深灰色")
# book = Book("盗墓笔记", "南派杉树", 10)
# book1 = Book("鬼吹灯", "天下霸唱", 8)
# stu = Student("songsong", computer, book)
# print(stu)
# stu.borrow_book(book1)




# class Road:
#     def __init__(self, name, len):
#         self.name = name
#         self.len = len

# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#     def get_time(self, road):
#         ran_time = random.randint(1, 10)
#         msg = '{}品牌的车在{}上已{}速度行驶了{}小时'.format(self.brand, road.name, self.speed, ran_time)
#         print(msg)
#     def __str__(self):
#         return '{}品牌的，速度：{}'.format(self.brand, self.speed)
#
# #创建实例化对象
# r = Road('京藏高速',120)
# r.name = "京哈高速"
# audi = Car('奥迪', 120)
# print(audi)
# audi.get_time(r)

"""
写一个简单的工资管理程序，程序可以管理一下四类人：工人（worker）、销售员（salesman）、经理（manager）、销售经理（salemanager）。
所有的员工都具有员工号，姓名，工资等属性，有设置姓名，获得姓名，获取员工号，计算工资等方法
   1、工人：工人具有工作小时数和时薪的属性，工资计算方法为工作小时数*时薪
   2、销售员：具有销售额和提成比例的属性，工资计算方法为销售额*提成比例
   3、经理：具有固定月薪的属性， 工资计算方法为固定月薪
   4、销售经理：工资计算为销售额*提成比例+固定月薪
请根据以上要求设计合理的类，完成以下功能：
    1、添加所有类型的人员
    2、计算月薪
    3、显示所有人员工资情况
"""
class Person:
    def __init__(self, nu, name, salary):
        self.nu = nu
        self.name = name
        self.salary = salary
    def __str__(self):
        msg = "工号：{}, 姓名：{},本月工资：{}".format(self.nu, self.name, self.salary)
        return msg

    def getSalary(self):
        return self.salary
class Worker(Person):
    def __init__(self, nu, name, salary, hours, per_money):
        super().__init__(nu, name, salary)
        self.hours = hours
        self.per_money = per_money
    def getSalary(self):
        money = self.hours*self.per_money
        self.salary += money
        return self.salary
class Saleman(Person):
    def __init__(self, no, name, salary, salemoney, percent):
        super().__init__(nu, name, salary)
        self.salemoney = salemoney
        self.percent = percent
    def getSalary(self):
        money = self.salemoney*self.percent
        self.salary += money
        return self.salary

w = Worker('001', 'king', 2000, 160, 50)
s = w.getSalary()
print('月薪是：', s)
print(w)
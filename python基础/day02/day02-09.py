# #返回一个列表的最大值和第二大值
# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2
#
# #计算指定的年月日是这一年的第几天
# def is_sleep_year(year):
#     """
#     判断年份是不是闰年
#     :param year: 年份
#     :return: 返回True False
#     """
#     return year % 4 ==0 and year % 100 != 0 or year % 400 ==0
# def which_day(year, month, data):
#     day_of_month = [[31, 28,31,30,31,30,31,31, 30,31,30,31],
#                     [31, 29,31,30,31,30,31,31, 30,31,30,31]][is_sleep_year(year)]
#     totol = 0
#     for index in range(month-1):
#         totol += day_of_month[index]
#     return totol + data




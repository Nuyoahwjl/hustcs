def print_(x):
    if type(x) == float:
        print("%.4f" % x)
    else:
        print(x)
# ********** Begin ********** #
#请在每一题的print语句内完成题目所需的表达式

#第一题
print_(1234%123)

#第二题
print_(90*365*24*60*60)

#第三题
print_(123//12)

#第四题
print_(123/12)

#第五题：输出10亿秒是多少年
print_(1.0E9/(365*24*60*60))

#第六题：要求编写两式比较的表达式，输出为True或False
print_(3**3+4**3+5**3==6**3)

#第七题
print_(1.02**365)
print_(1.01**365)

#第八题：要求编写两式比较的表达式，输出为True或False
print_(0.99**2>1.01)
# ********** End ********** #
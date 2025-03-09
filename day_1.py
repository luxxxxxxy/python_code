# 1.1 变量类型
# 变量类型：整数、浮点数、字符串、布尔值、列表、元组、字典、集�?

num1 = 1
string2 = "hello"
boolean3 = True or 2
float4 = 1.0
list5 = [1, 2, 3, 4]   # list和tuple区别：list可以修改，tuple不能修改
tuple6 = (1, 2, 3, 4)
dict7 = {"name": "zhangsan", "age": 18}
set8 = {1, 2, 3, 4,4,3,'1','1'} #set 和list区别：set不能有重复元素，list可以有重复元�?

# print(type(set8))
print(list5[1:]) #[2, 3, 4]
print(list5[:-1]) #[1, 2, 3]
del list5[1]
print(list5) #[1, 3, 4]

 #报错，tuple不能修改
# del tuple6[1]
# print(tuple6)

print(set8) #set会自从去�?

#list
print('--list--')
list5.append(5) #末尾添加元素
print(list5)
list5.insert(0,6) #指定位置添加元素
print(list5)
list5.pop() #删除末尾元素
list5.pop(0) #删除指定位置元素
print(list5)


#len
print('--len--')
print(len(list5))
print(len(tuple6))
print(len(dict7))
print(len(set8))


#1.2条件语句
print('--if--')
# if elif else 练习
# 小明身高1.75，体�?80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数�?
# 低于18.5：过�?
# 18.5-25：正�?
# 25-28：过�?
# 28-32：肥�?
# 高于32：严重肥�?
xiaoming_height = 1.75
xiaoming_weight = 80.5
xiaoming_bmi = xiaoming_weight / (xiaoming_height ** 2) # **表示乘方
if xiaoming_bmi < 18.5:
    print("严重")
elif 18.5 <= xiaoming_bmi < 25:
    print("正常")
elif 25 <= xiaoming_bmi < 28:
    print("过重")
elif 28 <= xiaoming_bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")


# 1.3 match 练习 等于 switch
print('--match--')
score = 'A'
match score.upper():
    case 'A':
        print('excellent')
    case 'B':
        print('good')
    case 'C':
        print('Its ok')
    case _:
        print('Its bad') # case _ 相当于 default


# 1.4 循环语句
# for循环
print('--for循环--')
sum = 0
for i in range(1,10):
    sum+=i
print(sum)




# 2.1 函数
print('--函数--')
def add(a,b):
    return a+b
print(add(1,2))

#2.1.1 内置函数
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000

print(hex(n1), hex(n2))  # 0xff 0x3e8


#2.2 空函数
def nop():
    pass  # pass作为占位。没有会报错

#2.3 参数检查
def changeable(a,b=1):
    print(a,b)

changeable(1) #1 1 b默认可不写，也可以写会更改

## 可变
def changeable2(a,b=1,*args): # *args表示可变参数，args是一个tuple
    for i in args:
        print(i)
    print(a,b,args)

changeable2(1,2,3,4,5) #1 2 (3, 4, 5)

# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

##2.4 列表生成式
L = [x*x for x in range(1,10) if x%2!=0]
print(L)


## isinstance可以判断类型 isinstance(变量，类型)
print(isinstance(num1,int))
print(isinstance(list5,tuple))





L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str) is True]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


## 3.1 生成器

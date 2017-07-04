def fact(n):
    if n ==1:
        return 1
    return n*fact(n-1)

print('fact(1)=',fact(1))
print('fact(5)=',fact(5))
print('fact(10)=',fact(10))

def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(4,'A','B','C')

#
#
#
#
# # # 计算n次方
# # #
# # # def power(x,n=2):
# # #     s=1
# # #     while n>0:
# # #         n = n - 1
# # #         s = s * x
# # #     return s
# # #
# # #
# # # print (power(15,3))
# # #
# # #
# # # def person(name,age,**kw):
# # #     print('name:',name,'age:',age,'other:',kw)
# # #
# # # extra = {'city':'BeiJing','job':'Engineer'}
# # # person('lqx',23,**extra)
# #
# # def f1(a,b,c=0,*args,**kw):
# #     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
# #
# #
# # def f2(a,b,c=0,*,d,**kw):
# #     print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
# #
# #
# # f2(1,2,3)
#
#

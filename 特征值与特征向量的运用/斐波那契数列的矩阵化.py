# -*- coding: utf-8 -*-
'''首要问题是理解为什么要这样做，
斐波那契数列的矩阵求法
python在这里完全就是充当工具角色，因为人工手算很麻烦
'''
import sympy as sp
k = sp.symbols('k',positive=True,integer=True)

a = sp.Matrix([[0,1],[1,1]])
val = a.eigenvals() #求特征值，后面用不上,返回一个字典
vec = a.eigenvects()  #会把特征值，特征向量一起求出来

#print(val)
#print(vec[0][2])  #特征向量是一个列向量

P,D = a.diagonalize()  #给a相似对角化
#print(P)  #特征向量平面
#print(D)  #特征值对角矩阵
ak = P@(D ** k)@(P.inv())
F = ak @ sp.Matrix([1,1])
#print(F)
#print(F[0])  #这就是我们要的通项公式
s = sp.simplify(F[0])  #化简通项公式
#print(s)
print(s.subs(k,19))           #subs()的作用是把原表达式中的变量k替换为19，相当与得到一个可以计算的表达式
print(s.subs(k,19).n(5))      #n(5)表示整数部分加上小数合计5位数
print(s.subs(k,19).evalf(2))  #目前发现和n()的功能类似
sm = []

for i in range(0,10):
    sm.append(s.subs(k,i).n(5))  #用i的值替换变量k，相当于求出k=0，1，……9的解
print(sm)









# l=[3,2,1,0,3,0,0]
# l1=[0,0,0]
# print(any(l))
# print(all(l))
# print(any(l1))
# print(all(l1))


# empty_list = []
# int=[]
# print(any(empty_list))
# print(all(empty_list))
# i=0
# print(bool(i))

# i=int()
# print(i)

# ------ Str -------
# s=' ' 
# print(bool(s))
# print()
# ---------- list --------

# l=[]
# l2=list()
# l1=[3,4,5,5]
# print(bool(l))
# print(bool(l2))
# print(bool(l1))

# # --------tuple --------

# t=()
# tuple()
# t1=(4,5,6)
# print(bool(t))
# print(bool(tuple))
# print(bool(t1))

# x=0
# y='a'
# print(any((x,y)))     #or
# print(all((x,y)))     #and


# ---------- Namespace ---------
# name + objectvalue = namespace
''' types
1.loacal
2.global
3.builtin
= for avoid conflict used namespace
'''

'''import builtins
x=10
y=20
z=30
def first():
    x=5
    y=15
    z=25
    print(locals())
first()
print(globals())
print(dir(builtins))

'''
# --------scope-------
''' scope
1.Global
2.Local
3.Nonlocal-

'''

x=10
def outer_fun():
    x=20
    def inner_fun():
        nonlocal x #nested ke form mai ye lagega
        x=30
    inner_fun()
    print(x)
outer_fun()
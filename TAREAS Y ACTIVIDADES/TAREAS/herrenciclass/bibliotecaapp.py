
from user import *
from account import *
from book import *
from student import *
from stalf import *

ob=user('juan',1301245)
print(ob.getname())
print(ob.getcode())

obbook=account('juan',1301245,'libro','27/5/2023','27/6/2023','NO', 0.00)
ob.agregarbooks(obbook)
ob.accountbook()
ob.accountbook()
for biblioteca in ob.veraccount():
    print(biblioteca.getNombre())

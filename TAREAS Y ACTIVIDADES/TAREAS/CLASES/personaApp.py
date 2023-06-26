from persona import *
ob1=Persona("Brandon", 123456)
print(type(ob1))
print(ob1.getNombre())
ob1.setNombre(100)
print(ob1.getNombre())
ob1.setCurso("hl")
print(ob1.getCurso())
ob1.setCurso("bom")
print(ob1.getCurso())

ob1.deleteCurso("hl")
print(ob1.getCurso())

ob1.deleteCurso("hola")
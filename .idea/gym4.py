import re
x='Привет, как дела? А у меня нормально!!'
result= re.findall(r'[БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ]\w+', x)
print(result)


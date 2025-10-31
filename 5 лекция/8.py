""" 8. Проверьте строки:
 • "12345" — состоит ли только из цифр?
 • "HelloWorld" — состоит ли только из букв?
 • "Python3" — состоит ли только из букв?"""
str1 = '12345'
str2 = 'HelloWorld'
str3 = 'Python3'
print(str1.isdigit())
print(str2.isalpha())
print(str3.isalpha())
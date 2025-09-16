#Арефмитические операторы
print("выберите действие")
print("+ Сложение")
print("- Вычитание")
print("/ Деление")
print("// Целочисленное деление")
print("* Умножение")
print("% Остаток от деления")
print("** Возведение в степень")
#Операторы сравнения
print("== равно")
print("!= Не равно")
print("> Больше")
print("< Меньше")
print(">= Больше или равно")
print("<= Меньше или равно")
#Логические операторы
print("and Логическое И")
print("or Логическое ИЛИ")
print("not Логическое НЕ")
#
print("& Побитовое И")
print("| Побитовое ИЛИ")
print("^ Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ")
print("~ Побитовое НЕ")
print("<< Побитовый сдвиг влево")
print(">> Побитовый сдвиг вправо")

print("in Принадлежность")
print("not in Не принадлежность")

print("is Тождественно")
print("is not Не тождественно")

c=input(str("введите знак"))
if c == "and" or c== "or" :
    v=str(input("ведите первое выражение"))
    x=str(input("ведите второе выражение"))
    if c == "and" :
        result1 = eval (v)
        result2 = eval (x)
        print( result1 and result2 )
    elif c == "or" :
        result1 = eval (v)
        result2 = eval (x)
        print( result1 or result2)
elif c == "not" :
    g = str(input("введите выражение"))
    result3 = eval (g)
    print( not result3 )
elif c == "~" :
    j = int(input("введите число"))
    print (~j)
elif c == "in" or c == "not in" :
    r=input("введите набор символов")
    s=input("введите символ")
    if c== "in" :
        print (s in r)
    elif c== "not in" :
        print (s not in r)
elif c == "is" or c == "is not":
    y=input("введите символы")
    p=input("введите символы")
    if c == "is":
        print(y is p)
    elif c== "is not":
        print(y is not p)
else :
    a=int(input("введите первое число"))
    b=int(input("введите второе число"))
    if c == "+" :
        print(a+b)
    elif c == "-" :
        print (a-b)
    elif c == "/" :
        if b == 0 :
            print("Ошибка. Деление на 0 невозможно")
        else :
            print (a/b)
    elif c == "//" :
        if b == 0 :
            print("Ошибка. Деление на 0 невозможно")
        else :
            print (a//b)
    elif c == "*" :
        print (a*b)
    elif c== "%" :
        if b == 0 :
            print("Ошибка. Деление на 0 невозможно")
        else :
            print (a%b)
    elif c== "**" :
        print (a**b)
    elif c == "==" :
        print (a==b)
    elif c == "!=" :
        print (a!=b)
    elif c == ">" :
        print (a>b)
    elif c == "<" :
        print (a<b)
    elif c == ">=" :
        print (a>=b)
    elif c =="<=":
        print (a<=b)
    elif c == "&" :
        print (a&b)
    elif c == "|" :
        print (a|b)
    elif c == "^" :
        print (a^b)
    elif c == "<<" :
        print (a<<b)
    elif c == ">>" :
        print (a>>b)
    else :
        print ("Ошибка. Неправельно указан знак")
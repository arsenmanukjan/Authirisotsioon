logins=["Arsen"]
passwords=["Manukjan.0"]
roll=False # Не вошел в систему.
log=""
def auto():
    import random
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper() # QWERTYUIOPASDFGHJKLZXCVBNM
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    print(psword)
    return psword


def checkpass(passwor):                 # Проверка пароля на надежность
    isdig = False                           # проверка пароля по фунциям.
    isupper = False                    # проверка пароля по фунциям.
    islower = False                         # проверка пароля по фунциям.
    isalnum = False                       # проверка пароля по фунциям.
    for c in passwor: 
        if c.isdigit():
            isdig = True
        elif c.isupper():
            isupper = True
        elif c.islower():
            islower = True
        elif c.isalnum():
            isalnum = True
        if isdig and isupper and islower and isalnum:     # Проверяется условие пароля
            return True
    return False
    

def manual():                               # Создание собственного пароля
    passvor=input("Создание собственного пароля ")
    if checkpass(passvor):
        return passvor
    

def register():                    # Регистрация 
    psword=""
    log=input("Логин ")
    if not( log in logins):
        select=input("Создание пароля способ: a-auto, m-manual: ")
        if select=="a":
            psword=auto()
        elif select=="m":
            psword=manual()
        logins.append(log)
        passwords.append(psword)
    else:
        pass # пользователь уже есть с таким именем
def avtoriz(log,passwor):
    if log in logins and passwor in passwords and logins.index(log)==passwords.index(passwor):
        print("Добро пожаловать!")
        roll=True # Вошел в систему.
    else:
        print("Данные отсутствуют")
        roll=False
        log=""
    return roll,log

while True:
    if roll==False:
        print("1-Регистрация \n2-Авторизация \n3-Выход ")
    elif roll==True:
        print(f"{log}: \n1-Регистрация \n2-Авторизация \n3-Выход ")

    select=int(input(""))
    if select==1:
        print("Регистрация")
        register()
    elif select==2:
        print("Авторизация")
        roll,log=avtoriz(input("Логин "),input("Пароль "))
    else:
        print("Выход")
        break


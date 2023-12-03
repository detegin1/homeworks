print('регистрация')

login = input('введите логин')
login2 = input('введите логин')
password = input('введите пароль')
password2 = input('введите пароль')
name = input('введите имя')
name2 = input('введите имя')

logins = []
passwords = []
names = []

passwords.append(password)
passwords.append(password2)
logins.append(login)
logins.append(login2)
names.append(name)
names.append(name2)

print("Вход в аккаунт...")
login = input("введите логин")
password = input('введите пароль')

if login in logins and password in passwords:
    print('Здравствуйте ', names)
else:
    print("пароль или логин неверны")


print('Логины ',logins)
print('Пароли', passwords)
print('Имена ',names)



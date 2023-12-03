print("привет как дела")
good=input()
if good == 'хорошо':
    print("почему")
    answer = input()
    if answer == 'просто так':
        print('круто')
    if answer == 'получил 5':
        print('молодец')
        answer = input()
        if answer == 'мне купили телефон':
            print('даш поиграть')
        if answer == 'получил 5':
            print('имба')
        if answer == 'мне купили кота':
            print('даш погладить')
        if answer == 'я выйграл':
            print('ок')      
        if answer == 'у меня 10000000000000000000000000000000000000000000000000000000000000000000000000000000':
            print('набери мне тоже')
        if answer == 'ура снег выпал':
            print('го в снежки')
    else:
        print('я не знаю что сказать')
else:
    print("как тебе помочь?")  
    bad=input()
    if bad =='дай списать д/з':
        print('ок')
    if bad == 'дай мне телефон':
        print("нет")
        bad = input()
        if bad == 'почему': 
            print("ты мне все кубки сольёшь")  
    else:
        print("я не знаю как помочь")


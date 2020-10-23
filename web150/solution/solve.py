from requests import get, post

SERVER = "192.168.2.144:43100"

fields = ['cheeseburger', 'hamburger', 'shrimpburger', 'big_king', 'roll', 'potato_fri', 'potato_country', 'nuggets', 'chicken', 'icecream', 'coke', 'lipton', 'mirinda']

values = ['n'] * 13

def send(cntr):
    global values
    if cntr == 13:
        params = {"submit": "Take"}
        for i in range(0, 13):
            if values[i] == 'y':
                params[fields[i]] = 'y'
        print(values)
        d = post(f'http://{SERVER}/web150', data=params)
        print(d.content.decode("utf-8"))
        return
    for var in 'n', 'y':
        values[cntr] = var
        send(cntr + 1)

send(-1)

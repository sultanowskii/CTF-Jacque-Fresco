import socket
import threading
import random
import time

HOST = ""
PORT = 43100
states = dict()

sock = socket.socket()
sock.bind(('', 43100)) # config
sock.listen(50) # how many connections it's able to have
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print(f"[\033[032m✅\033[00m]\033[032mSocket server successfuly launched on {PORT} port!\033[0m")
print("[\033[034m👨‍\033[0m]\033[034mServer made by \033[035m\033[004m@sultanowskii\033[0m")
print("[\033[036m📄\033[0m]\033[036mServer logs:\033[0m\n")

songs = {"Ночное Рандеву": "крис кельми",
         "Immortals": "fall out boys",
         "Show must go on": "the queen|queen",
         "Песня уклониста": "гробовая доска",
         "Gymn for the Weekend": "coldplay",
         "1000 миль": "би-2|би2|би 2",
         "Серебряный Сентябрь": "кукрыниксы",
         "DEUTSCHLAND": "rammstein",
         "King, Scar.": "scarlxrd",
         "Звезды 3000": "смысловые галлюцинации",
         "The Final Countdown": "europe",
         "Slam (Angel Miners)": "awolnation",
         "Симфония огня": "ария|кипелов",
         "Voyage Voyage": "desreless",
         "SAD!": "xxxtentacion",
         "Хабибуллин": "крематорий",
         "Сектор Газа": "сектор газа",
         "Хрустальный мир": "кукрыниксы",
         "EZ4ENCE": "the verkkars|verkkars",
         "Take me to Church": "hoizer",
         "Way Down We Go": "kaleo",
         "Некрещеная луна": "7б",
         "Хару мамбуру": "ногу свело!|ногу свело",
         "Защитник свиней": "киш|горшок|король и шут",
         "Трасса E-95": "алиса",
         "Призраки Там-тама": "княzz|князь",
         "Castle in the snow": "kadebostany",
         "U Can't Tocuh This": "mc hammer",
         "Counting Stars": "onerepublic|one republic",
         "Шар цвета Хаки": "nautilus pompilius|наутилус помпилиус"
         }

def answer(conn, addr):
    conn.send(bytes("Тебе выпала большая честь решить величайшее уравнение, придуманное одним из моих учеников.\n", encoding="utf-8"))
    conn.send(bytes("Уравнение: (√(x − 2) − 3) * (3^(x^2 - 11x + 30) − 1) * ln(x + 9) = 0. Назови мне любой x в течение 2 минут. Решай аккуратно и быстро:\n", encoding="utf-8"))
    while True:
        data = conn.recv(1024).decode("utf-8", errors="ignore").strip()
        if not data:
            conn.send(bytes("Ответа не получено, соединение разорвано.", encoding="utf-8"))
            conn.close()
            print(f"Client \033[031maborted\033[0m connection: {addr}")
            break
        if not data.is_digit():
            conn.send(bytes("Я жду от тебя число\n", encoding="utf-8"))
            continue
        if data in ["5", "6", "11"]:
            conn.send(bytes("Отличная работа, сейчас схожу за флагом...\n", encoding="utf-8"))
            break
        else:
            conn.send(bytes("Ты пытался. За старание я дам тебе флаг. Сейчас я за ним схожу...\n", encoding="utf-8"))
            break
    time.sleep(3)
    conn.send(bytes("[WARNING] Connection is not stable\n", encoding="utf-8"))
    time.sleep(1)
    conn.send(bytes("А вот и я. Готовься писать, диктую по буквам:\n", encoding="utf-8"))
    time.sleep(1)
    conn.send(bytes("f\n", encoding="utf-8"))
    time.sleep(1)
    conn.send(bytes("l\n", encoding="utf-8"))
    time.sleep(1)
    conn.send(bytes("a\n", encoding="utf-8"))
    time.sleep(1)
    conn.send(bytes("g\n", encoding="utf-8"))
    time.sleep(1)
    conn.send(bytes("{\n", encoding="utf-8"))
    time.sleep(1)
    conn.send(bytes("d\n", encoding="utf-8"))
    time.sleep(1)
    conn.send(bytes("[ERROR] Connection with Jacque Fresco was interrupted by 3rd client\n", encoding="utf-8"))
    time.sleep(2)
    used_questions = set()
    curr_question = ""
    states[addr] = 0
    conn.send(bytes("прив это дадо. необычная встреча но ок. короче там все оч сложно я даю оч простую версию этого ппц пятьдесят. я решил обмануть систему шага вреско. дадо предлагает так дадо говорит название песни ты пишешь исполнителя дадо дает тряпку на палке которая тебе нужна да. идет ок? ответь \"да\" или \"нет\"\n", encoding="utf-8"))

    def check_answer(line: str):
        if line.lower() in songs[curr_question].split("|"):
            return True
        return False

    def generate_curr_question(used_questions, question):
        used_questions.add(question)
        question = random.choice(list(songs.keys()))
        while question in used_questions:
            question = random.choice(list(songs.keys()))
        return used_questions, question

    while True:
        data = conn.recv(1024).decode("utf-8", errors="ignore").strip()
        if not data:
            conn.send(bytes("Ответа не получено, соединение разорвано.", encoding="utf-8"))
            conn.close()
            print(f"Client \033[031maborted\033[0m connection: {addr}")
            break

        if states[addr] == 0:
            if data =="да":
                used_questions, curr_question = generate_curr_question(used_questions, curr_question)
                conn.send(bytes("вот название песни скажи название группы пж " + curr_question + "\n", encoding="utf-8"))
                states[addr] = 1
            elif data == "нет":
                conn.send(bytes("ок.\n", encoding="utf8"))
                conn.close()
                print(f"Client \033[031mregreted passing test\033[0m: {addr}")
                break
            else:
                conn.send(bytes("всм ответь \"да\" или \"нет\"", encoding="utf8"))

        elif 1 <= states[addr] < 15:
            if check_answer(data):
                conn.send(bytes("верно.\n", encoding="utf-8"))
                used_questions, curr_question = generate_curr_question(used_questions, curr_question)
                conn.send(bytes(curr_question + "\n", encoding="utf-8"))
                states[addr] += 1
            else:
                conn.send(bytes("ответ неверный, соединение разорвано.\n", encoding="utf-8"))
                conn.close()
                print(f"\033[031mWrong answer\033[0m from client: {addr}")
                break

        elif states[addr] == 15:
            if check_answer(data):
                conn.send(bytes("верно.\n", encoding="utf-8"))
                conn.send(bytes("отличная работа футболка на палке твоя flag{d4d0_15_f41r_c4p1t4l15t}\n", encoding="utf-8"))
                del states[addr]
                print(f"Client \033[036mSuccessfuly passed the test\033[0m: {addr}")
                conn.close()
                break
            else:
                conn.send(bytes("ответ неверный.", encoding="utf-8"))
                conn.close()
                print(f"\033[031mWrong answer\033[0m from client: {addr}")
                break

while True:
    conn, addr = sock.accept()
    print(f"Client \033[032mconnected\033[0m: {addr}")
    th = threading.Thread(name=addr, target=answer, args=(conn, addr))
    th.start()
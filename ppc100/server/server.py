import asyncio
import random

HOST, PORT = '0.0.0.0', 43100
FLAG = "flag{d4d0_15_f41r_c4p1t4l15t}"
TASKS_COUNT = 10
SONGS = {"Ночное Рандеву": "крис кельми",
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
         "Voyage Voyage": "desireless",
         "SAD!": "xxxtentacion",
         "Хабибуллин": "крематорий",
         "Сектор Газа": "сектор газа",
         "Хрустальный мир": "кукрыниксы",
         "EZ4ENCE": "the verkkars|verkkars",
         "Take me to Church": "hozier",
         "Way Down We Go": "kaleo",
         "Некрещеная луна": "7б",
         "Хару мамбуру": "ногу свело!|ногу свело",
         "Защитник свиней": "киш|горшок|король и шут",
         "Трасса E-95": "алиса",
         "Призраки Там-тама": "княzz|князь",
         "Castle in the snow": "kadebostany",
         "U Can't Tocuh This": "mc hammer",
         "Counting Stars": "onerepublic|one republic",
         "Шар цвета Хаки": "nautilus pompilius|наутилус помпилиус",
         "Rolling In The Deep": "adele|адель",
         "Надвигается северный флот": "северный флот",
         "They Don't Care About As": "michael jackson",
         "bad guy": "billie eilish",
         "Мертвый город": "мертвые дельфины|мёртвые дельфины",
         "Red Sky": "status quo",
         "Life is Life": "opus",
         "Моя бабушка курит трубку": "гарик сукачев|гарик сукачёв|неприкасаемые",
         "Tuesday": "burak yeter",
         "Кто-то из нас двоих": "тараканы!|тараканы",
         "Big City Life": "mattafix",
         "Witchcraft": "pendulum",
         "Boulevard of Broken Dreams": "green day",
         "Stressed out": "twenty one pilots",
         "Take me home, County Roads": "john denver",
         "Закрой за мной дверь": "кино|цой|виктор цой",
         "If Everyone Cared": "nickelback",
         "Я не ходил на карате": "mad show boys|гарри польский"
         }


class JacqueServer(asyncio.Protocol):
    def __init__(self):
        global SONGS
        self.loop = asyncio.get_running_loop()
        self.cur_time_limit = 120
        self.state = 0
        self.songs = SONGS
        self.curr_question = ""
        self.used_questions = set()

    def set_timer(self, time):
        self.cur_time_limit = time
        if hasattr(self, "timeout_handle"):
            self.timeout_handle.cancel()
        self.timeout_handle = self.loop.call_later(
            self.cur_time_limit, self._timeout,
        )

    def check_answer(self, line: str):
        if line.lower() in self.songs[self.curr_question].split("|"):
            return True
        return False

    def generate_curr_question(self):
        self.used_questions.add(self.curr_question)
        self.curr_question = random.choice(list(self.songs.keys()))
        while self.curr_question in self.used_questions:
            self.curr_question = random.choice(list(self.songs.keys()))

    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        print(f"Client \033[032mconnected\033[0m: {self.peername}")
        self.transport = transport
        self.transport.write(
            bytes("Тебе выпала большая честь решить величайшее уравнение, придуманное одним из моих учеников.\n",
                  encoding="utf-8"))
        self.transport.write(bytes(
            "Уравнение: (√(x − 2) − 3) * (3^(x^2 - 11x + 30) − 1) * ln(x + 9) = 0. Назови мне любой x в течение 2 минут. Решай аккуратно и быстро:\n",
            encoding="utf-8"))
        self.set_timer(120)

    async def send_dialog_text(self):
        await asyncio.sleep(5)
        self.transport.write(bytes("А вот и я. Готовься писать, диктую по буквам:\n", encoding="utf-8"))
        await asyncio.sleep(2)
        self.transport.write(bytes("f\n", encoding="utf-8"))
        await asyncio.sleep(2)
        self.transport.write(bytes("[WARNING] Connection is not stable\n", encoding="utf-8"))
        await asyncio.sleep(1)
        self.transport.write(bytes("l\n", encoding="utf-8"))
        await asyncio.sleep(1)
        self.transport.write(bytes("a\n", encoding="utf-8"))
        await asyncio.sleep(1)
        self.transport.write(bytes("g\n", encoding="utf-8"))
        await asyncio.sleep(1)
        self.transport.write(bytes("{\n", encoding="utf-8"))
        await asyncio.sleep(1)
        self.transport.write(bytes("d\n", encoding="utf-8"))
        await asyncio.sleep(10)
        self.transport.write(
            bytes("[ERROR] Connection with Jacque Fresco was interrupted by 3rd client\n", encoding="utf-8"))
        await asyncio.sleep(1)
        self.transport.write(bytes(
            "прив это дадо. необычная встреча но ок. я как всегда вовремя я думаю сам ты это равнение не решишь а значит не получишь флаг. короче там все оч сложно я даю оч простую версию этого ппц сто. я решил обмануть систему шага вреско. дадо предлагает так дадо говорит название песни ты пишешь исполнителя дадо дает тряпку на палке которая тебе нужна да. идет ок? ответь \"да\" или \"нет\"\n",
            encoding="utf-8"))

    def math_task(self, data):
        if not data.isdigit():
            self.transport.write(bytes("Я жду от тебя число\n", encoding="utf-8"))
            return
        self.state = 1
        if data in ["5", "6", "11"]:
            self.transport.write(bytes("Отличная работа! Сейчас схожу за флагом...\n", encoding="utf-8"))
        else:
            self.transport.write(
                bytes("Ты пытался. За старание я дам тебе флаг. Сейчас я за ним схожу...\n", encoding="utf-8"))
        self.dialog_typer = asyncio.ensure_future(self.send_dialog_text())  # So here we run a typing of dialog
        self.set_timer(60)

    def dialog(self, data):
        if data == "да":
            self.generate_curr_question()
            self.transport.write(
                bytes("вот название песни скажи название группы пж  " + self.curr_question + "\n", encoding="utf-8"))
            self.state = 2
            self.set_timer(240)
        elif data == "нет":
            self.transport.write(bytes("ок.\n", encoding="utf8"))
            self.transport.close()
            print(f"Client \033[031mregreted passing test\033[0m: {self.peername}")
        else:
            self.transport.write(bytes("всм ответь \"да\" или \"нет\"", encoding="utf8"))

    def task(self, data):
        if self.check_answer(data):
            if self.state == TASKS_COUNT + 1:
                self.transport.write(bytes("верно.\n", encoding="utf-8"))
                self.transport.write(bytes("отличная работа футболка на палке твоя " + FLAG + "\n", encoding="utf-8"))
                print(f"Client \033[036msuccessfuly passed the test\033[0m: {self.peername}")
                self.transport.close()
            else:
                self.generate_curr_question()
                self.transport.write(bytes("верно. следующее 'таск':\n", encoding="utf-8"))
                self.transport.write(bytes(self.curr_question + "\n", encoding="utf-8"))
                self.state += 1
        else:
            self.transport.write(bytes("ответ неверный, соединение разорвано.\n", encoding="utf-8"))
            self.transport.close()
            print(f"\033[031mWrong answer\033[0m from client: {self.peername}")

    def data_received(self, data):
        data = data.decode(errors="ignore").strip()
        if self.state == 0:
            self.math_task(data)
        elif self.state == 1:
            self.dialog(data)
        elif 1 < self.state <= TASKS_COUNT + 1:
            self.task(data)

    def connection_lost(self, exc=None):
        if not self.transport.get_extra_info("open"):
            self.transport.write(b"Something went wrong.")
        try:  # we close dialog_typer if it's opened because even after closing self.transport it keeps trying to send text
            self.dialog_typer.cancel()
        except AttributeError:
            pass
        self.transport.close()
        print(f"Client \033[031maborted\033[0m connection: {self.peername}")

    def _timeout(self):
        self.transport.write(bytes("Время вышло, соединение закрыто", encoding="utf-8"))
        print(f"\033[031mTimed out\033[0m connection: {self.peername}")
        self.transport.close()


async def main(host, port):
    loop = asyncio.get_running_loop()
    server = await loop.create_server(JacqueServer, host, port)
    print(f"[\033[032m✅\033[00m]\033[032m Socket server successfuly launched on {port} port!\033[0m")
    print("[\033[034m👨‍\033[0m]\033[034m Server made by \033[035m\033[004m@sultanowskii\033[0m")
    print("[\033[036m📄\033[0m]\033[036m Server logs:\033[0m\n")
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main(HOST, PORT))

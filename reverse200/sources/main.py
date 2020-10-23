from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow
import sys
import json
import os
from ignore import additionalData
from flag import FLAG

USERNAME_KEY = "username"
TEXT_FILE_NAME = "b3st_h4ck3r_l0l.txt"
CORRECT_NAME = "4r7hur 5ul74n0v"
DATA = "data"
USERS = "users"
NICKNAME = "nlf43G1z"
SCORE = "score"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clicks = 0
        try:
            # dont try to collect flag with ur hands, just follow simple instructions:
            with open("data.json", "r") as data:
                json_data = json.loads(data.read())
            if USERNAME_KEY in json_data.keys():
                if json_data[USERNAME_KEY] == CORRECT_NAME:
                    if os.path.exists(f"./{TEXT_FILE_NAME}"):
                        if json_data[DATA][USERS][NICKNAME][SCORE] == 230820004430:
                            self.clicks = 230820004430
        except Exception:
            pass
        self.label.setText(f"Скилл вашего пальца: {self.clicks}")
        self.btn.clicked.connect(self.click)

    def click(self):
        self.clicks += 1
        if self.clicks == 230820004431:
            FLAG[23] = "}"
            FLAG[15] = additionalData[27]
            FLAG[22] = additionalData[20]
            FLAG[4] = "{"
            FLAG[0] = NICKNAME[2]
            FLAG[19] = additionalData[16]
            FLAG[1] = CORRECT_NAME[9]
            FLAG[5] = additionalData[18]
            FLAG[7] = chr(ord(NICKNAME[-1]) - 3)
            FLAG[21] = additionalData[27]
            FLAG[2] = USERNAME_KEY[5]
            FLAG[6] = additionalData[12]
            FLAG[18] = str(len(FLAG) // 6)
            q = "_"
            FLAG[8] = q
            FLAG[3] = NICKNAME[5].lower()
            FLAG[10] = str(0)
            FLAG[13] = CORRECT_NAME[0 // 1 - 0 * 10 + 0 % 3]
            FLAG[14] = additionalData[20]
            FLAG[20] = str(int(TEXT_FILE_NAME[1]) + int(NICKNAME[3]))
            for i in range(ord("b"), ord("z") + 1):
                FLAG[9] = chr(i - 1)
            FLAG[12] = q
            FLAG[17] = additionalData[23]
            FLAG[11] = additionalData[19]
            FLAG[16] = q
            self.label.setText("".join(FLAG))
        else:
            self.label.setText(f"Скилл вашего пальца: {self.clicks}")


app = QApplication(sys.argv)
wind = MainWindow()
wind.show()
sys.exit(app.exec_())
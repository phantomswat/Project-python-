import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow
from ss2000 import Ui_MainWindow

pygame.mixer.init()
def play_ah():
    pygame.mixer.music.load("mp3/AH.mp3")
    pygame.mixer.music.play()
    # a = pygame.mixer.Sound("mp3/AH.mp3")
    # a.play()
def play_man():
    pygame.mixer.music.load("mp3/MAN.mp3")
    pygame.mixer.music.play()
    # b = pygame.mixer.Sound("mp3/MAN.mp3")
    # b.play()
def play_hl():
    pygame.mixer.music.load("mp3/HL.mp3")
    pygame.mixer.music.play(-1)
def play_yelp():
    pygame.mixer.music.load("mp3/YELP.mp3")
    pygame.mixer.music.play(-1)
def play_wail():
    pygame.mixer.music.load("mp3/WAIL.mp3")
    pygame.mixer.music.play(-1)

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

    def pushButton_click(self):
        Sender = self.sender()
        clickevent = Sender.text()
        if clickevent == "H/L":
            play_hl()
        elif clickevent == "YELP":
            play_yelp()
        elif clickevent == "WAIL":
            play_wail()
        else:
            pygame.mixer.music.stop()

    def pushButton_pressed(self):
        Sender = self.sender()
        clickevent = Sender.text()
        if clickevent == "A/H":
            play_ah()
        else:
            play_man()

    def pushButton_released(self):
        Sender = self.sender()
        clickevent = Sender.text()
        if clickevent == "A/H":
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
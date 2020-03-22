import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('시작')
        btn1.clicked.connect(self.start_btn)

        btn2 = QPushButton('종료')
        btn2.clicked.connect(self.end_btn)

        btn3 = QPushButton('완전 종료')
        btn3.clicked.connect(self.close_btn)

        btn4 = QPushButton('리셋')
        btn4.clicked.connect(self.reset_btn)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        groupbox1 = QGroupBox('시작 시간')
        self.bx1 = QVBoxLayout()
        groupbox1.setLayout(self.bx1)

        groupbox2 = QGroupBox('종료 시간')
        self.bx2 = QVBoxLayout()
        groupbox2.setLayout(self.bx2)

        groupbox3 = QGroupBox('총 시간')
        self.bx3 = QVBoxLayout()
        groupbox3.setLayout(self.bx3)

        groupbox4 = QGroupBox('논 시간')
        self.bx4 = QVBoxLayout()
        groupbox4.setLayout(self.bx4)

        hbox = QHBoxLayout()
        hbox.addWidget(groupbox1)
        hbox.addWidget(groupbox2)
        hbox.addWidget(groupbox3)
        hbox.addWidget(groupbox4)
        hbox.addLayout(vbox)

        self.setWindowTitle('Chronometry')
        self.setLayout(hbox)
        self.setGeometry(100, 100, 600, 150)
        self.show()

    def start_btn(self):
        print('시작버튼')

    def end_btn(self):
        print('종료버튼')

    def close_btn(self):
        print('완전종료버튼')

    def reset_btn(self):
        print('리셋버튼')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
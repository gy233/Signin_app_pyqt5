from PyQt5.QtCore import QThread, QMutex, pyqtSignal
import sys, time


class Thread1(QThread):
    log = pyqtSignal(int)

    def __init__(self):
        super(Thread1, self).__init__()
        self.qmut_1 = QMutex()

    def run(self):
        self.qmut_1.lock()  # 加锁
        values = [1, 2, 3, 4, 5]
        for i in values:
            print(i)
            time.sleep(0.5)  # 休眠
        self.qmut_1.unlock()  # 解锁


class Thread2(QThread):
    log = pyqtSignal(str)
    signal = pyqtSignal()

    def __init__(self):
        super(Thread2, self).__init__()

    def run(self):
        values = ["a", "b", "c", "d", "e"]
        for i in values:
            print(i)
            self.log.emit(i)
            time.sleep(0.5)
        self.signal.emit()

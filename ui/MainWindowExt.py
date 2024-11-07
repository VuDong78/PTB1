from ui.MainWindow import Ui_MainWindow
from utils import Function

class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass

        self.MainWindow=MainWindow
        self.pushButtonSolve.clicked.connect(self.Solve)
        self.SignalAndSlot()
    def Solve(self):
        a=float(self.lineEditA.text())
        b=float(self.lineEditB.text())
        result=Function(a,b)
        self.lineEditResult.setText(result)

    def showWindow(self):
        self.MainWindow.show()



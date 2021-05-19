import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        

        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("DeskMan: Text Editor")
        self.setStyleSheet("background-color: white;")

        self._createMenuBar()
        self._textedit()

    def _createMenuBar(self):

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        #file actions
        actionFile = menuBar.addMenu("&File")
        newAction = actionFile.addAction("New")
        openAction = actionFile.addAction("Open")
        saveAction = actionFile.addAction("Save")
        saveasAction = actionFile.addAction("Save As")
        actionFile.addSeparator()
        quitAction = actionFile.addAction("Quit")

        #file actions shortcuts
        saveAction.setShortcut("Ctrl+S")
        saveasAction.setShortcut("Shift+Ctrl+S")
        newAction.setShortcut("Ctrl+N")
        openAction.setShortcut("Ctrl+O")
        quitAction.setShortcut("Ctrl+Q")
        
        #editing options
        editMenu = menuBar.addMenu("&Edit")
        copyAction = editMenu.addAction("Copy")
        pasteAction = editMenu.addAction("Paste")
        cutAction = editMenu.addAction("Cut")

        #edit option shortcuts
        copyAction.setShortcut("Ctrl+C")
        pasteAction.setShortcut("Ctrl+V")
        cutAction.setShortcut("Ctrl+X")

        #finding actions
        findMenu = menuBar.addMenu("&Find")
        findAction =findMenu.addAction("Find")
        replaceAction = findMenu.addAction("Replace")

        #find and replace shortcuts
        findAction.setShortcut("Ctrl+F")
        replaceAction.setShortcut("Ctrl+H")

        helpMenu = menuBar.addMenu("&Help")


    def _textedit(self):
        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)

    def _filemanager(self):
        




    
        
        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())








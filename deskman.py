import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        

        self.setGeometry(100,100,1030,800)
        self.setStyleSheet("background-color: white;")

        self.path = None

        self.text_edit()
        self.create_MenuBar()
        self.update_page_title()

        # setting default font for editor 
        defaultfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        defaultfont.setPointSize(12)
        self.textEditor.setFont(defaultfont)

        self.status = QStatusBar()
        self.setStatusBar(self.status)


    def create_MenuBar(self):

        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        menuFont = menuBar.font()
        menuFont.setPointSize(13)
        menuBar.setFont(menuFont)

        self.setStyleSheet("""QMenuBar { background-color:rgba(135,206,235 ,1 ); }""")

        #menu item i

        #file actions
        actionFile = menuBar.addMenu("&File")

        #open new file
        newAction = actionFile.addAction("New")
        newAction.setShortcut("Ctrl+N")
        
        
        #open existing files
        openAction = actionFile.addAction("Open")
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.open_file)

        #save
        saveAction = actionFile.addAction("Save")
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.save_file)

        #save as 
        saveasAction = actionFile.addAction("Save As")
        saveasAction.setShortcut("Shift+Ctrl+S")
        saveasAction.triggered.connect(self.save_as_file)

        
        #menu item ii
        
        #editing options
        editMenu = menuBar.addMenu("&Edit")

        copyAction = QAction("Copy",self)
        copyAction.setStatusTip("Copy selected text")
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.textEditor.copy)
        editMenu.addAction(copyAction)

        pasteAction = QAction("Paste",self)
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.setStatusTip("paste copied text")
        pasteAction.triggered.connect(self.textEditor.paste)
        editMenu.addAction(pasteAction)

        cutAction = QAction('Cut',self)
        cutAction.setShortcut("Ctrl+X")
        cutAction.setStatusTip("cut selected text")
        cutAction.triggered.connect(self.textEditor.cut)
        editMenu.addAction(cutAction)

        #menu item iii

        helpMenu = menuBar.addMenu("&Help")


    def text_edit(self):
        self.textEditor = QTextEdit(self)
        self.setCentralWidget(self.textEditor)


    #open file method
    def open_file(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Open file", "", 
                             "Text documents (*.txt);Python Files (*.py); PHP Files(*.php); All Files(*.*)")
        if self.path:
        	with open(self.path, 'r') as f:
        		text_content = f.read()
        		self.textEditor.setText(text_content)
        		self.update_page_title()
        else:
            self.path_error()

    #save files method
    def save_file(self):
    	if not self.path:
    		return self.save_as_file()
    	self.save_file_to_path(self.path)


    #save as method

    def save_file_to_path(self,path):
    	self.text = self.textEditor.toPlainText()

    	with open(path, 'w') as f:
    		f.write(self.text)
    	self.path = path
    	self.update_page_title()

    # save file to path method
    def save_as_file(self):
    	self.path,_ =QFileDialog.getSaveFileName(self,"Save as","",
    		               "Text Documents (*.txt); Python Files (*.py); PHP Files (*.php); All Files(*.*)")
    	if not self.path:
    		return
    	self.save_file_to_path(self.path)

    def update_page_title(self):
    	self.setWindowTitle("%s - DeskMan: Text Editor"%(os.path.basename(self.path)
    		                                             if self.path else "Untitled"))
    def path_error(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Invalid file type")
        messageBox.setText("Selected file or path is invalid. Please select valid file or  double check path ")
        messageBox,exec()  	
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("DeskMan: Text Editor")
    screen = Window()
    screen.show()
    sys.exit(app.exec_())
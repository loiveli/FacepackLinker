from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Slot

class FileBrowser(QtWidgets.QWidget):
    def __init__(self,label, text,acceptedTypes,file = True, *args, **kwargs):
        super(FileBrowser, self).__init__(*args, **kwargs)
        self.acceptedTypes = acceptedTypes
        self.text = text
        self.file = file
        self.fileName = ""
        layout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel(f"{label}:")
        self.pathField = QtWidgets.QLineEdit("")
        self.button = QtWidgets.QPushButton("Browse")
        layout.addWidget(self.label)
        layout.addWidget(self.pathField)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.browse)
        self.setLayout(layout)

    def browse(self):
        if(self.file):
            self.fileName, filter = QtWidgets.QFileDialog().getOpenFileName(self, self.text, self.fileName,self.acceptedTypes)
        else:
            self.fileName= QtWidgets.QFileDialog().getExistingDirectory(self, self.text, self.fileName)
        self.pathField.setText(self.fileName)

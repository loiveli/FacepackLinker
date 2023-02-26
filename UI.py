import sys
import functionality
from PySide6 import QtCore, QtWidgets, QtGui
from FileBrowser import FileBrowser


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.shortlist = FileBrowser("Shortlist","Select the shortlist file", "Web page (*.html)")
        self.playerPictures = FileBrowser("Player folder", "Select the folder with the pictures", "", False)
        self.layout = QtWidgets.QFormLayout(self)
        renameLabel = QtWidgets.QLabel("Rename the files to player IDs")
        self.rename = QtWidgets.QCheckBox(self)
        self.functionalityButton = QtWidgets.QPushButton("Link pictures", enabled=False)
        self.renameLayout = QtWidgets.QHBoxLayout()
        self.renameLayout.addWidget(renameLabel)
        self.renameLayout.addWidget(self.rename)
        self.layout.addRow(self.shortlist)
        self.layout.addRow(self.playerPictures)
        self.layout.addRow(self.renameLayout)
        self.layout.addRow(self.functionalityButton)
        self.shortlist.pathField.textChanged[str].connect(self.activateButton)
        self.playerPictures.pathField.textChanged[str].connect(self.activateButton)
        self.functionalityButton.clicked.connect(self.linkPlayers)
    def activateButton(self):
        if self.shortlist.pathField.text() and self.playerPictures.pathField.text():
            self.functionalityButton.setEnabled(True)
    def linkPlayers(self):
        messageBox = QtWidgets.QMessageBox()
        messageText = functionality.linkPlayers(self.shortlist.fileName, self.playerPictures.fileName, self.rename.isChecked() )
        messageBox.setText(messageText)
        messageBox.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 200)
    widget.show()

    sys.exit(app.exec())
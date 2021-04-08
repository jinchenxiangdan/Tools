
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        

        # initial UI
        self.setWindowTitle('Mew Translator')
        self.setGeometry(300,300,400,300)
        # layout 
        topLayout = QHBoxLayout()
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)


        # create a widget 
        widget = QWidget()
        # text edit
        text_edit_1 = QTextEdit()
        text_edit_1.setPlainText('Input words that you want to transfer.')
        text_edit_2 = QTextEdit()
        text_edit_2.setPlainText('This will show the translated output.')
        # create widget layout
        widget2hbox = QHBoxLayout()
        widget2hbox.setContentsMargins(5, 5, 5, 5)
        widget2hbox.addWidget(text_edit_1)
        widget.setLayout(widget2hbox)
        self.setWidget(widget)



        # set style of this GUI
        self.changeStyle('Fusion')
        self.show()

    def changeStyle(self, styleName):
            QApplication.setStyle(QStyleFactory.create(styleName))
            QApplication.setPalette(QApplication.style().standardPalette())
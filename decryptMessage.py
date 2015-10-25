#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows a QProgressBar widget.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar,QPushButton, QApplication, QLabel)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 400, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(190, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 480, 160)
        self.setWindowTitle('QProgressBar')

        self.lbl2 = QLabel('                                                                           ', self)
        self.lbl2.move(100, 2)
        self.show()
        
        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        if self.step == 20:
            self.lbl2.setText("It actually doesn't take this long to decrypt...")

        if self.step == 50:
            self.lbl2.setText("It just looks more intense.....")

        if self.step == 70:
            self.lbl2.setText("  ;)   :)")
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

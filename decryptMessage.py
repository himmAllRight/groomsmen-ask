import sys
import rycrypt

from PyQt5.QtWidgets import (QWidget, QProgressBar,QPushButton, QApplication, QLabel, QMessageBox)
from PyQt5.QtCore import QBasicTimer
from operator import itemgetter
    
def decrypt(pairList):
    indexList = pairList[0]
    s = pairList[1]
    m = list(map((lambda x, y: [x, y]), list(map(int, indexList.split(","))), s))
    m = sorted(m, key=itemgetter(0))
    return("".join(list(map((lambda x: x[1]), m))))


class Example(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 400, 25)

        self.btn = QPushButton('            Start            ', self)
        self.btn.move(160, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 480, 160)
        self.setWindowTitle('QProgressBar')

        self.lbl2 = QLabel('                                                                           ', self)
        self.lbl2.move(100, 2)

        self.loaded = False
        
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText(decrypt(('3,18,19,14,13,12,10,8,15,7,2,0,17,9,16,11,6,4,1,5', 'cgeem e soiCassetkl ')))
            self.loaded = True
            return

        if self.step == 20:
            self.lbl2.setText(decrypt(('28,35,33,8,16,39,27,7,17,22,2,4,19,31,1,42,6,5,37,26,21,38,40,10,11,36,32,9,29,34,3,13,44,25,47,12,41,20,14,46,18,23,24,43,30,0,45,15', "stglneia'k c otyut hadcy onl  aott.drte.te plI.s")))

        if self.step == 50:
            self.lbl2.setText(decrypt(('13,10,27,20,24,21,26,28,25,11,18,14,8,0,19,5,9,3,23,15,1,12,17,30,16,4,29,7,6,22,2', ' o.nst..ek mlIisojnotse.ru. te ')))

        if self.step == 70:
            self.lbl2.setText(decrypt(('4,8,5,3,6,7,1,2,0', ' ) ) : ; ')))

        self.step = self.step + 1
        self.pbar.setValue(self.step)
        

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        elif self.loaded:
            self.btn.setText('Cool.')
            QMessageBox.information(self,decrypt(('5,2,8,1,4,3,7,0,6', 'an!orgsCt')), decrypt(('19,57,104,395,48,457,170,91,176,222,287,70,433,335,345,413,420,318,119,360,385,220,382,24,323,45,326,190,339,425,262,398,309,128,245,112,379,276,172,417,330,73,200,40,5,229,18,359,59,310,350,69,54,158,342,351,182,219,291,206,152,38,268,407,325,243,145,410,253,150,305,81,53,20,3,346,353,10,363,86,139,447,29,165,39,336,142,80,242,167,28,97,166,452,378,125,2,403,375,193,277,218,116,174,109,89,161,186,349,434,390,281,267,212,401,240,295,440,332,127,129,239,204,455,72,22,155,143,197,67,271,228,352,340,231,46,273,261,203,215,192,308,51,9,76,194,184,302,181,87,95,427,255,265,405,312,103,82,269,415,223,300,138,78,224,254,225,108,201,149,411,232,355,258,458,446,77,294,377,298,316,289,396,185,426,386,371,226,256,233,160,68,217,199,235,88,168,130,422,213,52,32,380,55,99,98,419,64,154,406,370,49,238,162,164,221,293,17,260,387,306,90,365,177,115,93,122,373,105,7,208,384,444,107,313,151,341,34,448,12,251,216,178,230,102,171,58,279,358,376,234,114,26,196,284,288,338,301,101,404,74,356,94,141,14,322,304,337,163,324,47,280,173,210,211,83,381,431,42,383,368,428,392,272,317,331,63,92,329,454,374,56,246,416,31,189,111,187,123,348,250,188,354,195,205,180,4,275,120,436,439,159,388,71,441,274,148,113,278,283,23,33,175,132,11,423,241,110,421,147,25,6,75,191,282,209,140,244,227,367,247,400,259,156,389,456,362,202,307,144,394,357,303,391,66,41,451,408,361,16,237,319,393,79,43,366,44,402,443,429,442,299,61,15,399,137,321,21,214,146,136,85,169,35,118,248,36,0,252,257,327,438,296,249,435,126,418,430,333,198,372,347,13,292,8,133,117,179,424,397,134,135,412,432,1,37,60,96,131,315,320,285,449,207,311,344,121,334,450,414,297,266,27,453,437,270,286,65,106,157,343,314,445,183,62,290,124,409,30,236,84,263,369,50,328,264,100,153,364', "esam Ph iuui iv u       l bi aisn eah tsfr yiihnedhfoldi Ioe gtrmaoo 'thrrsege  ye euo whllilb oipa a ot ntltt e   Ii net r u  stI  na bo ungu hoayvywwieivrlahtmh tbdlasnna y.xufdtn e sreecl  ee a ehsgkooetmceedm.otj wteotosmods  co lstntcatc tBam enl i ,tsa  eE ue  n aew detwt tuehcdunt etm 'sklo y o.tca ea neagtdd,slI ht   Bclws nloovd hdpad:fo h vet sasi pte tuouerh  aedeeiunIwheoeTordurwor  chrrrut.rses A,oh nrxah u eenttisnllrebeBb teboymiau tnya .by")))
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

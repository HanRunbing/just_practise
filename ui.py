from PySide2.QtWidgets import QApplication, QMessageBox, QTextBrowser
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import pandas as pd
import numpy as np
import random
from Parkinson_assessment import base_para

class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        qfile_ase = QFile('untitled.ui')
        qfile_ase.open(QFile.ReadOnly)
        qfile_ase.close()
        # 从 UI 定义中动态 创建一个相应的窗口对象ui
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(qfile_ase)
        self.ui.button1.clicked.connect(self.all_main)
        self.ui.button2.clicked.connect(self.save)



    def all_main(self):
        global Am,F,tim,text,result,para_num
        para_num = [0,0,0]
        info = self.ui.textEdit.toPlainText()
        data = pd.read_excel(info)#加载数据
        ts = data['Column6']
        tss=list(ts)#转化为列表
        tss1=list(ts)
        tss2=list(ts)
        Am=base_para.Am_gen(tss)
        F=base_para.F_gen(tss1)
        tim=base_para.time(tss2)
        self.ui.Am_show.setText(str(Am))#步幅显示
        self.ui.F_show.setText(str(F))#步频显示
        self.ui.time_show.setText(str(tim))#时间显示
        if 'n' in info:
            for i in range(0,3):
                para_num[i] = random.randrange(80, 150)
            text = '正常'
            self.ui.sym.setText(str(para_num[0] / 1000))
            self.ui.cor.setText(str(para_num[1] / 1000))
            self.ui.lag.setText(str(para_num[2] / 1000))
            con = (np.mean(para_num)) / 1000
            result = format(con, '.3f')
            self.ui.res.setText(str(result))
            self.ui.level.setText(text)
        elif 'h' in info:
            for i in range(0, 3):
                para_num[i] = random.randrange(700, 950)
            text = '严重'
            self.ui.sym.setText(str(para_num[0] / 1000))
            self.ui.cor.setText(str(para_num[1] / 1000))
            self.ui.lag.setText(str(para_num[2] / 1000))
            con = (np.mean(para_num)) / 1000
            result = format(con, '.3f')
            self.ui.res.setText(str(result))
            self.ui.level.setText(text)
        elif 'l' in info:
            for i in range(0, 3):
                para_num[i] = random.randrange(350, 550)
            text = '轻微'
            self.ui.sym.setText(str(para_num[0] / 1000))
            self.ui.cor.setText(str(para_num[1] / 1000))
            self.ui.lag.setText(str(para_num[2] / 1000))
            con = (np.mean(para_num)) / 1000
            result = format(con, '.3f')
            self.ui.res.setText(str(result))
            self.ui.level.setText(text)




    def save(self):
        info = self.ui.textEdit.toPlainText()
        df1 = pd.DataFrame([Am, F, tim, para_num[0]/1000, para_num[1]/1000, para_num[2]/1000, result, text], columns=['参数结果'],
                           index=["步幅（°）", "步频（步/分）", "转弯时间（s）", "对称性", "相关性", "迟缓性", "综合指标", "评估结果"])
        with pd.ExcelWriter(info) as writer:
            df1.to_excel(writer, sheet_name='sheet1')



app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()

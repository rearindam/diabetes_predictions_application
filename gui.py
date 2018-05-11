
"""
GUI for diabetes prediction.
"""
import sys,os

from PyQt5.QtWidgets import QFrame, QSpacerItem, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QLine, QSize
import pandas as pd
#import diabetes
import joblib

class Diabetes(QWidget):

    def __init__(self)  :
        super(Diabetes, self).__init__()
        self.cwd = os.path.dirname(__file__)
        self.sub_head = QLabel("Patient's Details")
        self.sub_head.setStyleSheet("color: #02205b; font: 25pt Palatino Linotype")
        self.l0 = QLineEdit()
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()
        self.l4 = QLineEdit()
        self.l5 = QLineEdit()
        self.t0 = QLabel("Patient's Name:")
        self.t0.setStyleSheet("color: #02205b; font: 15pt ; font-family: Palatino Linotype; padding-left:25px ")
        self.t1 = QLabel("Plasma glucose concentration:")
        self.t1.setStyleSheet("color: #02205b; font: 15pt Palatino Linotype; padding-left:25px")
        self.t2 = QLabel("Diastolic blood pressure:")
        self.t2.setStyleSheet("color: #02205b; font: 15pt Palatino Linotype; padding-left:25px")
        self.t3 = QLabel("Triceps skin fold thickness:")
        self.t3.setStyleSheet("color: #02205b; font: 15pt Palatino Linotype; padding-left:25px")
        self.t4 = QLabel("Serum insulin:")
        self.t4.setStyleSheet("color: #02205b; font: 15pt Palatino Linotype; padding-left:25px")
        self.t5 = QLabel("Body mass index:")
        self.t5.setStyleSheet("color: #02205b; font: 15pt Palatino Linotype; padding-left:25px")
        self.r0 = QLabel("")
        self.r1 = QLabel(" mg/dl")
        self.r1.setStyleSheet("color: #02205b; font: 12pt Palatino Linotype")
        self.r2 = QLabel(" mm Hg")
        self.r2.setStyleSheet("color: #02205b; font: 12pt Palatino Linotype")
        self.r3 = QLabel(" mm")
        self.r3.setStyleSheet("color: #02205b; font: 12pt Palatino Linotype")
        self.r4 = QLabel(" mIU/L")
        self.r4.setStyleSheet("color: #02205b; font: 12pt Palatino Linotype")
        self.r5 = QLabel("")
        self.r5.setStyleSheet("color: #02205b; font: 12pt Palatino Linotype")
        self.h1 = QHBoxLayout()
        self.h0 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.space = QSpacerItem(25, 10)
        self.h1.addSpacerItem(self.space)
        self.h1.addSpacing(20)
        self.h0.addSpacerItem(self.space)
        self.h0.addSpacing(20)
        self.h2.addSpacerItem(self.space)
        self.h2.addSpacing(20)
        self.h3.addSpacerItem(self.space)
        self.h3.addSpacing(20)
        self.h4.addSpacerItem(self.space)
        self.h4.addSpacing(20)
        self.h5.addSpacerItem(self.space)
        self.h5.addSpacing(20)
        self.clbtn = QPushButton("CLEAR")
        self.clbtn.setFixedWidth(100)
        self.clbtn.setFixedHeight(20)
        self.clbtn.setFont(QFont("Times",10, weight=QFont.Bold))
        self.clbtn.setStyleSheet("QPushButton { background-color: #b1bbcc }"
                           "QPushButton:pressed { background-color: grey }"
                           "QPushButton { padding: 1px; border-radius: 3px; border: 1px solid grey }")
        self.submit = QPushButton("SUBMIT")
        self.submit.setFixedWidth(100)
        self.submit.setFixedHeight(20)
        self.submit.setFont(QFont("Times",10, weight=QFont.Bold))
        self.submit.setStyleSheet("QPushButton { background-color: #b1bbcc }"
                           "QPushButton:pressed { background-color: grey }"
                           "QPushButton { padding: 1px; border-radius: 3px; border: 1px solid grey }")
        self.v1_box = QVBoxLayout()
        self.v2_box = QVBoxLayout()
        self.head_l = QHBoxLayout()
        self.final_hbox = QHBoxLayout()
        self.initui()
        self.setStyleSheet('background-color: #c8cec8')
        

    def initui(self) :
        """ The gui is created and widgets elements are set here """
        self.v1_box.addSpacing(10)
        self.v1_box.setSpacing(2)
        about = QPushButton(QIcon(self.cwd+"/icons/info.png"), "")
        about.setToolTip("ABOUT")
        about.setFixedSize(30, 30)
        about.setIconSize(QSize(20, 20))
        about.setStyleSheet("QPushButton { background-color: #ffffff }"
                           "QPushButton:pressed { background-color: grey }"
                           "QPushButton { padding: 1px; border-radius: 8px; border: 1px solid grey }")
        about.clicked.connect(lambda: self.about())
        self.head_l.addSpacing(210)
        self.head_l.addWidget(self.sub_head, 0, Qt.AlignCenter)
        
        self.head_l.addWidget(about,0,Qt.AlignRight)
        self.v1_box.addLayout(self.head_l)
        self.l1.setValidator(QDoubleValidator())
        self.l2.setValidator(QDoubleValidator())
        self.l3.setValidator(QDoubleValidator())
        self.l4.setValidator(QDoubleValidator())
        self.l5.setValidator(QDoubleValidator())
        self.l0.setToolTip("Enter name here")
        self.l1.setToolTip("2 hours in an oral glucose tolerance test \nrange:70-180 mg/dl")
        self.l2.setToolTip("80-140mm Hg")
        self.l3.setToolTip("10-50mm")
        self.l4.setToolTip("15-276MIU/ml")
        self.l5.setToolTip("weight in kg/(height in m)^2 \nrange:10-50")
        self.l0.setFixedSize(300, 30)
        self.l0.setStyleSheet("background-color: #e0e1e2; font: 12pt Palatino Linotype")
        self.l0.setContentsMargins(150,0,0,0)
        self.l1.setFixedSize(40,30)
        self.l1.setStyleSheet("background-color: #e0e1e2; font: 12pt Palatino Linotype")
        self.l2.setFixedSize(40,30)
        self.l2.setStyleSheet("background-color: #e0e1e2; font: 12pt Palatino Linotype")
        self.l3.setFixedSize(40,30)
        self.l3.setStyleSheet("background-color: #e0e1e2; font: 12pt Palatino Linotype")
        self.l4.setFixedSize(40,30)
        self.l4.setStyleSheet("background-color: #e0e1e2; font: 12pt Palatino Linotype")
        self.l5.setFixedSize(40,30)
        self.l5.setStyleSheet("background-color: #e0e1e2; font: 12pt Palatino Linotype")
        self.h0.addWidget(self.t0)
        self.h0.addSpacing(15)
        self.h0.addWidget(self.l0)
        self.h0.addWidget(self.r0)
        self.v1_box.addLayout(self.h0)
        self.h1.addWidget(self.t1)
        self.h1.addSpacing(36)
        self.h1.addWidget(self.l1)
        self.h1.addWidget(self.r1)        
        self.v1_box.addLayout(self.h1)
        self.h2.addWidget(self.t2)
        self.h2.addSpacing(83)
        self.h2.addWidget(self.l2)
        self.h2.addWidget(self.r2)       
        self.v1_box.addLayout(self.h2)
        self.h3.addWidget(self.t3)
        self.h3.addSpacing(65)
        self.h3.addWidget(self.l3)
        self.h3.addWidget(self.r3)       
        self.v1_box.addLayout(self.h3)
        self.h4.addWidget(self.t4)
        self.h4.addSpacing(128)
        self.h4.addWidget(self.l4)
        self.h4.addWidget(self.r4)      
        self.v1_box.addLayout(self.h4)
        self.h5.addWidget(self.t5)
        self.h5.addSpacing(128)
        self.h5.addWidget(self.l5)
        self.h5.addWidget(self.r5)      
        self.v1_box.addLayout(self.h5)
        self.h6 = QHBoxLayout()
        self.submit.clicked.connect(lambda: self.test_input())
        self.submit.setToolTip("Click to check if patient has diabetes")
        self.clbtn.clicked.connect(lambda: self.clfn())
        self.h6.addWidget(self.submit)
        self.h6.addWidget(self.clbtn)
        self.v1_box.addLayout(self.h6)
        self.final_hbox.addLayout(self.v1_box)
        self.final_hbox.addSpacerItem(QSpacerItem(30, 30))
        self.setLayout(self.final_hbox)
        self.setWindowIcon(QIcon(self.cwd+'/icons/gui.ico'))
        

    def clfn(self):
        """ clear all the text fields via clear button"""
        self.l0.clear()
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
        self.l3.clear()
        self.l4.clear()
        self.l5.clear()
        

    def test_input(self) :
        """ test for diabetes"""
        l = []
        try:
            my_dict = {"B":float(self.l1.text()), "C":float(self.l2.text()),"D":float(self.l3.text()), "E":float(self.l4.text()), "F": float(self.l5.text())}
            l = list(my_dict.values())
            print(l)
        except:
            self.warning()
            return
        
        if None in l:
            self.warning()
            return
        output = self.check_input(my_dict)
        report = "Patient's name: {}\nPlasma glucose concentration: {}mg/dl \
 \nDiastolic blood pressure: {} mm Hg\nTriceps skin fold thickness: {} mm\nSerum insulin: {} mIU/L\nBody mass index: {}\n".format(self.l0.text(), self.l1.text(), self.l2.text(), self.l3.text(),self.l4.text(),self.l5.text())
        if output == 0:
            report+="Result: Our Diagnosis suggests that patient does not suffers from diabetes."
        else:
            report+="Result: Our diagnosis suggests patient does suffer from diabetes.Please get checked soon."
        #
        rep = ReportWindow(output,self.l0.text(),report)
        rep.show()

    def mwindow(self) :
        """ window features are set here and application is loaded into display"""
        self.setFixedSize(700, 422)
        self.setWindowTitle("Diabetes Prediction App")
        self.show()
    
    def find_data_file(self,filename):
        if getattr(sys, "frozen", False):
        # The application is frozen.
            datadir = os.path.dirname(sys.executable)
        else:
        # The application is not frozen.
            datadir = os.path.dirname(__file__)
        return os.path.join(datadir, filename)


    def check_input(self,data) :
        df=pd.DataFrame(data=data,index=[0])
        with open(self.find_data_file('svc.pkl'),'rb') as model:
            p=joblib.load(model)
        op=p.predict(df)
        return op[0]

    def about(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(
            "We have used Support Vector Classifier from sklearn python library.\nAccuracy of model: 80%\nFor the GUI PyQt5 has been used.")
        msg.setInformativeText(
            "The dataset has been taken from UCI PIMA Indian dataset containig 786 instances.\nIcons and images are taken from www.flaticons.com")
        msg.setWindowTitle("About")
        msg.setDetailedText(
            "The creators of this app are: \nAbhisek Hazra\nAbisek Sutradhar\nArindam Ghosh")
        msg.setStyleSheet('background-color: #c8cec8')
        msg.exec_()

    def warning(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Please provide all the inputs")
        msg.setWindowTitle("Warning")
        msg.setStyleSheet('background-color: #c8cec8')
        msg.exec_()

class ReportWindow(QWidget):
        def __init__(self, output, name, report)  :
            QWidget.__init__(self)
            self.cwd = os.path.dirname(__file__) 
            self.setWindowTitle("{}'s Report".format(name))
            self.layout = QVBoxLayout()
            self.label = QLabel("Report")
            self.label.setStyleSheet("color: #02205b; font: 25pt Palatino Linotype")
            self.image = QLabel()
            self.result = QLabel("")
            self.result.setStyleSheet("color: #02205b; font: 18pt Palatino Linotype")
            self.output = output
            self.report()
            self.result.setWordWrap(True)
            self.layout.addWidget(self.label,0, Qt.AlignCenter)
            self.layout.addWidget(self.image,0,Qt.AlignCenter)
            self.layout.addWidget(self.result,0, Qt.AlignCenter)
            self.layout.addSpacerItem(QSpacerItem(100,40))
            self.close_btn = QPushButton("Close")
            self.close_btn.clicked.connect(lambda: self.close())
            self.close_btn.setFixedWidth(100)
            self.close_btn.setFixedHeight(20)
            self.close_btn.setFont(QFont("Times",10, weight=QFont.Bold))
            self.close_btn.setStyleSheet("QPushButton { background-color: #b1bbcc }"
                           "QPushButton:pressed { background-color: grey }"
                           "QPushButton { padding: 1px; border-radius: 3px; border: 1px solid grey }")
            self.save_btn = QPushButton("Save")
            self.save_btn.clicked.connect(lambda: self.save_report(name,report))
            self.save_btn.setFixedWidth(100)
            self.save_btn.setFixedHeight(20)
            self.save_btn.setFont(QFont("Times",10, weight=QFont.Bold))
            self.save_btn.setStyleSheet("QPushButton { background-color: #b1bbcc }"
                           "QPushButton:pressed { background-color: grey }"
                           "QPushButton { padding: 1px; border-radius: 3px; border: 1px solid grey }")
            self.h_box = QHBoxLayout()
            self.h_box.addWidget(self.save_btn)
            self.h_box.addWidget(self.close_btn)
            self.layout.addLayout(self.h_box)
            self.setFixedSize(600, 400)
            self.setLayout(self.layout)
            self.setStyleSheet('background-color: #c8cec8')
            self.setWindowIcon(QIcon(self.cwd+'/icons/gui.ico'))
            
        def report(self):
            if self.output == 0:
                self.image.setPixmap(QPixmap(self.cwd+'/icons/happy.png'))
                self.result.setText("Our diagnosis suggests that patient does not suffers from diabetes.")
            else :
                self.image.setPixmap(QPixmap(self.cwd+'/icons/sad.png'))
                self.result.setText("Our diagnosis suggests patient does suffer from diabetes.\nPlease get checked soon.")
                self.label.setStyleSheet("color: #f44242 ; font: 25pt Palatino Linotype")
                self.result.setStyleSheet("color: #f44242; font: 18pt Palatino Linotype")
                
            
        def save_report(self, name, result): 
            if not os.path.exists("reports"):
                os.makedirs("reports")
            cwd = os.getcwd()
            file_path = cwd+"\\reports\\"+name+"_report.txt"
            with open(file_path, 'w') as f:
                f.write(result)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Report saved to {}".format(file_path))
            msg.setWindowTitle("Saved Successfully")
            msg.setStyleSheet('background-color: #c8cec8')
            
            msg.exec_()
        
            

            

if __name__=="__main__":
    app = QApplication(sys.argv)
    a_window = Diabetes()
    a_window.mwindow()
sys.exit(app.exec_())

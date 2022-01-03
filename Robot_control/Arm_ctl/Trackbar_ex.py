# -*- coding: utf-8 -*-
import sys
import time
from Arm_Lib import Arm_Device
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

Arm = Arm_Device()
time.sleep(.1)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 150, 600, 500)  # 창의 위치와 크기
        self.setWindowTitle("Slider Widget")
        self.UI()
        
    def UI(self):
        vbox = QVBoxLayout()
        vbox.addStretch(0)
        self.text = QLabel("DOFBOT")
        self.text.setAlignment(Qt.AlignCenter)
        fontSize = 40
        font = QFont("Times",fontSize)
        self.text.setFont(font)
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(180)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.setValue(90)
        self.slider.valueChanged.connect(self.getValue)
        self.text1 = QLabel("90")
        self.text1.setAlignment(Qt.AlignCenter)
        
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(180)
        self.slider2.setTickPosition(QSlider.TicksAbove)
        self.slider2.setTickInterval(10)
        self.slider2.setValue(90)
        self.slider2.valueChanged.connect(self.getValue)
        self.text2 = QLabel("90")
        self.text2.setAlignment(Qt.AlignCenter)
        
        self.slider3 = QSlider(Qt.Horizontal)
        self.slider3.setMinimum(0)
        self.slider3.setMaximum(180)
        self.slider3.setTickPosition(QSlider.TicksAbove)
        self.slider3.setTickInterval(10)
        self.slider3.setValue(90)
        self.slider3.valueChanged.connect(self.getValue)
        self.text3 = QLabel("90")
        self.text3.setAlignment(Qt.AlignCenter)
        
        self.slider4 = QSlider(Qt.Horizontal)
        self.slider4.setMinimum(0)
        self.slider4.setMaximum(180)
        self.slider4.setTickPosition(QSlider.TicksAbove)
        self.slider4.setTickInterval(10)
        self.slider4.setValue(90)
        self.slider4.valueChanged.connect(self.getValue)
        self.text4 = QLabel("90")
        self.text4.setAlignment(Qt.AlignCenter)
        
        self.slider5 = QSlider(Qt.Horizontal)
        self.slider5.setMinimum(0)
        self.slider5.setMaximum(180)
        self.slider5.setTickPosition(QSlider.TicksAbove)
        self.slider5.setTickInterval(10)
        self.slider5.setValue(90)
        self.slider5.valueChanged.connect(self.getValue)
        self.text5 = QLabel("90")
        self.text5.setAlignment(Qt.AlignCenter)
        
        self.slider6 = QSlider(Qt.Horizontal)
        self.slider6.setMinimum(0)
        self.slider6.setMaximum(180)
        self.slider6.setTickPosition(QSlider.TicksAbove)
        self.slider6.setTickInterval(10)
        self.slider6.setValue(90)
        self.slider6.valueChanged.connect(self.getValue)
        self.text6 = QLabel("90")
        self.text6.setAlignment(Qt.AlignCenter)
        
        vbox.addWidget(self.text)
        vbox.addWidget(self.text1)
        vbox.addWidget(self.slider)
        vbox.addWidget(self.text2)
        vbox.addWidget(self.slider2)
        vbox.addWidget(self.text3)
        vbox.addWidget(self.slider3)
        vbox.addWidget(self.text4)
        vbox.addWidget(self.slider4)
        vbox.addWidget(self.text5)
        vbox.addWidget(self.slider5)
        vbox.addWidget(self.text6)
        vbox.addWidget(self.slider6)
        vbox.addStretch(5)
        self.setLayout(vbox)                       
        self.show()
        
    def getValue(self):
        val = self.slider.value()
        val2 = self.slider2.value()
        val3 = self.slider3.value()
        val4 = self.slider4.value()
        val5 = self.slider5.value()
        val6 = self.slider6.value()
        print("{} {} {} {} {} {}".format(val, val2, val3, val4, val5, val6))
        self.text1.setText(str(val))
        self.text2.setText(str(val2))
        self.text3.setText(str(val3))
        self.text4.setText(str(val4))
        self.text5.setText(str(val5))
        self.text6.setText(str(val6))     
        
        Arm.Arm_serial_servo_write(6, val, 500)
        Arm.Arm_serial_servo_write(5, val2, 500)
        Arm.Arm_serial_servo_write(4, val3, 500)
        Arm.Arm_serial_servo_write(3, val4, 500)
        Arm.Arm_serial_servo_write(2, val5, 500)
        Arm.Arm_serial_servo_write(1, val6, 500)   
            
def test():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())    

if __name__ == '__main__':
    test()
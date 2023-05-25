from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QAbstractAnimation,  QMargins

class AnimaButtonHover(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.marginsAnim = QPropertyAnimation(self, b'geometry')
        #self.marginsAnim.setEasingCurve(QEasingCurve.OutElastic)
        self.marginsAnim.setDuration(200)

    def enterEvent(self,event):
        self.marginsAnim.setDirection(QAbstractAnimation.Forward)
        if self.marginsAnim.state() == self.marginsAnim.State.Stopped:
            rect = self.geometry()
            self.marginsAnim.setStartValue(rect)
            rect+=QMargins(10,10,10,10)
            self.marginsAnim.setEndValue(rect)
            self.marginsAnim.start()
        QPushButton.enterEvent(self, event)

    def leaveEvent(self,event):
        self.marginsAnim.setDirection(QAbstractAnimation.Backward)
        if self.marginsAnim.state() == self.marginsAnim.State.Stopped: self.marginsAnim.start()
        QPushButton.leaveEvent(self, event)

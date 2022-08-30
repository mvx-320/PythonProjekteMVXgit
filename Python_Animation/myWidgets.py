from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QPropertyAnimation

class JumpButton(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.anim = QPropertyAnimation(self, b'geometry')       # Man erstellt ein Eigenschaftsanimation und verändert die Geometrie
        self.anim.setDuration(2000)                             # Setzt die Dauer der Animation

        rect = self.geometry()                                  # Erstellt ein Rechteck
        self.anim.setStartValue(rect)                           # Setzt den Startwert der Animation auf die Koordinaten des Rechtecks
        rect.translate(30,-30)                                  # Verändert die Koordinaten des Rechtecks
        # self.setGeometry(rect) # Um das Rechteck selbst zu verändern

        self.anim.setEndValue(rect)                             # Setzt den Endwert der Animation

    def enterEvent(self, event):
        self.anim.start()
        QPushButton.enterEvent(self, event)
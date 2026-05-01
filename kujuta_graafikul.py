import sys
from PyQt5 import QtWidgets
import pyqtgraph as pg
from PyQt5.QtGui import *

from hangi_andmed import hangi_t6en2osused


class ProbabilityLine(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tõenäosuste skaala")
        self.setGeometry(100, 100, 1000, 300)

        data = hangi_t6en2osused()

        data.sort(key=lambda x: x[1]) #Sorteeri t6en2osused suuruse j2rgi

        labels = [item[0] for item in data]
        values = [item[1] for item in data]

        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)

        self.plot_widget.hideAxis('left') #Peidame Y telje
        self.plot_widget.setXRange(0, 1) #Tõenäosus on min 0 ja max 1
        self.plot_widget.setLimits(xMin=0, xMax=1)

        self.plot_widget.setLabel('bottom', 'Tõenäosus (0 → 1)')

        self.plot_widget.plot([0, 1], [0, 0], pen=pg.mkPen(width=2))

        #Punktid teljel
        scatter = pg.ScatterPlotItem(
            x=values,
            y=[0] * len(values),
            size=10,
            brush=pg.mkBrush(100, 200, 255)
        )
        self.plot_widget.addItem(scatter)

        #Selgitav tekst iga punkti juures
        font = QFont('Arial', 11)
        for i, (label, value) in enumerate(data):
            text = pg.TextItem(
                text=f"{label}\n({value:.4f})",
                anchor=(0, 0),
                #angle=75
                
            )
            y_offset = 0.02 + (i % 3) * 0.02
            text.setPos(value, y_offset)
            self.plot_widget.addItem(text)
            text.setFont(font)
            line = pg.PlotDataItem(x=[value, value], y=[0, y_offset], pen=pg.mkPen(color=(150, 150, 150), width=1))
            self.plot_widget.addItem(line)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProbabilityLine()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

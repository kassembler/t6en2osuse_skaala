import sys
from PyQt5 import QtWidgets
import pyqtgraph as pg

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
        for i, (label, value) in enumerate(data):
    
            #Üle ühe silt alla ja üles
            if i % 2 == 0:
                y = 0.15   #Üleval
                anchor = (0.5, 0)
            else:
                y = -0.15  #All
                anchor = (0.5, 1)

            text = pg.TextItem(
                text=f"{label}\n({value:.4f})",
                anchor=anchor
            )
            
            text.setPos(value, y)
            self.plot_widget.addItem(text)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProbabilityLine()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
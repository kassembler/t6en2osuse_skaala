import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
import pyqtgraph as pg

from hangi_andmed import hangi_t6en2osused


class ProbabilityLine(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tõenäosuste skaala")
        self.setGeometry(100, 100, 1000, 300)

        self.init_ui()

    def init_ui(self):
        data = hangi_t6en2osused()
        data.sort(key=lambda x: x[1]) #Sorteeri andmed suuruse järgi

        values = [item[1] for item in data]

        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)
        pg.setConfigOptions(antialias=True)

        self.plot_widget.hideAxis('left')
        self.plot_widget.setXRange(0, 1)
        self.plot_widget.setLimits(xMin=0, xMax=1)
        self.plot_widget.setLabel('bottom', 'Tõenäosus (0 → 1)') #Tõenäosus saab olla vaid 0 kuni 1

        self.plot_widget.plot([0, 1], [0, 0], pen=pg.mkPen(width=2))

        scatter = pg.ScatterPlotItem(
            x=values,
            y=[0] * len(values),
            size=10,
            brush=pg.mkBrush(100, 200, 255)
        )
        self.plot_widget.addItem(scatter)

        font = QFont('Arial', 10) #Font

        for i, (label, value) in enumerate(data):
            y_offset = 0.03 + i * 0.03 #Selleks, et tekstid kattuksid vähem

            text = pg.TextItem(
                text=f"{label}\n({value:.4f})",
                anchor=(0, 0)
            )
            text.setFont(font)
            text.setPos(value, y_offset)

            self.plot_widget.addItem(text)

            line = pg.PlotDataItem(
                x=[value, value],
                y=[0, y_offset],
                pen=pg.mkPen(color=(150, 150, 150), width=1)
            )
            self.plot_widget.addItem(line)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProbabilityLine()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

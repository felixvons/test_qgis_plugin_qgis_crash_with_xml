from pathlib import Path

from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtWidgets import QMessageBox, QPushButton
from qgis.core import QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY, QgsProject

def simple_point_vector_layer() -> QgsVectorLayer:
    """ Returns a basic memory vector layer with the geometry type of point.
        The returned layer has the CRS EPSG:4326, with containing features (first fid is 1) and the attribute field "id"

    """

    # create a memory layer with the given URI (from the PyQGIS documentation)
    uri = "point?crs=epsg:4326&field=id:integer"
    layer = QgsVectorLayer(uri, "Scratch point layer", "memory")
    assert layer.isValid()

    # create some test features
    for i in range(1, 101):
        feature = QgsFeature(layer.dataProvider().fields())
        feature["id"] = i
        feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(float(i), float(i))))

        assert layer.dataProvider().addFeature(feature)

    assert layer.featureCount() == 100

    return layer


class Plugin:

    def __init__(self, iface):
        self.iface = iface
        ...

    def initGui(self):
        self.button_lxml = QPushButton(self.iface.mainWindow())
        self.button_lxml.setText("LXML-TEST (click me twice)")
        font = self.button_lxml.font()
        font.setPixelSize(32)
        self.button_lxml.setFont(font)
        self.button_lxml.show()
        self.button_lxml.clicked.connect(self.run_lxml)

        self.button_openpyxl = QPushButton(self.iface.mainWindow())
        self.button_openpyxl.setText("OPENPYXL-TEST (click me twice)")
        font = self.button_openpyxl.font()
        font.setPixelSize(32)
        self.button_openpyxl.setFont(font)
        self.button_openpyxl.show()
        self.button_openpyxl.clicked.connect(self.run_openpyxl)

        self.button_lxml.adjustSize()
        self.button_openpyxl.move(self.button_lxml.x(), self.button_lxml.y() + self.button_lxml.height())
        self.button_openpyxl.adjustSize()

    def run_lxml(self):

        from .tests import test_qgis

        # Aufruf 1
        test_qgis.test_lxml()

    def run_openpyxl(self):

        from .tests import test_qgis

        test_qgis.test_openpyxl()



    def unload(self):
        ...


def classFactory(iface):
    return Plugin(iface)
from pathlib import Path

from qgis.core import QgsVectorLayer, QgsProject


def test_lxml():

    layer_path = Path(__file__).parent / "test.gpkg"

    layer = QgsVectorLayer(f"{layer_path.as_posix()}|layername=test_empty", "TEST", "ogr")
    assert layer.isValid()

    assert QgsProject.instance().addMapLayer(layer)

    from lxml.etree import Element

    el = Element("test")


def test_openpyxl():

    layer_path = Path(__file__).parent / "test.gpkg"

    layer = QgsVectorLayer(f"{layer_path.as_posix()}|layername=test_empty", "TEST", "ogr")
    assert layer.isValid()

    assert QgsProject.instance().addMapLayer(layer)

    import openpyxl
    wb = openpyxl.Workbook()

from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(cls, importer):
        cls.data = []
        cls.importer = importer

    def __iter__(cls):
        return InventoryIterator(cls.data)

    def import_data(cls, file_path, report_type):
        cls.data.extend(cls.importer.import_data(file_path))

        if report_type == "simples":
            return SimpleReport.generate(cls.data)

        if report_type == "completo":
            return CompleteReport.generate(cls.data)

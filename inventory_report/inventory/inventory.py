from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as ET
import csv
import json


class Inventory:

    @staticmethod
    def arquivos_xml(file):
        tree = ET.parse(file).getroot()
        """ Identifica as chaves arquivo do XML. """
        todos_registros = tree.findall("record")
        inventory = []
        for records in todos_registros:
            file_dict = {}
            for tag in records:
                file_dict[tag.tag] = tag.text
            inventory.append(file_dict)
        return inventory

    @staticmethod
    def arquivos_csv(path):
        with open(path) as file:
            converter_aquivo_csv = csv.DictReader(file, delimiter=",")
            inventory = [row for row in converter_aquivo_csv]
        return inventory

    @staticmethod
    def arquivos_json(path):
        with open(path) as file:
            inventory = json.load(file)
        return inventory

    @classmethod
    def verifica_caminho(cls, path):
        if path.endswith(".csv"):
            itens = cls.arquivos_csv(path)
        elif path.endswith(".json"):
            itens = cls.arquivos_json(path)
        else:
            itens = cls.arquivos_xml(path)
        return itens

    @classmethod
    def import_data(cls, path, type):
        inventory = cls.verifica_caminho(path)
        if type == "simples":
            return SimpleReport.generate(inventory)

        if type == "completo":
            return CompleteReport.generate(inventory)

'''
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path_file, report_type):
        ext = path_file.split('.')[1]
        if ext == "json":
            data = JsonImporter().import_data(path_file)
        elif ext == "csv":
            data = CsvImporter().import_data(path_file)
        else:
            data = XmlImporter().import_data(path_file)
        return cls.generate(data, report_type)

    @classmethod
    def generate(cls, data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
'''

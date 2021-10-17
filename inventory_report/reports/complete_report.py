from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, lista_de_dicts):
        report = SimpleReport.generate(lista_de_dicts) + '\n'
        report += 'Produtos estocados por empresa: \n'

        nome_da_empresa = []

        for x in lista_de_dicts:
            nome_da_empresa.append(x['nome_da_empresa'])
        print(nome_da_empresa)

        nomeEmpresa = list()
        for x in range(0, len(nome_da_empresa)):
            if nome_da_empresa[x] in nomeEmpresa:
                pass
            else:
                nome = nome_da_empresa[x]
                quantidade = nome_da_empresa.count(nome)
                nomeEmpresa.append(nome)
                report += "- " + nome + ": "
                report += str(quantidade) + "\n"
        return report

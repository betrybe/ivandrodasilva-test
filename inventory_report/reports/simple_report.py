from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, lista_de_dicts):
        today = str(datetime.today())

        # São criadas duas variaveis para receber os primeiros
        # os dados do dicionario, referentes a datas de fabricação e validade

        data_fab_mais_antiga = lista_de_dicts[0]["data_de_fabricacao"]
        data_val_mais_proxima = lista_de_dicts[0]["data_de_validade"]

        for x in lista_de_dicts:
            # loop para achar a data de fabricação mais antiga.
            if x["data_de_fabricacao"] <= data_fab_mais_antiga:
                data_fab_mais_antiga = x["data_de_fabricacao"]

        for x in lista_de_dicts:
            # Loop para achar a data de validade mais próxima
            if (
                x["data_de_validade"] < data_val_mais_proxima
                and x["data_de_validade"] >= today
            ):
                data_val_mais_proxima = x["data_de_validade"]
        # Utilizando a função max() para obter o nome da empresa
        # que aperece mais vezes dentro do dicionario.
        firm_name = max(
            x["nome_da_empresa"]
            for x in lista_de_dicts
        )

        return (
            f"Data de fabricação mais antiga: {data_fab_mais_antiga}\n"
            f"Data de validade mais próxima: {data_val_mais_proxima}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{firm_name}\n"
        )

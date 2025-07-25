import xmltodict


def nomesMoedas():
    with open("ListaDeMoedas.xml", "rb") as arquivoMoeda: #Abre o arquivo moedas.xml
        dic_moedas= xmltodict.parse(arquivoMoeda)

    moedas = dic_moedas["xml"]
    return moedas

def conversoesDisponiveis():
    with open("conversoes.xml", "rb") as arquivo_conversoes:
        dic_conversoes = xmltodict.parse(arquivo_conversoes)
    
    conversoes = dic_conversoes["xml"]
    dic_conversoesDisponiveis={}
    for parConversao in conversoes:
        moeda_origem, moeda_destino = parConversao.split("-")
        if moeda_origem in dic_conversoesDisponiveis:
            dic_conversoesDisponiveis[moeda_origem].append(moeda_destino)
        else:
            dic_conversoesDisponiveis[moeda_origem] = [moeda_destino]
    return dic_conversoesDisponiveis    








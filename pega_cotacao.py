import requests

def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"
        resposta = requests.get(url, verify=False)  # verify=False apenas para testes locais
        resposta.raise_for_status()  # Lança erro se a resposta for ruim (4xx ou 5xx)

        dados = resposta.json()
        chave = f"{moeda_origem}{moeda_destino}"
        cotacao = dados[chave]["bid"]
        print(f"1 {moeda_origem} = {cotacao} {moeda_destino}")
        return cotacao

    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição: {erro}")
    except KeyError:
        print("Erro ao acessar os dados da cotação. Verifique os códigos das moedas.")

# Exemplo de uso
pegar_cotacao_moeda("USD", "BRL")















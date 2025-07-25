import customtkinter
from pegarMoedas import nomesMoedas, conversoesDisponiveis
from pega_cotacao import pegar_cotacao_moeda

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")

janela = customtkinter.CTk() #cria configura a janela
janela.geometry("500x500")

dic_conversoesDisponiveis  = conversoesDisponiveis()

#botões e outros elementos
titulo = customtkinter.CTkLabel(janela, text="conversor de moeda", font=("", 20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Diga moeda de Origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Diga moeda de Destino")
texto_cotacao_moeda= customtkinter.CTkLabel(janela, text="")

def carregarMoedasDestino(moeda_selecionada):
    listaMoeda = dic_conversoesDisponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=listaMoeda)
    campo_moeda_destino.set(listaMoeda[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoesDisponiveis.keys()), command=carregarMoedasDestino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de Origem"])

def converterMoeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")

botaoDeConverter = customtkinter.CTkButton(janela, text="Converter", command=converterMoeda)

listaMoeda = customtkinter.CTkScrollableFrame(janela)

moedasDisponiveis = nomesMoedas()


for CodigoMoeda in moedasDisponiveis:
    nomesMoedas = moedasDisponiveis[CodigoMoeda]
    texto_moeda = customtkinter.CTkLabel(listaMoeda, text=f"{CodigoMoeda}: {nomesMoedas}")
    texto_moeda.pack()



# exibir elementos tela
titulo.pack(padx=10, pady=10)

# Primeiro a moeda de origem
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10, pady=10)

# Depois a moeda de destino
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10, pady=10)

# Agora o botão de converter
botaoDeConverter.pack(padx=10, pady=10)

texto_cotacao_moeda.pack(padx=10, pady=10)

# E por fim a lista de moedas
listaMoeda.pack(padx=10, pady=10)





#roda janela
janela.mainloop()
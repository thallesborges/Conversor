import requests
import json
import customtkinter as ctk

# Conexão com a API
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/BRL-USD,BRL-EUR")
cotacoes = cotacoes.json()
print(cotacoes)

cotacao_dolar = float(cotacoes['BRLUSD']['bid'])
cotacao_euro = float(cotacoes['BRLEUR']['bid'])

# Tela de Cotação
janela = ctk.CTk()
janela.geometry("400x400")
janela.title("Conversão de Moedas")

# Funções dentro da Tela de Cotação
def calculo_euro():
    valor_real = round(float(entrada_real.get()), 2)
    valor_cotacao.configure(frame_resultado, text = f'R$1.00 = €{round(cotacao_euro, 2)}')
    resultado_calculo.configure(frame_resultado, text = f'R${valor_real} = €{round(valor_real*cotacao_euro, 2)}')

def calculo_dolar():
    valor_real = round(float(entrada_real.get()), 2)
    valor_cotacao.configure(frame_resultado, text = f'R$1.00 = ${round(cotacao_dolar, 2)}')
    resultado_calculo.configure(frame_resultado, text = f'R${valor_real} = ${round(valor_real*cotacao_dolar, 2)}')

# Frames da Tela
frame_painel = ctk.CTkFrame(janela)
frame_painel.pack(padx = 10, pady = 10)

frame_botoes = ctk.CTkFrame(janela)
frame_botoes.pack(padx = 10, pady = 10)

frame_resultado = ctk.CTkFrame(janela)
frame_resultado.pack(padx = 10, pady = 10)

# Conteúdo da Janela
texto_janela = ctk.CTkLabel(frame_painel, text = "Insira o valor em R$ abaixo:")
texto_janela.pack(padx = 10, pady = 5)

entrada_real = ctk.CTkEntry(frame_painel, placeholder_text = "R$0.00")
entrada_real.pack(padx = 10, pady = 10)

botao_calculo_euro = ctk.CTkButton(frame_botoes, text = "Euro", command = calculo_euro)
botao_calculo_euro.pack(padx = 10, pady = 10)

botao_calculo_dolar = ctk.CTkButton(frame_botoes, text = "Dólar", command = calculo_dolar)
botao_calculo_dolar.pack(padx = 10, pady = 10)

valor_cotacao = ctk.CTkLabel(frame_resultado, text = "")
valor_cotacao.pack(padx = 10, pady = 10)

resultado_calculo = ctk.CTkLabel(frame_resultado, text = "")
resultado_calculo.pack(padx = 10, pady = 10)

janela.mainloop()
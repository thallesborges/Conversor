# 💱 Conversor de Moedas (BRL → USD/EUR)

Este projeto é um conversor de moedas com **interface gráfica**, desenvolvido em Python utilizando a biblioteca [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) e a API pública da [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas).

O usuário informa um valor em **Reais (BRL)** e o programa exibe o valor convertido para **Dólar (USD)** ou **Euro (EUR)** com base na cotação atual.

---

## 🚀 Funcionalidades

- Conexão com a **AwesomeAPI** para obter cotações atualizadas.
- Conversão de **BRL para USD** e **BRL para EUR**.
- Interface gráfica amigável com botões e campos de entrada.
- Exibição da cotação atual e do valor convertido.

---

## 📦 Requisitos

- Python **3.8+**
- [Requests](https://pypi.org/project/requests/) — para acessar a API de cotações.
- [CustomTkinter](https://pypi.org/project/customtkinter/) — para criar a interface gráfica.

---

## 🔧 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/thallesborges/Conversor.git
   cd Conversor
   ```

2. **(Opcional) Crie um ambiente virtual**
   ```bash
   python -m venv venv
   # Ative o ambiente:
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Como usar

Execute o script principal:

```bash
python conversor_moedas.py
```

Na janela que abrir:

1. Digite o valor em **Reais (R$)**.
2. Clique em **"Euro"** ou **"Dólar"** para ver a conversão.
3. O programa exibirá:
   - Cotação atual (ex: `R$1.00 = $0.20`)
   - Valor convertido (ex: `R$100.00 = $20.00`)

---

## 🗂 Estrutura do projeto

```
Conversor/
├── conversor_moedas.py   # Script principal com interface e lógica de conversão
├── requirements.txt      # Lista de dependências (opcional)
└── README.md             # Documentação do projeto
```

---

## 📜 Licença

Este projeto é de uso livre para estudos e modificações. Caso utilize, mantenha os créditos ao autor.

---

## ✨ Melhorias futuras

- Adicionar mais moedas disponíveis.
- Escolha de moedas via menu suspenso.
- Exibir data/hora da última atualização.
- Tratar erros de conexão ou API indisponível.
- Criar executável (.exe) para facilitar o uso sem Python instalado.

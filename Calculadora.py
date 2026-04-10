import tkinter as tk

# Função para adicionar número na tela
def clicar(valor):
    entrada.set(entrada.get() + str(valor))

# Função para limpar
def limpar():
    entrada.set("")

# Função para calcular
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(str(resultado))
    except:
        entrada.set("Erro")

# Criando janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.config(bg="#1e1e1e")

entrada = tk.StringVar()

# Tela
tela = tk.Entry(janela, textvariable=entrada, font=("Arial", 20), bd=10, relief="ridge", justify="right")
tela.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Frame dos botões
frame = tk.Frame(janela, bg="#1e1e1e")
frame.pack()

# Botões
botoes = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for linha in botoes:
    linha_frame = tk.Frame(frame, bg="#1e1e1e")
    linha_frame.pack(expand=True, fill="both")
    
    for item in linha:
        if item == "=":
            btn = tk.Button(linha_frame, text=item, font=("Arial", 18), bg="#4CAF50", fg="white",
                            command=calcular)
        else:
            btn = tk.Button(linha_frame, text=item, font=("Arial", 18), bg="#333", fg="white",
                            command=lambda x=item: clicar(x))
        
        btn.pack(side="left", expand=True, fill="both")

# Botão limpar
btn_clear = tk.Button(janela, text="C", font=("Arial", 18), bg="#f44336", fg="white", command=limpar)
btn_clear.pack(fill="both", padx=10, pady=5)

# Rodar app
janela.mainloop()

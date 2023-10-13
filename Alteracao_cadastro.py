import tkinter as tk


def abrir_janela_alterar_cadastro():
    janela = tk.Tk()
    janela.title("Glamour Fashion")
    janela.geometry("650x430+670+260")
    janela.resizable(False, False)
    janela.configure(bg="#FFE8E5")

    # Titulo
    titulo = tk.Label(janela, text="Glamour Fashion", anchor="center", bg="#FFE8E5")
    titulo.config(font=("Cooper Black", 25), fg="#EB0DAD")
    titulo.pack()
    subtitulo = tk.Label(janela, text="CADASTRO DE CLIENTES", anchor="center", bg="#FFE8E5")
    subtitulo.config(font=("Arial", 10))
    subtitulo.pack()

    # Nome
    nome_completo = tk.Entry(janela, font=14, width=58)
    nome_completo.pack()
    nome_completo.place(x=50, y=78)

    # Rotulo Nome
    nome_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Nome:", bg="#FFE8E5")
    nome_rotulo.pack()
    nome_rotulo.place(x=48, y=56)

    # Nascimeto
    nascimento = tk.Entry(janela, font=14, width=13)
    nascimento.pack()
    nascimento.place(x=50, y=135)

    # Rotulo nascimento
    nascimento_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Nascimento:", bg="#FFE8E5")
    nascimento_rotulo.pack()
    nascimento_rotulo.place(x=48, y=110)

    # Botao Feminino
    sexo = tk.BooleanVar()

    tk.Radiobutton(janela, text="F", value=2, variable=sexo, bg="#FFE8E5", command=lambda: print(sexo.get())).place(x=190, y=136)
    tk.Radiobutton(janela, text="M", value=1, bg="#FFE8E5", variable=sexo).place(x=243, y=136)

    # Email
    email = tk.Entry(janela, font=14, width=30)
    email.pack()
    email.place(x=301, y=135)

    # Email Rotulo
    email_rotulo = tk.Label(janela, font=("Helvetica", 10), text="E-mail:", bg="#FFE8E5",)
    email_rotulo.pack()
    email_rotulo.place(x=298, y=110)

    # Rua
    rua = tk.Entry(janela, font=14, width=42)
    rua.pack()
    rua.place(x=50, y=190)

    # Rua rotulo
    rua_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Rua:", bg="#FFE8E5",)
    rua_rotulo.pack()
    rua_rotulo.place(x=48, y=165)

    # Numero
    numero = tk.Entry(janela, font=14, width=6)
    numero.pack()
    numero.place(x=516, y=190)

    # Numero rotulo
    numero_rotulo = tk.Label(janela, font=("Helvetica", 10), text="N°:", bg="#FFE8E5",)
    numero_rotulo.pack()
    numero_rotulo.place(x=514, y=165)

    # Cidade
    cidade = tk.Entry(janela, font=14, width=20)
    cidade.pack()
    cidade.place(x=50, y=250)

    # Cidade rotulo

    rua_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Cidade:", bg="#FFE8E5",)
    rua_rotulo.pack()
    rua_rotulo.place(x=48, y=225)

    # UF
    uf = tk.Entry(janela, font=14, width=5)
    uf.pack()
    uf.place(x=295, y=250)

    # Uf rotulo
    rua_rotulo = tk.Label(janela, font=("Helvetica", 10), text="UF:", bg="#FFE8E5",)
    rua_rotulo.pack()
    rua_rotulo.place(x=293, y=225)

    # Cep
    cep = tk.Entry(janela, font=14, width=21)
    cep.pack()
    cep.place(x=381, y=250)

    # Cep Rotulo
    cep_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Cep:", bg="#FFE8E5",)
    cep_rotulo.pack()
    cep_rotulo.place(x=379, y=225)

    # ID
    id = tk.Entry(janela, font=14, width=5)
    id.pack()
    id.place(x=50, y=310)

    # ID rotulo

    id_rotulo = tk.Label(janela, font=("Helvetica", 10),  text="ID:", bg="#FFE8E5",)
    id_rotulo.pack()
    id_rotulo.place(x=48, y=285)

    # Celular DDD
    celular_ddd = tk.Entry(janela, font=14, width=5)
    celular_ddd.pack()
    celular_ddd.place(x=295, y=310)

    # Celular DDD rotulo

    celular_Ddd_rotulo = tk.Label(janela, font=("Helvetica", 10), text="DDD:", bg="#FFE8E5",)
    celular_Ddd_rotulo.pack()
    celular_Ddd_rotulo.place(x=293, y=285)

    #  Celular
    celular = tk.Entry(janela, font=14, width=21)
    celular.pack()
    celular.place(x=381, y=310)

    # Celular rotulo
    celular_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Celular:", bg="#FFE8E5",)
    celular_rotulo.pack()
    celular_rotulo.place(x=379, y=285)

    def salvar_cadastro():
        # Implemente a lógica de salvamento aqui
        janela.destroy()

    def cancelar_cadastro():
        janela.destroy()

        # Botão "Salvar"

    button_cancelar = tk.Button(janela, text="Cancelar", bg="#EB0DAD", fg="White", font=("Cooper Black", 11),
                                command=cancelar_cadastro)
    button_cancelar.pack()
    button_cancelar.place(x=430, y=370)
    button_cancelar.config(width=9, height=2)

    button_salvar = tk.Button(janela, text="Salvar", bg="#EB0DAD", fg="White", font=("Cooper Black", 11),
                              command=salvar_cadastro)
    button_salvar.pack()
    button_salvar.place(x=540, y=370)
    button_salvar.config(width=9, height=2)

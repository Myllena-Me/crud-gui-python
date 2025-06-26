import tkinter as tk
from tkinter import messagebox

usuarios = []

def atualizar_lista():
    lista.delete(0, tk.END)
    for i, usuario in enumerate(usuarios,start=1):
        lista.insert(tk.END,f"{i} - {usuario['nome']}, {usuario['idade']} anos")

def adicionar_usuario():
    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if not nome or not idade:
        messagebox.showwarning("Atenção","Preencha todos os campos.")
        return
    
    usuarios.append({"nome": nome, "idade": idade})
    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)
    atualizar_lista()

def remover_usuario():
    try:
        index = lista.curselection()[0] -1
        usuarios.pop(index)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Atenção","Selecione um usuário para remover.")

def atualizar_usuario():
    try:
        index = lista.curselection()[0] -1
        nome = entrada_nome.get()
        idade = entrada_idade.get()
        if not nome or not idade:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return
        usuarios[index]= {"nome": nome, "idade": idade}
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione um usuário para atualizar.")

janela = tk.Tk()
janela.title("CRUD de usuários")

tk.Label(janela,text= "Nome:").grid(row=0,column=0)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0,column=1)

tk.Label(janela,text= "Idade:").grid(row=1, column=0)
entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=1,column=1)

tk.Button(janela, text="Adicionar", command= adicionar_usuario).grid(row=2,column=0, pady=5)
tk.Button(janela, text= "Atualizar",command=atualizar_usuario).grid(row=2, column=1)
tk.Button(janela, text= "Remover",command=remover_usuario).grid(row=2, column=2)


lista = tk.Listbox(janela, width= 50)
lista.grid(row=3, column=0, columnspan=3, padx=10,pady=10)

janela.mainloop()
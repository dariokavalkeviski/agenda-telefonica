import tkinter as tk
from tkinter import messagebox
import csv

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}
        self.janela = tk.Tk()
        self.janela.title("Agenda Telefônica")

        # Criar campos de entrada
        self.nome_label = tk.Label(self.janela, text="Nome:")
        self.nome_label.grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.janela)
        self.nome_entry.grid(row=0, column=1)

        self.telefone_label = tk.Label(self.janela, text="Telefone:")
        self.telefone_label.grid(row=1, column=0)
        self.telefone_entry = tk.Entry(self.janela)
        self.telefone_entry.grid(row=1, column=1)

        # Criar botões
        self.adicionar_button = tk.Button(self.janela, text="Adicionar", command=self.adicionar_contato)
        self.adicionar_button.grid(row=2, column=0)

        self.atualizar_button = tk.Button(self.janela, text="Atualizar", command=self.atualizar_contato)
        self.atualizar_button.grid(row=2, column=1)

        self.remover_button = tk.Button(self.janela, text="Remover", command=self.remover_contato)
        self.remover_button.grid(row=2, column=2)

        self.listar_button = tk.Button(self.janela, text="Listar", command=self.listar_contatos)
        self.listar_button.grid(row=3, column=0, columnspan=3)

        self.exportar_button = tk.Button(self.janela, text="Exportar para CSV", command=self.exportar_contatos)
        self.exportar_button.grid(row=4, column=0, columnspan=3)

        # Criar área de texto para listar contatos
        self.contatos_text = tk.Text(self.janela, height=10, width=40)
        self.contatos_text.grid(row=5, column=0, columnspan=3)

    def adicionar_contato(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        if nome in self.contatos:
            messagebox.showerror("Erro", f"Contato '{nome}' já existe.")
        else:
            self.contatos[nome] = telefone
            messagebox.showinfo("Sucesso", f"Contato '{nome}' adicionado com sucesso.")

    def atualizar_contato(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        if nome in self.contatos:
            self.contatos[nome] = telefone
            messagebox.showinfo("Sucesso", f"Contato '{nome}' atualizado com sucesso.")
        else:
            messagebox.showerror("Erro", f"Contato '{nome}' não encontrado.")

    def remover_contato(self):
        nome = self.nome_entry.get()
        if nome in self.contatos:
            del self.contatos[nome]
            messagebox.showinfo("Sucesso", f"Contato '{nome}' removido com sucesso.")
        else:
            messagebox.showerror("Erro", f"Contato '{nome}' não encontrado.")

    def listar_contatos(self):
        self.contatos_text.delete(1.0, tk.END)
        for nome, telefone in self.contatos.items():
            self.contatos_text.insert(tk.END, f"{nome}: {telefone}\n")

    def exportar_contatos(self):
        with open('contatos.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Nome", "Telefone"])
            for nome, telefone in self.contatos.items():
                writer.writerow([nome, telefone])
        messagebox.showinfo("Sucesso", "Contatos exportados com sucesso para o arquivo 'contatos.csv'.")

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    agenda = AgendaTelefonica()
    agenda.run()
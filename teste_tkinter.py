import tkinter as tk

janela = tk.Tk()
janela.title("Teste Tkinter")
janela.geometry("400x200")

label = tk.Label(
    janela,
    text="Tkinter funcionando!",
    font=("Arial", 18)
)

label.pack(pady=70)

janela.mainloop()

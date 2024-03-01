import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("Calvino Academy")
    root.geometry("480x360")
    root.iconbitmap('Utilities/icon.ico')
    
    button1 = tk.Button(root, text = "Anno Scolastico")
    button1.pack()

    button2 = tk.Button(root, text = "Classe di Appartenenza")
    button2.pack()

    button3 = tk.Button(root, text = "Nome Studente")
    button3.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("Calvino Academy Certifications by Year")
    root.geometry("1080x720")
    root.iconbitmap('Utilities\icon.ico')

    root.mainloop()

if __name__ == "__main__":
    create_gui()
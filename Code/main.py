import tkinter as tk
import subprocess
import sys

def run_script(script_path):
    subprocess.run(["python", script_path])
    sys.exit()

def create_gui():
    root = tk.Tk()
    root.title("Calvino Academy Certifications")
    root.geometry("400x380")
    root.iconbitmap('Utilities\icon.ico')

    default_font = ('Comfortaa', 12)
    root.option_add('*Font', default_font)

    frame = tk.Frame(root)
    frame.pack(expand=True)

    button_width = int((root.winfo_screenwidth() * 2 / 3) / 10) 

    button1 = tk.Button(frame, text="Per Anno Scolastico", height=2, width=button_width, command=lambda: run_script("Code\Programs\year.py"))
    button1.pack(padx=20, pady=20)

    button2 = tk.Button(frame, text="Per Classe", height=2, width=button_width, command=lambda: run_script("script2.py"))
    button2.pack(padx=20, pady=20)

    button3 = tk.Button(frame, text="Per Singolo Alunno", height=2, width=button_width, command=lambda: run_script("script3.py"))
    button3.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
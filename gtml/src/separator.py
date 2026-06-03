import tkinter as tk
def buduj_separator(silnik, element, rodzic, funkcja_budujaca):
    sep = tk.Frame(rodzic, height=1, bg="#1a1a1a") # Ciemnoszara linia
    sep.pack(fill='x', pady=20, padx=30)
    return sep
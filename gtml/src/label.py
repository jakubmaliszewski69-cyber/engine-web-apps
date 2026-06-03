import tkinter as tk

def buduj_label(silnik, element, rodzic, funkcja_budujaca):
    tekst = element.text or ""
    # Używamy Segoe UI Symbol - to czcionka Windowsa z pełną obsługą Unicode
    widget = tk.Label(rodzic, text=tekst, bg="#000000", fg="#ffffff", 
                      font=("Segoe UI Symbol", 12))
    widget.pack(anchor="w")
    return widget
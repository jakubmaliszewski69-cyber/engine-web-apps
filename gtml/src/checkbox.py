import tkinter as tk

def buduj_checkbox(silnik, element, rodzic, funkcja_budujaca):
    var = tk.BooleanVar()
    nowy_widget = tk.Checkbutton(rodzic, text=element.text or "Opcja", variable=var)
    nowy_widget.pack(pady=2, anchor='w')
    return nowy_widget
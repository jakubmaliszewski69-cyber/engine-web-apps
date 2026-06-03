import tkinter as tk

def buduj_shell(silnik, element, rodzic, funkcja_budujaca):
    # Zmieniamy domyślne tło na czarne
    frame = tk.Frame(rodzic, bg="#000000")
    frame.pack(fill='both', expand=True)
    funkcja_budujaca(silnik, element, frame)
    return frame
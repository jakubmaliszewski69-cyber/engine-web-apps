import tkinter as tk

def buduj_sidebar(silnik, element, rodzic, funkcja_budujaca):
    szerokosc = int(element.get('width', 45))
    
    # Głęboka czerń paska
    frame = tk.Frame(rodzic, bg="#181818", width=szerokosc)
    frame.pack(side="left", fill="y")
    frame.pack_propagate(False)
    
    silnik.w_sidebarze = True
    silnik.przyciski_menu = {}
    
    # Budujemy dzieci paska
    funkcja_budujaca(silnik, element, frame)
    
    silnik.w_sidebarze = False
    return frame
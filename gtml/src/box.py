import tkinter as tk

def buduj_box(silnik, element, rodzic, funkcja_budujaca):
    # Pobieramy kolor tła od rodzica, żeby nic się nie gryzło
    bg_color = rodzic.cget("bg") if hasattr(rodzic, "cget") else "#000000"
    nowy_widget = tk.Frame(rodzic, bg=bg_color)
    
    # SPRAWDZAMY CZY MA SIĘ ROZCIĄGAĆ (Domyślnie tak, chyba że zabronimy)
    czy_expand = element.get('expand', 'true').lower() == 'true'
    kierunek = tk.LEFT if element.get('layout') == 'horizontal' else tk.TOP
    
    # Jeśli expand="false", wypełniamy tylko w osi Y/X, ale nie pompujemy na siłę
    nowy_widget.pack(side=kierunek, fill='both' if czy_expand else 'none', expand=czy_expand)
        
    funkcja_budujaca(silnik, element, nowy_widget)
    return nowy_widget
import tkinter as tk

def buduj_input(silnik, element, rodzic, funkcja_budujaca):
    is_password = element.get('type') == 'password'
    
    # Mroczny, płaski design pola tekstowego
    nowy_widget = tk.Entry(
        rodzic, 
        bg="#111111",                  # Bardzo ciemnoszare tło pola
        fg="#ffffff",                  # Śnieżnobiały tekst
        insertbackground="#ffffff",    # Biały kursor (kreska)
        relief="flat",                 # Brak starych ramek 3D
        highlightthickness=1,          # Cienka nowoczesna obwódka
        highlightbackground="#333333", # Szara obwódka domyślnie
        highlightcolor="#ffffff",      # Biała obwódka, gdy klikniesz!
        font=("Segoe UI", 12)
    )
    
    # Wewnętrzny margines (ipady=8) robi pole grubszym i czytelniejszym
    nowy_widget.pack(pady=10, ipady=8, fill='x')
    
    # Jeśli to hasło, ukrywamy znaki
    if is_password:
        nowy_widget.config(show="•")
        
    return nowy_widget
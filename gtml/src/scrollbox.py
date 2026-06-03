import tkinter as tk

def buduj_scrollbox(silnik, element, rodzic, funkcja_budujaca):
    # Kontener główny
    kontener = tk.Frame(rodzic, bg="#09090B")
    kontener.pack(fill='both', expand=True)

    # Canvas i Scrollbar (scrollbar ukryty, ale istniejący dla logiki)
    canvas = tk.Canvas(kontener, bg="#09090B", highlightthickness=0)
    scrollbar = tk.Scrollbar(kontener, orient="vertical", command=canvas.yview)
    
    # Ramka na treść
    zawartosc = tk.Frame(canvas, bg="#09090B")
    
    # Rysujemy ramkę na canvasie
    canvas.create_window((0, 0), window=zawartosc, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def on_configure(event):
        # Aktualizujemy obszar przewijania do rozmiaru ramki z treścią
        canvas.configure(scrollregion=canvas.bbox("all"))
        # Wymuszamy szerokość ramki na szerokość canvasu
        canvas.itemconfig(1, width=event.width)

    zawartosc.bind("<Configure>", on_configure)
    canvas.bind("<Configure>", on_configure)

    # Mousewheel - bindowanie bezpośrednio do Canvasu i kontenera
    def scroll(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    canvas.bind_all("<MouseWheel>", scroll)

    canvas.pack(side="left", fill="both", expand=True)

    # Budujemy treść
    funkcja_budujaca(silnik, element, zawartosc)
    
    return kontener
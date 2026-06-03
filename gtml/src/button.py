import tkinter as tk

def buduj_button(silnik, element, rodzic, funkcja_budujaca):
    akcja = element.get('onclick')
    tekst = element.text or ""
    cel = akcja.split(':')[1] if akcja and akcja.startswith('widok:') else None
    
    # 1. PRZYCISK W SIDEBARZE (Label udający przycisk)
    if getattr(silnik, 'w_sidebarze', False):
        # Wymuszamy font "Segoe UI Symbol" - to eliminuje białe kwadraty!
        btn = tk.Label(rodzic, text=tekst, bg="#181818", fg="#a0a0a0", 
                       font=("Segoe UI Symbol", 16), cursor="hand2", anchor="center", pady=12)
        btn.pack(fill="x", pady=2)
        
        if cel:
            silnik.przyciski_menu[cel] = btn
            btn.bind("<Button-1>", lambda e, c=cel: silnik.zmien_widok(c))
            
        # Efekt hover
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#2d2d2d", fg="#ffffff") if b.cget("bg") != "#37373d" else None)
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#181818", fg="#a0a0a0") if b.cget("bg") != "#37373d" else None)
        return btn

    # 2. ZWYKŁY PRZYCISK (Wewnątrz aplikacji)
    # Również z poprawną czcionką
    nowy_widget = tk.Button(
        rodzic, 
        text=tekst, 
        command=lambda: silnik.zmien_widok(cel) if cel else None,
        cursor="hand2",
        font=("Segoe UI Symbol", 10),
        bg="#111111",
        fg="#ffffff",
        relief="flat",
        activebackground="#222222"
    )
    nowy_widget.pack(pady=10, padx=5)
    return nowy_widget
import tkinter as tk

def buduj_view(silnik, element, rodzic, funkcja_budujaca):
    # Zmieniamy #0e0e0e na głęboką czerń #000000
    nowy_widget = tk.Frame(rodzic, bg="#000000")
    vid = element.get('id')
    
    if vid: 
        silnik.widoki[vid] = nowy_widget
        
    funkcja_budujaca(silnik, element, nowy_widget)
    
    if element.get('active') == 'true':
        nowy_widget.pack(fill='both', expand=True)
            
    return nowy_widget
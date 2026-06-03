import tkinter as tk
from PIL import Image, ImageTk

def buduj_image(silnik, element, rodzic, funkcja_budujaca):
    sciezka = element.get('src')
    
    # Pobieramy atrybuty z tagu <image>
    szerokosc = int(element.get('width', 100))  # Domyślnie 100
    wysokosc = int(element.get('height', 100))  # Domyślnie 100
    align = element.get('align', 'center')      # Domyślnie środek
    
    # Ładowanie i skalowanie obrazka
    img = Image.open(sciezka)
    img = img.resize((szerokosc, wysokosc), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    
    # Tworzenie widgetu
    label = tk.Label(rodzic, image=photo)
    label.image = photo 
    
    # Wyrównanie (pozycjonowanie)
    anchor = 'center'
    if align == 'left': anchor = 'w'
    elif align == 'right': anchor = 'e'
    
    label.pack(pady=10, padx=10, anchor=anchor)
    return label
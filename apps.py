import sys
import os
import tkinter as tk
import tkinter.font as tkFont

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from gtml.gtml import SilnikGTML
from src.ekstraktor import wydobadz_sekcje
from qsslite.qsslite import SilnikQSSLite

def napraw_czcionki(silnik):
    font_fix = tkFont.Font(family="Segoe UI Symbol", size=10)
    for widget in silnik.wszystkie_elementy:
        try:
            if 'font' in widget.keys():
                widget.config(font=font_fix)
        except:
            continue

def uruchom():
    if len(sys.argv) < 2:
        print("Użycie: python apps.py <nazwa_pliku>.apps")
        sys.exit(1)
        
    sciezka = sys.argv[1]
    if not os.path.exists(sciezka):
        print(f"Błąd: Nie znaleziono pliku '{sciezka}'.")
        sys.exit(1)
        
    with open(sciezka, 'r', encoding='utf-8') as plik:
        kod = plik.read()
        
    sekcje = wydobadz_sekcje(kod)
    
    if not sekcje['gtml']:
        print("Błąd: Plik .apps musi zawierać sekcję <gtml>!")
        sys.exit(1)
        
    print("[APPS Proxy] Znaleziono GTML. Przekazuję do silnika...")

    silnik_widoku = SilnikGTML(sekcje['gtml'])
    
    if sekcje['qsslite']:
        print("[QSSLite] Aplikowanie zaawansowanych stylów...")
        silnik_stylow = SilnikQSSLite(sekcje['qsslite'])
        # ZMIANA: Przekazujemy CAŁY silnik widoku
        silnik_stylow.naloz_style(silnik_widoku)

    napraw_czcionki(silnik_widoku)

    if sekcje['litescript']: 
        print("[APPS Proxy] Znaleziono logikę LiteScript (system gotowy na parsowanie)")

    print("[APPS Proxy] Aplikacja wystartowała.")
    silnik_widoku.uruchom()

if __name__ == "__main__":
    uruchom()
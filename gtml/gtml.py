import tkinter as tk
import xml.etree.ElementTree as ET
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))
from budowniczy import buduj_meta, buduj_interfejs

class SilnikGTML:
    def __init__(self, kod_gtml, qsslite_kod="", ls_kod=""):
        self.okno = tk.Tk()
        self.elementy = {} # Szybki dostęp po ID
        self.wszystkie_elementy = [] # NOWOŚĆ: Dostęp dla klas i tagów w QSSLite
        self.widoki = {}
        
        self.kod_stylow = qsslite_kod
        self.kod_logiki = ls_kod
        
        self.parsuj(kod_gtml)

    def parsuj(self, kod):
        try:
            root = ET.fromstring(kod)
        except ET.ParseError as e:
            print(f"[Błąd GTML] Niepoprawna struktura: {e}")
            sys.exit(1)

        meta = root.find('meta')
        if meta is not None:
            buduj_meta(self.okno, meta)

        body = root.find('body')
        if body is not None:
            self.okno.configure(bg="#000000")
            self.kontener = tk.Frame(self.okno, bg="#000000")
            self.kontener.pack(fill='both', expand=True)
            buduj_interfejs(self, body, self.kontener)

    def zmien_widok(self, id_widoku):
        if id_widoku in self.widoki:
            nowy_widok = self.widoki[id_widoku]
            rodzic_widoku = nowy_widok.master
            
            for vid_id, widget in self.widoki.items():
                if widget.master == rodzic_widoku and widget != nowy_widok:
                    widget.pack_forget()
                    
            nowy_widok.pack(fill='both', expand=True)

            if hasattr(self, 'przyciski_menu'):
                for btn in self.przyciski_menu.values():
                    btn.config(bg="#181818", fg="#a0a0a0")
                
                if id_widoku in self.przyciski_menu:
                    self.przyciski_menu[id_widoku].config(bg="#37373d", fg="#ffffff")

    def uruchom(self):
        self.okno.mainloop()
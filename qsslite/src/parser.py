import re

def parsuj_style(kod_qsslite):
    # 1. Usuwamy komentarze
    kod = re.sub(r'/\*.*?\*/', '', kod_qsslite, flags=re.DOTALL)
    zmienne = {}
    style = {}

    # 2. Wyciąganie zmiennych konfiguracyjnych
    zmienne_blok = re.search(r'@variables\s*\{([^}]+)\}', kod)
    if zmienne_blok:
        for deklaracja in zmienne_blok.group(1).split(';'):
            if ':' in deklaracja:
                klucz, wartosc = deklaracja.split(':', 1)
                zmienne[klucz.strip()] = wartosc.strip()
        kod = re.sub(r'@variables\s*\{[^}]+\}', '', kod)

    # NAPRAWA 1: Sortujemy zmienne od najdłuższej nazwy! 
    # (Dzięki temu $accent_hover zamieni się przed $accent)
    posortowane_zmienne = sorted(zmienne.items(), key=lambda x: len(x[0]), reverse=True)
    
    for klucz, wartosc in posortowane_zmienne:
        kod = kod.replace(f'${klucz}', wartosc)
    
    # 3. Szukamy wzorca
    bloki = re.findall(r'([^{]+)\{([^}]+)\}', kod)
    
    for selektory_surowe, wlasciwosci in bloki:
        selektory = [s.strip() for s in selektory_surowe.split(',')]
        
        deklaracje = {}
        for deklaracja in wlasciwosci.split(';'):
            if ':' in deklaracja:
                klucz, wartosc = deklaracja.split(':', 1)
                deklaracje[klucz.strip()] = wartosc.strip()
                
        for selektor in selektory:
            if selektor not in style:
                style[selektor] = {}
            style[selektor].update(deklaracje)
                
    return style
def parsuj_meta(okno, meta):
    tytul = meta.find('title')
    if tytul is not None and tytul.text:
        okno.title(tytul.text)

    rozmiar = meta.find('size')
    if rozmiar is not None:
        w = rozmiar.get('width', '400')
        h = rozmiar.get('height', '300')
        okno.geometry(f"{w}x{h}")
        
        # NOWOŚĆ: Blokowanie zmiany rozmiaru
        resizable = rozmiar.get('resizable', 'true').lower()
        if resizable == 'false':
            okno.resizable(False, False)
        else:
            okno.resizable(True, True)
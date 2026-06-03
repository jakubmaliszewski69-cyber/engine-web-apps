import tkinter as tk

def zastosuj_style(style_slownik, silnik_widoku):
    for selektor, wlasciwosci in style_slownik.items():
        if selektor.startswith('#'):
            el_id = selektor[1:]
            if el_id in silnik_widoku.elementy:
                aplikuj_wlasciwosci(silnik_widoku.elementy[el_id], wlasciwosci)
                
        elif selektor.startswith('.'):
            klasa = selektor[1:]
            for widget in silnik_widoku.wszystkie_elementy:
                if hasattr(widget, 'gtml_class') and klasa in widget.gtml_class:
                    aplikuj_wlasciwosci(widget, wlasciwosci)
                    
        else:
            for widget in silnik_widoku.wszystkie_elementy:
                if hasattr(widget, 'gtml_tag') and widget.gtml_tag == selektor.lower():
                    aplikuj_wlasciwosci(widget, wlasciwosci)

def aplikuj_wlasciwosci(widget, wlasciwosci):
    konfiguracja_wygladu = {}
    konfiguracja_ukladu = {}
    
    # NAPRAWA 2: Pobieramy listę argumentów, jakie obsługuje dany widget
    dostepne_opcje = widget.keys() if hasattr(widget, 'keys') else []
    
    oryginalny_bg = widget.cget('bg') if 'bg' in dostepne_opcje else None
    oryginalny_fg = widget.cget('fg') if 'fg' in dostepne_opcje else None
    
    try:
        # Tylko jeśli widget potrafi obsłużyć tekst (fg)
        if 'color' in wlasciwosci and 'fg' in dostepne_opcje:
            konfiguracja_wygladu['fg'] = wlasciwosci['color']
            oryginalny_fg = wlasciwosci['color']
            
        # Tylko jeśli widget potrafi obsłużyć tło (bg)
        if ('background' in wlasciwosci or 'bg' in wlasciwosci) and 'bg' in dostepne_opcje:
            kolor = wlasciwosci.get('background', wlasciwosci.get('bg'))
            konfiguracja_wygladu['bg'] = kolor
            oryginalny_bg = kolor
            
            if widget.winfo_class() == 'Button':
                konfiguracja_wygladu['relief'] = 'flat'
                konfiguracja_wygladu['activebackground'] = kolor
                if 'borderwidth' in dostepne_opcje:
                    konfiguracja_wygladu['borderwidth'] = 0
                
        if 'width' in wlasciwosci and 'width' in dostepne_opcje: 
            konfiguracja_wygladu['width'] = int(wlasciwosci['width'])
        
        # Bezpieczna aplikacja paddingu
        if 'padding' in wlasciwosci:
            pad = int(wlasciwosci['padding'])
            if 'padx' in dostepne_opcje: konfiguracja_wygladu['padx'] = pad
            if 'pady' in dostepne_opcje: konfiguracja_wygladu['pady'] = pad
            if widget.winfo_class() == 'Frame':
                konfiguracja_ukladu['ipadx'] = pad
                konfiguracja_ukladu['ipady'] = pad

        ma_czcionke = any(k in wlasciwosci for k in ['font-family', 'font-size', 'font-weight'])
        if ma_czcionke and 'font' in dostepne_opcje:
            rodzina = wlasciwosci.get('font-family', 'Arial')
            rozmiar = int(wlasciwosci.get('font-size', 10))
            waga = wlasciwosci.get('font-weight', 'normal')
            konfiguracja_wygladu['font'] = (rodzina, rozmiar, waga)

        padx, pady = [0, 0], [0, 0]
        ma_margines = False

        if 'margin' in wlasciwosci:
            m = int(wlasciwosci['margin'])
            padx, pady, ma_margines = [m, m], [m, m], True
        if 'margin-top' in wlasciwosci: pady[0] = int(wlasciwosci['margin-top']); ma_margines = True
        if 'margin-bottom' in wlasciwosci: pady[1] = int(wlasciwosci['margin-bottom']); ma_margines = True
        if 'margin-left' in wlasciwosci: padx[0] = int(wlasciwosci['margin-left']); ma_margines = True
        if 'margin-right' in wlasciwosci: padx[1] = int(wlasciwosci['margin-right']); ma_margines = True

        if ma_margines:
            konfiguracja_ukladu['padx'] = tuple(padx) if padx[0] != padx[1] else padx[0]
            konfiguracja_ukladu['pady'] = tuple(pady) if pady[0] != pady[1] else pady[0]

        if 'align' in wlasciwosci:
            align = wlasciwosci['align']
            if align == 'center': konfiguracja_ukladu['anchor'] = 'center'
            elif align == 'left': konfiguracja_ukladu['anchor'] = 'w'
            elif align == 'right': konfiguracja_ukladu['anchor'] = 'e'

        if 'border-width' in wlasciwosci and 'highlightthickness' in dostepne_opcje:
            konfiguracja_wygladu['highlightthickness'] = int(wlasciwosci['border-width'])
        if 'border-color' in wlasciwosci and 'highlightbackground' in dostepne_opcje:
            konfiguracja_wygladu['highlightbackground'] = wlasciwosci['border-color']
            konfiguracja_wygladu['highlightcolor'] = wlasciwosci['border-color']
            
        if 'focus-border' in wlasciwosci and 'highlightcolor' in dostepne_opcje:
            konfiguracja_wygladu['highlightcolor'] = wlasciwosci['focus-border']

        if 'cursor' in wlasciwosci and 'cursor' in dostepne_opcje:
            kursor = wlasciwosci['cursor']
            if kursor == 'pointer': kursor = 'hand2'
            elif kursor == 'text': kursor = 'xterm'
            konfiguracja_wygladu['cursor'] = kursor

        # Konfigurujemy natywny widget (tylko to, na co pozwala!)
        if konfiguracja_wygladu: widget.config(**konfiguracja_wygladu)
        if konfiguracja_ukladu:
            try: widget.pack_configure(**konfiguracja_ukladu)
            except tk.TclError: pass

        # Bezpieczne zdarzenia Hover
        if 'hover-background' in wlasciwosci or 'hover-color' in wlasciwosci:
            h_bg = wlasciwosci.get('hover-background', oryginalny_bg)
            h_fg = wlasciwosci.get('hover-color', oryginalny_fg)
            
            if 'bg' in dostepne_opcje:
                hover_kw = {'bg': h_bg}
                orig_kw = {'bg': oryginalny_bg}
                if 'fg' in dostepne_opcje:
                    hover_kw['fg'] = h_fg
                    orig_kw['fg'] = oryginalny_fg
                    
                widget.bind("<Enter>", lambda e, w=widget, kw=hover_kw: w.config(**kw), add="+")
                widget.bind("<Leave>", lambda e, w=widget, kw=orig_kw: w.config(**kw), add="+")

    except Exception as e:
        print(f"[Ostrzeżenie QSSLite] Nie udało się nałożyć stylu: {e}")
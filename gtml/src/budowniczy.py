import sys
import os

katalog_src = os.path.dirname(os.path.abspath(__file__))
if katalog_src not in sys.path:
    sys.path.insert(0, katalog_src)

from meta import parsuj_meta
from view import buduj_view
from box import buduj_box
from label import buduj_label
from input import buduj_input
from button import buduj_button
from image import buduj_image
from checkbox import buduj_checkbox
from separator import buduj_separator
from shell import buduj_shell
from sidebar import buduj_sidebar

# NOWE IMPORTY
from scrollbox import buduj_scrollbox
from slider import buduj_slider

REJESTR_TAGOW = {
    'view': buduj_view,
    'box': buduj_box,
    'label': buduj_label,
    'input': buduj_input,
    'button': buduj_button,
    'image': buduj_image,
    'checkbox': buduj_checkbox,
    'separator': buduj_separator,
    'app-shell': buduj_shell,
    'sidebar': buduj_sidebar,
    'scrollbox': buduj_scrollbox,
    'slider': buduj_slider
}

def buduj_meta(okno, meta):
    parsuj_meta(okno, meta)

def buduj_interfejs(silnik, wezel, rodzic):
    for element in wezel:
        tag = element.tag.lower()
        el_id = element.get('id')
        nowy_widget = None

        if tag in REJESTR_TAGOW:
            nowy_widget = REJESTR_TAGOW[tag](silnik, element, rodzic, buduj_interfejs)
        else:
            print(f"[Ostrzeżenie GTML] Nieznany tag: <{tag}>.")

        if nowy_widget:
            # Zapisujemy meta-dane dla QSSLite
            nowy_widget.gtml_class = element.get('class', '').split()
            nowy_widget.gtml_tag = tag
            
            # Wrzucamy do głównej puli dla stylizatora klas
            silnik.wszystkie_elementy.append(nowy_widget)
            
            # Zapisujemy ID, jeśli istnieje
            if el_id:
                silnik.elementy[el_id] = nowy_widget
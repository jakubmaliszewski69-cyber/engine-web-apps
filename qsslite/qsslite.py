from .src.parser import parsuj_style
from .src.aplikator import zastosuj_style

class SilnikQSSLite:
    def __init__(self, kod_qsslite):
        self.kod = kod_qsslite
        self.style = {}
        
        if self.kod:
            self.style = parsuj_style(self.kod)

    def naloz_style(self, silnik_widoku):
        if not self.style:
            return
            
        print("[QSSLite] Aplikowanie stylów...")
        zastosuj_style(self.style, silnik_widoku)
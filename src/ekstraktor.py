import re

def wydobadz_sekcje(kod_zrodlowy):
    # Szukamy sekcji w kodzie. Flaga re.DOTALL pozwala czytać wiele linijek.
    gtml = re.search(r'<gtml>(.*?)</gtml>', kod_zrodlowy, re.DOTALL | re.IGNORECASE)
    qsslite = re.search(r'<qsslite>(.*?)</qsslite>', kod_zrodlowy, re.DOTALL | re.IGNORECASE)
    ls = re.search(r'<litescript>(.*?)</litescript>', kod_zrodlowy, re.DOTALL | re.IGNORECASE)
    
    return {
        # Dodajemy z powrotem tagi <gtml>, żeby parser XML miał główny korzeń
        'gtml': f"<gtml>{gtml.group(1)}</gtml>" if gtml else None,
        'qsslite': qsslite.group(1).strip() if qsslite else "",
        'litescript': ls.group(1).strip() if ls else ""
    }
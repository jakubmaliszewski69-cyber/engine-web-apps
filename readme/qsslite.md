Oto potężny, profesjonalny dokument README.md stworzony specjalnie dla modułu QSSLite. Jest on napisany tak, aby wyglądał jak dokumentacja dużego frameworka (w stylu React czy Tailwind CSS).Skopiuj to do swojego pliku QSSLITE_README.md (lub dodaj do głównego README):🎨 QSSLite: Dokumentacja StylizacjiQSSLite to zaawansowany silnik stylizacji dla Acme OS Engine. Pozwala na oddzielenie logiki biznesowej od warstwy wizualnej za pomocą składni przypominającej CSS, oferując pełną kontrolę nad wyglądem aplikacji w czasie rzeczywistym.🚀 Szybki StartStyle definiowane są w bloku <qsslite> wewnątrz pliku .apps. Każdy selektor może odwoływać się do ID elementu (np. #login_btn) lub klasy (np. Button).CSS<qsslite>
  #login_btn {
    background: #000000;
    color: #ffffff;
    hover-background: #38bdf8;
    hover-color: #000000;
  }
</qsslite>
📚 Kompletna lista właściwości1. Podstawy wizualneWłaściwośćOpisPrzykładbackgroundKolor tła elementu#000000colorKolor tekstu (foreground)#fffffffont-familyRodzina czcionekConsolasfont-sizeWielkość tekstu w px14font-weightGrubość czcionkibold / normal2. Layout i MarginesySilnik obsługuje precyzyjne sterowanie przestrzenią:margin: Ustawia margines dla wszystkich stron naraz.margin-top, margin-bottom, margin-left, margin-right: Precyzyjne sterowanie odstępami.align: Pozycjonowanie (left, right, center).3. Interakcje (Efekty profesjonalne)To serce QSSLite. Twój interfejs nie musi być statyczny!cursor: Zmienia wskaźnik myszy (pointer, text, arrow).border-width & border-color: Dodaje nowoczesne ramki do elementów.Stan HOVER: * hover-background: Kolor tła po najechaniu myszką.hover-color: Kolor tekstu po najechaniu myszką.Stan FOCUS:focus-border: Kolor ramki aktywnego pola tekstowego.🛠 Zaawansowane TechnikiGrupowanie selektorówNie musisz duplikować kodu! Użyj przecinków, aby nałożyć ten sam styl na wiele komponentów:CSS#btn_save, #btn_next, #btn_back {
    background: #1e293b;
    border-width: 1;
    border-color: #38bdf8;
}
Hierarchia i nadpisywanieSilnik przetwarza style od góry do dołu. Jeśli zdefiniujesz styl dla klasy (np. Button), a potem dla konkretnego #ID, to to drugie będzie miało priorytet.🖥 Debugowanie stylówJeśli style nie nakładają się poprawnie:Sprawdź ID: Upewnij się, że #ID w QSSLite zgadza się z id="..." w GTML.Kolejność: Upewnij się, że plik qsslite.py jest inicjowany po zbudowaniu drzewa widgetów.Logi: Silnik drukuje ostrzeżenia [Ostrzeżenie QSSLite], jeśli nie znajdzie selektora w GUI.🔮 Roadmapa QSSLite[ ] Wsparcie dla Gradientów (tła przejściowe).[ ] Wprowadzenie border-radius (zaokrąglone rogi).[ ] Animacje stanów (płynne przechodzenie kolorów).Z QSSLite Twój interfejs staje się żywy. Pamiętaj: Czysty kod = Czysty design.

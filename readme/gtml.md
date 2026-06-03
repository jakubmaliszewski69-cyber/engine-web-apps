Acme OS Engine (GTML/QSSLite Framework)



Acme OS Engine to zaawansowany, modularny framework do budowy interfejsów graficznych (GUI) w Pythonie. System opiera się na GTML (struktura XML) oraz QSSLite (style CSS-like), co pozwala na szybkie tworzenie responsywnych, nowoczesnych aplikacji w stylu "Dark Mode".







🏗 Architektura systemu



Projekt składa się z trzech głównych warstw:







Silnik (gtml.py): Zarządza oknem i przełączaniem widoków (SPA).







Budowniczy (budowniczy.py): Rejestr komponentów, który interpretuje tagi z plików .apps.







Stylizator (QSSLite): Odpowiada za warstwę wizualną, obsługę stanów hover i marginesów.







🛠 Jak rozbudować framework (Instrukcja Dewelopera)



Każdy element interfejsu to osobny plik w /apps/gtml/src/. Aby dodać nową funkcję, wykonaj te 3 kroki:







1\\. Stwórz plik modułu (np. switch.py)



Każdy moduł musi zawierać funkcję buduj\\\_..., która przyjmuje 4 argumenty:







Python



import tkinter as tk







def buduj\\\_switch(silnik, element, rodzic, funkcja\\\_budujaca):



\&#x20;   # Logika tworzenia widgetu



\&#x20;   widget = tk.Checkbutton(rodzic, text=element.text)



\&#x20;   widget.pack()



\&#x20;   return widget



2\\. Zarejestruj w budowniczy.py



W pliku budowniczy.py zaimportuj swój moduł i dopisz go do REJESTR\\\_TAGOW:







Python



from switch import buduj\\\_switch







REJESTR\\\_TAGOW = {



\&#x20;   'switch': buduj\\\_switch,



\&#x20;   # ... reszta modułów ...



}



3\\. Użyj w pliku .apps



Teraz możesz używać swojego modułu w dowolnym miejscu:







XML



<switch>Tryb Nocny</switch>



📜 Przykład: Budowa profesjonalnej strony ustawień



Oto jak połączyć GTML z QSSLite, aby uzyskać profesjonalny panel:







Struktura (settings.apps):







XML



<gtml>



\&#x20; <body>



\&#x20;   <view id="settings">



\&#x20;     <label id="header">Ustawienia</label>



\&#x20;     <box id="panel" layout="vertical">



\&#x20;       <input id="username" placeholder="Nowa nazwa..." />



\&#x20;       <button id="btn\\\_save" onclick="akcja:zapisz">ZAPISZ ZMIANY</button>



\&#x20;     </box>



\&#x20;   </view>



\&#x20; </body>



</gtml>



Style (settings.qss):







CSS



<qsslite>



\&#x20; #panel { background: #000000; margin: 20; }



\&#x20; 



\&#x20; #btn\\\_save { 



\&#x20;   background: #1e293b; 



\&#x20;   color: #ffffff; 



\&#x20;   cursor: pointer;



\&#x20;   border-width: 1;



\&#x20;   border-color: #38bdf8;



\&#x20;   hover-background: #38bdf8; /\\\* Efekt najechania \\\*/



\&#x20;   hover-color: #000000;



\&#x20; }



</qsslite>



📂 Struktura plików



Plaintext



/apps



\&#x20; /gtml/



\&#x20;   /src/              # <-- Tutaj dodajesz nowe moduły .py



\&#x20;     budowniczy.py    # Rejestracja tagów



\&#x20;     box.py           # Kontenery



\&#x20;     button.py        # Logika przycisków



\&#x20; /qsslite/            # Silnik stylów



test.apps              # Główny plik projektu



apps.py                # Launcher aplikacji



💡 Porady dla dewelopera



Zasada 3xM: Moduł, Metoda, Mapping. Zawsze trzymaj się tej ścieżki (Stwórz moduł -> Dodaj metodę budującą -> Dodaj do mapowania w budowniczy.py).







Unikaj twardych kodów: Kolory i czcionki definiuj w QSSLite, a nie wewnątrz plików .py. Dzięki temu zmienisz wygląd całego systemu w kilka sekund.







Acme OS Engine - Twórz GUI jak profesjonalista.




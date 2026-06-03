import tkinter as tk

def buduj_slider(silnik, element, rodzic, funkcja_budujaca):
    min_val = float(element.get('min', 0))
    max_val = float(element.get('max', 100))
    val = float(element.get('value', 50))

    bg_color = rodzic.cget("bg") if hasattr(rodzic, "cget") else "#000000"

    suwak = tk.Scale(
        rodzic,
        from_=min_val, to=max_val,
        orient="horizontal",
        bg=bg_color,
        fg="#ffffff",
        troughcolor="#333333",  # Kolor ścieżki (rynny)
        highlightthickness=0,
        activebackground="#38bdf8", # Kolor najechania myszką
        relief="flat"
    )
    suwak.set(val)
    suwak.pack(fill="x", pady=10, padx=5)

    return suwak
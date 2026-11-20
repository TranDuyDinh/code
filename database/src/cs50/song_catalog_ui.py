import tkinter as tk
from tkinter import ttk


SONGS = (
    (1, "Blinding Lights", "The Weeknd"),
    (2, "Levitating", "Dua Lipa"),
    (3, "Stay", "The Kid LAROI, Justin Bieber"),
    (4, "As It Was", "Harry Styles"),
    (5, "Shivers", "Ed Sheeran"),
    (6, "good 4 u", "Olivia Rodrigo"),
    (7, "Heat Waves", "Glass Animals"),
    (8, "Peaches", "Justin Bieber, Daniel Caesar, Giveon"),
)


def create_window():
    root = tk.Tk()
    root.title("Song Catalog")
    root.geometry("800x460")
    root.minsize(620, 340)
    root.configure(background="#f4f6f8")

    style = ttk.Style(root)
    style.configure("Catalog.Treeview", rowheight=36, font=("Segoe UI", 10))
    style.configure(
        "Catalog.Treeview.Heading",
        font=("Segoe UI", 10, "bold"),
        padding=(10, 9),
    )

    content = ttk.Frame(root, padding=(28, 24))
    content.pack(fill="both", expand=True)
    content.columnconfigure(0, weight=1)
    content.rowconfigure(2, weight=1)

    ttk.Label(content, text="Song Catalog", font=("Segoe UI", 19, "bold")).grid(
        row=0, column=0, sticky="w"
    )
    ttk.Label(
        content,
        text="Browse songs and artists",
        font=("Segoe UI", 10),
        foreground="#5b6573",
    ).grid(row=1, column=0, sticky="w", pady=(4, 16))

    table_frame = ttk.Frame(content)
    table_frame.grid(row=2, column=0, sticky="nsew")
    table_frame.columnconfigure(0, weight=1)
    table_frame.rowconfigure(0, weight=1)

    columns = ("id", "name", "artists")
    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        style="Catalog.Treeview",
        selectmode="browse",
    )
    table.heading("id", text="ID", anchor="w")
    table.heading("name", text="Song Name", anchor="w")
    table.heading("artists", text="Artists", anchor="w")
    table.column("id", width=70, minwidth=60, stretch=False, anchor="w")
    table.column("name", width=280, minwidth=160, anchor="w")
    table.column("artists", width=340, minwidth=180, anchor="w")
    table.tag_configure("even", background="#f5f7fa")

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    table.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    for index, song in enumerate(SONGS):
        table.insert("", "end", values=song, tags=("even",) if index % 2 else ())

    ttk.Label(
        content,
        text="{} songs".format(len(SONGS)),
        font=("Segoe UI", 9),
        foreground="#5b6573",
    ).grid(row=3, column=0, sticky="w", pady=(12, 0))

    return root


if __name__ == "__main__":
    create_window().mainloop()

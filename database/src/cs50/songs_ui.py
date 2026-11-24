import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from interfaces import DATABASE_PATH, PAGE_SIZE, load_songs

# songs = (
#     (1, "Blinding Lights", "The Weeknd"),
#     (2, "Levitating", "Dua Lipa"),
#     (3, "Stay", "The Kid LAROI, Justin Bieber"),
#     (4, "As It Was", "Harry Styles"),
#     (5, "Shivers", "Ed Sheeran"),
#     (6, "good 4 u", "Olivia Rodrigo"),
#     (7, "Heat Waves", "Glass Animals"),
#     (8, "Peaches", "Justin Bieber, Daniel Caesar, Giveon"),
# )


def load_next_batch(
    table: ttk.Treeview,
    status: ttk.Label,
    root: tk.Tk,
    load_button: ttk.Button,
    page_offset: tk.IntVar,
) -> None:
    offset = page_offset.get()
    print(f"offset: {offset}\n")
    try:
        songs = load_songs(offset=offset)
    except sqlite3.Error as error:
        status.configure(text="Unable to load songs")
        messagebox.showerror(
            "Database Error",
            "Could not read the song database at:\n{}\n\n{}".format(
                DATABASE_PATH, error
            ),
            parent=root,
        )
        return

    if not songs:
        load_button.configure(state="disabled")
        status.configure(
            text="All {} songs loaded".format(offset) if offset else "No songs found"
        )
        return

    table.delete(*table.get_children())
    for index, song in enumerate(songs):
        row_index = offset + index
        table.insert(
            "",
            "end",
            values=song,
            tags=("even",) if row_index % 2 else (),
        )

    page_offset.set(offset + len(songs))
    status.configure(
        text="{}-{} songs loaded".format(offset + 1, page_offset.get())
    )
    if len(songs) < PAGE_SIZE:
        load_button.configure(state="disabled")


def create_window():
    root = tk.Tk()
    root.title("Test")
    root.geometry("800x560")
    root.minsize(620, 340)
    root.configure(background="#ffffff")

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

    ttk.Label(content, text="Songs", font=("Segoe UI", 19, "bold")).grid(
        row=0, column=0, sticky="w"
    )

    # define table
    table_frame = ttk.Frame(content)
    table_frame.grid(row=2, column=0, sticky="nsew")
    table_frame.columnconfigure(0, weight=1)
    table_frame.rowconfigure(0, weight=1)

    columns = ("id", "name", "artists")
    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        height=PAGE_SIZE,
        style="Catalog.Treeview",
        selectmode="browse",
    )
    table.heading("id", text="ID", anchor="w")
    table.heading("name", text="Song Name", anchor="w")
    table.heading("artists", text="Artists", anchor="w")
    table.column("id", width=70, minwidth=60, stretch=False, anchor="w")
    table.column("name", width=280, minwidth=160, anchor="w")
    table.column("artists", width=340, minwidth=180, anchor="w")
    table.tag_configure("even", background="#dde6f4")

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    table.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    status = ttk.Label(
        content,
        text="",
        font=("Segoe UI", 9),
        foreground="#5b6573",
    )
    status.grid(row=3, column=0, sticky="w", pady=(12, 0))

    page_offset = tk.IntVar(root, value=0)
    load_button = ttk.Button(
        content,
        text="Next Page",
        command=lambda: load_next_batch(
            table, status, root, load_button, page_offset
        ),
    )
    load_button.grid(row=10, column=1, sticky="e")
    load_next_batch(table, status, root, load_button, page_offset)

    return root



import sqlite3
import tkinter as tk
from contextlib import closing
from pathlib import Path
from tkinter import messagebox, ttk
from typing import List, Tuple


DATABASE_PATH = Path(__file__).resolve().parent / "songs" / "songs.db"
PAGE_SIZE = 10
Song = Tuple[int, str, str]


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
    status.configure(text="{}-{} songs loaded".format(offset + 1, page_offset.get()))
    if len(songs) < PAGE_SIZE:
        load_button.configure(state="disabled")


def load_songs(database_path: Path = DATABASE_PATH, offset: int = 0) -> List[Song]:
    if offset < 0:
        raise ValueError("offset must be non-negative")

    database_uri = database_path.resolve().as_uri() + "?mode=ro"
    query = """
        SELECT songs.id, songs.name, artists.name
        FROM songs
        JOIN artists ON artists.id = songs.artist_id
        ORDER BY songs.id
        LIMIT ? OFFSET ?
    """

    with closing(sqlite3.connect(database_uri, uri=True)) as connection:
        return [
            (song_id, song_name, artist_name)
            for song_id, song_name, artist_name in connection.execute(
                query, (PAGE_SIZE, offset)
            )
        ]

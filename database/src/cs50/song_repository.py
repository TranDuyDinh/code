import sqlite3
from contextlib import closing
from pathlib import Path
from typing import List, Tuple


DATABASE_PATH = Path(__file__).resolve().parent / "songs" / "songs.db"
Song = Tuple[int, str, str]


def load_songs(database_path: Path = DATABASE_PATH) -> List[Song]:
    database_uri = database_path.resolve().as_uri() + "?mode=ro"
    query = """
        SELECT songs.id, songs.name, artists.name
        FROM songs
        JOIN artists ON artists.id = songs.artist_id
        ORDER BY songs.id
    """

    with closing(sqlite3.connect(database_uri, uri=True)) as connection:
        return [
            (song_id, song_name, artist_name)
            for song_id, song_name, artist_name in connection.execute(query)
        ]

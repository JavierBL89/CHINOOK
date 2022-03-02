from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)


# LINK PYTHON FILE TO CHINOOK DB
db = create_engine("postgresql:///chinook")

# METADATA CLASS WILL CONTAIN A COLLECTION OF OUR TABLE OBJECTS
meta = MetaData(db)

artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey(
        "artist_table.ArtistId"))   # we relate tables here
)

track_tabe = (
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey(
        "album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer),
    Column("Composer", String),
    Column("Miliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# MAKING THE CONNECTION

with db.connect() as connection:
    # QUERY 1
    # select_query = artist_table.select()

    # QUERY 2
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # QUERY 3
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # QUERY 4
    select_query = artist_table.select().with_only_columns(
                                     [artist_table.c.Name])

    # QUERY 5
    select_query = album_table.select().where(album_table.c.ArtistId == 51)
    results = connection.execute(select_query)
    for result in results:
        print(result)

from flask import Flask, request, send_file
from webargs import fields, validate
from webargs.flaskparser import  use_kwargs
from hw4.database_handler import execute_query
from hw4.validator import order_price_validator, track_id_validator

app = Flask(__name__)


@app.route('/order_price')
@use_kwargs(
    order_price_validator,
    location = "query",
)
def order_price(country):
    query = """
     SELECT invoices.BillingCountry, SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS TotalSales
     FROM invoices JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
     GROUP BY invoices.BillingCountry
    """

    if country:
        query += f"HAVING invoices.BillingCountry = '{country}'"

    records = execute_query(query=query)
    return records

@app.route('/get_all_info_about_track')
@use_kwargs(
    track_id_validator,
    location = "query",
)
def get_all_info_about_track(track_id):
    query = f"""
    SELECT 
        tracks.TrackId, 
        tracks.Name AS TrackName, 
        albums.Title AS AlbumTitle, 
        artists.Name AS ArtistName, 
        genres.Name AS Genre, 
        media_types.Name AS MediaType, 
        tracks.Composer, 
        tracks.Milliseconds, 
        tracks.Bytes, 
        tracks.UnitPrice
    FROM tracks
    LEFT JOIN albums ON tracks.AlbumId = albums.AlbumId
    LEFT JOIN artists ON albums.ArtistId = artists.ArtistId
    LEFT JOIN genres ON tracks.GenreId = genres.GenreId
    LEFT JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
    WHERE tracks.TrackId = {track_id}
    """

    records = execute_query(query=query)
    return records



@app.route('/get_time_of_all_tracks')
def get_time_of_all_tracks():
    query = """
    SELECT 
    albums.Title AS AlbumTitle, 
    SUM(tracks.Milliseconds) / 1000.0 / 60 / 60 AS TotalHours
    FROM tracks
    LEFT JOIN albums ON tracks.AlbumId = albums.AlbumId
    GROUP BY albums.AlbumId;
    """

    records = execute_query(query=query)
    result = 0

    for row in records:
        result += row[1]

    return f'Time of all tracks of all albums: {str(round(result, 2))}hours'



if __name__ == "__main__":
    app.run(
        debug=True,
        host="localhost",
    )
from flask import Flask

from webargs.flaskparser import  use_kwargs

from hw5.database_handler import execute_query
from hw5.validator import stats_by_city_validator

app = Flask(__name__)


@app.route('/stats_by_city')
@use_kwargs(
    stats_by_city_validator,
    location = "query",
)
def stats_by_city(genre):
    if genre is None:
        return 'You have not specified the genre.'

    query = """
    SELECT customers.City, COUNT(invoices.InvoiceId) AS purchase_count
    FROM customers
    JOIN invoices ON customers.CustomerId = invoices.CustomerId
    JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
    JOIN tracks ON invoice_items.TrackId = tracks.TrackId
    JOIN genres ON tracks.GenreId = genres.GenreId
    WHERE genres.Name = ?
    GROUP BY customers.City
    ORDER BY purchase_count DESC
    """

    cities = execute_query(query, (genre,))

    if not cities:
        return "No data available for this genre."

    city_list = [{"city": city[0], "purchase_count": city[1]} for city in cities]
    return f'Most listened to {genre} in: {city_list[:2]}'


if __name__ == "__main__":
    app.run(
        debug=True,
        host="localhost",
    )


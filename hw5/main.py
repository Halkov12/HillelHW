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
    SELECT City, purchase_count 
    FROM GenreStatsByCity
    WHERE Genre = ? AND rank_position = 1;
    """

    cities = execute_query(query, (genre,))

    if cities:
        return cities
    else:
        return 'No data available for this genre.'



if __name__ == "__main__":
    app.run(
        debug=True,
        host="localhost",
    )


# Day 64: Ranking Movies Dynamically with Flask and TMDB API

Today the focus was on improving our movie ranking system in the Flask app. The key learning was how to dynamically assign a ranking to movies based on their ratings, so the front of the movie cards no longer shows 'None' but the correct rank according to the rating.

I updated the `home` route to:

- Fetch all movies from the database and sort them by rating in descending order.  
- Assign ranking numbers dynamically based on their position in the sorted list.  
- Commit the updated rankings to the database so they persist and automatically update whenever ratings change.

Additionally, I reinforced how to use the TMDB API to search for movies by title and then use the selected movie's ID to fetch detailed information (like poster URLs, description, and year of release) to populate the database. This way, the user can select a movie from a list, and it will appear as a card with proper ranking and information.

This workflow ensures that the best-rated movies always appear at the top, and rankings adjust automatically as ratings are added or edited.

**Key takeaways:**
- Using `order_by()` in SQLAlchemy to sort query results.
- Assigning dynamic properties to model instances before committing to the database.
- Fetching and using external API data (TMDB) to populate a database.
- Ensuring UI reflects backend logic dynamically without changing HTML templates.

Feeling more confident in building interactive, data-driven web applications with Flask! 🚀

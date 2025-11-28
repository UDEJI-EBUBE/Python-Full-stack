**Day 63: Building a Dynamic Flask Library App with Database Integration**

Today, the course focused on integrating SQLAlchemy with Flask to create a dynamic library app. Key takeaways from today’s session:

1. **Database fundamentals:**  
   Learned how to define models with SQLAlchemy, create tables, and add records to an SQLite database. I got hands-on experience initializing the database and committing new entries.

2. **Displaying records dynamically:**  
   Fetched all books from the database and displayed them on the homepage. Learned to loop through records in Jinja templates and handle empty libraries gracefully.

3. **Edit functionality:**  
   Implemented an edit route to update a book’s rating. Learned how to pass the book’s ID through URLs and fetch the correct record for editing.

4. **Delete functionality:**  
   Explored multiple ways to delete records:
   - Handling deletion in the same route using `if` statements.
   - Sending the book ID via forms or query parameters.
   - Even using anchor `<a>` tags for deletion (GET requests), while understanding why POST is safer.

5. **Passing values in templates:**  
   Learned how to use `url_for` correctly with variables, and the importance of not putting variables in quotes when passing them to URLs.

6. **Form handling best practices:**  
   Learned how to handle multiple buttons in one form using the `name` and `value` attributes, and identify which button was clicked in the backend using `request.form.get()`.

By the end of today, my app can:  
- Display all books from the database.  
- Edit book ratings.  
- Delete books using different techniques while sending the correct ID.  

Today reinforced my understanding of **databases, routing, template rendering, and dynamic user interactions** in Flask, making the app fully interactive and database-driven.

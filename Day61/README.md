**Day 61 of the 100 Days of Python Journey**

Today’s lesson focused on building cleaner, more secure, and more professional Flask applications by combining WTForms, Flask-WTF, and Flask-Bootstrap5.

Here’s what the course covered:

**WTForms & Validation**  
We created structured form classes (like the `LoginForm`) using `StringField`, `PasswordField`, and validators such as `DataRequired()`. This made the form logic cleaner and easier to manage inside Python instead of raw HTML.

**CSRF Protection with Flask-WTF**  
By using `FlaskForm` and setting a secret key, CSRF protection was automatically added to prevent malicious form submissions. This made the login form both functional and secure.

**Flask-Bootstrap5 Integration**  
Instead of manually writing Bootstrap classes, we used `Bootstrap5(app)` and the `render_form()` helper to instantly style the login page. This kept the interface clean with minimal code.

**Template Inheritance for Cleaner HTML**  
A base layout file (`base.html`) was created with the necessary CSS and blocks. The login page (`login.html`) then extended this base template and only added page-specific content. This helps maintain a consistent design across multiple pages while keeping templates organized.

By combining these tools, today’s work produced a login system that is secure, visually polished, and easier to scale.

Looking forward to Day 62.
Form handling using wtforms

# Day 68: Password Hashing, Salting, and Authentication in Flask

Today, I focused on securing user data in web applications. I learned how to:

- **Password Hashing**: Use `werkzeug.security.generate_password_hash()` to safely store passwords so plain-text passwords are never saved.  
- **Salting**: Add randomness to passwords before hashing to ensure that even if two users have the same password, their hashes are unique.  
- **Authentication with Flask-Login**: Implement login, logout, and session management. I explored how to protect routes so only logged-in users can access sensitive pages, and how `UserMixin`, `user_loader`, and `login_user()` work together to manage user sessions securely.  

This gave me a solid understanding of the core techniques needed to handle user credentials safely and control access in Flask applications.

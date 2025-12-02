# Day 67

Today’s work focused on improving the blog project by moving all the blog data into a real **database** instead of using the previous npoint API. This change made the project more reliable, scalable, and properly structured. With the database in place, every blog post is now stored as a record with fields like title, subtitle, author, image URL, and body.

We also applied the core rules that guide how data is managed inside a database. This included **adding new records**, **retrieving existing posts**, **updating blog entries**, and **deleting posts** when needed. These operations were implemented using SQLAlchemy’s session methods to ensure that every modification was saved correctly.

By integrating proper database storage and applying the principles of adding, updating, and deleting data, the blog project became more dynamic and much closer to a real-world application. Today’s progress formed a strong foundation for future features and improvements.

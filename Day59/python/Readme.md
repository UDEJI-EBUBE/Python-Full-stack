# Day 59: Python + Flask + Bootstrap – Dynamic Blog Webpage

Today, the course focused on combining Flask with Bootstrap to create a dynamic blog webpage. The main highlight was learning how to use Flask's `url_for` function to dynamically link static resources like CSS and JavaScript, instead of hardcoding the paths. This ensures that links to static files always work, even if the project structure changes.

Another new concept introduced was using Jinja’s `{% include %}` directive to include reusable HTML components, like headers and footers, across multiple pages. This makes templates cleaner and easier to maintain.

During the lesson, I built an index page that displays blog posts dynamically from a JSON API. Each post links to its own page using a dynamic route (`/post/<int:num>`), allowing individual blog pages to be generated on the fly.

By the end of the session, I was able to:
- Fetch JSON data from an API using Python's `requests` module.
- Pass that data to Flask templates and loop through it using Jinja to render multiple posts.
- Use `url_for` for linking static files and internal routes.
- Include reusable HTML components with `{% include %}` to maintain a consistent layout.

Overall, it was an exciting step into creating fully dynamic websites with Flask and Bootstrap.

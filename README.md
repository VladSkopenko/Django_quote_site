### Deploy app : https://vladislav-skopenko-site-maker.fly.dev/
### Dockerhub : https://hub.docker.com/r/skopenkovladislav/vsco_quote_app

Here’s the project description in English:

Quotes to Scrape
Quotes to Scrape is a web application designed for collecting and displaying quotes. Users can view, search, and filter quotes by authors and tags. The project is built using Django with Bootstrap for styling and CSS for custom design.

# Features:
View Quotes: Users can browse a list of quotes, each showing the author and associated tags.
Search and Filter: Users can search quotes by tags and authors. A simple and intuitive search form allows quick access to desired quotes.
Tags: Displays popular tags with the ability to filter quotes by selected tags.
Authentication: Supports user registration and authentication. Users can add new quotes and authors, and manage their profile.
# Technical Details:
Tech Stack: Django, Python, Bootstrap, HTML/CSS.
Templates: Utilizes templates to separate logic from presentation. The main template (base.html) includes common interface elements across pages, such as the header, search form, and user panel.
Data Models: Models for storing quotes, authors, and tags. Relationships between models are established for easy data display and filtering.
Authentication: Standard Django authentication with registration, login, and logout functionalities.

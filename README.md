# Crochet Shop
### File Structure:
```
crochet
└───.gitignore
|
└───README.md
│
└───app
│   │   __init__.py
|   |   app.py
│
└───static
│   └───css
|   |   |   main.css
│   │  
│   └───images
│   └───scripts
│
└───templates
│   │   index.html
|   |   layout.html
│
└───__pycache__
|   .gitignore
|   README.md
```

## General Use
To run this directory, first make sure your requirements match.

`pip install -r requirements.txt`

Create a `.env` file by making a copy of `sample.env`, configuring to your MySQL database, and renaming to `.env`.

Then navigate to crochet/app/ and run `flask run`.
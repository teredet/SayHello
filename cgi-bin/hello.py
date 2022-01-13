#!/usr/bin/env python3
import cgi
import html
import sqlite3


conn = sqlite3.connect('names.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS names(
   first_name TEXT,
   second_name TEXT);
""")


form = cgi.FieldStorage()
first_name = form.getfirst("FirstName", "None")
first_name = html.escape(first_name)
second_name = form.getfirst("SecondName", "None")
second_name = html.escape(second_name)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Hello</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        </head>
        <style>
            body {
            padding-top: 56px;
        }
        </style>
        <body>
            <div class="container">""")

info = cur.execute('SELECT * FROM names WHERE first_name = ? AND second_name = ?;', (first_name, second_name))

if info.fetchone() is None: 
    cur.execute(f"""INSERT INTO names VALUES(?, ?);""", (first_name, second_name))
    conn.commit()
    
    print(f"<h1>Hello, {first_name} {second_name}</h1>")
else:
    print(f"<h1>Already seen, {first_name} {second_name}</h1>")

conn.close()

print("""</div>
        </body>
        </html>""")
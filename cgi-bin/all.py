#!/usr/bin/env python3
import sqlite3


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


conn = sqlite3.connect('names.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS names(
   first_name TEXT,
   second_name TEXT);
""")

cur.execute('SELECT * FROM names;')
info = cur.fetchall()

print('''
<h1>List of all who greeted</h1>
<table class="table">
    <tbody>
        <tr>
            <td>First Name</td>
            <td>Second Name</td>
        </tr>''')
for name, surname in info:
    print(f'''<tr>
    <td>{name}</td>
    <td>{surname}</td>
    </tr>''')
print('''
    </tbody>
</table> 
''')

conn.close()
print("""</div>
        </body>
        </html>""")

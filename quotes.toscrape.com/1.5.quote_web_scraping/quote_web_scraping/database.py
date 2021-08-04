import sqlite3

con = sqlite3.connect('allmyquotes.db')

cursor = con.cursor()

cursor.execute("""  create table tbl_quotes (
                            desc text ,
                            author text,
                            tag text
                        )""")

con.commit()
con.close()
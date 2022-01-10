import csv
import sqlite3

x = 0
t = 0
award_list = []
filename = "database_code/awards.csv"
with open(filename, mode='r') as data:
    csvfile = csv.DictReader(data)
    for lines in csvfile:
        registrant = [lines['nominee_fl'], lines['description'], lines['Image_File'], lines['Num_of_votes']]
        award_list.append(registrant)
        print(award_list)
# setting all the fields for the first registrant

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('Conference.sqlite')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the AWARDS table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS AWARDS")


# Creating table
def create_table():
    cursor_obj.execute(
        'CREATE TABLE IF NOT EXISTS AWARDS (Num_of_votes REAL, Image_File TEXT, description TEXT, Nominee_fl TEXT,id INTEGER PRIMARY KEY AUTOINCREMENT)')


def data_entry():
    a = 0
    ids = 123
    while 0 <= a < 3:
        Nominee_fl = award_list[a][0]
        descriptions = award_list[a][1]
        Image_File = award_list[a][2]
        Num_of_votes = award_list[a][3]
        ids = ids + 1
        a = a + 1
        print(a)
        cursor_obj.execute(
            "INSERT INTO AWARDS (Num_of_votes, Image_File, description, Nominee_fl, id) VALUES(?, ?, ?, ?, ?)",
            (Num_of_votes, Image_File, descriptions, Nominee_fl, ids))


create_table()
data_entry()
connection_obj.commit()
cursor_obj.close()
connection_obj.close()
print("Table is Ready")

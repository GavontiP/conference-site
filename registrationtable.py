import csv
import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('Conference.sqlite')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the AWARDS table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS REGISTRANTS")

# Creating table
x = 0
t = 0
registrant_list = []
filename = "database_code/registrant_data_simplified.csv"
with open(filename, mode='r') as data:
    csvfile = csv.DictReader(data)
    for lines in csvfile:
        registrant = [lines['Registration_date'], lines['Title'], lines['firstName'], lines['lastName'],
                      lines['Street'], lines['Suite'], lines['City'], lines['State'], lines['Zip'],
                      lines['Phone'], lines['email'], lines['website'], lines['position'], lines['company'],
                      lines['session1'], lines['session2'], lines['session3']]
        registrant_list.append(registrant)
        print(registrant_list)
# setting all the fields for the first registrant

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('Conference.sqlite')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the AWARDS table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS REGISTRANTS")


# Creating table
def create_table():
    cursor_obj.execute(
        'CREATE TABLE IF NOT EXISTS REGISTRANTS(Registration_date TEXT, Title TEXT, firstName TEXT, lastName TEXT, Street TEXT, Suite TEXT, City TEXT, States TEXT,'
        'Zip REAL, Phone TEXT, email TEXT, website TEXT, positions TEXT, company TEXT, session1 TEXT, session2 TEXT,session3 TEXT)')


def data_entry():
    a = 0
    while 0 <= a < 36:
        Registration_date = registrant_list[a][0]
        Title = registrant_list[a][1]
        firstName = registrant_list[a][2]
        lastName = registrant_list[a][3]
        Street = registrant_list[a][4]
        Suite = registrant_list[a][5]
        City = registrant_list[a][6]
        States = registrant_list[a][7]
        Zip = registrant_list[a][8]
        Phone = registrant_list[a][9]
        email = registrant_list[a][10]
        website = registrant_list[a][11]
        positions = registrant_list[a][12]
        company = registrant_list[a][13]
        session1 = registrant_list[a][14]
        session2 = registrant_list[a][15]
        session3 = registrant_list[a][16]
        a = a + 1
        print(a)
        cursor_obj.execute(
            "INSERT INTO REGISTRANTS (Registration_date,"
            " Title,"
            " firstName,"
            " lastName,"
            " Street,"
            " Suite,"
            " City,"
            " States,"
            " Zip,"
            " Phone,"
            " email,"
            " website,"
            " positions,"
            " company,"
            " session1,"
            " session2,"
            " session3) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (Registration_date, Title, firstName, lastName, Street,
             Suite, City, States, Zip, Phone,
             email, website, positions, company, session1, session2, session3))


create_table()
data_entry()
connection_obj.commit()
cursor_obj.close()
connection_obj.close()
print("Table is Ready")

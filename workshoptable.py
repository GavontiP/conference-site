import csv
import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('Conference.sqlite')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the AWARDS table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS WORKSHOPS")

# Creating table
x = 0
t = 0
workshop_list = []
filename = "database_code/workshops.csv"
with open(filename, mode='r') as data:
    csvfile = csv.DictReader(data)
    for lines in csvfile:
        registrant = [lines['name_title'], lines['time_slot'], lines['room_number'], lines['start_time'],
                      lines['end_time']]
        workshop_list.append(registrant)
        print(workshop_list)
# setting all the fields for the first registrant

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('Conference.sqlite')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the AWARDS table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS WORKSHOPS")


# Creating table
def create_table():
    cursor_obj.execute(
        'CREATE TABLE IF NOT EXISTS WORKSHOPS (name_title TEXT, time_slot TEXT, room_number TEXT, start_time TEXT,end_time TEXT)')


def data_entry():
    a = 0
    ids = 123
    while 0 <= a < 3:
        name_title = workshop_list[a][0]
        time_slot = workshop_list[a][1]
        room_number = workshop_list[a][2]
        start_time = workshop_list[a][3]
        end_time = workshop_list[a][4]
        a = a + 1
        print(a)
        cursor_obj.execute(
        "INSERT INTO WORKSHOPS (name_title, time_slot, room_number, start_time, end_time) VALUES(?, ?, ?, ?, ?)",
        (name_title, time_slot, room_number, start_time, end_time))


create_table()
data_entry()
connection_obj.commit()
cursor_obj.close()
connection_obj.close()
print("Table is Ready")

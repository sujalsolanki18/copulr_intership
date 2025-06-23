import sqlite3

# Connect to database (creates if it doesn't exist)
conn = sqlite3.connect('college.db')


conn.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY,
             name TEXT,
             age INTEGER)''')


conn.execute("INSERT INTO students (name, age) VALUES ('pawan', 20),('rahul', 22),('sanjay', 21),('gaurav', 23)")



print("All students:")
cursor = conn.execute("SELECT * FROM students")
for row in cursor:
    print(row)


conn.execute("UPDATE students SET age = 23 WHERE name = 'Bob'")

# Delete Charlie
conn.execute("DELETE FROM students WHERE name = 'Charlie'")

# Show updated list
print("\nAfter changes:")
cursor = conn.execute("SELECT * FROM students")
for row in cursor:
    print(row)


conn.commit()
conn.close()
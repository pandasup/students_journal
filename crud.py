import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        age INTEGER,
        major TEXT NOT NULL
    )''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name VARCHAR NOT NULL,
        instructor TEXT NOT NULL
    )''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS students_courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )''')


def create_student(name, age, major):
    cursor.execute(
    """INSERT INTO students (name, age, major) 
    VALUES (?, ?, ?)""", 
    [name, age, major]
    )
    conn.commit()
    
def create_course(course_name, instructor):
    cursor.execute(
    """INSERT INTO courses (course_name, instructor) 
    VALUES (?, ?)""", 
    [course_name, instructor]
    )
    conn.commit()
    
def get_students():
    cursor.execute("""SELECT * FROM students"""
    )
    students = cursor.fetchall()
    return students

def get_courses():
    cursor.execute("""SELECT * FROM courses"""
    )
    courses = cursor.fetchall()
    return courses
    
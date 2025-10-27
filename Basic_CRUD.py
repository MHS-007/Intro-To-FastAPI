from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 🎓 Student model
class Student(BaseModel):
    ID: int
    Name: str
    Age: int

# 🧺 List to store all students
students = []

# 🏠 Default route
@app.get("/")
def defaultFunc():
    return {"Messasge": "This is a default message."}

# 📄 Get all students
@app.get("/students")
def getStudents():
    return students

# ➕ Add or create student
@app.post("/students")
def addStudent(student: Student):
    students.append(student)
    return {"Message" : "Student Added", "Data": student}

# 🔍 Get specific student by ID
@app.get("/students/{id}")
def getStudentById(id: int):
    for s in students:
        if s.ID == id:
            return {"Message": "Student Retrieved", "Data": s}
    return {"Message": "Student does not exist!"}

# ✏️ Update student by ID
@app.put("/students/{id}")
def updateStudent(id: int, updatedStudent: Student):
    for i, s in enumerate(students):
        if s.ID == id:
            students[i] = updatedStudent
            return {"Message": "Student Updated", "Data": updatedStudent}
    return {"Message": "Student not found for update."}

# ❌ Delete student by ID
@app.delete("/students/{id}")
def deleteStudent(id: int):
    for i, s in enumerate(students):
        if s.ID == id:
            deleted = students.pop(i)
            return {"Message": "Student Deleted", "Data": deleted}
    return {"Message": "Student not found for deletion."}
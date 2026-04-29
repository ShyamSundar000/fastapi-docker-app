from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students=[]

class Student(BaseModel):
    name:str
    age:int
    marks:float

@app.get("/students")
def get_students():
    return {
        "Total":len(students),
        "Data":students
    }

@app.get("/students/{index}")
def get_student(index:int):
    if index<0 or index>=len(students):
        return {"error":"Student not found"}
    return students[index]

@app.post("/students")
def add_student(student:Student):
    students.append(student)
    return {"message":"Student added successfully!","data":students}

@app.put("/students/{index}")
def update_student(index:int,student:Student):
    if index<0 or index>=len(students):
        return {"error":"Student not found"}
    students[index]=student
    return {"message":"Student updated successfully!","data":students}

@app.delete("/students/{index}")
def remove_student(index:int):
    if index<0 or index>=len(students):
        return {"error":"Student not found"}
    removed=students.pop(index)
    return {"message":"Student removed", "data":students}
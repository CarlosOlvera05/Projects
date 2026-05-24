from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Carlos"}

students = {
    1: "Carlos",
    2: "Carla",
    3: "Alex"
}

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id in students:
        return {
            "id": student_id,
            "name": students[student_id]
        }

    return {"error": "Student not found"}
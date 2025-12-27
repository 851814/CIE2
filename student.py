def student_details(usn,name,division,age):
    result=(
        f"Student USN:{usn}"
        f"Student Name:{name}"
        f"Division:{division}"
        f"Age:{age}"
    )
if __name__ == "__main__":
    usn="01fe24bca274"
    name="soumya"
    division="E"
    age=19
    print(student_details(usn,name,division,age))

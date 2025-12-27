def student_details(usn,name,division,age):
    result=(
        f"Student USN:{usn}\n"
        f"Student Name:{name}\n"
        f"Division:{division}\n"
        f"Age:{age}\n"
    )
if __name__ == "__main__":
    usn="01fe24bca274"
    name="soumya"
    division="E"
    age=19
    print(student_details(usn,name,division,age))

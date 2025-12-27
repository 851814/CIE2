from student import student_details
def text_student_details():
    expected_output=(
        "Student USN:01fe24bca274\n"
        "Student name:soumya\n"
        "Division:E\n"
        "Age:19"
    )
    assert student_details("01fe24bca274","soumya","E",19)== expected_output
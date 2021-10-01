import backend

exam_template = 'ExamTemplate.pdf'      # Template
room = "Hewlett 200"                    # Which room?
start = 1                               # Fefault: 1
number = 10                             # Number of Exams

OAE = False
left = False                            # Left-handed

backend.Exams(exam_template, room, start, number, left, OAE)


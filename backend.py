from pdf_annotate import PdfAnnotator, Location, Appearance
import pdf_annotate as pa


def get_num_pages(a):
    n = 0
    while True:
        try: 
            a.get_size(n)
            n += 1
        except:
            break

    return n

def get_pages_to_write_to(a):

    n = get_num_pages(a)
    
    return range(0,n,2)

def get_seats(room):

    if room == 'Hewlett 200':
        import Hewlett200
        return Hewlett200.normal, Hewlett200.front, Hewlett200.left

    elif room == 'Hewlett 201':
        import Hewlett201
        return Hewlett201.normal, Hewlett201.front, Hewlett201.left


def Exams(template, room, start, num, left=False, OAE=False):

    # which pages to write to
    pages = get_pages_to_write_to(PdfAnnotator(template))

    # which exam numbers
    exams = range(start, start+num)

    # room seats
    seats = get_seats(room)
    mod = ''
    if not left and not OAE:
        seats = seats[0]
    elif left and not OAE:
        seats = seats[1]
        mod = 'L'
    elif OAE:
        seats = seats[2]
        mod = 'OAE'


    for exam in exams:
        # Open up template
        a = PdfAnnotator(template)
        for page in pages:
            size = a.get_size(page)

            x1 = size[0]*0.70
            y1 = size[1]*0.94
            
            x2 = size[0]*0.97
            y2 = size[1]*0.99

            a.add_annotation('text', Location(x1=x1, y1=y1, x2=x2, y2=y2, page=page), Appearance(fill=[0, 0, 0], stroke_width=1, font_size=10, content=f"{room}, Seat {seats[exam-1]}, Exam {mod}{exam} "))
                

            #'text',
            #Location(x1=x0, y1=y0, page=page),
            #content = f"{room}: Exam {exam}")


        print(f"Writing Exam {exam}")
        a.write(f'Exam{exam}.pdf')  # or use overwrite=True if you feel lucky
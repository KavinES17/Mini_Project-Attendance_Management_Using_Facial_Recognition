from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import webbrowser
import shutil
from faceencoding import*

win = Tk()

width = win.winfo_screenwidth()
height = win.winfo_screenheight()

win.geometry("%dx%d" % (width, height))

bg_image_path = r"C:\Users\kavin\Downloads\10450447.png"
bg = ImageTk.PhotoImage(file=bg_image_path)

canvas = Canvas(win, width=750, height=3500)
canvas.pack(fill=BOTH, expand=True)

canvas.create_image(0, 0, image=bg, anchor='nw')

def resize_image(e):
    global image, resized, image2
    image = Image.open(bg_image_path)
    
    resized = image.resize((e.width, e.height), Image.LANCZOS)
    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')
    canvas_id = canvas.create_text(100, 250, anchor="nw")
    canvas.itemconfig(
        canvas_id, text="Welcome To The Attendance Management System\n\nLet's get Started"*1, width=780,)
    canvas.itemconfig(canvas_id, font=("courier", 16), fill='#F5F5DC')
    canvas.insert(canvas_id, 16, "")
    canvas_h = canvas.create_text(300, 50, anchor="nw")
    canvas.itemconfig(
        canvas_h, text="Attendance Management System using Face Recognition"*1, width=800)
    canvas.itemconfig(canvas_h, font=("Times New Roman bold", 25), fill='#BCBC8F')
    canvas.insert(canvas_h, 16, "")

win.bind("<Configure>", resize_image)
win.title("Automated Attendance System")

button1 = Button(win, text="Take Attendance",
                bg='DodgerBlue4', fg='white', height='2', width='15', border='5', font=("Times New Roman", 11), command=take_attendance)
button1.pack(pady='10')

button2 = Button(win, bg="DodgerBlue4", fg="white", text="View Attendance",
            height='2', width='15', border='5', font=("Times New Roman", 11), command=show_attendance)
button2.pack(pady='10')

def new_registration():
    file = fd.askopenfilename(title="Select an image to register", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    
    if file:
        destination = r"C:\Users\kavin\OneDrive\Pictures\Lenovo\Facial-Recognition-Attendance\Facial-Recognition-Attendance\images"
        
        shutil.copy(file, destination)
        
        print("Face added successfully to the directory!")


button3 = Button(win, bg="DodgerBlue4", fg="white", text="Click to register a new student",
                border='5', height='2', width='25', font=("Times New Roman", 11), command=new_registration)
button3.pack()

def help():
    webbrowser.open("https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAN__lSuQihUQ1NUTTE0MlA5TEtaNDNVSURNVkxXTEhRNS4u")

button4 = Button(win, bg="DodgerBlue4", fg="white", text="Get Help",
                height='2', width='8', border='5', font=("Times New Roman", 11), command=help)
button4.pack()

def exit_program():
    win.destroy()

button5 = Button(win, bg="DodgerBlue4", fg="white", text="Exit", height='2',
        width='8', border='5', command=exit_program, font=("Times New Roman", 11))
button5.pack()

canvas.create_image(0, 0, image=bg, anchor="nw")

button1_canvas = canvas.create_window(100, 550, anchor="nw", window=button1)
button2_canvas = canvas.create_window(300, 550, anchor="nw", window=button2)
button3_canvas = canvas.create_window(680, 550, anchor="nw", window=button3)
button4_canvas = canvas.create_window(950, 550, anchor="nw", window=button4)
button5_canvas = canvas.create_window(520, 550, anchor="nw", window=button5)

win.mainloop()

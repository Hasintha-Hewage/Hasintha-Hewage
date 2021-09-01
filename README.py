import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox as mbox

run_once = False

'''Windows Interface'''
window = Tk()
window.title("Face Detection")
window.geometry('700x250+500+100')

# Label for instruction
lbl = Label(window, text="Enter the Address of the videoFeed")
lbl.pack()

# Entry
value = StringVar()
e = Entry(window, textvariable=value, width=80)
e.pack()

# command Function
def myclick():
    window.quit()
    return value.get()

def instruction():
    global run_once
    if run_once:
        return
    file = open("Readme.txt", 'r')
    t = file.read()
    textbox = Text(window, width=85, height=8)
    textbox.pack()
    textbox.insert(END, t)
    file.close()
    run_once = True

# buttons
mybutton = Button(window, text="Confirm", command=myclick)
mybutton.pack(pady=2)

mybutton2 = Button(window, text="Instruction", command=instruction)
mybutton2.pack(pady=2)

window.mainloop()

# Loading image
s = myclick()
if s == "0" or s == "1" or s == "-1":
    a = int(s)
elif s=="":
    sys.exit()
else:
    a = s

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(a)
cap.set(3, 640)  # set video widht
cap.set(4, 480)  # set video height
minW = 0.1 * cap.get(3)
minH = 0.1 * cap.get(4)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    except Exception:
        mbox.showerror("Error", "Not a valid Address")
        break
    else:
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.01, 1)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Display
        cv2.putText(img, "Press \"ESC\" to exit", (10, 40), font, 1, (0, 0, 0), 1)
        cv2.imshow('Face Detection', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
sys.exit()



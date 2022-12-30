from tkinter import *
from tkinter import messagebox
import re

#function executed on clicking the button
def check():

    score = 0
    passwd = user_input.get()
    specialChar = ['!', '@', '$', '%', "&", '*', '/']

    #checks if Entry field is empty or not
    if passwd:
        if len(passwd) < 8:
            score = 0

        else:
            if re.search("[a-z]", passwd):
                score += 1

                if re.search("[A-Z]", passwd):
                    score += 1

                    if re.search("[0-9]", passwd):
                        score += 1

        

        #checks score and displays the message according to that score
        if score == 0:
            messagebox.showwarning('Highly Vulnerable', 'Too Weak. Your password is easily crackable!!!')

        elif score == 1:
            messagebox.showinfo('Vulnerable', 'Too Weak. Try adding some uppercase characters to it!!!')

        elif score == 2:
            messagebox.showinfo('Medium', 'Weak. Try adding some numeric values!!!')

        elif score == 3:
            messagebox.showinfo('Medium', 'Weak. Try adding some special characters!!!')

        elif score == 4:
            messagebox.showinfo('Strong', 'Very Strong. Your password cannot be cracked!!!')


    else:
        messagebox.showerror('Error', 'Cannot be blank')


#window initialising
window = Tk()
window.title('Password Strength Tester')
window.geometry('900x500')

#Label
lbl = Label(window, text='PASSWORD STRENGTH TEST', font=("Arial", 25))
lbl.pack(pady=24)

lbl = Label(window, text='Enter your password', font='Bold')
lbl.pack(pady=24)

#Entry box
user_input = Entry(window, width=20, bg='White', fg='black')
user_input.pack(pady=0)

#Button
btn = Button(window, text = "Check", command = check, bg='White', fg='black')
btn.pack(pady=24)

#window closing
window.mainloop()
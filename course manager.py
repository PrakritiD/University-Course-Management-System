import tkinter
from tkinter import *
from tkinter import messagebx

#the command called when a submit button is pressed
def onSubmit():
    root.destroy()

#first tkinter window which asks user total credits needed and their current term
root = Tk()
credit_lbl = Label(root, text='Number of credits required to graduate:')
credit_ent = Entry(root)
curr_term_lbl = Label(root, text='Current term:')
curr_term_ent = Entry(root)
submit = Button(root, text='Submit', command=OnSubmit)

#the main tkinter window
root = Tk()
w = 300
h = 200
root.geometry("300x200")
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
pos_x = int(screen_w/2 - w/2)
pos_y = int(screen_h/2 - h/2)
root.geometry("+{}+{}".format(pos_x, pos_y))
root['bg'] = '#ffffff'

title = Label(root, text='Course Management System')
crse_num_lbl = Label(root, text='Enter course number')
crse_num_ent = Entry(root)
crse_name_lbl = Label(root, text='Enter course name')
crse_name_ent = Entry(root)
crse_term_lbl = Label(root, text='Enter term course is completed in or is planned to be completed in:')
crse_term_ent = Entry(root)
crse_deets = Label(root, text='Course Details')
table_term = Label(root, text='Term')
table_crse = Label(root, text='Course')
table_credit = Label(root, text='Credits')

#table showing data entered
update = Button(root, text='Update Course Details', command=update_list)
plan = Button(root, text='View plan', command=open_plan)
submit = Button(root,   text='Submit', command=OnSubmit)
crse_deets = Text(root)


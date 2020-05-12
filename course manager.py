import tkinter
from tkinter import *
from tkinter import messagebox

#the command called when a submit button is pressed
def on_submit():
    starter.destroy()

#first tkinter window which asks user total credits needed and their current term
starter = Tk()
starter['bg'] = '#ffffff'
credit_lbl = Label(starter, text='Number of credits required to graduate:', fg='#0d3163', bg='#ffffff')
credit_ent = Entry(starter, highlightbackground='#994203', highlightcolor='#0d3163',highlightthickness=1,relief=FLAT)
curr_term_lbl = Label(starter, text='Current term:', fg='#0d3163', bg='#ffffff')
curr_term_ent = Entry(starter, highlightbackground='#994203', highlightcolor='#0d3163',highlightthickness=1,relief=FLAT)
submit = Button(starter, text='Submit', command=on_submit,bg='#994203',fg='#ffffff',activebackground='#ffffff')

#organizing widgets on screen
credit_lbl.grid(padx=5, pady=3)
credit_ent.grid(row=0,column=1,padx=5, pady=3)
curr_term_lbl.grid(row=1,column=0,padx=5, pady=3)
curr_term_ent.grid(row=1,column=1,padx=5, pady=3)
submit.grid(row=2,column=0,columnspan=2,padx=5,pady=3)

#the command called when an exit button is pressed
def on_exit():
    root.destroy()

#the main tkinter window
root = Tk()
w = 1000
h = 600
#root.geometry("1000x600")
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
pos_x = int(screen_w/2 - w/2)
pos_y = int(screen_h/2 - h/2)
root.geometry("+{}+{}".format(pos_x, pos_y))
root['bg'] = '#ffffff'

title = Label(root, text='Course Management System', fg='#0d3163', bg='#ffffff', font = "Helvetica 22 bold", height=2)
crse_num_lbl = Label(root, text='Course Number:', fg='#0d3163', bg='#ffffff', font = "Helvetica 10 bold",width=15)
crse_num_ent = Entry(root, highlightbackground='#994203', highlightcolor='#0d3163',highlightthickness=1,relief=FLAT)
crse_name_lbl = Label(root, text='Course Name:', fg='#0d3163', bg='#ffffff', font = "Helvetica 10 bold",width=15)
crse_name_ent = Entry(root, highlightbackground='#994203', highlightcolor='#0d3163',highlightthickness=1,relief=FLAT)
crse_term_lbl = Label(root, text='Term:', fg='#0d3163', bg='#ffffff', font = "Helvetica 10 bold",width=15)
crse_term_ent = Entry(root, highlightbackground='#994203', highlightcolor='#0d3163',highlightthickness=1,relief=FLAT)

#table showing data entered
crse_deets_lbl = Label(root, text='Course Details:', fg='#994203', bg='#ffffff', font = "Helvetica 13 bold",width=15)
table_term = Label(root, text='Term', fg='#0d3163', bg='#ffffff', font = "Helvetica 10 bold",width=15)
table_crse = Label(root, text='Course', fg='#0d3163', bg='#ffffff', font = "Helvetica 10 bold",width=15)
table_credit = Label(root, text='Credits', fg='#0d3163', bg='#ffffff', font = "Helvetica 10 bold",width=15)
scroll = Scrollbar(root)
crse_deets_txt = Text(root, yscrollcommand = scroll.set, bg='#994203', fg='#ffffff',height=10,width=60,font = "Helvetica 10 bold")
scroll.config(command=crse_deets_txt.yview)

#buttons
#, command=update_list
#, command=open_plan
#
enter = Button(root, text='Update',width=15,bg='#0d3163',fg='#ffffff',activebackground='#ffffff', font = "Helvetica 10 bold")
save = Button(root, text='Update',width=15,bg='#0d3163',fg='#ffffff',activebackground='#ffffff', font = "Helvetica 10 bold")
#
update = Button(root, text='Update',width=15,bg='#0d3163',fg='#ffffff',activebackground='#ffffff', font = "Helvetica 10 bold")
plan = Button(root, text='View plan',width=15,bg='#0d3163',fg='#ffffff',activebackground='#ffffff', font = "Helvetica 10 bold")
exit_cmmd = Button(root, text='Exit', command=on_exit,width=15,bg='#0d3163',fg='#ffffff',activebackground='#ffffff', font = "Helvetica 10 bold")

empty1 = Label(root, text=' ', bg='#ffffff')
empty2 = Label(root, text=' ', bg='#ffffff')
empty3 = Label(root, text=' ', bg='#ffffff')
empty4 = Label(root, text=' ', bg='#ffffff')
empty4 = Label(root, text=' ', bg='#ffffff')

#organizing widgets on screen
empty1.grid(padx=5,pady=5)
title.grid(row=0, column=1, columnspan=7, padx=7)#, pady=5)
crse_num_lbl.grid(row=1, column=1, padx= 10, pady=5)
crse_num_ent.grid(row=1, column=2)#, padx=10, pady=7)
empty4.grid(row=2, padx=3,pady=1)
crse_name_lbl.grid(row=3, column=1, padx= 10, pady=5)
crse_name_ent.grid(row=3, column=2)#, padx= 5, pady=5)
crse_term_lbl.grid(row=4, column=1, padx= 10, pady=5)
crse_term_ent.grid(row=4, column=2)#, padx= 5, pady=5)
empty2.grid(row=2, column=3,padx=18,pady=5)
crse_deets_lbl.grid(row=1, column=4, pady=5)
table_term.grid(row=2, column=4)#, padx= 5, pady=5)
table_crse.grid(row=2, column=5)#, padx= 5, pady=5)
table_credit.grid(row=2, column=6)#, padx= 5, pady=5)
crse_deets_txt.grid(row=3, column=4, columnspan=3, rowspan=2)#, padx= 5, pady=5)
scroll.grid(row=3, column=7,rowspan=2)
empty3.grid(row=5,padx=5,pady=5)
update.grid(row=6, column=2, padx=5,columnspan=2)#, pady=5)
plan.grid(row=6, column=4)#, padx=5, pady=5)
exit_cmmd.grid(row=6, column=5)#, padx=5, pady=5)
empty4.grid(row=7,column=8,padx=5,pady=5)

mainloop()

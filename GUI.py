from tkinter import *
from finalSearcher import check
import webbrowser

#Opens the file in a new tab of the system's default browser
def open_url(f):
    fi = "file:///"+f
    webbrowser.open_new(fi)

#Removing Widgets of Frame2 and Frame3
def removeFrameWidgets():
    global no_label, time_label, search_label, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10
    no_label.pack_forget()
    time_label.pack_forget()
    search_label.pack_forget()
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    label4.pack_forget()
    label5.pack_forget()
    label6.pack_forget()
    label7.pack_forget()
    label8.pack_forget()
    label9.pack_forget()
    label10.pack_forget()

def startSearch():
    removeFrameWidgets()
    query = textbox.get().lower().strip()
    
    # replace non-alphanumeric with space and make a list
    # query=converter(query)    
    wordList=query.split()
    
    # If query is empty it will show 
    for i in query:
        if i == "":
            no_label.pack()
            return  
    links, time = check(wordList)

    #####========================= Setting Label Texts =================================#####
    time_label.config(text = "Time Taken: "+str(time)+" sec")
    label1.config(text = links[0])
    label2.config(text = links[1])
    label3.config(text = links[2])
    label4.config(text = links[3])
    label5.config(text = links[4])
    label6.config(text = links[5])
    label7.config(text = links[6])
    label8.config(text = links[7])
    label9.config(text = links[8])
    label10.config(text = links[9])

    #####================= Making Labels clickable to open the file =====================#####
    label1.bind("<Button-1>", lambda l: open_url(links[0]))
    label2.bind("<Button-1>", lambda l: open_url(links[1]))
    label3.bind("<Button-1>", lambda l: open_url(links[2]))
    label4.bind("<Button-1>", lambda l: open_url(links[3]))
    label5.bind("<Button-1>", lambda l: open_url(links[4]))
    label6.bind("<Button-1>", lambda l: open_url(links[5]))
    label7.bind("<Button-1>", lambda l: open_url(links[6]))
    label8.bind("<Button-1>", lambda l: open_url(links[7]))
    label9.bind("<Button-1>", lambda l: open_url(links[8]))
    label10.bind("<Button-1>", lambda l: open_url(links[9]))

    #####============ Label color Blue when mouse is on the label ========================#####
    label1.bind("<Enter>", lambda l: label1.config(fg = "blue"))
    label2.bind("<Enter>", lambda l: label2.config(fg = "blue"))
    label3.bind("<Enter>", lambda l: label3.config(fg = "blue"))
    label4.bind("<Enter>", lambda l: label4.config(fg = "blue"))
    label5.bind("<Enter>", lambda l: label5.config(fg = "blue"))
    label6.bind("<Enter>", lambda l: label6.config(fg = "blue"))
    label7.bind("<Enter>", lambda l: label7.config(fg = "blue"))
    label8.bind("<Enter>", lambda l: label8.config(fg = "blue"))
    label9.bind("<Enter>", lambda l: label9.config(fg = "blue"))
    label10.bind("<Enter>", lambda l: label10.config(fg = "blue"))

    #####============ Label color back to Black when Mouse is not on the label ============#####
    label1.bind("<Leave>", lambda l: label1.config(fg = "black"))
    label2.bind("<Leave>", lambda l: label2.config(fg = "black"))
    label3.bind("<Leave>", lambda l: label3.config(fg = "black"))
    label4.bind("<Leave>", lambda l: label4.config(fg = "black"))
    label5.bind("<Leave>", lambda l: label5.config(fg = "black"))
    label6.bind("<Leave>", lambda l: label6.config(fg = "black"))
    label7.bind("<Leave>", lambda l: label7.config(fg = "black"))
    label8.bind("<Leave>", lambda l: label8.config(fg = "black"))
    label9.bind("<Leave>", lambda l: label9.config(fg = "black"))
    label10.bind("<Leave>", lambda l: label10.config(fg = "black"))

    #####============ Displaying the Labels on the Frame 2&3 ============#####
    time_label.pack(pady=(10,15))
    search_label.pack(pady=(0,15))
    label1.pack(pady=(5,5))
    label2.pack(pady=(5,5))
    label3.pack(pady=(5,5))
    label4.pack(pady=(5,5))
    label5.pack(pady=(5,5))
    label6.pack(pady=(5,5))
    label7.pack(pady=(5,5))
    label8.pack(pady=(5,5))
    label9.pack(pady=(5,5))
    label10.pack(pady=(5,5))

# Main Window Initialization and Settings
main_window = Tk()
main_window.state('zoomed')
main_window.title('Google 2.0')
main_window.configure(background="#EFD451")

# Frames
frame1 = Frame(main_window)
frame2 = Frame(main_window)
frame3 = Frame(main_window)
frame1.configure(background="#EFD451")
frame2.configure(background="#EFD451")
frame3.configure(background="#EFD451")
frame1.pack()
frame2.pack()
frame3.pack()

# Frame 1 Widgets
mainlabel = Label(frame1, text="GOOGLE 2.0", bg="#EFD451", fg="#000000", font=('Bebas', 68 ,'bold'), justify=CENTER)  
search_button = Button(frame1, text="SEARCH", bg="#EFD451", bd=4, font=('Bebas', 15 ,'bold'), width=10, command=startSearch)  #adding search button
textbox = Entry(frame1, width=100, bd=3)   #textbox for adding input query

# Frame 2 Widgets
no_label = Label(frame2, text="Nothing Entered", bg="#EFD451", fg="black", font=('Ariel', 12), justify=CENTER)
time_label = Label(frame2, text="", bg="#EFD451", fg="black", font=('Ariel', 12), justify=CENTER)
search_label = Label(frame2, text="TOP 10 SEARCH RESULTS: ", bg="#EFD451", fg="#FFFFFF", font=('Bebas', 15), justify=LEFT)

# Frame 3 Widgets
label1=Label(frame3,text="", fg="black", bg="#EFD451", font=('Calibri', 12), justify=CENTER)
label2=Label(frame3,text="", fg="black", bg="#EFD451", font=('Calibri', 12), justify=CENTER)
label3=Label(frame3,text="", fg="black", bg="#EFD451", font=('Calibri', 12), justify=CENTER)
label4=Label(frame3,text="", fg="black", bg="#EFD451", font=('Calibri', 12), justify=CENTER)
label5=Label(frame3,text="", fg="black", bg="#EFD451", font=('Calibri', 12), justify=CENTER)
label6=Label(frame3,text="", fg="black", bg="#EFD451", font=('Calibri', 12), justify=CENTER)
label7=Label(frame3,text="", fg="black", bg="#EFD451", font=('Calibri', 12), justify=CENTER)
label8=Label(frame3,text="", fg="black", bg="#EFD451", font=('Calibri', 12), justify=CENTER)
label9=Label(frame3,text="", fg="black", bg="#EFD451", font=('Calibri', 12), justify=CENTER)
label10=Label(frame3,text="", fg="black", bg="#EFD451", font=('Calibri', 12), justify=CENTER)

# Displaying Frame 1 Widgets
mainlabel.pack(pady=60)
textbox.pack()
textbox.focus() #TO put the keyboard focus on the text box
search_button.pack()

main_window.mainloop()

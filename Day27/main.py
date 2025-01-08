from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# Entries
entry = Entry(width=7)
entry.grid(column=1, row=0)

# Labels
top_right_label = Label(text="Miles")
top_right_label.grid(column=2, row=0)

bottom_label = Label(text="0")
bottom_label.grid(column=1, row=1)

bottom_left_label = Label(text="is equal to")
bottom_left_label.grid(column=0, row=1)

bottom_right_label = Label(text="Km")
bottom_right_label.grid(column=2, row=1)


# Buttons
def action():
    distance_miles = float(entry.get())
    distance_km = round(distance_miles * 1.609)
    bottom_label["text"] = f"{distance_km}"


# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

window.mainloop()

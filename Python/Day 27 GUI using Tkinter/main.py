# import tkinter
#
# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
#
# # Label
#
# my_label = tkinter.Label(text="I am a winner", font=("Arial", 24, "bold"))
# my_label.pack()
#
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
#
#
# # Buttons
#
#
# def button_clicked():
#     print("I got clicked")
#     my_label.config(text=jeff.get())
#
#
# button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
#
#
# # Entry
# jeff = tkinter.Entry(width=10)
# jeff.pack()
# # print(jeff.get())
#
# window.mainloop()

# Mile to Kilometer converter program.

import tkinter


def mile_to_kilometer():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=90)
window.config(padx=20, pady=20)


miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="Is equal to.")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = tkinter.Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=mile_to_kilometer)
calculate_button.grid(column=1, row=2)


window.mainloop()

# import tkinter as tk
#
# def create_rounded_rectangle(canvas, x, y, width, height, radius, color):
#     x1, y1 = x, y
#     x2, y2 = x + width, y + height
#     canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="", tags="rounded")
#
#     # Draw arcs for rounded corners
#     canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.ARC, outline="", fill=color)
#     canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.ARC, outline="", fill=color)
#     canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.ARC, outline="", fill=color)
#     canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.ARC, outline="", fill=color)
#
# root = tk.Tk()
# root.title("Canvas with Rounded Rectangle")
# root.geometry("700x400")  # Adjust window size
#
# canvas_width = 680
# canvas_height = 365
# canvas_bg_color = "#FFE382"
# rounded_rect_width = 503
# rounded_rect_height = 239
# rounded_rect_radius = 26
# rounded_rect_x = 89
# rounded_rect_y = 27
# rounded_rect_color = "#FFAD84"
#
# canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg=canvas_bg_color)
# canvas.pack()
#
# create_rounded_rectangle(canvas, rounded_rect_x, rounded_rect_y, rounded_rect_width, rounded_rect_height, rounded_rect_radius, rounded_rect_color)
#
# root.mainloop()
#

import tkinter as tk
import pandas

print("Hi")
# Reading the CSV file which we had created and the content of file is french words with their english conversion. First column is Frnch words andd second column i English words. We wrote 30 French words in google sheets and applied the following formula =GOOGLETRANSLATE(A2,"fr","en") and dragged it to all the words of french words to generate the englsh conversion
try:
    file = pandas.read_csv("frenchEnglishWords.csv")
except NameError:
    print("The file which you had specified does not exist")
else:
    # Converting the CSV file in dictionary
    file_dict = {row.French: row.English for (index, row) in file.iterrows()}
    print(file_dict)

# ChatGPT generated code for UI
def create_rounded_rectangle(canvas, x, y, width, height, radius, color):
    x1, y1 = x, y
    x2, y2 = x + width, y + height
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="", tags="rounded")

    # Draw arcs for rounded corners
    canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, style=tk.ARC, outline="", fill=color)
    canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, style=tk.ARC, outline="", fill=color)
    canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, style=tk.ARC, outline="", fill=color)
    canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, style=tk.ARC, outline="", fill=color)

def create_rounded_button(canvas, x, y, width, height, radius, color, text):
    x1, y1 = x, y
    x2, y2 = x + width, y + height
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline="", tags="button")

    text_x = x + width / 2
    text_y = y + height / 2
    canvas.create_text(text_x, text_y, text=text, fill="white", font=("Arial", 20, "bold italic"))

root = tk.Tk()
root.title("Canvas with Rounded Shapes and Buttons")
root.geometry("700x500")  # Adjust window size

canvas_width = 680
canvas_height = 365
canvas_bg_color = "#FFE382"
rounded_rect_width = 503
rounded_rect_height = 239
rounded_rect_radius = 26
rounded_rect_x = 89
rounded_rect_y = 27
rounded_rect_color = "#FFAD84"

button1_width = 62
button1_height = 60
button1_x = 89
button1_y = 289
button1_color = "#E48F45"

button2_width = 62
button2_height = 60
button2_x = 530
button2_y = 291
button2_color = "#FF8F8F"

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg=canvas_bg_color)
canvas.pack()

create_rounded_rectangle(canvas, rounded_rect_x, rounded_rect_y, rounded_rect_width, rounded_rect_height, rounded_rect_radius, rounded_rect_color)

text1_x = rounded_rect_x + rounded_rect_width / 2
text1_y = rounded_rect_y + rounded_rect_height / 2
canvas.create_text(text1_x, text1_y, text="English", fill="white", font=("Arial", 40, "italic"))

text2_x = rounded_rect_x + rounded_rect_width / 2
text2_y = rounded_rect_y + 150  # Adjust y-coordinate for 'Request' text
canvas.create_text(text2_x, text2_y, text="Request", fill="white", font=("Arial", 50, "bold italic"))

create_rounded_button(canvas, button1_x, button1_y, button1_width, button1_height, 20, button1_color, "❌")
create_rounded_button(canvas, button2_x, button2_y, button2_width, button2_height, 20, button2_color, "✓")

root.mainloop()

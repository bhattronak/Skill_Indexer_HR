import tkinter as tk
from tkinter import filedialog
from score_func import rank_smi

def browse_button():
    global path
    path = filedialog.askdirectory()
    path_label.config(text="Directory path: " + path)

def calculate_scores():
    JD = JD_textbox.get('1.0', 'end-1c')
    scores = rank_smi(path, JD)
    output_textbox.delete('1.0', 'end')
    for phone_number, score in scores.items():
        output_textbox.insert('end', f"{phone_number}: {score}\n")
    output_textbox.tag_config('left', justify='left')
    output_textbox.tag_add('left', '1.0', 'end')

root = tk.Tk()
root.title("Resume Scoring")

# JD textbox
JD_label = tk.Label(root, text="Enter JD:")
JD_label.pack()
JD_textbox = tk.Text(root, height=10)
JD_textbox.pack()

# Browse button for directory path
path_label = tk.Label(root, text="")
path_label.pack()
browse_button = tk.Button(root, text="Browse", command=browse_button)
browse_button.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate scores", command=calculate_scores)
calculate_button.pack()

# Output textbox
output_label = tk.Label(root, text="Scores:")
output_label.pack()
output_textbox = tk.Text(root, height=20)
output_textbox.pack()

root.mainloop()

from ctypes import alignment
import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import os
from ttkthemes import ThemedStyle

def browse_for_batch_file():
    file_path = filedialog.askopenfilename(filetypes=[("Batch Files", "*.bat")])
    if file_path:
        entry_batch_file.delete(0, tk.END)
        entry_batch_file.insert(0, file_path)

def browse_for_project_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        entry_project_directory.delete(0, tk.END)
        entry_project_directory.insert(0, dir_path)

def process_batch_file():
    batch_file_path = entry_batch_file.get()
    project_directory = entry_project_directory.get()

    if not batch_file_path or not project_directory:
        # Provide a warning if either field is empty
        result_text.set("Please provide both batch file and project directory.")
        return

    try:
        # Run the batch file with the specified project directory
        batch_dir = os.path.dirname(os.path.abspath(batch_file_path))
        command = f'{batch_file_path} {project_directory}'
        subprocess.Popen(command, shell=True, cwd=batch_dir)
        result_text.set(f"✅ Batch file processed successfully. \n You can find it at .\{project_directory}")
    except Exception as e:
        # Print the error details
        print(f"Error processing batch file: {e}")
        result_text.set(f"❌ Error processing batch file. See console for details.")

# Create the main application window
app = tk.Tk()
app.title("Batch File Processor")

# Configure window attributes
app.geometry("450x250")  # Set initial size
app.resizable(False, False)  # Disable maximize

# Center the window on the screen
window_width = app.winfo_reqwidth()
window_height = app.winfo_reqheight()
position_right = int(app.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(app.winfo_screenheight() / 2 - window_height / 2)
app.geometry(f"+{position_right}+{position_down}")

style = ThemedStyle(app)
style.set_theme('radiance')

# Create and place widgets in the window
label_batch_file = tk.Label(app, text="Select Batch File:", font=("Arial", 10),justify="left")  # Adjust font size here
label_batch_file.grid(row=0, column=0, pady=5)

# Create an entry for displaying the selected batch file
entry_batch_file = tk.Entry(app, width=35, font=("Arial", 10))  # Adjust font size here
entry_batch_file.grid(row=0, column=1, pady=5)

# Create a button to browse for the batch file
button_browse_batch = tk.Button(app, text="Browse", command=browse_for_batch_file, font=("Arial", 10))  # Adjust font size here
button_browse_batch.grid(row=0, column=2, pady=5)

label_project_directory = tk.Label(app, text="Select Project Directory:", font=("Arial", 10),justify="left")  # Adjust font size here
label_project_directory.grid(row=1, column=0, pady=5)

# Create an entry for displaying the selected project directory
entry_project_directory = tk.Entry(app, width=35, font=("Arial", 10))  # Adjust font size here
entry_project_directory.grid(row=1, column=1, pady=5)

# Create a button to browse for the project directory
button_browse_project = tk.Button(app, text="Browse", command=browse_for_project_directory, font=("Arial", 10))  # Adjust font size here
button_browse_project.grid(row=1, column=2, pady=5)

button_process = tk.Button(app, text="Process Batch File", command=process_batch_file, font=("Arial", 12),highlightbackground="green")  # Adjust font size here
button_process.grid(row=2, column=0, columnspan=3, pady=10)

result_text = tk.StringVar()
label_result = tk.Label(app, textvariable=result_text, font=("Arial", 10))  # Adjust font size here
label_result.grid(row=3, column=0, columnspan=3, pady=10)

# Start the application
app.mainloop()

import tkinter as tk
from tkinter import ttk
import subprocess
import os
from ttkthemes import ThemedStyle

def update_combobox():
    # Get the list of batch files in the root directory
    batch_files_in_root = [f for f in os.listdir() if os.path.isfile(f) and f.lower().endswith('.bat')]
    # Update the combobox with the batch file list
    entry_batch_file['values'] = batch_files_in_root

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
        command = f'{batch_file_path} "{project_directory}"'
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
app.geometry("400x200")  # Set initial size
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
label_batch_file = tk.Label(app, text="Select Batch File:")
label_batch_file.grid(row=0, column=0, pady=5)

# Create a combobox with batch files in the root directory
entry_batch_file = ttk.Combobox(app, values=(), width=35)
entry_batch_file.grid(row=0, column=1, pady=5)

# Update the combobox with batch files in the root directory
update_combobox()

label_project_directory = tk.Label(app, text="Project Name:")
label_project_directory.grid(row=1, column=0, pady=5)

entry_project_directory = tk.Entry(app, width=40)
entry_project_directory.grid(row=1, column=1, pady=5)

button_process = tk.Button(app, text="Process Batch File", command=process_batch_file)
button_process.grid(row=2, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
res = ""
label_result = tk.Label(app, textvariable=result_text)
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Start the application
app.mainloop()

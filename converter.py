import tkinter as tk
from tkinter import filedialog, scrolledtext
from pydub import AudioSegment
import os
import threading  # Import threading


def convert_mp3_to_wav(input_paths, output_dir):
    """Converts multiple MP3 files to WAV files.

    Args:
        input_paths: A list of paths to the input MP3 files.
        output_dir:  The directory to save the output WAV files.
    """
    for input_path in input_paths:
        try:
            sound = AudioSegment.from_mp3(input_path)
            # Construct output filename:  basename + .wav
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            output_path = os.path.join(output_dir, base_name + ".wav")
            sound.export(output_path, format="wav")
            add_to_log(f"Converted: {input_path} -> {output_path}\n")  # Use add_to_log
        except Exception as e:
            add_to_log(f"Error converting {input_path}: {e}\n")  # Use add_to_log


def browse_input_files():
    filepaths = filedialog.askopenfilenames(
        filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")]
    )
    if filepaths:
        # Store the filepaths (don't clear previous ones).
        current_files = input_entry.get()
        if current_files:  # If there are already files listed...
            filepaths = current_files.split(";") + list(filepaths)  # ...combine them.
        input_entry.delete(0, tk.END)
        input_entry.insert(0, ";".join(filepaths))  # Use semicolon as separator


def browse_output_dir():
    dirpath = filedialog.askdirectory()
    if dirpath:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, dirpath)


def start_conversion():
    input_files_str = input_entry.get()
    output_dir = output_entry.get()

    if not input_files_str or not output_dir:
        add_to_log("Please select input files and an output directory.\n")
        return

    input_files = input_files_str.split(";")  # Split into a list of paths

    for input_file in input_files:
        if not os.path.exists(input_file):
          add_to_log(f"Input file: {input_file} does not exist.\n")
          return

    if not os.path.exists(output_dir):
        add_to_log(f"Output directory: {output_dir} does not exist.\n")
        return;


    # --- Threading ---
    convert_button.config(state=tk.DISABLED)  # Disable button during conversion
    thread = threading.Thread(target=conversion_thread, args=(input_files, output_dir))
    thread.start()


def conversion_thread(input_files, output_dir):
    """Handles the conversion in a separate thread."""
    try:
        convert_mp3_to_wav(input_files, output_dir)
    finally:
        # Re-enable the button, even if there's an error.  Use the GUI thread.
        root.after(0, lambda: convert_button.config(state=tk.NORMAL))


def add_to_log(message):
    """Adds a message to the log textbox."""
    log_text.insert(tk.END, message)
    log_text.see(tk.END)  # Scroll to the end


# --- GUI Setup ---
root = tk.Tk()
root.title("MP3 to WAV Converter")

# Input Files (Multiple selection)
input_label = tk.Label(root, text="Input MP3 Files:")
input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
input_button = tk.Button(root, text="Browse", command=browse_input_files)
input_button.grid(row=0, column=2, padx=5, pady=5)

# Output Directory
output_label = tk.Label(root, text="Output Directory:")
output_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=5, pady=5)
output_button = tk.Button(root, text="Browse", command=browse_output_dir)
output_button.grid(row=1, column=2, padx=5, pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=start_conversion)
convert_button.grid(row=2, column=1, pady=10)

# Log Textbox (ScrolledText)
log_label = tk.Label(root, text="Conversion Log:")
log_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
log_text = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD)
log_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()

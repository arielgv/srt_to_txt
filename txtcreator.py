import tkinter as tk
from tkinter import filedialog
import re

def load_srt_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("SRT files", "*.srt")])
    return file_path

def process_srt_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    pattern = re.compile(r'(\d+)\r?\n(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)\r?\n(.+?)\r?\n\r?\n', re.DOTALL)
    matches = pattern.findall(content)

    output_lines = []

    for match in matches:
        start_time = convert_time(match[1])
        end_time = convert_time(match[2])
        output_lines.append(f"start={start_time:.1f}s stop={end_time:.1f}s speaker_SPEAKER_")

    output_path = file_path.replace(".srt", "_output.txt")

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write('\n'.join(output_lines))

    print(f"Output file saved as: {output_path}")

def convert_time(time_string):
    hours, minutes, seconds_milliseconds = time_string.split(":")
    seconds, milliseconds = seconds_milliseconds.split(",")

    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000
    return total_seconds

if __name__ == "__main__":
    srt_file_path = load_srt_file()
    if srt_file_path:
        process_srt_file(srt_file_path)
    else:
        print("No file selected.")
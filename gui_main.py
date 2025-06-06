
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import threading
import sys
import queue


from login_module import automate_discord_login_flow
from open_server import click_div_with_data_list_item_id, click_channel_by_id
from spammer import spam_channel_with_message


active_driver = None


class QueueWriter:
    """A class to redirect stdout to a thread-safe queue."""

    def __init__(self, queue):
        self.queue = queue

    def write(self, text):
        self.queue.put(text)

    def flush(self):
        pass


def start_spam_process(server_id, channel_id, message):
    """The main logic that runs in a separate thread."""
    global active_driver
    discord_url = "https://discord.com/login"

    try:
        # --- Step 1: Login (gets credentials from .env) ---
        print("\nStarting the Discord login automation flow...")
        active_driver = automate_discord_login_flow(discord_url)

        if not active_driver:
            print("\nThe login automation flow failed.")
            messagebox.showerror("Error", "Login failed. Check the console output and your .env file.")
            return

        print("\nLogin successful.")

        # --- Step 2: Select Server ---
        print(f"\nAttempting to open Server '{server_id}'...")
        if not click_div_with_data_list_item_id(active_driver, server_id):
            print(f"Could not click Server '{server_id}'.")
            messagebox.showerror("Error", f"Server ID '{server_id}' not found.")
            if active_driver: active_driver.quit()
            return

        print("Server opened successfully.")

        # --- Step 3: Select Channel ---
        print(f"\nAttempting to open Channel '{channel_id}'...")
        if not click_channel_by_id(active_driver, channel_id):
            print(f"Could not click Channel '{channel_id}'.")
            messagebox.showerror("Error", f"Channel ID '{channel_id}' not found.")
            if active_driver: active_driver.quit()
            return

        print("Channel opened successfully.")

        # --- Step 4: Start Spamming ---
        print("\nStarting to spam...")
        spam_channel_with_message(active_driver, message)

    except Exception as e:
        print(f"An unexpected error occurred in the main process: {e}")
        messagebox.showerror("Unexpected Error", f"An error occurred:\n{e}")
    finally:
        if active_driver:
            print("Process finished. Closing browser.")
            active_driver.quit()
        messagebox.showinfo("Finished", "The process has finished and the browser has been closed.")
        spam_button.config(state=tk.NORMAL)


def on_spam_button_click():
    server_id = entry_server_id.get().strip()
    channel_id = entry_channel_id.get().strip()
    message = entry_message.get().strip()

    if not all([server_id, channel_id, message]):
        messagebox.showwarning("Missing Input", "Please fill in all fields!")
        return

    console_output.config(state=tk.NORMAL)
    console_output.delete('1.0', tk.END)
    console_output.config(state=tk.DISABLED)

    spam_button.config(state=tk.DISABLED)

    thread = threading.Thread(target=start_spam_process, args=(server_id, channel_id, message))
    thread.start()


# --- GUI Setup ---
root = tk.Tk()
root.title("Discord Spammer 1.0")
root.geometry("500x400")
root.resizable(False, False)

try:
    bg_image_pil = Image.open("discordspammer.png")
    bg_image = ImageTk.PhotoImage(bg_image_pil)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except FileNotFoundError:
    root.config(bg="black")

# --- Style Definitions ---
label_style = {'bg': 'black', 'fg': '#00FF00', 'font': ('Courier', 11, 'bold')}
entry_style = {'bg': '#333333', 'fg': 'white', 'font': ('Courier', 11), 'width': 12, 'bd': 1, 'relief': 'solid'}

# --- Labels and Entry Fields (Repositioned for 500x400 layout) ---
# Server ID
label_server_id = tk.Label(root, text="Server ID", **label_style)
label_server_id.place(x=20, y=80)
entry_server_id = tk.Entry(root, **entry_style)
entry_server_id.place(x=140, y=80)

# Channel ID
label_channel_id = tk.Label(root, text="Channel ID", **label_style)
label_channel_id.place(x=20, y=120)
entry_channel_id = tk.Entry(root, **entry_style)
entry_channel_id.place(x=140, y=120)

# Message
label_message = tk.Label(root, text="Message", **label_style)
label_message.place(x=20, y=160)
entry_message = tk.Entry(root, **entry_style)
entry_message.place(x=140, y=160)

# Spam Button
spam_button = tk.Button(
    root, text="Spam Now", font=('Courier', 12, 'bold'), bg='#00FF00', fg='black',
    command=on_spam_button_click, relief='raised', bd=2, width=20, height=1,
    activebackground='#333333', activeforeground='#00FF00'
)
spam_button.place(x=20, y=210)

# --- Console Output Area ---
console_output = ScrolledText(root, state='disabled', width=34, height=4, bg='black', fg='white', font=('Courier', 9))
console_output.place(x=20, y=260)

# --- Stdout Redirection and Queue Handling ---
log_queue = queue.Queue()
sys.stdout = QueueWriter(log_queue)


def check_queue():
    """Periodically check the queue for new messages and update the console output."""
    while not log_queue.empty():
        line = log_queue.get_nowait()
        console_output.config(state=tk.NORMAL)
        console_output.insert(tk.END, line)
        console_output.see(tk.END)
        console_output.config(state=tk.DISABLED)
    root.after(100, check_queue)


# Start polling the queue
root.after(100, check_queue)

# Start the GUI
root.mainloop()
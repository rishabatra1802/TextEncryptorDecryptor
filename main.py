import tkinter as tk
from tkinter import Text, Label, Entry, Button, Frame, StringVar, GROOVE, WORD, Toplevel, END, messagebox

# Simple Caesar Cipher encryption (shift by 4)
def caesar_encrypt(message):
    shift = 4
    result = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Vigenère Cipher encryption
def vigenere_encrypt(message, key):
    result = ""
    key = key.lower()
    key_len = len(key)
    for i, char in enumerate(message):
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[i % key_len]) - ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Railfence Cipher encryption
def railfence_encrypt(message, rails=3):
    if rails < 2:  # Ensure there are at least 2 rails
        raise ValueError("Number of rails must be at least 2.")
    
    result = [''] * rails  # Initialize the result list with 'rails' empty strings
    row, step = 0, 1

    for char in message:
        if char.isalpha():  # Only process alphabetical characters
            result[row] += char
            # Debugging line to see row and result at each step
            print(f"Row: {row}, Step: {step}, Result: {result}")
            
            # If we're at the top or bottom rail, we reverse the step (up or down)
            if row == 0 or row == rails - 1:
                step = -step
            row += step  # Move to the next row

    return ''.join(result)

# Playfair Cipher encryption
def playfair_encrypt(message, key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # Remove duplicates and preserve order
    message = message.replace('J', 'I')  # Treat J as I
    message_pairs = []
    i = 0
    while i < len(message):
        if i + 1 < len(message) and message[i] != message[i+1]:
            message_pairs.append(message[i:i+2])
            i += 2
        else:
            message_pairs.append(message[i] + 'X')
            i += 1
    result = ""
    for pair in message_pairs:
        result += pair  # Simple pass-through for demo
    return result

# Beaufort Cipher encryption
def beaufort_encrypt(message, key):
    result = ""
    key = key.lower()
    key_len = len(key)
    for i, char in enumerate(message):
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[i % key_len]) - ord('a')
            result += chr((shift_base + shift - ord(char)) % 26 + shift_base)
        else:
            result += char
    return result

# Autokey Cipher encryption
def autokey_encrypt(message, key):
    result = ""
    key = key.lower() + message.lower()
    key_len = len(key)
    for i, char in enumerate(message):
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[i]) - ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Function to handle encryption and decryption action
def process_action(action, selected_cipher):
    global screen, text1, code
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title(f"{action.capitalize()} {selected_cipher} Cipher")
        screen1.geometry("400x250")
        screen1.configure(bg="#00bd56" if action == "encrypt" else "#ed3833")

        message = text1.get(1.0, END).strip()
        if message:
            # Select the appropriate cipher and action
            if selected_cipher == "Caesar":
                result = caesar_encrypt(message) if action == "encrypt" else "Decryption logic here"
            elif selected_cipher == "Vigenère":
                result = vigenere_encrypt(message, "key") if action == "encrypt" else "Decryption logic here"
            elif selected_cipher == "Railfence":
                result = railfence_encrypt(message) if action == "encrypt" else "Decryption logic here"
            elif selected_cipher == "Playfair":
                result = playfair_encrypt(message, "key") if action == "encrypt" else "Decryption logic here"
            elif selected_cipher == "Beaufort":
                result = beaufort_encrypt(message, "key") if action == "encrypt" else "Decryption logic here"
            elif selected_cipher == "Autokey":
                result = autokey_encrypt(message, "key") if action == "encrypt" else "Decryption logic here"

            Label(
                screen1,
                text=f"{action.capitalize()}ED MESSAGE",
                font=("Arial", 14),
                fg="white",
                bg="#00BD56" if action == "encrypt" else "#ed3833"
            ).pack(pady=10)

            text2 = Text(screen1, font=("Roboto", 12), bg="white", relief=GROOVE, wrap=WORD, bd=1)
            text2.pack(padx=10, pady=10, fill="both", expand=True)
            text2.insert(END, result)
        else:
            messagebox.showerror(f"{action.capitalize()} Error", f"No message to {action}!")
    elif password == "":
        messagebox.showerror(f"{action.capitalize()} Error", "Input Password")
    else:
        messagebox.showerror(f"{action.capitalize()} Error", "Invalid Password")

# Create cipher selection window
def cipher_selection_window():
    global screen
    screen2 = Toplevel(screen)
    screen2.title("Select Cipher")
    screen2.geometry("300x200")
    
    Label(screen2, text="Select a Cipher:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

    # Buttons to select cipher
    Button(screen2, text="Caesar", font=("Arial", 12), command=lambda: cipher_action_window("Caesar")).pack(pady=5)
    Button(screen2, text="Vigenère", font=("Arial", 12), command=lambda: cipher_action_window("Vigenère")).pack(pady=5)
    Button(screen2, text="Railfence", font=("Arial", 12), command=lambda: cipher_action_window("Railfence")).pack(pady=5)
    Button(screen2, text="Playfair", font=("Arial", 12), command=lambda: cipher_action_window("Playfair")).pack(pady=5)
    Button(screen2, text="Beaufort", font=("Arial", 12), command=lambda: cipher_action_window("Beaufort")).pack(pady=5)
    Button(screen2, text="Autokey", font=("Arial", 12), command=lambda: cipher_action_window("Autokey")).pack(pady=5)

# Function to handle the action (Encrypt or Decrypt) after selecting a cipher
def cipher_action_window(selected_cipher):
    global screen
    screen2 = Toplevel(screen)
    screen2.title(f"{selected_cipher} Cipher Action")
    screen2.geometry("300x200")
    
    Label(screen2, text=f"Select Action for {selected_cipher} Cipher:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

    Button(screen2, text="Encrypt", font=("Arial", 12), command=lambda: process_action("encrypt", selected_cipher)).pack(pady=5)
    Button(screen2, text="Decrypt", font=("Arial", 12), command=lambda: process_action("decrypt", selected_cipher)).pack(pady=5)

# Main window to enter text and choose cipher
def main_scr():
    global screen, text1, code
    screen = tk.Tk()
    screen.geometry("500x550")
    screen.title("EncryDecryAPP")
    screen.config(bg="#f0f0f0")

    text_frame = Frame(screen, bg="white", bd=2, relief=GROOVE)
    text_frame.place(x=20, y=20, width=460, height=150)

    Label(
        text_frame, 
        text="Enter text to encrypt or decrypt:", 
        fg="black", 
        bg="white", 
        font=("Calibri", 15)
    ).pack(anchor="w", padx=10, pady=5)

    text1 = Text(
        text_frame,
        font=("Roboto", 12), 
        bg="white", 
        relief=GROOVE, 
        wrap=WORD, 
        bd=1
    )
    text1.pack(padx=10, pady=5, fill="both", expand=True)

    key_frame = Frame(screen, bg="#e0e0e0", bd=2, relief=GROOVE)
    key_frame.place(x=20, y=200, width=460, height=100)

    Label(
        key_frame, 
        text="Enter secret key:", 
        fg="black", 
        bg="#e0e0e0", 
        font=("Calibri", 15)
    ).pack(anchor="w", padx=10, pady=5)

    code = StringVar()
    Entry(
        key_frame, 
        textvariable=code, 
        width=22, 
        bd=1, 
        font=("Arial", 14)
    ).pack(padx=10, pady=5)

    Button(
        screen, 
        text="Choose Cipher", 
        bg="#4CAF50", 
        fg="white", 
        font=("Arial", 14),
        command=cipher_selection_window
    ).place(x=180, y=350, width=140, height=40)

    Button(
        screen,
        text="RESET",
        bg="#FF5722",
        fg="white",
        font=("Arial", 14),
        command=lambda: [text1.delete(1.0, "end"), code.set("")]
    ).place(x=180, y=420, width=120, height=40)

    screen.mainloop()

if __name__ == "__main__":
    main_scr()
    

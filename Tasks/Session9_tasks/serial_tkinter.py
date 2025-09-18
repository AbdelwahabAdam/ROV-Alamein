
from tkinter import *
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports

ser = None  # serial object
led_states = [0, 0, 0, 0]  # store LED states

def refresh_ports():
    ports = serial.tools.list_ports.comports()
    port_list = [p.device for p in ports]
    port_combo["values"] = port_list
    if port_list:
        port_combo.current(0)

def connect_port():
    global ser
    port = port_combo.get()
    if not port:
        messagebox.showerror("Error", "No COM port selected!")
        return
    try:
        ser = serial.Serial(port, 9600, timeout=1)
        messagebox.showinfo("Connected", f"Connected to {port}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def toggle_led(idx):
    led_states[idx] = 1 - led_states[idx]  # toggle 0/1
    buttons[idx].config(
        text=f"LED {idx+1}: {'ON' if led_states[idx] else 'OFF'}",
        bg="green" if led_states[idx] else "red"
    )

def send_frame():
    if ser is None or not ser.is_open:
        messagebox.showerror("Error", "Not connected to any port!")
        return
    frame = "*" + ",".join(str(x) for x in led_states) + "#"
    ser.write(frame.encode())
    print("Sent:", frame)

# --- GUI ---

# --- Simple Layout: All widgets in main window ---
window = Tk()
window.title("LED Controller (Arduino)")


# --- All widgets use grid on window ---
Label(window, text="Select Port:").grid(row=0, column=0, padx=5, pady=10, sticky="w")
port_combo = ttk.Combobox(window, width=15)
port_combo.grid(row=0, column=1, padx=5, pady=10)
Button(window, text="Refresh", command=refresh_ports).grid(row=0, column=2, padx=5, pady=10)
Button(window, text="Connect", command=connect_port).grid(row=0, column=3, padx=5, pady=10)

# LED buttons in a row on row 1
buttons = []
for i in range(4):
    btn = Button(window, text=f"LED {i+1}: OFF", width=15, height=2,
                bg="red", command=lambda i=i: toggle_led(i))
    btn.grid(row=1, column=i, padx=5, pady=20)
    buttons.append(btn)

# Send button below LED buttons, spanning all columns
Button(window, text="Send to Arduino", command=send_frame, width=20, height=2).grid(row=2, column=0, columnspan=4, pady=10)

# Load ports on startup
refresh_ports()

# Ensure serial port is closed on exit
def on_closing():
    global ser
    if ser is not None and ser.is_open:
        try:
            ser.close()
        except Exception:
            pass
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()

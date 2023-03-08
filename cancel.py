import keyboard
import psutil

# Define the hotkey to listen for
HOTKEY = 'F6'

# Define the function to terminate all running Python processes
def terminate_python_processes():
    for proc in psutil.process_iter():
        try:
            if 'python' in proc.name().lower():
                proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Register the hotkey listener
keyboard.add_hotkey(HOTKEY, terminate_python_processes)

# Start the keyboard event listener
keyboard.wait()

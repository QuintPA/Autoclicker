import pyautogui
import keyboard
from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Listener
import threading
import time
import sys

class AutoClicker:
    def __init__(self):
        self.running = False
        self.mouse = Controller()
        self.click_speed = 0.01
        self.target_x = None
        self.target_y = None
        self.use_current_position = True
        self.keys_to_press = ['a']
        self.listener = None
        self.click_thread = None
        
    def set_click_speed(self, speed):
        """Set clicking speed in seconds between clicks"""
        self.click_speed = speed
        
    def set_target_coordinates(self, x, y):
        """Set specific coordinates to click"""
        self.target_x = x
        self.target_y = y
        self.use_current_position = False
        print(f"Target coordinates set to: ({x}, {y})")
        
    def use_mouse_position(self):
        """Click at current mouse position"""
        self.use_current_position = True
        print("Will click at current mouse position")
        
    def set_keys(self, *keys):
        """Set multiple keys to press simultaneously"""
        self.keys_to_press = list(keys)
        print(f"Keys set to: {self.keys_to_press}")
        
    def click_loop(self):
        """Main clicking loop"""
        while self.running:
            try:
                if self.use_current_position:
                    self.mouse.click(Button.left, 1)
                else:
                    current_pos = self.mouse.position
                    self.mouse.position = (self.target_x, self.target_y)
                    self.mouse.click(Button.left, 1)
                    self.mouse.position = current_pos
                
                time.sleep(self.click_speed)
            except Exception as e:
                print(f"Error during clicking: {e}")
                self.stop()
    
    def press_keys_loop(self):
        """Press and hold multiple keys in a loop"""
        while self.running:
            try:
                for key in self.keys_to_press:
                    keyboard.press(key)
                
                time.sleep(self.click_speed / 2)
                
                for key in self.keys_to_press:
                    keyboard.release(key)
                
                time.sleep(self.click_speed / 2)
            except Exception as e:
                print(f"Error pressing keys: {e}")
                self.stop()
    
    def start(self, mode='click'):
        """Start the autoclicker"""
        if self.running:
            print("Autoclicker is already running!")
            return
        
        self.running = True
        print(f"\nAutoclicker started! ({mode} mode)")
        print("Press 'ESC' to stop\n")
        
        if mode == 'click':
            self.click_thread = threading.Thread(target=self.click_loop, daemon=False)
        elif mode == 'keys':
            self.click_thread = threading.Thread(target=self.press_keys_loop, daemon=False)
        else:
            print("Invalid mode!")
            self.running = False
            return
        
        self.click_thread.start()
    
    def stop(self):
        """Stop the autoclicker"""
        if self.running:
            self.running = False
            print("\nAutoclicker stopped!")
        else:
            print("Autoclicker is not running")


def print_menu():
    """Print the menu"""
    print("\n" + "="*50)
    print("AUTOCLICKER MENU")
    print("="*50)
    print("1. Start clicking (current position)")
    print("2. Start clicking (set coordinates)")
    print("3. Start pressing keys")
    print("4. Stop autoclicker")
    print("5. Set click speed")
    print("6. Set keys to press")
    print("7. Set target coordinates")
    print("8. Get current mouse position")
    print("9. Exit")
    print("="*50)


def get_current_position():
    """Get current mouse position"""
    try:
        pos = pyautogui.position()
        print(f"Current mouse position: X={pos[0]}, Y={pos[1]}")
        return pos
    except Exception as e:
        print(f"Error getting position: {e}")
        return None


def main():
    autoclicker = AutoClicker()
    
    print("\n" + "="*50)
    print("WELCOME TO AUTOCLICKER")
    print("="*50)
    print("Press 'ESC' at any time to stop the autoclicker")
    print("="*50)
    
    # Start ESC key listener in background thread
    def listen_for_escape():
        def on_press(key):
            try:
                if key == Key.esc:
                    autoclicker.stop()
            except AttributeError:
                pass
        
        with Listener(on_press=on_press) as listener:
            listener.join()
    
    escape_thread = threading.Thread(target=listen_for_escape, daemon=True)
    escape_thread.start()
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '1':
            autoclicker.use_mouse_position()
            autoclicker.start(mode='click')
        
        elif choice == '2':
            try:
                x = int(input("Enter X coordinate: "))
                y = int(input("Enter Y coordinate: "))
                autoclicker.set_target_coordinates(x, y)
                autoclicker.start(mode='click')
            except ValueError:
                print("Invalid input! Please enter numbers.")
        
        elif choice == '3':
            autoclicker.start(mode='keys')
        
        elif choice == '4':
            autoclicker.stop()
        
        elif choice == '5':
            try:
                speed = float(input("Enter click speed in seconds (e.g., 0.01 for 10ms): "))
                autoclicker.set_click_speed(speed)
                print(f"Click speed set to {speed} seconds")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        elif choice == '6':
            keys_input = input("Enter keys separated by commas (e.g., 'a, shift, w'): ")
            keys = [k.strip().lower() for k in keys_input.split(',')]
            autoclicker.set_keys(*keys)
        
        elif choice == '7':
            try:
                x = int(input("Enter X coordinate: "))
                y = int(input("Enter Y coordinate: "))
                autoclicker.set_target_coordinates(x, y)
            except ValueError:
                print("Invalid input! Please enter numbers.")
        
        elif choice == '8':
            get_current_position()
        
        elif choice == '9':
            autoclicker.stop()
            print("Exiting autoclicker. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAutoclicker closed.")
        sys.exit(0)

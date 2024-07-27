import sys
import time
from pynput import keyboard
from PIL import ImageGrab
import pyautogui
from pynput import mouse

class ScreenShotter:
    def __init__(self):
        self.running = True
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        try:
            if key == keyboard.Key.esc:
                print("Exiting...")
                self.running = False
                self.listener.stop()
                return False  # Para detener el listener
            elif key == keyboard.Key.ctrl_l:
                self.take_screenshot()
        except AttributeError:
            pass    
    def on_click(self, x, y, button, pressed):
        if pressed:
            # Guardar la posición inicial al presionar el botón del ratón
            self.x1, self.y1 = x, y
            print(f"Top-left corner: ({self.x1}, {self.y1})")
        else:
            # Guardar la posición final al soltar el botón del ratón
            self.x2, self.y2 = x, y
            print(f"Bottom-right corner: ({self.x2}, {self.y2})")
            # Terminar el listener
            return False

    def take_screenshot(self):
        try:
            print("Please select the area for screenshot.")
            # Crear un listener para el ratón
            with mouse.Listener(on_click=self.on_click) as listener:
                listener.join()

            if self.x1 != self.x2 and self.y1 != self.y2:
                bbox = (self.x1, self.y1, self.x2, self.y2)
                screenshot = ImageGrab.grab(bbox=bbox)
                screenshot.save("screenshot.png")
                print("Screenshot saved as screenshot.png")
            else:
                print("No valid area selected. Screenshot not taken.")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")

    def run(self):
            print("Press Ctrl+A to take a screenshot, Esc to exit.")
            while self.running:
                time.sleep(0.1)                  

if __name__ == "__main__":
    screen_shotter = ScreenShotter()
    screen_shotter.run()            
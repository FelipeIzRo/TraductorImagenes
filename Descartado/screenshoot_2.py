import pyautogui
from PIL import Image, ImageDraw,ImageGrab
import numpy as np
import cv2
from pynput import mouse
import time

class ScreenshotTaker:
    def __init__(self):
        self.x1, self.y1 = None, None
        self.x2, self.y2 = None, None
        self.listener = None

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

    def show_overlay(self):
        if self.x1 is not None and self.y1 is not None:
            # Capturar la pantalla
            screen = np.array(pyautogui.screenshot())
            # Convertir a imagen de PIL
            screen_img = Image.fromarray(screen)

            # Crear una imagen de capa de oscurecimiento
            overlay = Image.new('RGBA', screen_img.size, (0, 0, 0, 128))
            draw = ImageDraw.Draw(overlay)
            # Dibujar un rectángulo blanco transparente
            draw.rectangle([self.x1, self.y1, self.x2, self.y2], fill=(0, 0, 0, 0))

            # Combinar la imagen de la pantalla con la capa de oscurecimiento
            combined = Image.alpha_composite(screen_img.convert('RGBA'), overlay)
            # Convertir a una imagen de OpenCV para mostrarla
            cv_image = cv2.cvtColor(np.array(combined), cv2.COLOR_RGBA2BGR)

            # Mostrar la imagen con OpenCV
            cv2.imshow('Selection Area', cv_image)
            cv2.waitKey(1)

    def take_screenshot(self):
        try:
            print("Please select the area for screenshot.")
            # Crear un listener para el ratón
            with mouse.Listener(on_click=self.on_click) as listener:
                self.listener = listener
                listener.join()

            if self.x1 is not None and self.x2 is not None and self.y1 is not None and self.y2 is not None:
                if self.x1 != self.x2 and self.y1 != self.y2:
                    bbox = (self.x1, self.y1, self.x2, self.y2)
                    screenshot = ImageGrab.grab(bbox=bbox)
                    screenshot.save("screenshot.png")
                    print("Screenshot saved as screenshot.png")
                else:
                    print("No valid area selected. Screenshot not taken.")
            else:
                print("No valid area selected. Screenshot not taken.")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
        finally:
            # Cerrar la ventana de OpenCV si está abierta
            cv2.destroyAllWindows()

if __name__ == "__main__":
    taker = ScreenshotTaker()
    taker.take_screenshot()

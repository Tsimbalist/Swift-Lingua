import tkinter as tk
import mtranslate as mt
import keyboard

def SwiftLingua():
    try:
        selected_text = root.clipboard_get()
        translated_text = mt.translate(selected_text, 'en')

        translation_window = tk.Toplevel(root)
        translation_window.title("Swift Lingua")

        result_label = tk.Label(translation_window, text=translated_text, wraplength=400)
        result_label.pack(padx=10, pady=10)

        translation_window.lift()

    except Exception as e:
        translation_window = tk.Toplevel(root)
        translation_window.title("Swift Lingua")

        error_label = tk.Label(translation_window, text="Translation Error", wraplength=400)
        error_label.pack(padx=10, pady=10)

        translation_window.lift()

root = tk.Tk()
root.title("Swift Lingua")
root.withdraw()

keyboard.add_hotkey('ctrl+alt+t', SwiftLingua)

root.mainloop()

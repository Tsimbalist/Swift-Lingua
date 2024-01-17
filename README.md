# Swift Lingua

Swift Lingua is a simple Python utility that allows users to translate selected text from the clipboard using a keyboard shortcut. It utilizes the `mtranslate` library for translation and the `keyboard` library for handling hotkeys.

## Usage

1. Copy the text you want to translate.
2. Press `Ctrl+Alt+T` to initiate the translation.

## Configuration

### Language Settings

By default, the translation is from the clipboard text language to English. If you want to change the target language, modify the following line in the code:

   ```python
   translated_text = mt.translate(selected_text, 'en')
   ```
Replace 'en' with the desired language code (e.g., 'ru' for Russian).

### Keyboard Shortcut
To change the keyboard shortcut, update the following line in the code:

   ```python
   keyboard.add_hotkey('ctrl+alt+t', SwiftLingua)
   ```
Replace 'ctrl+alt+t' with your preferred keyboard shortcut combination.

## Installation

1. Make sure you have Python installed (recommended version 3.6 and above).
2. Clone the repository:

   ```bash
   git clone https://github.com/Tsimbalist/Swift-Lingua.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Swift-Lingua
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage
![Example Tutorial](tutorial.gif)

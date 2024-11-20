# Matrix Screensaver

This repository contains a Python-based "Matrix" screensaver that can be set up as an actual screensaver on your computer. The screensaver mimics the falling green text effect seen in "The Matrix" movies and activates after user inactivity.

---

## Features
- **Dynamic Falling Text:** Random characters cascading down the screen.
- **Customizable Settings:** Adjust frame rate, text size, color, and more.
- **Screensaver Mode:** Automatically starts after user inactivity and exits on any keyboard or mouse activity.

---

## Supported Platforms
- **Windows** (Tested on Windows 10/11)
- **MacOS** (with some manual steps)
- **Linux** (Tested on Ubuntu, requires additional steps for screensaver integration)

---

## Prerequisites
- **Python 3.8 or newer** (Ensure Python is installed on your system)
- Required Python libraries:
  - `pygame`

Install dependencies by running:
```bash
pip install pygame
```

---

## Setup Instructions

### For Windows
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ADISHA2003/python_matrix_screensaver.git
   cd matrix-screensaver
   ```

2. **Convert the Script to an Executable**:
   - Install PyInstaller:
     ```bash
     pip install pyinstaller
     ```
   - Create an executable:
     ```bash
     pyinstaller --onefile --windowed matrix_screensaver.py
     ```
   - The executable will be located in the `dist` folder.

3. **Rename the Executable**:
   - Rename the file to `matrix_screensaver.scr`.

4. **Move the `.scr` File**:
   - Copy the renamed file to the `C:\Windows\System32` directory:
     1. Open the `dist` folder in File Explorer.
     2. Right-click the `.scr` file and select **Copy**.
     3. Navigate to `C:\Windows\System32` and paste the file (you may need administrative permissions).

5. **Set Up as a Screensaver**:
   - Open **Control Panel** > **Appearance and Personalization** > **Change screen saver**.
   - Select `matrix_screensaver` from the dropdown menu and click **Apply**.

---

### For MacOS
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ADISHA2003/python_matrix_screensaver.git
   cd matrix-screensaver
   ```

2. **Install Dependencies**:
   ```bash
   pip install pygame
   ```

3. **Run the Screensaver**:
   - Start the script manually:
     ```bash
     python3 matrix_screensaver.py
     ```
   - For an automatic screensaver:
     - Use a third-party app like **SaveHollywood** to run Python-based screensavers.
     - Save the executable version of the script and use it as the screensaver source.

---

### For Linux
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ADISHA2003/python_matrix_screensaver.git
   cd matrix-screensaver
   ```

2. **Install Dependencies**:
   ```bash
   pip install pygame
   ```

3. **Run the Screensaver**:
   - Start the script manually:
     ```bash
     python3 matrix_screensaver.py
     ```

4. **Set Up as a Screensaver**:
   - Use tools like **xscreensaver** or **gnome-screensaver**:
     - Add the script or executable as a custom screensaver option.

---

## Customization
- **Adjustable Parameters**:
  - Edit the `state` dictionary in the `matrix_screensaver.py` file to modify:
    - `fps`: Frames per second.
    - `color`: Text color (RGB values).
    - `charset`: Characters to display.
    - `size`: Font size.
    - `fadeEffect`: Enable or disable fading.

---

## Contributing
Feel free to submit pull requests to enhance functionality or compatibility for more platforms.
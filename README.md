# Color Picker

Color Picker is a Python application that allows users to choose a color and copy its hexadecimal and RGB values. The application is built using the PyQt5 library.

## Table of Contents
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Usage

Follow these steps to use the Color Picker application:

1. **Prerequisites**: Make sure you have Python installed on your system.

2. **Install PyQt5**: If you haven't already, install the PyQt5 library by running the following command:

    ```shell
    pip install PyQt5
    ```


3. **Run the Application**:
- Create a Python file, for example, `ColorPicker.py`.
- Copy the provided Python code into the `ColorPicker.py` file.

4. **Execute the Application**: Open your terminal or command prompt, navigate to the directory containing `ColorPicker.py`, and run the following command:

    ```python
    python ColorPicker.py
    ```


5. **Use the Color Picker**:
- The Color Picker window will open.
- Click on the color field to open a color picker dialog.
- Choose a color from the dialog, and the selected color will be displayed in the color field.
- The hexadecimal value of the selected color will be displayed below the color field.
- The RGB value of the selected color will also be displayed below the color field.
- Click the "Kopieren (Hex)" (Copy Hex) button to copy the hexadecimal value to the clipboard.
- Click the "Kopieren (RGB)" (Copy RGB) button to copy the RGB value to the clipboard.

6. **Save Changes Prompt**: If you make any changes to the color and attempt to close the window, a prompt will appear, asking if you want to save the changes.

## Dependencies

The following dependency is required to run the Color Picker:

- PyQt5

Make sure to install PyQt5 using the provided instructions in the Usage section.

## License

This project is licensed under the [MIT License](LICENSE).

# Import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QColorDialog, QMessageBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

# Define a class to create the GUI
class ColorPickerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Farbwähler")  # Set the window title
        self.setGeometry(100, 100, 400, 300)  # Set the window size and position

        central_widget = QWidget()  # Create a central widget
        self.setCentralWidget(central_widget)  # Set the central widget

        layout = QVBoxLayout()  # Create a vertical layout
        central_widget.setLayout(layout)  # Set the layout for the central widget

        # Create a label to display text
        self.color_label = QLabel(central_widget)
        self.color_label.setText("Klicken Sie auf das Farbfeld, um eine Farbe auszuwählen")  # Set the text for the label
        self.color_label.setAlignment(Qt.AlignCenter)  # Set the alignment for the label
        layout.addWidget(self.color_label)  # Add the label to the layout

        # Create a button to choose a color
        self.color_button = QPushButton(central_widget)
        self.color_button.setStyleSheet("background-color: #FFFFFF")  # Set the background color of the button
        self.color_button.setFixedSize(375, 150)  # Set the size of the button
        self.color_button.clicked.connect(self.choose_color)  # Connect the button to the choose_color method
        layout.addWidget(self.color_button)  # Add the button to the layout

        # Create a label to display the selected color in hexadecimal format
        self.hex_label = QLabel(central_widget)
        self.hex_label.setAlignment(Qt.AlignCenter)  # Set the alignment for the label
        layout.addWidget(self.hex_label)  # Add the label to the layout

        # Create a label to display the selected color in RGB format
        self.rgb_label = QLabel(central_widget)
        self.rgb_label.setAlignment(Qt.AlignCenter)  # Set the alignment for the label
        layout.addWidget(self.rgb_label)  # Add the label to the layout

        # Create a button to copy the selected color's hexadecimal code to the clipboard
        self.copy_hex_button = QPushButton(central_widget)
        self.copy_hex_button.setText("Kopieren (Hex)")  # Set the text for the button
        self.copy_hex_button.clicked.connect(self.copy_hex)  # Connect the button to the copy_hex method
        layout.addWidget(self.copy_hex_button)  # Add the button to the layout

        # Create a button to copy the selected color's RGB code to the clipboard
        self.copy_rgb_button = QPushButton(central_widget)
        self.copy_rgb_button.setText("Kopieren (RGB)")  # Set the text for the button
        self.copy_rgb_button.clicked.connect(self.copy_rgb)  # Connect the button to the copy_rgb method
        layout.addWidget(self.copy_rgb_button)  # Add the button to the layout

        # Add a variable to track whether the color has been changed or not
        self.color_changed = False

    # Define a method to choose a color using a QColorDialog
    def choose_color(self):
        color = QColorDialog.getColor()  # Open a QColorDialog to choose a color
        if color.isValid():
            self.color_button.setStyleSheet("background-color: " + color.name())  # Set the background color of the button to the chosen color
            self.hex_label.setText(color.name())  # Display the chosen color in hexadecimal format
            self.rgb_label.setText(f"RGB: {color.red()}, {color.green()}, {color.blue()}") 
            self.color_changed = True  # Set the variable to True when the color is changed

    # Define a method to copy the hexadecimal code to the clipboard
    def copy_hex(self):
        color = self.color_button.palette().button().color().name()  # Get the color from the button's palette
        QApplication.clipboard().setText(color)  # Copy the color to the clipboard

    # Define a method to copy the RGB code to the clipboard
    def copy_rgb(self):
        color = self.color_button.palette().button().color()  # Get the color from the button's palette
        rgb_code = f"RGB: {color.red()}, {color.green()}, {color.blue()}"  # Create the RGB code
        QApplication.clipboard().setText(rgb_code)  # Copy the RGB code to the clipboard

    # Override the closeEvent method to prompt the user before closing the window
    def closeEvent(self, event):
        if self.color_changed:
            reply = QMessageBox.question(self, "Save changes?", "Do you want to save your changes?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # Show a QMessageBox to prompt the user to save changes
            if reply == QMessageBox.Yes:
                event.ignore()  # Ignore the close event if the user chooses to save
            elif reply == QMessageBox.No:       
                event.accept()    # Accept the close event if the user chooses to not save
            else:
                pass
        else:
            event.accept()  # Accept the close event if the user chooses to close the window


if __name__ == "__main__":  # If the file is executed directly
    app = QApplication(sys.argv)    # Create a QApplication
    picker = ColorPickerGUI()    # Create an instance of the ColorPickerGUI class
    picker.show()           # Show the GUI
    sys.exit(app.exec_())    # Run the application

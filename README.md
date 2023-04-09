# Color-Picker

Dieses Programm ist ein einfaches GUI-Tool zum Auswählen und Kopieren von Farbcodes.

Installation:

Dieses Programm benötigt Python 3 und die folgenden Bibliotheken: tkinter, tkinter.colorchooser.
Die Bibliotheken können mit pip installiert werden:
pip install tkinter
pip install tkcolorpicker

Verwendung:

Führen Sie das Programm aus, indem Sie "python color_picker.py" in der Kommandozeile eingeben.
Klicken Sie auf das Farbfeld, um das Farbauswahlfenster zu öffnen.
Wählen Sie eine Farbe aus dem Farbauswahlfenster aus. Die ausgewählte Farbe wird im Farbfeld angezeigt und der Hex-Code wird unter dem Feld angezeigt.
Klicken Sie auf die Schaltfläche "Kopieren", um den Hex-Code in die Zwischenablage zu kopieren.

Code-Erklärung:

Die Klasse ColorPickerGUI ist der Hauptteil des Programms. Es erstellt ein Fenster mit einem Farbfeld, einem Label zur Anzeige des Hex-Codes der ausgewählten Farbe und einer Schaltfläche zum Kopieren des Hex-Codes.
Die Methode choose_color wird aufgerufen, wenn das Farbfeld geklickt wird. Es öffnet ein Farbauswahlfenster und aktualisiert das Farbfeld und das Label mit der ausgewählten Farbe und dem Hex-Code.
Die Methode copy_hex wird aufgerufen, wenn die Schaltfläche "Kopieren" geklickt wird. Es kopiert den Hex-Code in die Zwischenablage des Betriebssystems.

!!Hinweis:

Das Programm verwendet das Modul tkinter.colorchooser zur Erstellung des Farbauswahlfensters.

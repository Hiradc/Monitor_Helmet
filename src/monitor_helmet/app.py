"""
Let's analyse your vertigo
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Monitor_Helmet(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(
            style=Pack(direction=COLUMN, padding=10, alignment="center")
        )

        self.my_label = toga.Label(
            "Monitor Helmet",
            style=Pack(padding=(0, 5), font_size=20, text_align="center"),
        )

        self.my_button = toga.Button(
            "Start Monitoring",
           # on_press=self.start_monitoring,
            style=Pack(padding=5, font_size=15),
        )
        
        self.my_button2 = toga.Button(
            "Show Data",
            #on_press=self.show_data,
            style=Pack(padding=5, font_size=15),
        )

        def start_monitoring(widget):
            self.my_label.text = "Monitoring started..."
            # Here you would add the code to start monitoring

        def show_data(widget):
            self.my_label.text = "Showing data..."
            # Here you would add the code to show data

        main_box.add(self.my_label)
        main_box.add(self.my_button)
        main_box.add(self.my_button2)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Monitor_Helmet()

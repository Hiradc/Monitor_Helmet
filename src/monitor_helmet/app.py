import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import cv2
import time


class Monitor_Helmet(toga.App):
    def startup(self):
        main_box = toga.Box(
            style=Pack(direction=COLUMN, padding=10, alignment="center")
        )

        self.my_label = toga.Label(
            "Monitor Helmet",
            style=Pack(padding=(0, 5), font_size=20, text_align="center"),
        )

        self.my_button = toga.Button(
            "Start Monitoring",
            on_press=self.start_monitoring,
            style=Pack(padding=5, font_size=15),
        )

        self.my_button2 = toga.Button(
            "Show Data",
            on_press=self.show_data,
            style=Pack(padding=5, font_size=15),
        )

        self.import_button = toga.Button(
            "Importer une vidéo",
            on_press=self.import_video,
            style=Pack(padding=5, font_size=15),
    )       

        main_box.add(self.my_label)
        main_box.add(self.import_button)
        main_box.add(self.my_button)
        main_box.add(self.my_button2)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        
    def start_monitoring(self, widget):
        self.my_label.text = "Recording video..."
        capture_video()
        self.my_label.text = "Done recording."


    def show_data(self, widget):
        self.my_label.text = "Showing data..."
        # TODO: afficher des données

    def capture_video():
        cap = cv2.VideoCapture(0)  # 0 = webcam par défaut

        if not cap.isOpened():
            print("Erreur : impossible d'accéder à la webcam.")
            return

        # Définir l'enregistreur vidéo (format AVI, codec XVID)
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

        print("📹 Enregistrement démarré pour 8 secondes...")
        start_time = time.time()

        while time.time() - start_time < 8:
            ret, frame = cap.read()
            if not ret:
                print("Erreur : pas de frame.")
                break
            out.write(frame)
            cv2.imshow("Enregistrement", frame)

            # Quitter si 'q' est pressé
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        print("✅ Enregistrement terminé. Fichier : output.avi")

        
    def import_video(self, widget):
    # Ouvre un explorateur de fichiers pour choisir une vidéo
        file = self.main_window.open_file_dialog(
            title="Sélectionner une vidéo",
            file_types=[".mp4", ".avi", ".mov"]
        )

        if file:
            self.my_label.text = f"Vidéo sélectionnée : {file.path}"
            # 🔁 Ici tu pourrais lancer un traitement, une lecture, etc.
        else:
            self.my_label.text = "Aucune vidéo sélectionnée."

        



def main():
    return Monitor_Helmet()

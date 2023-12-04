import tkinter as tk
from rocket_scorer import RocketScorer

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.scorer = RocketScorer()

        self.weight_entry = self.create_entry("Rocket weight at liftoff (grams)")
        self.length_entry = self.create_entry("Rocket length (millimeters)")
        self.upper_diameter_entry = self.create_entry("Upper body tube diameter (inches)")
        self.lower_diameter_entry = self.create_entry("Lower body tube diameter (inches)")
        self.altitude_entry = self.create_entry("Rocket altitude (feet)")
        self.duration_entry = self.create_entry("Rocket duration (seconds)")

        self.calculate_button = tk.Button(self)
        self.calculate_button["text"] = "Calculate"
        self.calculate_button["command"] = self.calculate_score
        self.calculate_button.grid()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid()

        self.score_label = tk.Label(self)
        self.score_label.grid()

    def create_entry(self, text):
        label = tk.Label(self, text=text)
        label.grid()
        entry = tk.Entry(self)
        entry.grid()
        return entry

    def calculate_score(self):
        weight = float(self.weight_entry.get())
        length = float(self.length_entry.get())
        upper_diameter = float(self.upper_diameter_entry.get())
        lower_diameter = float(self.lower_diameter_entry.get())
        altitude = float(self.altitude_entry.get())
        duration = float(self.duration_entry.get())

        score = self.scorer.calculate_total_score(duration, altitude)

        self.score_label["text"] = f"Rocket Score: {score}"

root = tk.Tk()
root.title("CVHS")
app = Application(master=root)
app.mainloop()
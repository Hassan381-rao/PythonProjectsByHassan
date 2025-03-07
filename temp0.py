import tkinter as tk
from tkinter import messagebox

class WeatherRecord:
    def __init__(self, date, temperature, humidity):
        self.date = date
        self.temperature = temperature
        self.humidity = humidity

    def __str__(self):
        return f"{self.date}: Temp={self.temperature}°C, Humidity={self.humidity}%"

class WeatherData:
    def __init__(self):
        self.records = []

    def add_record(self, date, temperature, humidity):
        record = WeatherRecord(date, temperature, humidity)
        self.records.append(record)

    def get_all_records(self):
        return "\n".join(str(record) for record in self.records)

    def calculate_average(self):
        if not self.records:
            return None, None

        total_temp = 0
        total_humidity = 0
        count = len(self.records)

        for record in self.records:
            total_temp += record.temperature
            total_humidity += record.humidity

        avg_temp = total_temp / count
        avg_humidity = total_humidity / count

        return avg_temp, avg_humidity

class WeatherApp:
    def __init__(self, root):
        self.weather_data = WeatherData()

        # Create and place widgets
        tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
        tk.Label(root, text="Temperature (°C):").grid(row=1, column=0)
        tk.Label(root, text="Humidity (%):").grid(row=2, column=0)

        self.date_entry = tk.Entry(root)
        self.temp_entry = tk.Entry(root)
        self.humidity_entry = tk.Entry(root)

        self.date_entry.grid(row=0, column=1)
        self.temp_entry.grid(row=1, column=1)
        self.humidity_entry.grid(row=2, column=1)

        tk.Button(root, text="Add Record", command=self.add_record).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Display Records", command=self.display_records).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Calculate Averages", command=self.calculate_average).grid(row=5, column=0, columnspan=2)

        self.records_text = tk.Text(root, height=10, width=50)
        self.records_text.grid(row=6, column=0, columnspan=2)

    def add_record(self):
        date = self.date_entry.get()
        try:
            temperature = float(self.temp_entry.get())
            humidity = float(self.humidity_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Temperature and Humidity must be numbers.")
            return

        self.weather_data.add_record(date, temperature, humidity)
        messagebox.showinfo("Record Added", "Weather record added successfully!")

        # Clear the entry fields
        self.date_entry.delete(0, tk.END)
        self.temp_entry.delete(0, tk.END)
        self.humidity_entry.delete(0, tk.END)

    def display_records(self):
        records = self.weather_data.get_all_records()
        self.records_text.delete(1.0, tk.END)
        self.records_text.insert(tk.END, records)

    def calculate_average(self):
        avg_temp, avg_humidity = self.weather_data.calculate_average()
        if avg_temp is None:
            messagebox.showinfo("Average Weather Data", "No records to calculate averages.")
        else:
            avg_info = (f"Average Temperature: {avg_temp:.2f}°C\n"
                        f"Average Humidity: {avg_humidity:.2f}%")
            messagebox.showinfo("Average Weather Data", avg_info)

# Create the main window
root = tk.Tk()
root.title("Weather Data Analysis")

# Create and run the application
app = WeatherApp(root)
root.mainloop()

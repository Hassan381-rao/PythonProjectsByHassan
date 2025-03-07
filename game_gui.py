import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Choose correct option.")
        root.configure(bg="Sky Blue")
        
        self.questions = [
            ("Who is the fastest bowler of the Pakistani cricket team?", ["Imran Khan", "Babar Azam", "Shoaib Akhtar", "Rizwan"], "Shoaib Akhtar"),
            ("What is the most famous programming language?", ["C#", "CSS", "Java", "Python"], "Python"),
            ("Which is the highest building in the world?", ["Heydar Aliyev Center", "Bilbao Guggenheim Museum", "Burj Khalifa", "Hagia Sophia"], "Burj Khalifa"),
            ("Which one is not a programming language?", ["C#", "Java", "Python", "H++"], "H++"),
            ("Complete the sentence: If you had let me know earlier, I ___ have been able to come.", ["should", "would", "could", "might"], "would")
        ]

        
        self.total_points = 0
        self.current_question = 0

        
        self.question_label = tk.Label(root, text=self.questions[self.current_question][0],bg="Sky Blue")
        self.question_label.pack()

        self.selected_option = tk.StringVar()

        self.radio_buttons = []
        for option in self.questions[self.current_question][1]:
            rb = tk.Radiobutton(root, text=option, variable=self.selected_option, value=option,bg="Sky Blue")
            rb.pack()
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer,bg="Sky Blue")
        self.submit_button.pack()

    def check_answer(self):
        user_answer = self.selected_option.get().strip().lower()
        correct_answer = self.questions[self.current_question][2].lower()

        if user_answer == correct_answer:
            self.total_points += 5

        
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.question_label.config(text="Quiz completed! Total points: " + str(self.total_points))
            self.submit_button.config(state=tk.DISABLED)

    def update_question(self):
        self.question_label.config(text=self.questions[self.current_question][0])
        options = self.questions[self.current_question][1]
        for i, option in enumerate(options):
            self.radio_buttons[i].config(text=option, value=option)
        self.selected_option.set("")  

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

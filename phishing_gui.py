import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from phishing_data import EMAIL_EXAMPLES, QUIZ_QUESTIONS


class PhishingAwarenessGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Awareness Simulation Tool")
        self.root.geometry("900x650")

        self.quiz_index = 0
        self.score = 0

        title = tk.Label(
            root,
            text="Phishing Awareness Simulation Tool",
            font=("Arial", 18, "bold")
        )

        title.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack()

        tk.Button(
            button_frame,
            text="View Examples",
            command=self.show_examples
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            button_frame,
            text="Take Quiz",
            command=self.start_quiz
        ).pack(side=tk.LEFT, padx=5)

        self.text_area = tk.Text(root, wrap="word")
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)

    def show_examples(self):
        self.text_area.delete("1.0", tk.END)

        for item in EMAIL_EXAMPLES:
            self.text_area.insert(
                tk.END,
                f"\n=== {item['title']} ===\n\n"
            )

            self.text_area.insert(
                tk.END,
                item["email"] + "\n"
            )

            self.text_area.insert(
                tk.END,
                "\nRed Flags:\n"
            )

            for tactic in item["tactics"]:
                self.text_area.insert(
                    tk.END,
                    f" - {tactic}\n"
                )

            self.text_area.insert(
                tk.END,
                "\n" + "=" * 60 + "\n"
            )

    def start_quiz(self):
        self.quiz_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):

        if self.quiz_index >= len(QUIZ_QUESTIONS):

            messagebox.showinfo(
                "Quiz Complete",
                f"Score: {self.score}/{len(QUIZ_QUESTIONS)}"
            )

            return

        q = QUIZ_QUESTIONS[self.quiz_index]

        quiz_window = tk.Toplevel(self.root)
        quiz_window.title("Quiz Question")

        tk.Label(
            quiz_window,
            text=q["question"],
            wraplength=400
        ).pack(pady=10)

        def submit(ans):

            if ans == q["answer"]:
                self.score += 1

            quiz_window.destroy()

            self.quiz_index += 1

            self.show_question()

        tk.Button(
            quiz_window,
            text="Phishing",
            command=lambda: submit("phishing")
        ).pack(pady=5)

        tk.Button(
            quiz_window,
            text="Legitimate",
            command=lambda: submit("legitimate")
        ).pack(pady=5)


root = tk.Tk()
app = PhishingAwarenessGUI(root)
root.mainloop()

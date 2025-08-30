
import random
from time import time
import tkinter as tk
import tkinter.ttk as ttk

#sample test list
texts= [
    "the quick brown fox jumps over the lazy dog",
    "python is a verstile and poweful programming language ",
    "hahaha guess what i am programmer " ,
    "you have speed you so good"
]
class TypingSpeedTestApp:
    def __init__(self , root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.sample_text = random.choice(texts)
        self.start_time = None
        # UI Elements
        self.label = tk.Label(self.root, text="Type the text below " , font=("Arial", 15))
        self.label.pack(pady=10)

        self.text_label = tk.Label(self.root, text=self.sample_text, font=("Arial", 13), wraplength=400)
        self.text_label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 13), width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)
        self.entry.bind("<Return>", self.check_result)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 13))
        self.result_label.pack(pady=10)

        self.rest_button = tk.Button(self.root, text="Rest", command=self.rest)
        self.rest_button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is  None:
            self.start_time = time()
    def check_result(self,event):
        end_time = time()
        typed_text = self.entry.get()
        time_taken = end_time - self.start_time
        words = len(typed_text.split())
        wpm = (words / time_taken) * 60 if time_taken > 0 else 0

        # Caculate the accuracy
        correct_chars = sum(1 for a , b in zip(typed_text.lower() , self.sample_text.lower())if a == b )
        accuracy = correct_chars / len(self.sample_text)*100
        advice = "great for me at all "
        if accuracy >= 80 and accuracy <= 100 and wpm <= 30:
            advice = "you have the most rating , capoo kima y9ol baha "
        self.result_label.config(
            text=f" Advice : {advice} \n WPM: {wpm:.2f}\n Accuracy: {accuracy:.2f}% \n Time : {time_taken:.2f}s")

    def rest(self):
        self.sample_text = random.choice(texts)
        self.text_label.config(text=self.sample_text, font=("Arial", 13))
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_timer = None

# Run the app
root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()

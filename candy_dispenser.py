import tkinter as tk
from tkinter import messagebox

from candy_model import CandyModel
from candy_utils import is_dark_color


class CandyDispenser:
    def __init__(self, root):
        self.root = root
        self.root.title("Candy Dispenser - Stack Data Structure")
        self.root.geometry("800x700")
        self.root.configure(bg='#f5f5f5')
import tkinter as tk
from tkinter import messagebox

from candy_model import CandyModel
from candy_view import CandyView


class CandyController:
    def __init__(self, root):
        self.root = root
        self.root.title("Candy Dispenser - Stack Data Structure")
        self.root.geometry("800x700")
        self.root.configure(bg='#f5f5f5')

        self.model = CandyModel()

        callbacks = {
            'push': self.push_candy,
            'pop': self.pop_candy,
            'peek': self.peek_candy,
            'clear': self.clear_stack,
            'is_empty': self.is_empty_check,
            'size': self.get_size,
        }

        self.view = CandyView(root, self.model, callbacks)

    def push_candy(self):
        if not self.model.can_push():
            messagebox.showwarning("Stack Full", "Cannot push more candies. Stack is full!")
            return

        candy = self.model.push()
        self.view.update_ui()
        if self.view.animate_var.get():
            self.view.animate_push()
        else:
            messagebox.showinfo("Candy Pushed", f"Added {candy['name']} candy to the dispenser!")

    def pop_candy(self):
        if not self.model.stack:
            messagebox.showwarning("Stack Empty", "Cannot pop candy. Stack is empty!")
            return

        start_spring_height = self.model.current_spring_height
        prev_size = len(self.model.stack)
        popped = self.model.pop()
        self.view.update_ui()
        if self.view.animate_var.get():
            self.view.animate_pop(popped, start_spring_height, prev_size)
        else:
            messagebox.showinfo("Candy Popped", f"Popped {popped['name']} candy!")

    def peek_candy(self):
        top = self.model.peek()
        if not top:
            messagebox.showinfo("Stack Empty", "Stack is empty. No candy to peek!")
            return
        messagebox.showinfo("Top Candy", f"Top candy is {top['name']}")

    def clear_stack(self):
        if not self.model.stack:
            messagebox.showinfo("Stack Empty", "Stack is already empty!")
            return
        if messagebox.askyesno("Clear Stack", "Are you sure you want to clear all candies?"):
            self.model.clear()
            self.view.update_ui()

    def is_empty_check(self):
        result = len(self.model.stack) == 0
        messagebox.showinfo("Stack is Empty?", str(result))

    def get_size(self):
        size = len(self.model.stack)
        messagebox.showinfo("Stack Size", str(size))



def main():
    root = tk.Tk()
    CandyController(root)
    root.mainloop()


if __name__ == "__main__":
    main()
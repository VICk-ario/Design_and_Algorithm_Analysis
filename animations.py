import tkinter as tk
from tkinter import messagebox

from candy_utils import is_dark_color


def animate_push(canvas, root, model, draw_dispenser):
    candy_x = 75
    candy_y = 50
    candy_width = 200
    candy_height = 30
    candy = model.stack[-1]
    anim_candy = canvas.create_rectangle(
        candy_x, candy_y,
        candy_x + candy_width, candy_y + candy_height,
        fill=candy['color'], outline='#333', width=2
    )
    anim_text = canvas.create_text(
        candy_x + candy_width/2, candy_y + candy_height/2,
        text=candy['name'], font=('Arial', 10, 'bold'),
        fill='white' if is_dark_color(candy['color']) else 'black'
    )
    spring_y = 450 - model.current_spring_height
    final_y = spring_y - (len(model.stack) * candy_height)

    def step(current_y):
        if current_y < final_y:
            canvas.move(anim_candy, 0, 5)
            canvas.move(anim_text, 0, 5)
            root.after(20, lambda: step(current_y + 5))
        else:
            canvas.delete(anim_candy)
            canvas.delete(anim_text)
            draw_dispenser()
            messagebox.showinfo("Candy Pushed", f"Added {model.stack[-1]['name']} candy to the dispenser!")

    step(candy_y)


def animate_pop(canvas, root, popped_candy, start_spring_height, prev_size, draw_dispenser):
    spring_y = 450 - start_spring_height
    candy_x = 75
    candy_height = 30
    candy_width = 200
    candy_y = spring_y - (prev_size * candy_height)
    anim_candy = canvas.create_rectangle(
        candy_x, candy_y,
        candy_x + candy_width, candy_y + candy_height,
        fill=popped_candy['color'], outline='#333', width=2
    )
    anim_text = canvas.create_text(
        candy_x + candy_width/2, candy_y + candy_height/2,
        text=popped_candy['name'], font=('Arial', 10, 'bold'),
        fill='white' if is_dark_color(popped_candy['color']) else 'black'
    )

    def step():
        canvas.move(anim_candy, 5, 0)
        canvas.move(anim_text, 5, 0)
        coords = canvas.coords(anim_candy)
        if coords and coords[0] < 400:
            root.after(20, step)
        else:
            canvas.delete(anim_candy)
            canvas.delete(anim_text)
            draw_dispenser()
            messagebox.showinfo("Candy Popped", f"Popped {popped_candy['name']} candy!")

    step()

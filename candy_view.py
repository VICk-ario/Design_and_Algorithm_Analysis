import tkinter as tk
from tkinter import messagebox

from candy_utils import is_dark_color
import animations


class CandyView:
    """View: builds UI, draws dispenser, and runs animations."""
    def __init__(self, root, model, callbacks=None):
        self.root = root
        self.model = model
        self._callbacks = callbacks or {}

        # Animation control
        self.animate_var = tk.BooleanVar(value=True)

        # Build UI
        self.setup_ui()

    def setup_ui(self):
        title_label = tk.Label(
            self.root,
            text="🍬 Candy Dispenser - Stack Data Structure 🍬",
            font=('Arial', 20, 'bold'),
            bg='#f5f5f5',
            fg='#333'
        )
        title_label.pack(pady=15)

        main_frame = tk.Frame(self.root, bg='#f5f5f5')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        left_frame = tk.Frame(main_frame, bg='#f5f5f5', width=400)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        dispenser_frame = tk.Frame(left_frame, bg='#f5f5f5')
        dispenser_frame.pack(pady=10)

        dispenser_label = tk.Label(
            dispenser_frame,
            text="CANDY DISPENSER",
            font=('Arial', 14, 'bold'),
            bg='#f5f5f5',
            fg='#444'
        )
        dispenser_label.pack()

        self.canvas = tk.Canvas(
            dispenser_frame,
            width=350,
            height=500,
            bg='white',
            highlightthickness=2,
            highlightbackground='#ddd'
        )
        self.canvas.pack(pady=10)

        right_frame = tk.Frame(main_frame, bg='#f5f5f5', width=300)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(20, 0))

        operations_frame = tk.LabelFrame(
            right_frame,
            text="Stack Operations",
            font=('Arial', 12, 'bold'),
            bg='#f5f5f5',
            padx=10,
            pady=10
        )
        operations_frame.pack(fill=tk.X, pady=(0, 15))

        self.push_btn = tk.Button(
            operations_frame,
            text="PUSH (Add Candy)",
            command=lambda: self._call('push'),
            bg='#4CAF50',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            width=20
        )
        self.push_btn.pack(pady=5)

        self.pop_btn = tk.Button(
            operations_frame,
            text="POP (Remove Candy)",
            command=lambda: self._call('pop'),
            bg='#f44336',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            width=20
        )
        self.pop_btn.pack(pady=5)

        peek_btn = tk.Button(
            operations_frame,
            text="PEEK (See Top Candy)",
            command=lambda: self._call('peek'),
            bg='#2196F3',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            width=20
        )
        peek_btn.pack(pady=5)

        clear_btn = tk.Button(
            operations_frame,
            text="CLEAR Stack",
            command=lambda: self._call('clear'),
            bg='#FF9800',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            width=20
        )
        clear_btn.pack(pady=5)

        is_empty_btn = tk.Button(
            operations_frame,
            text="IS EMPTY? (Check)",
            command=lambda: self._call('is_empty'),
            bg='#9C27B0',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            width=20
        )
        is_empty_btn.pack(pady=5)

        size_btn = tk.Button(
            operations_frame,
            text="SIZE (Get Size)",
            command=lambda: self._call('size'),
            bg='#00BCD4',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            width=20
        )
        size_btn.pack(pady=5)

        info_frame = tk.LabelFrame(
            right_frame,
            text="Stack Information",
            font=('Arial', 12, 'bold'),
            bg='#f5f5f5',
            padx=10,
            pady=10
        )
        info_frame.pack(fill=tk.X, pady=(10, 0))

        self.size_label = tk.Label(
            info_frame,
            text="Stack Size: 0",
            font=('Arial', 9),
            bg='#f5f5f5'
        )
        self.size_label.pack(pady=2)

        self.status_label = tk.Label(
            info_frame,
            text="Status: Empty",
            font=('Arial', 9),
            bg='#f5f5f5'
        )
        self.status_label.pack(pady=2)

        self.top_label = tk.Label(
            info_frame,
            text="Top Candy: None",
            font=('Arial', 9),
            bg='#f5f5f5'
        )
        self.top_label.pack(pady=2)

        self.spring_label = tk.Label(
            info_frame,
            text="Spring: Relaxed",
            font=('Arial', 9),
            bg='#f5f5f5'
        )
        self.spring_label.pack(pady=2)

        self.draw_dispenser()

    def _call(self, name):
        cb = self._callbacks.get(name)
        if cb:
            cb()

    def draw_dispenser(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(50, 50, 300, 450, outline='#555', width=3, fill='#f9f9f9')
        spring_y = 450 - self.model.current_spring_height
        self.draw_spring(spring_y)
        self.draw_candies(spring_y)
        self.canvas.create_text(175, 30, text="Candy Stack", font=('Arial', 12, 'bold'))
        self.canvas.create_text(50, 460, text="SPRING", font=('Arial', 10, 'bold'), anchor=tk.W)
        self.canvas.create_line(310, 100, 340, 100, arrow=tk.LAST, width=2)
        self.canvas.create_text(360, 100, text="POP", font=('Arial', 10, 'bold'))
        self.canvas.create_line(310, 400, 340, 400, arrow=tk.LAST, width=2)
        self.canvas.create_text(360, 400, text="PUSH", font=('Arial', 10, 'bold'))

    def draw_spring(self, spring_y):
        spring_top = spring_y
        spring_bottom = 450
        coil_count = 10
        coil_height = (spring_bottom - spring_top) / coil_count
        for i in range(coil_count):
            y = spring_top + i * coil_height
            x1 = 70 if i % 2 == 0 else 130
            x2 = 130 if i % 2 == 0 else 70
            self.canvas.create_line(x1, y, x2, y, width=2, fill='#888')
        self.canvas.create_rectangle(50, spring_bottom, 300, 455, fill='#ddd', outline='#888')
        spring_status = "Compressed" if self.model.current_spring_height < 100 else "Relaxed"
        self.spring_label.config(text=f"Spring: {spring_status} ({self.model.current_spring_height}px)")

    def draw_candies(self, spring_y):
        if not self.model.stack:
            self.canvas.create_text(175, 200, text="Empty Stack", font=('Arial', 14), fill='#999')
            return
        candy_height = 30
        candy_width = 200
        candy_x = 75
        for i, candy in enumerate(self.model.stack):
            candy_y = spring_y - ((i + 1) * candy_height)
            self.canvas.create_rectangle(
                candy_x, candy_y,
                candy_x + candy_width, candy_y + candy_height,
                fill=candy['color'], outline='#333', width=2
            )
            self.canvas.create_text(
                candy_x + candy_width/2, candy_y + candy_height/2,
                text=candy['name'], font=('Arial', 10, 'bold'),
                fill='white' if is_dark_color(candy['color']) else 'black'
            )
            self.canvas.create_text(
                candy_x - 20, candy_y + candy_height/2,
                text=str(i),
                font=('Arial', 9), fill='#555'
            )
        if self.model.stack:
            top_candy_y = spring_y - (len(self.model.stack) * candy_height)
            self.canvas.create_rectangle(
                candy_x - 5, top_candy_y - 5,
                candy_x + candy_width + 5, top_candy_y + candy_height + 5,
                outline='#FFD700', width=3
            )
            self.canvas.create_text(
                candy_x + candy_width/2, top_candy_y - 15,
                text="TOP", font=('Arial', 10, 'bold'),
                fill='#FFD700'
            )

    def update_ui(self):
        self.size_label.config(text=f"Stack Size: {len(self.model.stack)}")
        self.status_label.config(text=f"Status: {'Full' if len(self.model.stack) >= self.model.max_size else 'Empty' if len(self.model.stack) == 0 else 'Has Items'}")
        if self.model.stack:
            top_candy = self.model.stack[-1]
            self.top_label.config(text=f"Top Candy: {top_candy['name']}")
        else:
            self.top_label.config(text="Top Candy: None")
        self.draw_dispenser()

    # Animations (delegated to animations.py)
    def animate_push(self):
        animations.animate_push(self.canvas, self.root, self.model, self.draw_dispenser)

    def animate_pop(self, popped_candy, start_spring_height, prev_size):
        animations.animate_pop(self.canvas, self.root, popped_candy, start_spring_height, prev_size, self.draw_dispenser)

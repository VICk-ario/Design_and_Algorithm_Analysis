import tkinter as tk
from tkinter import messagebox
import random

class CandyDispenser:
    def __init__(self, root):
        self.root = root
        self.root.title("Candy Dispenser - Stack Data Structure")
        self.root.geometry("800x700")
        self.root.configure(bg='#f5f5f5')
        
        # Stack data structure to store candies
        self.stack = []
        
        # Candy properties
        self.candy_colors = ['#FF6B6B', '#4ECDC4', '#FFD166', '#06D6A0', 
                            '#118AB2', '#EF476F', '#9B5DE5', '#F15BB5']
        self.candy_names = ['Red', 'Teal', 'Yellow', 'Green', 
                           'Blue', 'Pink', 'Purple', 'Magenta']
        
        # Spring properties
        self.spring_height = 150  # Maximum spring height
        self.current_spring_height = 150  # Current spring height
        self.spring_compression = 25  # How much the spring compresses per candy
        
        # UI Setup
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🍬 Candy Dispenser - Stack Data Structure 🍬",
            font=('Arial', 20, 'bold'),
            bg='#f5f5f5',
            fg='#333'
        )
        title_label.pack(pady=15)
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#f5f5f5')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Left panel for stack visualization
        left_frame = tk.Frame(main_frame, bg='#f5f5f5', width=400)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Dispenser visualization
        dispenser_frame = tk.Frame(left_frame, bg='#f5f5f5')
        dispenser_frame.pack(pady=10)
        
        # Dispenser label
        dispenser_label = tk.Label(
            dispenser_frame, 
            text="CANDY DISPENSER",
            font=('Arial', 14, 'bold'),
            bg='#f5f5f5',
            fg='#444'
        )
        dispenser_label.pack()
        
        # Canvas for dispenser visualization
        self.canvas = tk.Canvas(
            dispenser_frame, 
            width=350, 
            height=500,
            bg='white',
            highlightthickness=2,
            highlightbackground='#ddd'
        )
        self.canvas.pack(pady=10)
        
        
        # Right panel for controls and info
        right_frame = tk.Frame(main_frame, bg='#f5f5f5', width=300)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(20, 0))
        
        # Stack operations frame
        operations_frame = tk.LabelFrame(
            right_frame, 
            text="Stack Operations",
            font=('Arial', 12, 'bold'),
            bg='#f5f5f5',
            padx=10,
            pady=10
        )
        operations_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Push button
        self.push_btn = tk.Button(
            operations_frame,
            text="PUSH (Add Candy)",
            command=self.push_candy,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            width=20
        )
        self.push_btn.pack(pady=5)
        
        # Pop button
        self.pop_btn = tk.Button(
            operations_frame,
            text="POP (Remove Candy)",
            command=self.pop_candy,
            bg='#f44336',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            width=20
        )
        self.pop_btn.pack(pady=5)
        
        # Peek button
        peek_btn = tk.Button(
            operations_frame,
            text="PEEK (See Top Candy)",
            command=self.peek_candy,
            bg='#2196F3',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            width=20
        )
        peek_btn.pack(pady=5)
        
        # Clear button
        clear_btn = tk.Button(
            operations_frame,
            text="CLEAR Stack",
            command=self.clear_stack,
            bg='#FF9800',
            fg='white',
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            width=20
        )
        clear_btn.pack(pady=5)
        
        # Stack info frame
        info_frame = tk.LabelFrame(
            right_frame, 
            text="Stack Information",
            font=('Arial', 12, 'bold'),
            bg='#f5f5f5',
            padx=10,
            pady=10
        )
        info_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Stack size label
        self.size_label = tk.Label(
            info_frame,
            text="Stack Size: 0",
            font=('Arial', 11),
            bg='#f5f5f5'
        )
        self.size_label.pack(pady=5)
        
        # Stack status label
        self.status_label = tk.Label(
            info_frame,
            text="Status: Empty",
            font=('Arial', 11),
            bg='#f5f5f5'
        )
        self.status_label.pack(pady=5)
        
        # Top candy label
        self.top_label = tk.Label(
            info_frame,
            text="Top Candy: None",
            font=('Arial', 11),
            bg='#f5f5f5'
        )
        self.top_label.pack(pady=5)
        
        # Spring status label
        self.spring_label = tk.Label(
            info_frame,
            text="Spring: Relaxed",
            font=('Arial', 11),
            bg='#f5f5f5'
        )
        self.spring_label.pack(pady=5)
        
        # Instructions
        instructions_frame = tk.Frame(right_frame, bg='#f5f5f5')
        instructions_frame.pack(fill=tk.X, pady=(15, 0))
        
        instructions = tk.Label(
            instructions_frame,
            text="Instructions:\n1. PUSH adds a candy to the dispenser\n2. POP removes the top candy\n3. The spring compresses when PUSH is used\n4. The spring expands when POP is used",
            font=('Arial', 10),
            bg='#f5f5f5',
            justify=tk.LEFT,
            wraplength=280
        )
        instructions.pack(anchor=tk.W)
        
        # Animation control
        self.animate_var = tk.BooleanVar(value=True)
        animate_check = tk.Checkbutton(
            instructions_frame,
            text="Enable Animations",
            variable=self.animate_var,
            bg='#f5f5f5',
            font=('Arial', 10)
        )
        animate_check.pack(anchor=tk.W, pady=(5, 0))
        # Draw the initial dispenser now that all UI elements exist
        self.draw_dispenser()
    
    def draw_dispenser(self):
        """Draw the candy dispenser with spring and candies"""
        self.canvas.delete("all")
        
        # Draw dispenser outline
        self.canvas.create_rectangle(50, 50, 300, 450, outline='#555', width=3, fill='#f9f9f9')
        
        # Draw spring area at the bottom
        spring_y = 450 - self.current_spring_height
        
        # Draw spring (as a coil)
        self.draw_spring(spring_y)
        
        # Draw candies in the stack
        self.draw_candies(spring_y)
        
        # Draw dispenser labels
        self.canvas.create_text(175, 30, text="Candy Stack", font=('Arial', 12, 'bold'))
        self.canvas.create_text(50, 460, text="SPRING", font=('Arial', 10, 'bold'), anchor=tk.W)
        
        # Draw arrow showing push/pop direction
        self.canvas.create_line(310, 100, 340, 100, arrow=tk.LAST, width=2)
        self.canvas.create_text(360, 100, text="POP", font=('Arial', 10, 'bold'))
        
        self.canvas.create_line(310, 400, 340, 400, arrow=tk.LAST, width=2)
        self.canvas.create_text(360, 400, text="PUSH", font=('Arial', 10, 'bold'))
    
    def draw_spring(self, spring_y):
        """Draw the spring at the bottom of the dispenser"""
        spring_top = spring_y
        spring_bottom = 450
        
        # Draw spring as a coil
        coil_count = 10
        coil_height = (spring_bottom - spring_top) / coil_count
        
        for i in range(coil_count):
            y = spring_top + i * coil_height
            # Alternate between left and right for coil effect
            x1 = 70 if i % 2 == 0 else 130
            x2 = 130 if i % 2 == 0 else 70
            self.canvas.create_line(x1, y, x2, y, width=2, fill='#888')
        
        # Draw spring base
        self.canvas.create_rectangle(50, spring_bottom, 300, 455, fill='#ddd', outline='#888')
        
        # Draw spring label with status
        spring_status = "Compressed" if self.current_spring_height < 100 else "Relaxed"
        self.spring_label.config(text=f"Spring: {spring_status} ({self.current_spring_height}px)")
    
    def draw_candies(self, spring_y):
        """Draw all candies in the stack"""
        if not self.stack:
            # Show empty stack message
            self.canvas.create_text(175, 200, text="Empty Stack", font=('Arial', 14), fill='#999')
            return
        
        # Draw each candy in the stack
        candy_height = 30
        candy_width = 200
        candy_x = 75
        
        # Draw from bottom (index 0) up to top (last element).
        # Bottom candy sits just above the spring at `spring_y - candy_height`.
        for i, candy in enumerate(self.stack):
            # i=0 is bottom, i increases upward
            candy_y = spring_y - ((i + 1) * candy_height)
            
            # Draw candy
            self.canvas.create_rectangle(
                candy_x, candy_y, 
                candy_x + candy_width, candy_y + candy_height,
                fill=candy['color'], outline='#333', width=2
            )
            
            # Draw candy label
            self.canvas.create_text(
                candy_x + candy_width/2, candy_y + candy_height/2,
                text=candy['name'], font=('Arial', 10, 'bold'),
                fill='white' if self.is_dark_color(candy['color']) else 'black'
            )
            
            # Draw stack index (0 = top)
            self.canvas.create_text(
                candy_x - 20, candy_y + candy_height/2,
                text=str(i),
                font=('Arial', 9), fill='#555'
            )
        
        # Highlight the top candy
        if self.stack:
            # Top candy is the last element; its Y depends on stack size
            top_candy_y = spring_y - (len(self.stack) * candy_height)
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
    
    def is_dark_color(self, hex_color):
        """Check if a color is dark for text contrast"""
        # Convert hex to RGB
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        
        # Calculate luminance
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return luminance < 0.5
    
    def push_candy(self):
        """Push a candy onto the stack"""
        if len(self.stack) >= 10:
            messagebox.showwarning("Stack Full", "Cannot push more candies. Stack is full!")
            return
        
        # Choose a random candy color
        idx = random.randint(0, len(self.candy_colors) - 1)
        candy = {
            'color': self.candy_colors[idx],
            'name': self.candy_names[idx]
        }
        
        # Add candy to the end so it becomes the top (last element)
        self.stack.append(candy)
        
        # Compress the spring
        self.compress_spring()
        
        # Update UI
        self.update_ui()
        
        # Show animation if enabled
        if self.animate_var.get():
            self.animate_push()
    
    def pop_candy(self):
        """Pop a candy from the stack"""
        if not self.stack:
            messagebox.showwarning("Stack Empty", "Cannot pop candy. Stack is empty!")
            return
        # Record spring height and size before removal to compute animation start
        start_spring_height = self.current_spring_height
        prev_size = len(self.stack)

        # Get the top candy (last element)
        popped_candy = self.stack.pop()

        # Expand the spring
        self.expand_spring()

        # Update UI
        self.update_ui()

        # Show animation if enabled
        if self.animate_var.get():
            self.animate_pop(popped_candy, start_spring_height, prev_size)
        else:
            messagebox.showinfo("Candy Popped", f"Popped {popped_candy['name']} candy!")
    
    def peek_candy(self):
        """Peek at the top candy without removing it"""
        if not self.stack:
            messagebox.showinfo("Stack Empty", "Stack is empty. No candy to peek!")
            return
        top_candy = self.stack[-1]
        messagebox.showinfo("Top Candy", f"Top candy is {top_candy['name']}")
    
    def clear_stack(self):
        """Clear the entire stack"""
        if not self.stack:
            messagebox.showinfo("Stack Empty", "Stack is already empty!")
            return
        
        if messagebox.askyesno("Clear Stack", "Are you sure you want to clear all candies?"):
            self.stack.clear()
            self.current_spring_height = 150  # Reset spring
            self.update_ui()
    
    def compress_spring(self):
        """Compress the spring when pushing a candy"""
        if self.current_spring_height > 30:  # Minimum spring height
            self.current_spring_height -= self.spring_compression
    
    def expand_spring(self):
        """Expand the spring when popping a candy"""
        if self.current_spring_height < 150:  # Maximum spring height
            self.current_spring_height += self.spring_compression
    
    def update_ui(self):
        """Update all UI elements"""
        # Update stack info
        self.size_label.config(text=f"Stack Size: {len(self.stack)}")
        self.status_label.config(text=f"Status: {'Full' if len(self.stack) >= 10 else 'Empty' if len(self.stack) == 0 else 'Has Items'}")
        
        # Update top candy
        if self.stack:
            top_candy = self.stack[-1]
            self.top_label.config(text=f"Top Candy: {top_candy['name']}")
        else:
            self.top_label.config(text="Top Candy: None")
        
        # Redraw the dispenser
        self.draw_dispenser()
    
    def animate_push(self):
        """Animate the push operation"""
        # Create a temporary candy at the top of the dispenser
        candy_x = 75
        candy_y = 50  # Start from top
        candy_width = 200
        candy_height = 30
        
        # Get the top candy (last element)
        candy = self.stack[-1]
        
        # Create animation candy
        anim_candy = self.canvas.create_rectangle(
            candy_x, candy_y, 
            candy_x + candy_width, candy_y + candy_height,
            fill=candy['color'], outline='#333', width=2
        )
        
        anim_text = self.canvas.create_text(
            candy_x + candy_width/2, candy_y + candy_height/2,
            text=candy['name'], font=('Arial', 10, 'bold'),
            fill='white' if self.is_dark_color(candy['color']) else 'black'
        )
        
        # Calculate final position (on top of the stack)
        spring_y = 450 - self.current_spring_height
        final_y = spring_y - (len(self.stack) * candy_height)
        
        # Animate the candy falling into place
        self.animate_falling(anim_candy, anim_text, candy_y, final_y, candy_height)
    
    def animate_pop(self, popped_candy, start_spring_height, prev_size):
        """Animate the pop operation starting from the candy's previous position

        `start_spring_height` is the spring height before the pop/expansion.
        """
        # Compute the spring Y position before removal
        spring_y = 450 - start_spring_height
        candy_x = 75
        candy_height = 30
        candy_width = 200
        # Top candy Y when it was present (depends on previous stack size)
        candy_y = spring_y - (prev_size * candy_height)
        
        # Create animation candy at the position where the top candy would be
        anim_candy = self.canvas.create_rectangle(
            candy_x, candy_y, 
            candy_x + candy_width, candy_y + candy_height,
            fill=popped_candy['color'], outline='#333', width=2
        )
        
        anim_text = self.canvas.create_text(
            candy_x + candy_width/2, candy_y + candy_height/2,
            text=popped_candy['name'], font=('Arial', 10, 'bold'),
            fill='white' if self.is_dark_color(popped_candy['color']) else 'black'
        )
        
        # Animate the candy being ejected
        self.animate_eject(anim_candy, anim_text, popped_candy)
    
    def animate_falling(self, candy_rect, candy_text, start_y, end_y, candy_height):
        """Animate candy falling into position"""
        if start_y < end_y:
            self.canvas.move(candy_rect, 0, 5)
            self.canvas.move(candy_text, 0, 5)
            self.root.after(20, lambda: self.animate_falling(candy_rect, candy_text, start_y + 5, end_y, candy_height))
        else:
            # Animation complete
            self.canvas.delete(candy_rect)
            self.canvas.delete(candy_text)
            self.draw_dispenser()
            messagebox.showinfo("Candy Pushed", f"Added {self.stack[-1]['name']} candy to the dispenser!")
    
    def animate_eject(self, candy_rect, candy_text, popped_candy):
        """Animate candy being ejected from the dispenser"""
        # Move candy to the right (out of the dispenser)
        self.canvas.move(candy_rect, 5, 0)
        self.canvas.move(candy_text, 5, 0)
        
        # Check if candy is out of the dispenser
        coords = self.canvas.coords(candy_rect)
        if coords[0] < 400:  # Still visible
            self.root.after(20, lambda: self.animate_eject(candy_rect, candy_text, popped_candy))
        else:
            # Animation complete
            self.canvas.delete(candy_rect)
            self.canvas.delete(candy_text)
            messagebox.showinfo("Candy Popped", f"Popped {popped_candy['name']} candy!")

def main():
    root = tk.Tk()
    app = CandyDispenser(root)
    root.mainloop()

if __name__ == "__main__":
    main()
import random


class CandyModel:
    """Model for the candy stack and spring state."""
    def __init__(self, max_size=10):
        # Stack data structure to store candies
        self.stack = []
        self.max_size = max_size

        # Candy properties
        self.candy_colors = ['#FF6B6B', '#4ECDC4', '#FFD166', '#06D6A0',
                             '#118AB2', '#EF476F', '#9B5DE5', '#F15BB5']
        self.candy_names = ['Red', 'Teal', 'Yellow', 'Green',
                            'Blue', 'Pink', 'Purple', 'Magenta']

        # Spring properties
        self.spring_height = 150  # Maximum spring height
        self.current_spring_height = 150  # Current spring height
        self.spring_compression = 25  # How much the spring compresses per candy

    def can_push(self):
        return len(self.stack) < self.max_size

    def push(self):
        if not self.can_push():
            return None
        idx = random.randint(0, len(self.candy_colors) - 1)
        candy = {'color': self.candy_colors[idx], 'name': self.candy_names[idx]}
        self.stack.append(candy)
        self.compress_spring()
        return candy

    def pop(self):
        if not self.stack:
            return None
        popped = self.stack.pop()
        self.expand_spring()
        return popped

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def clear(self):
        self.stack.clear()
        self.current_spring_height = self.spring_height

    def compress_spring(self):
        if self.current_spring_height > 30:
            self.current_spring_height -= self.spring_compression

    def expand_spring(self):
        if self.current_spring_height < self.spring_height:
            self.current_spring_height += self.spring_compression

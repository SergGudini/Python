class Node:
    """
          A class for creating a binary tree node and inserting elements.
          Attributes:
          -----------
          value : int, str
               The value that exists at this node of the tree.  eg. tree=Node(4) initializes a tree with
               a stump integer value of 4.

          Methods:
          --------
          insert(self, data) : Inserts a new element into the tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        if self.value is None:
            print("Узла не существует!")
        else:
            return f'Узел со значением {self.value} найден!'

    def display(self):
        """
        Функция отображения бинарного дерева на экране
        """
        lines, *_ = self.display_aux_()
        for line in lines:
            print(line)

    def display_aux_(self):
        """
        Вспомогательная функция для отображения бинарного дерева.
        Возвращает список строк, ширину, высоту и горизонтальную координату корня.
        """
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.display_aux_()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.display_aux_()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left.display_aux_()
        right, m, q, y = self.right.display_aux_()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

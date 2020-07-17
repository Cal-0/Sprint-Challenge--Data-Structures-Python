class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)


    def contains(self, target):
        if self.value == target:
            return True

        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)
       
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found


    def get_max(self):
        if self.value is None:
            return self

        max_value = self.value
        if self.right is None:
            return max_value

        if self.right.value > max_value:
            max_value = self.right.get_max()

        return max_value


    def for_each(self, fn):
        if self.value is None:
            return

        fn(self.value)

        if self.left is not None:
            self.left.for_each(fn)

        if self.right is not None:
            self.right.for_each(fn)


    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    def bft_print(self, node):
        if node is None:
            return

        queue = []

        queue.append(node)
        while(len(queue) > 0):
            data = queue.pop(0)
            print(data.value)

            if data.left is not None:
                queue.append(data.left)

            if data.right is not None:
                queue.append(data.right)


    def dft_print(self, node):
        if node is None:
            return

        stack = []

        stack.append(node)
        while(len(stack) > 0):
            data = stack.pop()
            print(data.value)

            if data.left is not None:
                stack.append(data.left)

            if data.right is not None:
                stack.append(data.right)
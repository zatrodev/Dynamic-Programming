class Node:
    def __init__(self, data = None, prev = None, next = None, top = None, bot = None):
        self.data = data
        self.prev = prev
        self.next = next
        self.top = top
        self.bot = bot


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __getitem__(self, index):
        if index < self.size / 2:
            trav = self.head
            for _ in range(index):
                trav = trav.next
        else:
            trav = self.tail
            for _ in range(self.size - index - 1):
                trav = trav.prev
            
        return trav

    def __len__(self):
        return self.size
    
    def add(self, node):
        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

        if self.size % len(matrix[0]) == 0 and self.size != 0 and self.size != len(matrix[0]):
            curr = bot = self.head
            top = self.tail
            for _ in range(len(matrix[0])):
                bot = bot.next
            for _ in range(len(matrix[0])):
                top = top.prev

            botStop = top
            topStop = bot

            while curr != botStop:
                curr.bot = bot
                curr = curr.next
                bot = bot.next

            curr = self.tail

            while curr != topStop:
                curr.top = top
                curr = curr.prev
                top = top.prev
        
        self.size += 1
    

matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

def set_elem_node(matrix):
    node_array = LinkedList()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            try:
                node_array.add(Node(matrix[i][j], Node(matrix[i][j - 1]), Node(matrix[i][j + 1]), Node(matrix[i - 1][j]), Node(matrix[i + 1][j])))
            except:
                node = Node(matrix[i][j])
                if j - 1 >= 0:
                    node.prev = Node(matrix[i][j - 1])
                if j + 1 < len(matrix[i]):
                    node.next = Node(matrix[i][j + 1])
                if i - 1 >= 0:
                    node.top = Node(matrix[i - 1][j])
                if i + 1 > len(matrix):
                    node.bot = Node(matrix[i + 1][j])

                node_array.add(node)

    return node_array


def check_if_safe(node, index, safe_indexes):
    if node.next != None:
        if node.next.data == 1 and index + 1 not in safe_indexes:
            safe_indexes.append(index + 1)
            check_if_safe(node.next, index + 1, safe_indexes)
    if node.prev != None:
        if node.prev.data == 1 and index - 1 not in safe_indexes:
            safe_indexes.append(index - 1)
            check_if_safe(node.prev, index - 1, safe_indexes)
    if node.bot != None:
        if node.bot.data == 1 and index + len(matrix[0]) not in safe_indexes:
            safe_indexes.append(index + len(matrix[0]))
            check_if_safe(node.bot, index + len(matrix[0]), safe_indexes)
    if node.top != None:
        if node.top.data == 1 and index - len(matrix[0]) not in safe_indexes and index - len(matrix[0]) > 0:
            safe_indexes.append(index - len(matrix[0]))
            check_if_safe(node.top, index - len(matrix[0]), safe_indexes)


def remove_islands(matrix):
    node_array = set_elem_node(matrix)
    border_indexes = [x for x in range(len(node_array)) if x < len(node_array) / len(matrix[0]) or x > len(node_array) - len(matrix[0]) or x % len(matrix[0]) == 0 or (x + 1) % len(matrix[0]) == 0]
    safe_indexes = border_indexes[:]

    for index in border_indexes:    
        if node_array[index].data == 1:
            check_if_safe(node_array[index], index, safe_indexes)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i * len(matrix[i]) + j not in safe_indexes:
                matrix[i][j] = 0

    return matrix


if __name__ == "__main__":
    matrix = remove_islands(matrix)
    for line in matrix:
        print(line)
class LRUCache:



    class Node:
        def __init__(self, key=-1, val=-1, next=None, prev = None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.nodes = {}
        self.head = self.Node()
        self.tail = self.Node()

        self.length = 0
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if not node:
            return -1
        
        #removes it
        node.prev.next = node.next
        node.next.prev = node.prev
        #puts it out in front
        
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
        

        return node.val

        



    def put(self, key: int, value: int) -> None:

        if key in self.nodes:
            self.nodes[key].val = value
            self.get(key)
            return 

        new_node = self.Node(key, value)


        if self.length < self.capacity:
            self.length += 1
        else:
            old_node = self.tail.prev
            
            

            old_node.prev.next = self.tail
            self.tail.prev = old_node.prev

            if old_node.key in self.nodes:
                del self.nodes[old_node.key]
        
        self.nodes[key] = new_node
        new_node.prev = self.head
        new_node.next = self.head.next

        self.head.next.prev = new_node
        self.head.next = new_node





# So, Linked Lists are useful here because they allow me to easily shuffle values around. The key look up, I dont think I can do better than linear to be honest. No I can't so I am thinking a store the values in a linked list, and the key : node is in a hashmap. So When I need to get I get the node from hashmap. then I move the node, to the front (head). Also the nodes should have a prev 

class MyHashMap:

    def __init__(self):
        self.a = []

    def put(self, key: int, value: int) -> None:
        for i in self.a:
            if i[0] == key:
                i[1] = value
                break
        else:
            self.a.append([key,value])

    def get(self, key: int) -> int:
        for i in self.a:
            if i[0] == key:
                return i[1]
        else:
            return -1        

    def remove(self, key: int) -> None:
        for i in self.a:
            if i[0] == key:
                self.a.remove(i)
        else:
            return None
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
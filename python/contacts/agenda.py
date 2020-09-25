import math
from contact import Contact

class Agenda:
    _size = 0
    def __init__(self, name=None):
        if name is None:
            self.head = None
        else:
            self.head = Contact(name)
            self._size = self._size + 1

    def add(self, name):
        if self.head:
            pointer = self.head
            while pointer:
                if max(name, pointer.name) == name:
                    if pointer.next:
                        if min(name, pointer.next.name) == name:
                            aux = pointer.next
                            pointer.next = Contact(name)
                            pointer.next.next = aux
                            break
                    else:
                        pointer.next = Contact(name)
                        break
                pointer = pointer.next
        else:
            self.head = Contact(name)
            self._size = self._size + 1

    def search(self, partial):
        partial = partial.lower()
        count = 0

        pointer = self.head

        while pointer:
            if partial in pointer.name:
                count = count + 1

            pointer = pointer.next
        return count

    def last_add(self):
        return self.head.name

    def meio(self):
        return math.floor(self._size/2)

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")

        if pointer:
            return pointer.name
        else:
            raise IndexError("list index out of range")

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.name) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
        
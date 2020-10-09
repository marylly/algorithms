#!/bin/python3

import os
import sys

class Contact:
    def __init__(self, name):
        self.name = name.lower()
        self.next = None
class Agenda:
    def __init__(self, name=None):
        if name is None:
            self.head = None
        else:
            self.head = Contact(name)

    def add(self, name):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next

            pointer.next = Contact(name)
        else:
            self.head = Contact(name)

    def search(self, partial):
        partial = partial.lower()
        count = 0
        pointer = self.head

        while pointer:
            if partial in pointer.name:
                count = count + 1

            pointer = pointer.next
        return count

def contacts(queries):
    agenda = Agenda()
    count = []
    for query in range(0, len(queries)):
        if queries[query][0] == 'add':
            agenda.add('hack')

        if queries[query][0] == 'find':
            partial = queries[query][1]
            count.append(agenda.search(partial))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

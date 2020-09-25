import unittest
from agenda import Agenda

class Test_Contacts(unittest.TestCase):

    def test_agenda_first_contact(self):
        name = 'hack'
        agenda = Agenda(name)
        contact = agenda.last_add()
        self.assertEqual(name, contact)

    def test_agenda_size(self):
        name = 'Hack'
        agenda = Agenda(name)
        self.assertEqual(len(agenda), 1)

    def test_agenda_new_contact(self):
        agenda = Agenda()
        agenda.add('hack')
        agenda.add('hackerrank')
        self.assertEqual(agenda[1],'hackerrank')

    def test_agenda_partial_search(self):
        name = 'hack'
        agenda = Agenda(name)
        partial = 'hac'
        count = agenda.search(partial)
        self.assertEqual(count, 1)

    def test_agenda_partial_search2(self):
        agenda = Agenda()
        agenda.add('hack')
        agenda.add('hackerrank')
        count = agenda.search('hac')
        self.assertEqual(count, 2)

    def test_agenda_list_index(self):
        name = 'hack'
        agenda = Agenda(name)
        self.assertEqual(agenda[0], name)

    def test_case_01(self):
        agenda = Agenda()
        agenda.add('s')
        agenda.add('ss')
        agenda.add('sss')
        agenda.add('ssss')
        agenda.add('sssss')
        self.assertEqual(agenda.search('s'), 5)
        self.assertEqual(agenda.search('ss'), 4)
        self.assertEqual(agenda.search('sss'), 3)
        self.assertEqual(agenda.search('ssss'), 2)
        self.assertEqual(agenda.search('sssss'), 1)
        self.assertEqual(agenda.search('ssssss'), 0)

if __name__ == '__main__':
    unittest.main()
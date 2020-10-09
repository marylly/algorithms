import unittest

from graph.Graph import Graph

class TestBFS_Case_15(unittest.TestCase):
    START = None
    graph = None

    def setUp(self):
        self.START = 152
        self.graph = Graph(self.START)
        self.graph.add_edge(165, 298)
        self.graph.add_edge(21, 34)
        self.graph.add_edge(115, 12)
        self.graph.add_edge(79, 102)
        self.graph.add_edge(116, 150)
        self.graph.add_edge(40, 94)
        self.graph.add_edge(51, 54)
        self.graph.add_edge(159, 72)
        self.graph.add_edge(35, 42)
        self.graph.add_edge(114, 98)
        self.graph.add_edge(14, 30)
        self.graph.add_edge(133, 68)
        self.graph.add_edge(101, 72)
        self.graph.add_edge(163, 132)
        self.graph.add_edge(165, 144)
        self.graph.add_edge(162, 84)
        self.graph.add_edge(125, 1)
        self.graph.add_edge(18, 78)
        self.graph.add_edge(15, 162)
        self.graph.add_edge(102, 54)
        self.graph.add_edge(81, 50)
        self.graph.add_edge(82, 138)
        self.graph.add_edge(7, 80)
        self.graph.add_edge(64, 28)
        self.graph.add_edge(164, 38)
        self.graph.add_edge(64, 154)
        self.graph.add_edge(25, 100)
        self.graph.add_edge(41, 92)
        self.graph.add_edge(102, 52)
        self.graph.add_edge(39, 92)
        self.graph.add_edge(32, 56)
        self.graph.add_edge(158, 64)
        self.graph.add_edge(79, 106)
        self.graph.add_edge(57, 150)
        self.graph.add_edge(102, 132)
        self.graph.add_edge(42, 28)
        self.graph.add_edge(102, 58)
        self.graph.add_edge(90, 100)
        self.graph.add_edge(104, 40)
        self.graph.add_edge(103, 102)
        self.graph.add_edge(117, 64)
        self.graph.add_edge(2, 50)
        self.graph.add_edge(117, 146)
        self.graph.add_edge(105, 130)
        self.graph.add_edge(97, 110)
        self.graph.add_edge(12, 32)
        self.graph.add_edge(155, 154)
        self.graph.add_edge(152, 92)
        self.graph.add_edge(23, 44)
        self.graph.add_edge(94, 58)
        self.graph.add_edge(121, 86)
        self.graph.add_edge(144, 98)
        self.graph.add_edge(27, 66)
        self.graph.add_edge(113, 10)
        self.graph.add_edge(62, 14)
        self.graph.add_edge(143, 26)
        self.graph.add_edge(72, 26)
        self.graph.add_edge(101, 128)
        self.graph.add_edge(22, 14)
        self.graph.add_edge(13, 14)
        self.graph.add_edge(132, 124)
        self.graph.add_edge(115, 90)
        self.graph.add_edge(154, 60)
        self.graph.add_edge(27, 84)
        self.graph.add_edge(83, 158)
        self.graph.add_edge(34, 50)
        self.graph.add_edge(120, 112)
        self.graph.add_edge(27, 118)
        self.graph.add_edge(108, 116)
        self.graph.add_edge(150, 66)
        self.graph.add_edge(81, 136)
        self.graph.add_edge(67, 126)
        self.graph.add_edge(109, 86)
        self.graph.add_edge(164, 128)
        self.graph.add_edge(122, 92)
        self.graph.add_edge(140, 30)
        self.graph.add_edge(159, 122)
        self.graph.add_edge(137, 98)
        self.graph.add_edge(142, 64)
        self.graph.add_edge(12, 124)
        self.graph.add_edge(123, 96)
        self.graph.add_edge(58, 162)
        self.graph.add_edge(150, 138)
        self.graph.add_edge(154, 34)
        self.graph.add_edge(159, 102)
        self.graph.add_edge(132, 100)
        self.graph.add_edge(8, 72)
        self.graph.add_edge(123, 90)
        self.graph.add_edge(40, 58)
        self.graph.add_edge(84, 144)
        self.graph.add_edge(121, 146)
        self.graph.add_edge(47, 108)
        self.graph.add_edge(25, 32)
        self.graph.add_edge(163, 100)
        self.graph.add_edge(43, 38)
        self.graph.add_edge(36, 94)
        self.graph.add_edge(73, 132)
        self.graph.add_edge(116, 134)
        self.graph.add_edge(67, 134)
        self.graph.add_edge(23, 32)
        self.graph.add_edge(63, 32)
        self.graph.add_edge(112, 74)
        self.graph.add_edge(21, 100)
        self.graph.add_edge(90, 54)
        self.graph.add_edge(81, 116)
        self.graph.add_edge(48, 82)
        self.graph.add_edge(34, 6)
        self.graph.add_edge(3, 12)
        self.graph.add_edge(156, 130)
        self.graph.add_edge(38, 154)
        self.graph.add_edge(112, 156)
        self.graph.add_edge(54, 80)
        self.graph.add_edge(95, 34)
        self.graph.add_edge(123, 62)
        self.graph.add_edge(60, 54)
        self.graph.add_edge(161, 156)
        self.graph.add_edge(112, 158)
        self.graph.add_edge(73, 46)
        self.graph.add_edge(96, 64)
        self.graph.add_edge(99, 76)
        self.graph.add_edge(10, 28)
        self.graph.add_edge(1, 146)
        self.graph.add_edge(41, 152)
        self.graph.add_edge(117, 18)
        self.graph.add_edge(35, 26)
        self.graph.add_edge(59, 128)
        self.graph.add_edge(63, 54)
        self.graph.add_edge(40, 144)
        self.graph.add_edge(93, 66)
        self.graph.add_edge(75, 78)
        self.graph.add_edge(109, 1)
        self.graph.add_edge(116, 70)
        self.graph.add_edge(157, 120)
        self.graph.add_edge(115, 110)
        self.graph.add_edge(51, 150)
        self.graph.add_edge(143, 116)
        self.graph.add_edge(15, 160)
        self.graph.add_edge(9, 54)
        self.graph.add_edge(120, 156)
        self.graph.add_edge(42, 10)
        self.graph.add_edge(45, 70)
        self.graph.add_edge(125, 58)
        self.graph.add_edge(119, 48)
        self.graph.add_edge(5, 76)
        self.graph.add_edge(31, 46)
        self.graph.add_edge(92, 8)
        self.graph.add_edge(39, 94)
        self.graph.add_edge(125, 22)
        self.graph.add_edge(115, 54)
        self.graph.add_edge(117, 124)
        self.graph.add_edge(162, 38)
        self.graph.add_edge(71, 90)
        self.graph.add_edge(10, 150)
        self.graph.add_edge(81, 94)
        self.graph.add_edge(87, 106)
        self.graph.add_edge(109, 136)
        self.graph.add_edge(150, 132)
        self.graph.add_edge(89, 134)
        self.graph.add_edge(142, 14)
        self.graph.add_edge(151, 164)
        self.graph.add_edge(111, 96)
        self.graph.add_edge(68, 56)
        self.graph.add_edge(142, 36)
        self.graph.add_edge(122, 164)
        self.graph.add_edge(150, 148)
        self.graph.add_edge(56, 6)
        self.graph.add_edge(49, 104)
        self.graph.add_edge(98, 32)
        self.graph.add_edge(147, 94)
        self.graph.add_edge(1, 80)
        self.graph.add_edge(58, 134)
        self.graph.add_edge(16, 8)
        self.graph.add_edge(30, 56)
        self.graph.add_edge(66, 144)
        self.graph.add_edge(143, 128)
        self.graph.add_edge(22, 94)
        self.graph.add_edge(98, 82)
        self.graph.add_edge(17, 26)
        self.graph.add_edge(35, 78)
        self.graph.add_edge(72, 80)
        self.graph.add_edge(142, 64)
        self.graph.add_edge(35, 18)
        self.graph.add_edge(122, 100)
        self.graph.add_edge(125, 24)
        self.graph.add_edge(143, 164)
        self.graph.add_edge(151, 52)
        self.graph.add_edge(142, 80)
        self.graph.add_edge(156, 1)
        self.graph.add_edge(117, 104)
        self.graph.add_edge(122, 30)
        self.graph.add_edge(132, 64)
        self.graph.add_edge(53, 26)
        self.graph.add_edge(2, 34)
        self.graph.add_edge(36, 160)
        self.graph.add_edge(158, 150)
        self.graph.add_edge(124, 8)
        self.graph.add_edge(54, 38)
        self.graph.add_edge(81, 44)
        self.graph.add_edge(137, 120)
        self.graph.add_edge(87, 138)
        self.graph.add_edge(126, 127)
        self.graph.add_edge(48, 134)
        self.graph.add_edge(104, 30)
        self.graph.add_edge(115, 70)
        self.graph.add_edge(63, 2)
        self.graph.add_edge(102, 92)
        self.graph.add_edge(90, 72)
        self.graph.add_edge(3, 72)
        self.graph.add_edge(58, 92)
        self.graph.add_edge(23, 108)
        self.graph.add_edge(90, 160)
        self.graph.add_edge(120, 138)
        self.graph.add_edge(83, 114)
        self.graph.add_edge(10, 52)
        self.graph.add_edge(144, 108)
        self.graph.add_edge(101, 114)
        self.graph.add_edge(108, 154)
        self.graph.add_edge(117, 96)
        self.graph.add_edge(14, 40)
        self.graph.add_edge(160, 48)
        self.graph.add_edge(95, 38)
        self.graph.add_edge(119, 36)
        self.graph.add_edge(151, 136)
        self.graph.add_edge(23, 74)
        self.graph.add_edge(65, 98)
        self.graph.add_edge(146, 78)
        self.graph.add_edge(71, 26)
        self.graph.add_edge(105, 92)
        self.graph.add_edge(145, 138)
        self.graph.add_edge(77, 10)
        self.graph.add_edge(24, 122)
        self.graph.add_edge(149, 48)
        self.graph.add_edge(23, 2)
        self.graph.add_edge(92, 134)
        self.graph.add_edge(103, 18)
        self.graph.add_edge(91, 96)
        self.graph.add_edge(11, 22)
        self.graph.add_edge(70, 152)
        self.graph.add_edge(96, 162)
        self.graph.add_edge(94, 88)
        self.graph.add_edge(75, 122)
        self.graph.add_edge(1, 42)
        self.graph.add_edge(144, 52)
        self.graph.add_edge(145, 74)
        self.graph.add_edge(75, 38)
        self.graph.add_edge(152, 88)
        self.graph.add_edge(139, 132)
        self.graph.add_edge(78, 50)
        self.graph.add_edge(15, 60)
        self.graph.add_edge(131, 78)
        self.graph.add_edge(83, 22)
        self.graph.add_edge(72, 44)
        self.graph.add_edge(1, 126)
        self.graph.add_edge(120, 136)
        self.graph.add_edge(41, 42)
        self.graph.add_edge(82, 74)
        self.graph.add_edge(18, 19)
        self.graph.add_edge(155, 32)
        self.graph.add_edge(27, 144)
        self.graph.add_edge(155, 28)
        self.graph.add_edge(99, 40)
        self.graph.add_edge(32, 102)
        self.graph.add_edge(3, 162)
        self.graph.add_edge(81, 16)
        self.graph.add_edge(154, 108)
        self.graph.add_edge(5, 114)
        self.graph.add_edge(150, 10)
        self.graph.add_edge(131, 68)
        self.graph.add_edge(163, 90)
        self.graph.add_edge(50, 64)
        self.graph.add_edge(64, 158)
        self.graph.add_edge(31, 102)
        self.graph.add_edge(73, 38)
        self.graph.add_edge(83, 68)
        self.graph.add_edge(64, 14)
        self.graph.add_edge(87, 100)
        self.graph.add_edge(15, 36)
        self.graph.add_edge(137, 34)
        self.graph.add_edge(114, 42)
        self.graph.add_edge(61, 80)
        self.graph.add_edge(54, 62)
        self.graph.add_edge(99, 74)
        self.graph.add_edge(154, 28)
        self.graph.add_edge(133, 12)
        self.graph.add_edge(161, 86)
        self.graph.add_edge(79, 158)
        self.graph.add_edge(79, 82)
        self.graph.add_edge(10, 146)
        self.graph.add_edge(150, 48)
        self.graph.add_edge(72, 6)
        self.graph.add_edge(107, 92)
        self.graph.add_edge(88, 80)
        self.graph.add_edge(19, 8)
        self.graph.add_edge(162, 10)
        self.graph.add_edge(118, 58)
        self.graph.add_edge(99, 10)
        self.graph.add_edge(84, 94)
        self.graph.add_edge(59, 86)
        self.graph.add_edge(93, 84)
        return super().setUp()

    def test_case_15(self):
        self.graph.get_all_paths()
        self.graph.get_costs()
        self.assertEqual(self.graph.get_costs(),[18, 30, 24, -1, 24, 24, 18, 12, 24, 18, 24, 18, 30, 24, 24, 18, 30, 24, 18, -1, 24, 18, 24, 18, 24, 24, 24, 18, -1, 18, 18, 18, -1, 30, 18, 18, -1, 24, 12, 18, 6, 12, 30, 24, 12, 24, 24, 18, 30, 24, 24, 18, 30, 18, -1, 24, 24, 12, 30, 24, 18, 24, 24, 24, 30, 24, 18, 30, -1, 6, 24, 18, 24, 30, 18, 30, 24, 24, 18, 12, 18, 24, 24, 18, -1, 30, 24, 6, 18, 18, 30, 6, 24, 12, 30, 24, 24, 24, 24, 18, 24, 12, 18, 24, 12, 24, 12, 18, 24, 18, 30, 30, 24, 18, 12, 12, 24, 18, 24, 30, 30, 12, 24, 18, 18, 24, 30, 24, -1, 18, 30, 18, 24, 12, -1, 24, 30, 24, 24, 24, -1, 18, 18, 24, 30, 24, 18, 24, 24, 18, 24, -1, 24, 24, 24, 36, 24, 18, 24, 30, 18, 24, 18, 30])

    def tearDown(self):
        del self.START
        del self.graph
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
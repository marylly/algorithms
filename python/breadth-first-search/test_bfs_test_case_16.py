import unittest

from graph.Graph import Graph

class TestBFS_Case_16(unittest.TestCase):
    START = None
    graph = None

    def setUp(self):
        self.START = 76
        self.graph = Graph(self.START)
        self.graph.add_edge(515, 804)
        self.graph.add_edge(12, 344)
        self.graph.add_edge(387, 256)
        self.graph.add_edge(507, 508)
        self.graph.add_edge(258, 300)
        self.graph.add_edge(222, 132)
        self.graph.add_edge(12, 264)
        self.graph.add_edge(219, 1)
        self.graph.add_edge(51, 284)
        self.graph.add_edge(297, 452)
        self.graph.add_edge(315, 272)
        self.graph.add_edge(132, 272)
        self.graph.add_edge(270, 468)
        self.graph.add_edge(66, 356)
        self.graph.add_edge(345, 236)
        self.graph.add_edge(93, 20)
        self.graph.add_edge(294, 168)
        self.graph.add_edge(396, 264)
        self.graph.add_edge(405, 104)
        self.graph.add_edge(273, 260)
        self.graph.add_edge(252, 512)
        self.graph.add_edge(249, 480)
        self.graph.add_edge(462, 248)
        self.graph.add_edge(219, 168)
        self.graph.add_edge(219, 236)
        self.graph.add_edge(333, 248)
        self.graph.add_edge(402, 488)
        self.graph.add_edge(42, 268)
        self.graph.add_edge(180, 164)
        self.graph.add_edge(279, 464)
        self.graph.add_edge(39, 80)
        self.graph.add_edge(480, 140)
        self.graph.add_edge(150, 220)
        self.graph.add_edge(18, 476)
        self.graph.add_edge(138, 416)
        self.graph.add_edge(69, 384)
        self.graph.add_edge(297, 232)
        self.graph.add_edge(135, 84)
        self.graph.add_edge(102, 428)
        self.graph.add_edge(399, 132)
        self.graph.add_edge(141, 232)
        self.graph.add_edge(300, 400)
        self.graph.add_edge(312, 388)
        self.graph.add_edge(489, 244)
        self.graph.add_edge(258, 424)
        self.graph.add_edge(132, 248)
        self.graph.add_edge(51, 220)
        self.graph.add_edge(207, 488)
        self.graph.add_edge(90, 140)
        self.graph.add_edge(306, 176)
        self.graph.add_edge(87, 260)
        self.graph.add_edge(174, 228)
        self.graph.add_edge(57, 300)
        self.graph.add_edge(18, 332)
        self.graph.add_edge(36, 404)
        self.graph.add_edge(66, 308)
        self.graph.add_edge(18, 128)
        self.graph.add_edge(252, 172)
        self.graph.add_edge(354, 300)
        self.graph.add_edge(474, 196)
        self.graph.add_edge(345, 192)
        self.graph.add_edge(246, 4)
        self.graph.add_edge(405, 228)
        self.graph.add_edge(348, 64)
        self.graph.add_edge(480, 208)
        self.graph.add_edge(276, 112)
        self.graph.add_edge(228, 324)
        self.graph.add_edge(1, 436)
        self.graph.add_edge(183, 344)
        self.graph.add_edge(204, 300)
        self.graph.add_edge(264, 112)
        self.graph.add_edge(216, 212)
        self.graph.add_edge(225, 248)
        self.graph.add_edge(114, 124)
        self.graph.add_edge(288, 240)
        self.graph.add_edge(312, 260)
        self.graph.add_edge(456, 292)
        self.graph.add_edge(456, 296)
        self.graph.add_edge(84, 136)
        self.graph.add_edge(429, 456)
        self.graph.add_edge(78, 396)
        self.graph.add_edge(465, 140)
        self.graph.add_edge(504, 80)
        self.graph.add_edge(327, 504)
        self.graph.add_edge(492, 60)
        self.graph.add_edge(339, 364)
        self.graph.add_edge(237, 72)
        self.graph.add_edge(258, 280)
        self.graph.add_edge(264, 340)
        self.graph.add_edge(159, 308)
        self.graph.add_edge(21, 36)
        self.graph.add_edge(99, 192)
        self.graph.add_edge(69, 68)
        self.graph.add_edge(414, 16)
        self.graph.add_edge(117, 440)
        self.graph.add_edge(321, 420)
        self.graph.add_edge(240, 360)
        self.graph.add_edge(312, 124)
        self.graph.add_edge(168, 488)
        self.graph.add_edge(12, 60)
        self.graph.add_edge(123, 380)
        self.graph.add_edge(18, 256)
        self.graph.add_edge(264, 488)
        self.graph.add_edge(438, 172)
        self.graph.add_edge(108, 220)
        self.graph.add_edge(102, 12)
        self.graph.add_edge(318, 492)
        self.graph.add_edge(471, 268)
        self.graph.add_edge(345, 488)
        self.graph.add_edge(120, 388)
        self.graph.add_edge(492, 24)
        self.graph.add_edge(504, 400)
        self.graph.add_edge(72, 84)
        self.graph.add_edge(237, 64)
        self.graph.add_edge(12, 392)
        self.graph.add_edge(438, 424)
        self.graph.add_edge(234, 112)
        self.graph.add_edge(318, 368)
        self.graph.add_edge(504, 480)
        self.graph.add_edge(486, 208)
        self.graph.add_edge(381, 432)
        self.graph.add_edge(279, 336)
        self.graph.add_edge(27, 296)
        self.graph.add_edge(180, 264)
        self.graph.add_edge(180, 140)
        self.graph.add_edge(438, 64)
        self.graph.add_edge(468, 44)
        self.graph.add_edge(138, 72)
        self.graph.add_edge(348, 144)
        self.graph.add_edge(1, 484)
        self.graph.add_edge(36, 124)
        self.graph.add_edge(48, 464)
        self.graph.add_edge(195, 336)
        self.graph.add_edge(69, 452)
        self.graph.add_edge(450, 400)
        self.graph.add_edge(453, 196)
        self.graph.add_edge(318, 292)
        self.graph.add_edge(366, 452)
        self.graph.add_edge(207, 396)
        self.graph.add_edge(222, 472)
        self.graph.add_edge(489, 140)
        self.graph.add_edge(477, 28)
        self.graph.add_edge(342, 48)
        self.graph.add_edge(384, 284)
        self.graph.add_edge(132, 412)
        self.graph.add_edge(225, 112)
        self.graph.add_edge(411, 476)
        self.graph.add_edge(225, 480)
        self.graph.add_edge(90, 132)
        self.graph.add_edge(309, 8)
        self.graph.add_edge(390, 152)
        self.graph.add_edge(351, 216)
        self.graph.add_edge(180, 228)
        self.graph.add_edge(348, 192)
        self.graph.add_edge(375, 8)
        self.graph.add_edge(342, 36)
        self.graph.add_edge(321, 508)
        self.graph.add_edge(492, 364)
        self.graph.add_edge(42, 176)
        self.graph.add_edge(441, 212)
        self.graph.add_edge(366, 188)
        self.graph.add_edge(297, 260)
        self.graph.add_edge(258, 252)
        self.graph.add_edge(54, 396)
        self.graph.add_edge(372, 80)
        self.graph.add_edge(48, 100)
        self.graph.add_edge(48, 240)
        self.graph.add_edge(216, 88)
        self.graph.add_edge(27, 476)
        self.graph.add_edge(3, 160)
        self.graph.add_edge(171, 360)
        self.graph.add_edge(75, 300)
        self.graph.add_edge(408, 312)
        self.graph.add_edge(390, 264)
        self.graph.add_edge(495, 508)
        self.graph.add_edge(345, 200)
        self.graph.add_edge(228, 392)
        self.graph.add_edge(387, 188)
        self.graph.add_edge(393, 388)
        self.graph.add_edge(348, 396)
        self.graph.add_edge(105, 312)
        self.graph.add_edge(309, 500)
        self.graph.add_edge(147, 452)
        self.graph.add_edge(201, 296)
        self.graph.add_edge(15, 192)
        self.graph.add_edge(153, 460)
        self.graph.add_edge(258, 164)
        self.graph.add_edge(261, 424)
        self.graph.add_edge(69, 364)
        self.graph.add_edge(270, 92)
        self.graph.add_edge(234, 424)
        self.graph.add_edge(312, 88)
        self.graph.add_edge(219, 84)
        self.graph.add_edge(342, 64)
        self.graph.add_edge(411, 348)
        self.graph.add_edge(192, 288)
        self.graph.add_edge(333, 260)
        self.graph.add_edge(9, 88)
        self.graph.add_edge(24, 272)
        self.graph.add_edge(444, 36)
        self.graph.add_edge(279, 272)
        self.graph.add_edge(45, 40)
        self.graph.add_edge(93, 276)
        self.graph.add_edge(396, 344)
        self.graph.add_edge(189, 260)
        self.graph.add_edge(321, 88)
        self.graph.add_edge(495, 152)
        self.graph.add_edge(222, 496)
        self.graph.add_edge(342, 72)
        self.graph.add_edge(513, 456)
        self.graph.add_edge(249, 312)
        self.graph.add_edge(345, 16)
        self.graph.add_edge(312, 200)
        self.graph.add_edge(453, 340)
        self.graph.add_edge(39, 288)
        self.graph.add_edge(231, 448)
        self.graph.add_edge(252, 404)
        self.graph.add_edge(267, 436)
        self.graph.add_edge(492, 332)
        self.graph.add_edge(453, 404)
        self.graph.add_edge(60, 56)
        self.graph.add_edge(228, 368)
        self.graph.add_edge(222, 504)
        self.graph.add_edge(315, 244)
        self.graph.add_edge(438, 76)
        self.graph.add_edge(177, 1)
        self.graph.add_edge(327, 276)
        self.graph.add_edge(471, 440)
        self.graph.add_edge(129, 484)
        self.graph.add_edge(378, 20)
        self.graph.add_edge(339, 508)
        self.graph.add_edge(357, 484)
        self.graph.add_edge(105, 340)
        self.graph.add_edge(504, 352)
        self.graph.add_edge(447, 428)
        self.graph.add_edge(210, 424)
        self.graph.add_edge(345, 144)
        self.graph.add_edge(24, 28)
        self.graph.add_edge(390, 436)
        self.graph.add_edge(96, 488)
        self.graph.add_edge(147, 144)
        self.graph.add_edge(483, 436)
        self.graph.add_edge(180, 432)
        self.graph.add_edge(102, 228)
        self.graph.add_edge(420, 504)
        self.graph.add_edge(183, 100)
        self.graph.add_edge(45, 116)
        self.graph.add_edge(351, 272)
        self.graph.add_edge(315, 168)
        self.graph.add_edge(258, 312)
        self.graph.add_edge(153, 344)
        self.graph.add_edge(477, 372)
        self.graph.add_edge(129, 332)
        self.graph.add_edge(36, 496)
        self.graph.add_edge(72, 132)
        self.graph.add_edge(384, 64)
        self.graph.add_edge(237, 144)
        self.graph.add_edge(192, 292)
        self.graph.add_edge(381, 152)
        self.graph.add_edge(474, 252)
        self.graph.add_edge(135, 108)
        self.graph.add_edge(99, 136)
        self.graph.add_edge(489, 304)
        self.graph.add_edge(39, 460)
        self.graph.add_edge(510, 48)
        self.graph.add_edge(51, 196)
        self.graph.add_edge(483, 64)
        self.graph.add_edge(141, 224)
        self.graph.add_edge(48, 380)
        self.graph.add_edge(360, 236)
        self.graph.add_edge(279, 368)
        self.graph.add_edge(75, 12)
        self.graph.add_edge(399, 12)
        self.graph.add_edge(243, 292)
        self.graph.add_edge(258, 288)
        self.graph.add_edge(408, 232)
        self.graph.add_edge(204, 380)
        self.graph.add_edge(189, 472)
        self.graph.add_edge(210, 268)
        self.graph.add_edge(123, 156)
        self.graph.add_edge(390, 212)
        self.graph.add_edge(42, 28)
        self.graph.add_edge(276, 156)
        self.graph.add_edge(294, 344)
        self.graph.add_edge(474, 248)
        self.graph.add_edge(72, 432)
        self.graph.add_edge(96, 444)
        self.graph.add_edge(309, 476)
        self.graph.add_edge(6, 272)
        self.graph.add_edge(312, 396)
        self.graph.add_edge(342, 224)
        self.graph.add_edge(351, 152)
        self.graph.add_edge(144, 416)
        self.graph.add_edge(450, 296)
        self.graph.add_edge(177, 444)
        self.graph.add_edge(297, 24)
        self.graph.add_edge(486, 188)
        self.graph.add_edge(183, 220)
        self.graph.add_edge(198, 236)
        self.graph.add_edge(324, 208)
        self.graph.add_edge(210, 484)
        self.graph.add_edge(129, 84)
        self.graph.add_edge(507, 504)
        self.graph.add_edge(123, 60)
        self.graph.add_edge(513, 364)
        self.graph.add_edge(111, 56)
        self.graph.add_edge(90, 188)
        self.graph.add_edge(375, 264)
        self.graph.add_edge(186, 412)
        self.graph.add_edge(15, 92)
        self.graph.add_edge(114, 300)
        self.graph.add_edge(411, 348)
        self.graph.add_edge(495, 96)
        self.graph.add_edge(219, 164)
        self.graph.add_edge(351, 244)
        self.graph.add_edge(432, 456)
        self.graph.add_edge(117, 420)
        self.graph.add_edge(405, 132)
        self.graph.add_edge(336, 252)
        self.graph.add_edge(423, 216)
        self.graph.add_edge(429, 184)
        self.graph.add_edge(153, 152)
        self.graph.add_edge(186, 228)
        self.graph.add_edge(60, 312)
        self.graph.add_edge(195, 380)
        self.graph.add_edge(453, 96)
        self.graph.add_edge(408, 156)
        self.graph.add_edge(261, 264)
        self.graph.add_edge(444, 512)
        self.graph.add_edge(48, 36)
        self.graph.add_edge(171, 64)
        self.graph.add_edge(249, 64)
        self.graph.add_edge(402, 232)
        self.graph.add_edge(270, 108)
        self.graph.add_edge(438, 236)
        self.graph.add_edge(51, 336)
        self.graph.add_edge(330, 88)
        self.graph.add_edge(252, 152)
        self.graph.add_edge(45, 452)
        self.graph.add_edge(18, 48)
        self.graph.add_edge(219, 404)
        self.graph.add_edge(327, 40)
        self.graph.add_edge(21, 408)
        self.graph.add_edge(417, 72)
        self.graph.add_edge(3, 156)
        self.graph.add_edge(72, 404)
        self.graph.add_edge(264, 176)
        self.graph.add_edge(219, 76)
        self.graph.add_edge(390, 168)
        self.graph.add_edge(279, 64)
        self.graph.add_edge(150, 48)
        self.graph.add_edge(414, 344)
        self.graph.add_edge(348, 248)
        self.graph.add_edge(54, 436)
        self.graph.add_edge(261, 280)
        self.graph.add_edge(486, 260)
        self.graph.add_edge(198, 124)
        self.graph.add_edge(57, 44)
        self.graph.add_edge(486, 356)
        self.graph.add_edge(441, 80)
        self.graph.add_edge(486, 136)
        self.graph.add_edge(510, 168)
        self.graph.add_edge(1, 220)
        self.graph.add_edge(114, 384)
        self.graph.add_edge(441, 36)
        self.graph.add_edge(420, 324)
        self.graph.add_edge(480, 508)
        self.graph.add_edge(456, 160)
        self.graph.add_edge(258, 4)
        self.graph.add_edge(210, 356)
        self.graph.add_edge(324, 356)
        self.graph.add_edge(294, 332)
        self.graph.add_edge(231, 416)
        self.graph.add_edge(255, 368)
        self.graph.add_edge(66, 20)
        self.graph.add_edge(231, 480)
        self.graph.add_edge(105, 88)
        self.graph.add_edge(162, 40)
        self.graph.add_edge(459, 300)
        self.graph.add_edge(66, 372)
        self.graph.add_edge(291, 360)
        self.graph.add_edge(498, 184)
        self.graph.add_edge(339, 192)
        self.graph.add_edge(21, 368)
        self.graph.add_edge(9, 60)
        self.graph.add_edge(288, 312)
        self.graph.add_edge(246, 112)
        self.graph.add_edge(1, 296)
        self.graph.add_edge(411, 292)
        self.graph.add_edge(450, 120)
        self.graph.add_edge(267, 400)
        self.graph.add_edge(225, 176)
        self.graph.add_edge(366, 232)
        self.graph.add_edge(420, 356)
        self.graph.add_edge(147, 464)
        self.graph.add_edge(27, 80)
        self.graph.add_edge(195, 60)
        self.graph.add_edge(267, 368)
        self.graph.add_edge(372, 196)
        self.graph.add_edge(258, 136)
        self.graph.add_edge(21, 160)
        self.graph.add_edge(9, 448)
        self.graph.add_edge(444, 344)
        self.graph.add_edge(483, 192)
        self.graph.add_edge(294, 256)
        self.graph.add_edge(285, 224)
        self.graph.add_edge(318, 112)
        self.graph.add_edge(486, 148)
        self.graph.add_edge(291, 96)
        self.graph.add_edge(405, 300)
        self.graph.add_edge(102, 316)
        self.graph.add_edge(450, 68)
        self.graph.add_edge(42, 320)
        self.graph.add_edge(9, 316)
        self.graph.add_edge(339, 400)
        self.graph.add_edge(42, 320)
        self.graph.add_edge(318, 120)
        self.graph.add_edge(459, 400)
        self.graph.add_edge(90, 364)
        self.graph.add_edge(3, 332)
        self.graph.add_edge(267, 108)
        self.graph.add_edge(447, 316)
        self.graph.add_edge(267, 168)
        self.graph.add_edge(303, 352)
        self.graph.add_edge(288, 44)
        self.graph.add_edge(243, 220)
        self.graph.add_edge(93, 436)
        self.graph.add_edge(498, 260)
        self.graph.add_edge(396, 332)
        self.graph.add_edge(159, 384)
        self.graph.add_edge(84, 240)
        self.graph.add_edge(312, 228)
        self.graph.add_edge(27, 216)
        self.graph.add_edge(108, 328)
        self.graph.add_edge(348, 212)
        self.graph.add_edge(393, 512)
        self.graph.add_edge(375, 372)
        self.graph.add_edge(282, 304)
        self.graph.add_edge(333, 364)
        self.graph.add_edge(318, 364)
        self.graph.add_edge(243, 132)
        self.graph.add_edge(408, 476)
        self.graph.add_edge(99, 440)
        self.graph.add_edge(351, 204)
        self.graph.add_edge(408, 268)
        self.graph.add_edge(429, 28)
        self.graph.add_edge(114, 260)
        self.graph.add_edge(279, 92)
        self.graph.add_edge(372, 408)
        self.graph.add_edge(363, 148)
        self.graph.add_edge(285, 508)
        self.graph.add_edge(156, 28)
        self.graph.add_edge(462, 348)
        self.graph.add_edge(282, 228)
        self.graph.add_edge(21, 312)
        self.graph.add_edge(141, 24)
        self.graph.add_edge(342, 100)
        self.graph.add_edge(159, 144)
        self.graph.add_edge(81, 24)
        self.graph.add_edge(9, 96)
        self.graph.add_edge(99, 368)
        self.graph.add_edge(363, 132)
        self.graph.add_edge(90, 40)
        self.graph.add_edge(132, 140)
        self.graph.add_edge(375, 88)
        self.graph.add_edge(156, 164)
        self.graph.add_edge(366, 144)
        self.graph.add_edge(39, 496)
        self.graph.add_edge(507, 184)
        self.graph.add_edge(177, 400)
        self.graph.add_edge(39, 76)
        self.graph.add_edge(399, 472)
        self.graph.add_edge(30, 16)
        self.graph.add_edge(408, 376)
        self.graph.add_edge(507, 500)
        self.graph.add_edge(129, 404)
        self.graph.add_edge(321, 44)
        self.graph.add_edge(150, 304)
        self.graph.add_edge(375, 264)
        self.graph.add_edge(60, 488)
        self.graph.add_edge(6, 392)
        self.graph.add_edge(339, 176)
        self.graph.add_edge(483, 16)
        self.graph.add_edge(312, 324)
        self.graph.add_edge(171, 104)
        self.graph.add_edge(381, 488)
        self.graph.add_edge(186, 320)
        self.graph.add_edge(468, 152)
        self.graph.add_edge(138, 28)
        self.graph.add_edge(336, 8)
        self.graph.add_edge(264, 288)
        self.graph.add_edge(321, 52)
        self.graph.add_edge(333, 328)
        self.graph.add_edge(273, 280)
        self.graph.add_edge(462, 272)
        self.graph.add_edge(96, 480)
        self.graph.add_edge(402, 340)
        self.graph.add_edge(189, 504)
        self.graph.add_edge(183, 452)
        self.graph.add_edge(495, 120)
        self.graph.add_edge(258, 12)
        self.graph.add_edge(132, 304)
        self.graph.add_edge(447, 352)
        self.graph.add_edge(84, 216)
        self.graph.add_edge(303, 88)
        self.graph.add_edge(129, 328)
        self.graph.add_edge(246, 328)
        self.graph.add_edge(195, 292)
        self.graph.add_edge(288, 132)
        self.graph.add_edge(15, 196)
        self.graph.add_edge(171, 124)
        self.graph.add_edge(195, 116)
        self.graph.add_edge(138, 184)
        self.graph.add_edge(324, 452)
        self.graph.add_edge(27, 172)
        self.graph.add_edge(210, 236)
        self.graph.add_edge(207, 20)
        self.graph.add_edge(384, 52)
        self.graph.add_edge(258, 72)
        self.graph.add_edge(375, 280)
        self.graph.add_edge(321, 488)
        self.graph.add_edge(141, 324)
        self.graph.add_edge(111, 216)
        self.graph.add_edge(174, 328)
        self.graph.add_edge(450, 372)
        self.graph.add_edge(195, 456)
        self.graph.add_edge(282, 464)
        self.graph.add_edge(117, 304)
        self.graph.add_edge(504, 116)
        self.graph.add_edge(318, 356)
        self.graph.add_edge(51, 32)
        self.graph.add_edge(330, 8)
        self.graph.add_edge(60, 48)
        self.graph.add_edge(117, 456)
        self.graph.add_edge(54, 100)
        self.graph.add_edge(186, 484)
        self.graph.add_edge(60, 296)
        self.graph.add_edge(363, 140)
        self.graph.add_edge(171, 136)
        self.graph.add_edge(510, 396)
        self.graph.add_edge(171, 364)
        self.graph.add_edge(42, 304)
        self.graph.add_edge(330, 464)
        self.graph.add_edge(474, 32)
        self.graph.add_edge(369, 20)
        self.graph.add_edge(78, 44)
        self.graph.add_edge(234, 320)
        self.graph.add_edge(180, 64)
        self.graph.add_edge(222, 352)
        self.graph.add_edge(333, 324)
        self.graph.add_edge(456, 348)
        self.graph.add_edge(192, 208)
        self.graph.add_edge(399, 464)
        self.graph.add_edge(399, 196)
        self.graph.add_edge(471, 88)
        self.graph.add_edge(180, 100)
        self.graph.add_edge(150, 272)
        self.graph.add_edge(321, 164)
        self.graph.add_edge(216, 268)
        self.graph.add_edge(354, 224)
        self.graph.add_edge(120, 496)
        self.graph.add_edge(180, 392)
        self.graph.add_edge(249, 100)
        self.graph.add_edge(63, 268)
        self.graph.add_edge(36, 484)
        self.graph.add_edge(513, 264)
        self.graph.add_edge(324, 292)
        self.graph.add_edge(177, 504)
        self.graph.add_edge(171, 204)
        self.graph.add_edge(381, 8)
        self.graph.add_edge(171, 400)
        self.graph.add_edge(54, 468)
        self.graph.add_edge(204, 324)
        self.graph.add_edge(261, 68)
        self.graph.add_edge(183, 352)
        self.graph.add_edge(18, 264)
        self.graph.add_edge(147, 276)
        self.graph.add_edge(273, 84)
        self.graph.add_edge(408, 320)
        self.graph.add_edge(399, 236)
        self.graph.add_edge(396, 68)
        self.graph.add_edge(330, 128)
        self.graph.add_edge(393, 252)
        self.graph.add_edge(261, 252)
        self.graph.add_edge(228, 484)
        self.graph.add_edge(414, 140)
        self.graph.add_edge(219, 316)
        self.graph.add_edge(306, 472)
        self.graph.add_edge(372, 316)
        self.graph.add_edge(237, 324)
        self.graph.add_edge(441, 492)
        self.graph.add_edge(501, 68)
        self.graph.add_edge(279, 104)
        self.graph.add_edge(3, 8)
        self.graph.add_edge(255, 452)
        self.graph.add_edge(225, 364)
        self.graph.add_edge(63, 92)
        self.graph.add_edge(219, 32)
        self.graph.add_edge(153, 488)
        self.graph.add_edge(432, 268)
        self.graph.add_edge(369, 148)
        self.graph.add_edge(177, 384)
        self.graph.add_edge(366, 436)
        self.graph.add_edge(219, 388)
        self.graph.add_edge(327, 364)
        self.graph.add_edge(393, 84)
        self.graph.add_edge(456, 408)
        self.graph.add_edge(243, 68)
        self.graph.add_edge(144, 412)
        self.graph.add_edge(216, 412)
        self.graph.add_edge(177, 164)
        self.graph.add_edge(243, 280)
        self.graph.add_edge(420, 328)
        self.graph.add_edge(456, 484)
        self.graph.add_edge(93, 176)
        self.graph.add_edge(99, 344)
        self.graph.add_edge(387, 176)
        self.graph.add_edge(237, 288)
        self.graph.add_edge(501, 276)
        self.graph.add_edge(93, 232)
        self.graph.add_edge(81, 20)
        self.graph.add_edge(57, 312)
        self.graph.add_edge(372, 20)
        self.graph.add_edge(84, 60)
        self.graph.add_edge(21, 152)
        self.graph.add_edge(183, 140)
        self.graph.add_edge(51, 368)
        self.graph.add_edge(147, 12)
        self.graph.add_edge(45, 356)
        self.graph.add_edge(429, 328)
        self.graph.add_edge(192, 240)
        self.graph.add_edge(345, 416)
        self.graph.add_edge(54, 336)
        self.graph.add_edge(453, 48)
        self.graph.add_edge(12, 328)
        self.graph.add_edge(384, 296)
        self.graph.add_edge(234, 64)
        self.graph.add_edge(429, 176)
        self.graph.add_edge(183, 220)
        self.graph.add_edge(192, 112)
        self.graph.add_edge(207, 416)
        self.graph.add_edge(1, 484)
        self.graph.add_edge(456, 360)
        self.graph.add_edge(108, 240)
        self.graph.add_edge(372, 224)
        self.graph.add_edge(195, 348)
        self.graph.add_edge(240, 1)
        self.graph.add_edge(306, 416)
        self.graph.add_edge(153, 460)
        self.graph.add_edge(126, 1)
        self.graph.add_edge(450, 248)
        self.graph.add_edge(501, 356)
        self.graph.add_edge(177, 188)
        self.graph.add_edge(282, 144)
        self.graph.add_edge(483, 304)
        self.graph.add_edge(24, 32)
        self.graph.add_edge(438, 300)
        self.graph.add_edge(408, 176)
        self.graph.add_edge(69, 420)
        self.graph.add_edge(102, 356)
        self.graph.add_edge(453, 436)
        self.graph.add_edge(81, 44)
        self.graph.add_edge(330, 264)
        self.graph.add_edge(174, 36)
        self.graph.add_edge(249, 460)
        self.graph.add_edge(93, 356)
        self.graph.add_edge(300, 32)
        self.graph.add_edge(174, 204)
        self.graph.add_edge(147, 160)
        self.graph.add_edge(387, 44)
        self.graph.add_edge(129, 280)
        self.graph.add_edge(210, 292)
        self.graph.add_edge(93, 8)
        self.graph.add_edge(261, 268)
        self.graph.add_edge(138, 120)
        self.graph.add_edge(441, 284)
        self.graph.add_edge(6, 404)
        self.graph.add_edge(426, 476)
        self.graph.add_edge(342, 244)
        self.graph.add_edge(141, 264)
        self.graph.add_edge(66, 60)
        self.graph.add_edge(351, 436)
        self.graph.add_edge(78, 388)
        self.graph.add_edge(141, 276)
        self.graph.add_edge(24, 464)
        self.graph.add_edge(471, 100)
        self.graph.add_edge(48, 484)
        self.graph.add_edge(168, 204)
        self.graph.add_edge(93, 76)
        self.graph.add_edge(441, 152)
        self.graph.add_edge(447, 404)
        self.graph.add_edge(273, 468)
        self.graph.add_edge(417, 392)
        self.graph.add_edge(72, 392)
        self.graph.add_edge(303, 504)
        self.graph.add_edge(243, 416)
        self.graph.add_edge(495, 472)
        self.graph.add_edge(471, 472)
        self.graph.add_edge(228, 28)
        self.graph.add_edge(273, 120)
        self.graph.add_edge(495, 108)
        self.graph.add_edge(117, 156)
        self.graph.add_edge(321, 300)
        self.graph.add_edge(153, 124)
        self.graph.add_edge(126, 204)
        self.graph.add_edge(279, 124)
        self.graph.add_edge(75, 472)
        self.graph.add_edge(231, 72)
        self.graph.add_edge(174, 348)
        self.graph.add_edge(15, 472)
        self.graph.add_edge(90, 400)
        self.graph.add_edge(321, 208)
        self.graph.add_edge(21, 20)
        self.graph.add_edge(177, 440)
        self.graph.add_edge(465, 68)
        self.graph.add_edge(246, 452)
        self.graph.add_edge(381, 236)
        self.graph.add_edge(30, 196)
        self.graph.add_edge(120, 340)
        self.graph.add_edge(6, 152)
        self.graph.add_edge(156, 300)
        self.graph.add_edge(447, 104)
        self.graph.add_edge(327, 504)
        self.graph.add_edge(198, 328)
        self.graph.add_edge(471, 32)
        self.graph.add_edge(153, 388)
        self.graph.add_edge(219, 512)
        self.graph.add_edge(294, 260)
        self.graph.add_edge(204, 192)
        self.graph.add_edge(393, 332)
        self.graph.add_edge(510, 400)
        self.graph.add_edge(369, 444)
        self.graph.add_edge(186, 1)
        self.graph.add_edge(75, 80)
        self.graph.add_edge(492, 128)
        self.graph.add_edge(405, 404)
        self.graph.add_edge(282, 84)
        self.graph.add_edge(237, 148)
        self.graph.add_edge(255, 240)
        self.graph.add_edge(378, 288)
        self.graph.add_edge(90, 440)
        self.graph.add_edge(60, 192)
        self.graph.add_edge(321, 344)
        self.graph.add_edge(246, 48)
        self.graph.add_edge(456, 228)
        self.graph.add_edge(507, 272)
        self.graph.add_edge(294, 88)
        self.graph.add_edge(420, 444)
        self.graph.add_edge(393, 304)
        self.graph.add_edge(465, 452)
        self.graph.add_edge(51, 168)
        self.graph.add_edge(456, 96)
        self.graph.add_edge(441, 120)
        self.graph.add_edge(126, 452)
        self.graph.add_edge(246, 132)
        self.graph.add_edge(459, 172)
        self.graph.add_edge(3, 448)
        self.graph.add_edge(330, 84)
        self.graph.add_edge(33, 104)
        self.graph.add_edge(237, 208)
        self.graph.add_edge(348, 472)
        self.graph.add_edge(240, 264)
        self.graph.add_edge(246, 204)
        self.graph.add_edge(177, 284)
        self.graph.add_edge(447, 60)
        self.graph.add_edge(291, 416)
        self.graph.add_edge(231, 384)
        self.graph.add_edge(306, 128)
        self.graph.add_edge(72, 16)
        self.graph.add_edge(345, 440)
        self.graph.add_edge(21, 64)
        self.graph.add_edge(90, 204)
        self.graph.add_edge(192, 424)
        self.graph.add_edge(201, 396)
        self.graph.add_edge(351, 472)
        self.graph.add_edge(156, 488)
        self.graph.add_edge(117, 52)
        self.graph.add_edge(411, 448)
        self.graph.add_edge(426, 212)
        self.graph.add_edge(75, 196)
        self.graph.add_edge(444, 445)
        self.graph.add_edge(189, 500)
        self.graph.add_edge(456, 136)
        self.graph.add_edge(39, 512)
        self.graph.add_edge(156, 484)
        self.graph.add_edge(261, 328)
        self.graph.add_edge(456, 116)
        self.graph.add_edge(453, 364)
        self.graph.add_edge(39, 160)
        self.graph.add_edge(213, 436)
        self.graph.add_edge(330, 512)
        self.graph.add_edge(189, 124)
        self.graph.add_edge(42, 232)
        self.graph.add_edge(108, 332)
        self.graph.add_edge(486, 428)
        self.graph.add_edge(174, 36)
        self.graph.add_edge(84, 256)
        self.graph.add_edge(267, 340)
        self.graph.add_edge(327, 268)
        self.graph.add_edge(459, 100)
        self.graph.add_edge(105, 500)
        self.graph.add_edge(348, 200)
        self.graph.add_edge(174, 188)
        self.graph.add_edge(330, 508)
        self.graph.add_edge(93, 168)
        return super().setUp()

    def test_case_16(self):
        self.graph.get_all_paths()
        self.graph.get_costs()
        self.assertEqual(self.graph.get_costs(),[12, -1, 18, 24, -1, 18, -1, 12, 18, -1, -1, 24, -1, -1, 24, 24, -1, 24, -1, 12, 18, -1, -1, 18, -1, -1, 18, 24, -1, 30, -1, 12, 30, -1, -1, 18, -1, -1, 6, 24, -1, 18, -1, 18, 18, -1, -1, 24, -1, -1, 18, 24, -1, 18, -1, 24, 18, -1, -1, 18, -1, -1, 30, 12, -1, 18, -1, 24, 24, -1, -1, 18, -1, -1, 18, -1, 18, -1, 12, 18, -1, -1, 12, -1, -1, 30, 24, -1, 24, -1, 24, 6, -1, -1, 24, -1, -1, 24, 24, -1, 18, -1, 24, 24, -1, -1, 24, -1, -1, 24, 18, -1, 18, -1, 24, 24, -1, -1, 18, -1, -1, 24, 24, -1, 18, -1, 24, 18, -1, -1, 18, -1, -1, 18, 18, -1, 24, -1, 24, 18, -1, -1, 24, -1, -1, 18, 24, -1, 24, -1, 24, 18, -1, -1, 18, -1, -1, 24, 12, -1, 30, -1, 12, -1, -1, -1, 12, -1, -1, 18, 12, -1, 24, -1, 12, 18, -1, -1, 18, -1, -1, 24, 24, -1, 18, -1, 24, 24, -1, -1, 18, -1, -1, 24, 24, -1, 18, -1, 24, 24, -1, -1, 18, -1, -1, 18, 24, -1, 18, -1, 24, 18, -1, -1, 18, -1, -1, 6, 18, -1, 18, -1, 24, 18, -1, -1, 24, -1, -1, 24, 12, -1, 18, -1, 12, 18, -1, -1, 18, -1, -1, 24, 24, -1, 24, -1, 24, 18, -1, -1, 18, -1, -1, 24, 18, -1, 18, -1, 24, 18, -1, -1, 18, -1, -1, 18, 24, -1, 30, -1, 24, 18, -1, -1, 12, -1, -1, 18, 24, -1, 18, -1, 24, 30, -1, -1, 12, -1, -1, 24, 24, -1, 18, -1, 18, 18, -1, -1, 12, -1, -1, 24, 24, -1, 18, -1, 24, 18, -1, -1, 18, -1, -1, 18, 12, -1, 18, -1, 24, 18, -1, -1, 18, -1, -1, 18, 24, -1, 18, -1, 24, 24, -1, -1, 18, -1, -1, 18, 24, -1, 18, -1, 24, 18, -1, -1, 18, -1, -1, 18, 24, -1, 18, -1, 12, 24, -1, -1, 18, -1, -1, 24, 24, -1, 18, -1, 24, 18, -1, -1, 18, -1, -1, 18, 24, -1, 18, -1, 24, 18, -1, -1, 18, -1, -1, 18, 12, -1, 18, -1, 24, 18, -1, -1, 24, -1, -1, 18, 18, -1, 18, -1, 12, 18, -1, -1, 18, -1, -1, 24, 24, -1, 30, -1, 24, 24, -1, -1, 18, -1, -1, 24, 12, -1, 30, -1, 24, 18, -1, -1, 24, -1, -1, -1, 12, -1, 6, -1, 24, 18, -1, -1, 18, 24, -1, 18, 24, -1, 24, -1, 24, 18, -1, -1, 18, -1, -1, 18, 12, -1, 24, -1, 24, 30, -1, -1, 24, -1, -1, 18, 24, -1, 18, -1, 24, 24, -1, -1, 24, -1, -1, 18, 18, -1, 18, -1, 18, 30, -1, -1, 24, -1, -1, 24, 12, -1, 30, -1, 24, 18, -1, -1, 18, -1, -1, 24, 24, -1, 18, -1, 12, 24, -1, -1])

    def tearDown(self):
        del self.START
        del self.graph
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
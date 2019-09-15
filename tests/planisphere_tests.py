import unittest
from planisphere import *


class BasicTestCase(unittest.TestCase):

    def test_room(self):
        gold = Room("GoldRoom",
                    """В этой комнате полно золота, которое можно украсть. 
                    Здесь есть дверь с выходом на север.""")
        self.assertEqual(gold.name, "GoldRoom")
        self.assertEqual(gold.paths, {})

    def test_room_paths(self):
        center = Room("Center", "Тестирование центральной комнаты.")
        north = Room("North", " Тестирование северной комнаты.")
        south = Room("South", " Тестирование южной комнаты.")

        center.add_paths({'north': north, 'south': south})
        self.assertEqual(center.go('north'), north)
        self.assertEqual(center.go('south'), south)

    def test_map(self):
        start = Room("Start", "Вы можете идти на запад и провалиться в яму.")
        west = Room("Trees", "Здесь есть деревья и вы можете отправиться на восток.")
        down = Room("Dungeon", "Здесь темно и вы можете подняться вверх.")

        start.add_paths({'west': west, 'down': down})
        west.add_paths({'east': start})
        down.add_paths({'up': start})

        self.assertEqual(start.go('west'), west)
        self.assertEqual(start.go('west').go('east'), start)
        self.assertEqual(start.go('down').go('up'), start)

    def test_gothon_game_map(self):
        start_room = load_room(rooms, START)
        self.assertEqual(start_room.go('shoot!'), rooms.get('generic_death'))
        self.assertEqual(start_room.go('dodge!'), rooms.get('generic_death'))
        self.assertEqual(start_room.go('anywhere'), None)

        room = start_room.go('tell a joke')
        self.assertEqual(room, rooms.get('laser_weapon_armory'))


        room2 = load_room(rooms, 'laser_weapon_armory')
        self.assertEqual(room2.go('*'), rooms.get('generic_death'))
        self.assertEqual(room2.go('anywhere'), None)

        next_room = room2.go('0132')
        self.assertEqual(next_room, rooms.get('the_bridge'))


        room3 = load_room(rooms, 'the_bridge')
        self.assertEqual(room3.go('throw the bomb'), rooms.get('generic_death'))
        self.assertEqual(room3.go('anywhere'), None)

        next_room = room3.go('slowly place the bomb')
        self.assertEqual(next_room, rooms.get('escape_pod'))


        room4 = load_room(rooms, 'escape_pod')
        self.assertEqual(room4.go('anywhere'), None)

        room = room4.go('2')
        self.assertEqual(room, rooms.get('the_end_winner'))

        room = room4.go('*')
        self.assertEqual(room, rooms.get('the_end_loser'))

if __name__ == '__main__':
    unittest.main()
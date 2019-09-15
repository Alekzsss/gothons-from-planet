import unittest
from planisphere_ru import *


class BasicTestCase(unittest.TestCase):

    def test_gothon_game_map(self):
        start_room = load_room(rooms, START)
        self.assertEqual(start_room.go('shoot!'), rooms.get('generic_death_ru'))
        self.assertEqual(start_room.go('dodge!'), rooms.get('generic_death_ru'))
        self.assertEqual(start_room.go('anywhere'), None)

        room = start_room.go('tell a joke')
        self.assertEqual(room, rooms.get('laser_weapon_armory_ru'))


        room2 = load_room(rooms, 'laser_weapon_armory_ru')
        self.assertEqual(room2.go('*'), rooms.get('generic_death_ru'))
        self.assertEqual(room2.go('anywhere'), None)

        next_room = room2.go('0132')
        self.assertEqual(next_room, rooms.get('the_bridge_ru'))


        room3 = load_room(rooms, 'the_bridge_ru')
        self.assertEqual(room3.go('throw the bomb'), rooms.get('generic_death_ru'))
        self.assertEqual(room3.go('anywhere'), None)

        next_room = room3.go('slowly place the bomb')
        self.assertEqual(next_room, rooms.get('escape_pod_ru'))


        room4 = load_room(rooms, 'escape_pod_ru')
        self.assertEqual(room4.go('anywhere'), None)

        room = room4.go('2')
        self.assertEqual(room, rooms.get('the_end_winner_ru'))

        room = room4.go('*')
        self.assertEqual(room, rooms.get('the_end_loser_ru'))

if __name__ == '__main__':
    unittest.main()
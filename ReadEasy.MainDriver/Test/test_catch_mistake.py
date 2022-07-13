import sys
sys.path.insert(0, '../')

import unittest
from db.database_manager import DatabaseManager
from src.catch_mistake import CatchMistake

class TestCatchMistake(unittest.TestCase):

    # def test_read_correctly(self):
    #     tempDB = DatabaseManager('../db/temp.db')

    #     test = 'i am a student'.split()
    #     valid = 'i am a student'.split()

    #     CM = CatchMistake(test, valid, tempDB)

    #     self.assertTrue(CM.catch())

    # def test_list_of_same_lenght_but_one_word_read_incorrectlty(self):
    #     tempDB = DatabaseManager('../db/temp.db')

    #     test = ['i', 'am', 'a', 'teacher']
    #     valid = ['i', 'am', 'a', 'student']
    #     CM = CatchMistake(test, valid, tempDB)
    #     self.assertFalse(CM.catch())

    # def test1(self):
    #     tempDB = DatabaseManager('../db/temp.db')

    #     test = 'i knew the teacher that the girl adores her'.split()
    #     valid = 'the teacher knew that the girl adores her'.split()
    #     CM = CatchMistake(test, valid, self._tempDB)
    #     correct = 'the teacher that the girl adores her'.split()
    #     added = ['i']
    #     missed = []
    #     wrong = []
    #     placement = ['knew']

    def test2(self):
        tempDB = DatabaseManager('../db/temp.db')

        test = 'i am a student at a school'.split()
        valid = 'i am a teacher at a university'.split()
        CM = CatchMistake(test, valid, tempDB).catch()
        correct = 'i am a at a'.split()
        added = []
        missed = []
        expected_replacements = [['teacher', 'student'], ['university', 'school']]
        placement = []

        replacements = tempDB.retrieve_replacements()

        tempDB.purge_table('Replacements')
        tempDB.closeConnection()

        self.assertEqual(replacements, expected_replacements)

    def test3(self):
        tempDB = DatabaseManager('../db/temp.db')

        test = 'the actor is charming accusative case marker the audience'.split()
        valid = 'the actor charmed accusative case marker the audience'.split()
        CM = CatchMistake(test, valid, tempDB).catch()
        correct = 'the actor accusative case marker the audience'.split()
        added = ['is']
        missed = []
        wrong = ['charmed']
        placement = []

        expected_replacements = [['charmed', 'charming']]

        replacements = tempDB.retrieve_replacements()
        tempDB.purge_table('Replacements')
        tempDB.closeConnection()

        self.assertEqual(replacements, expected_replacements)

    # def test4(self):
    #     tempDB = DatabaseManager('../db/temp.db')

    #     test = 'yosi noticed that michal was offended'.split()
    #     valid = 'yosi fell asleep and michal was offended'.split()
    #     CM = CatchMistake(test, valid)
    #     correct = 'yosi michal was offended'.split()
    #     added = 'noticed that'.split()
    #     missed = 'fell asleep and'.split()
    #     wrong = ['charmed']
    #     placement = []



if __name__ == '__main__':
    unittest.main()
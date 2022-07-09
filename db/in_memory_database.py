import sqlite3 as sl

class InMemoryDatabase:
    def __init__(self):
        self._conn = sl.connect("../db/temporary.db")
        self._c = self._conn.cursor()

    def createTables(self):
        # Create WrongWords Table
        self._c.execute('''CREATE TABLE IF NOT EXISTS WrongWords (
            CorrectWord text NOT NULL,
            WrongWord text NOT NULL,
            Score real DEFAULT 0,
            TotalCount INT DEFAULT 0,
            PRIMARY KEY (CorrectWord, WrongWord)
        )''')

    def addToWrongWords(self, correct_word, wrong_word, total_count):
        insert_commad = f'''INSERT INTO WrongWords (CorrectWord, WrongWord, Score,TotalCount)
        VALUES ('{correct_word}', '{wrong_word}', 1, {total_count})
        ON CONFLICT(CorrectWord, WrongWord) DO UPDATE SET Score=Score+1, TotalCount=TotalCount+{total_count}'''

        self._c.execute(insert_commad)

    def closeConnection(self):
        self._conn.commit()
        self._conn.close()

if __name__ == '__main__':
    DM = InMemoryDatabase()
import sqlite3 as sl
conn = sl.connect('AssistiveReading.db')
c = conn.cursor()

class DatabaseManager:
    def __init__(self):
        pass

    def createTables(self):
        # Create WrongWords Table
        c.execute('''CREATE TABLE IF NOT EXISTS WrongWords (
            CorrectWord text NOT NULL,
            WrongWord text NOT NULL,
            Score real DEFAULT 0,
            TotalCount INT DEFAULT 0,
            PRIMARY KEY (CorrectWord, WrongWord)
        )''')
        conn.commit()
        conn.close()

    def addToWrongWords(self, correct_word, wrong_word, total_count):
        insert_commad = f'''INSERT INTO WrongWords (CorrectWord, WrongWord, Score,TotalCount)
        VALUES ('{correct_word}', '{wrong_word}', 1, {total_count})
        ON CONFLICT(CorrectWord, WrongWord) DO UPDATE SET Score=Score+1, TotalCount=TotalCount+{total_count}'''

        c.execute(insert_commad)
        conn.commit()
        conn.close()

if __name__ == '__main__':
    DM = DatabaseManager()
    DM.createTables()
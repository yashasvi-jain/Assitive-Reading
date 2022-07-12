import sqlite3 as sl

class DatabaseManager:
    def __init__(self, connection: str):
        self._conn = sl.connect(connection)
        self._c = self._conn.cursor()

    def create_tables(self):
        # Create WrongWords Table
        self._c.execute('''CREATE TABLE IF NOT EXISTS WrongWords (
            CorrectWord text NOT NULL,
            WrongWord text NOT NULL,
            Score real DEFAULT 0,
            TotalCount INT DEFAULT 0,
            PRIMARY KEY (CorrectWord, WrongWord)
        )''')

    def add_to_wrong_words(self, correct_word: str, wrong_word: str, total_count: int):
        insert_commad = f'''INSERT INTO WrongWords (CorrectWord, WrongWord, Score,TotalCount)
        VALUES ('{correct_word}', '{wrong_word}', 1, {total_count})
        ON CONFLICT(CorrectWord, WrongWord) DO UPDATE SET Score=Score+1, TotalCount=TotalCount+{total_count}'''

        self._c.execute(insert_commad)

    def purge_database(self, table: str):
        """
        Removes from all the data from a given table.
        Parametes: {str} table - name of the table
        """
        purge_command = f'''DELETE FROM {table}'''
        self._c.execute(purge_command)

    def closeConnection(self):
        """
        Commits all changes to the database and then closes the connection for a paticular instance.
        """
        self._conn.commit()
        self._conn.close()

if __name__ == '__main__':
    DM = DatabaseManager('../db/AssistiveReading.db')
    DM.createTables()
    DM.closeConnection()
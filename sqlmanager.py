import sqlite3


class SQLManager:
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)

    def create_tables(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Quizz (
            quizz_id INTEGER PRIMARY KEY,
            quizz_name TEXT NOT NULL,
            description TEXT
            )
        ''')
        cursor.execute('''
                      CREATE TABLE IF NOT EXISTS Questions (
                           question_id INTEGER PRIMARY KEY,
                           quiz_id INTEGER,
                           content TEXT,
                           FOREIGN KEY (quiz_id) REFERENCES Quizz(quiz_id)
                      );
                      ''')
        cursor.execute('''
                      CREATE TABLE IF NOT EXISTS Answers (
                           answer_id INTEGER PRIMARY KEY,
                           question_id INTEGER,
                           content TEXT,
                           is_right BOOLEAN,
                           FOREIGN KEY (question_id) REFERENCES Questions(question_id)
                      );
                      ''')
        cursor.close()
        self.db.commit()


    def add_quizz(self, name, description):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO Quizz (quizz_name,description) VALUES (?, ?)
        """, [name, description])
        cursor.close()
        self.db.commit()


    def add_question(self, quiz_id, content):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO Questions (quiz_id,content) VALUES (?, ?)
        """, [quiz_id, content])
        cursor.close()
        self.db.commit()

    def add_answer(self, question_id, content, is_right):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO Answers (question_id,content,is_right) VALUES (?, ?, ?)
        """, [question_id, content,is_right])
        cursor.close()
        self.db.commit()

    def select_quizzes(self):
        cursor = self.db.cursor()
        cursor.execute("""
                    SELECT * FROM Quizz;
                """)
        records = cursor.fetchall()
        cursor.close()
        self.db.commit()
        return records



    def select_questions(self, quizz_id):
        cursor = self.db.cursor()
        cursor.execute("""
                            SELECT * FROM Questions WHERE quiz_id = ?;
                        """, [quizz_id])
        records = cursor.fetchall()
        cursor.close()
        self.db.commit()
        return records

    def select_answers(self, question_id):
        cursor = self.db.cursor()
        cursor.execute("""
                            SELECT * FROM Answers WHERE question_id = ?;
                        """, [question_id])
        records = cursor.fetchall()
        cursor.close()
        self.db.commit()
        return records
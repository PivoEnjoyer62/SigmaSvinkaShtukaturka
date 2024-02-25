from sqlmanager import SQLManager

sql = SQLManager("quizz.db")
sql.create_tables()

sql.add_quizz("SigmaSvinka", "Quizz about Sanya Forgottentimsov")
sql.add_question(1, "Sigma Svinka?")
sql.add_answer(1, "No, I am not. I'm Sigma Shtukaturka", True)
sql.add_answer(1, "Yes, I am.", False)

sql.add_quizz("Sanya Forgottentimsov", "Quizz about Sanya Forgottentimsov")
sql.add_question(2, "Sigma Sanya?")
sql.add_answer(2, "No, I am not. I'm Sigma Shtukaturka", False)
sql.add_answer(2, "Yes, I am.", True)

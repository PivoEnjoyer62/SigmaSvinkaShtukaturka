from flask import Flask, render_template, session, redirect, url_for
from sqlmanager import SQLManager


app = Flask(__name__)
app.secret_key = "SigmaSvinotaHryusha"


@app.route('/')
def index():
    return render_template("main.html")


@app.route('/quizzes')
def quizzes():
    sql = SQLManager("quizz.db")
    quizzes = sql.select_quizzes()
    return render_template("quizzes.html", quizzes=quizzes)


@app.route("/question/<int:quizz_id>")
def get_questions(quizz_id):
    sql = SQLManager("quizz.db")
    questions = sql.select_questions(quizz_id)
    session["questions"] = questions
    session["current_question"] = 0
    return redirect(url_for("show_question", quizz_id=quizz_id))


@app.route("/question/<int:quizz_id>/show_question")
def show_question(quizz_id):
    sql = SQLManager("quizz.db")
    current = session["current_question"]
    question= session["questions"][current]
    answers = sql.select_answers(question[0])
    return render_template("question.html", question= question, answers=answers, quizz_id=quizz_id)


@app.route("/question/<int:quizz_id>/answer", methods=["POST"])
def answer_func(quizz_id):
    sql = SQLManager("quizz.db")

    return "Answered"


if __name__ == "__main__":
    app.run()


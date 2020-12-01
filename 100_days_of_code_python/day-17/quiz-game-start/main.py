from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain
question_bank = []
for k in question_data:
    q_text = k["text"]
    q_answer = k["answer"]
    question = Question(q_text,q_answer)
    question_bank.append(question)

quiz =Quiz_brain(question_bank)
quiz.next_question()

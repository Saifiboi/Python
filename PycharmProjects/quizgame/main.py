from quiz_brain import QuizBrain
from question_model import Question_bank

new_ques = QuizBrain(Question_bank)
score = 0
total_score = 0
while new_ques.still_have_ques():
    res = new_ques.next_ques()
    total_score += 1
    if not res:
        print("You Got it Wrong!")
    else:
        score += 1
    print(f"Your Current Score is:{score}/{total_score}\n\n")
if not new_ques.still_have_ques():
    print("Quiz Complete!Hurrah")

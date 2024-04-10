from data import question_data


class Question:
    def __init__(self,d_text, ans):
        self.text = d_text
        self.answer = ans


Question_bank = []
for new_ques in question_data:
    Question_bank.append(Question(new_ques["text"], new_ques["answer"]))

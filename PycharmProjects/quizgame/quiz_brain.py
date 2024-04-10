class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list

    def next_ques(self):
        usr_ans = input(
            f"Q.{self.question_no + 1}: {self.question_list[self.question_no].text}? True or false:").lower()
        if usr_ans.lower() != self.question_list[self.question_no].answer.lower():
            return False
        self.question_no += 1
        return True

    def still_have_ques(self):
        return self.question_no < len(self.question_list)

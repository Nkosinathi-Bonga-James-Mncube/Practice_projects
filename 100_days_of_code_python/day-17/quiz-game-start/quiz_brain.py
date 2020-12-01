
class Quiz_brain:
    def __init__(self,question_list):
        self.question_number =0
        self.question_list = question_list
    def next_question(self):
        count = 1
        correct = 0
        while count <=len(self.question_list):
            current_question = self.question_list[self.question_number]
            self.question_number +=1
            user_answer=input(f"Q.{self.question_number}:{current_question.text} (true/false?):").lower()
            if (user_answer == current_question.answer.lower()):
                correct +=1
                print("Correct")
                print(f"You current score is :",correct,"/",count)
                print(" ")
            else:
                print("Incorrect")
                print("Corrent answer was :" , current_question.answer)
                print(f"You current score is :",correct,"/",count)
                print(" ")
            count +=1
        print("You have finsished the quiz")
        print("Total is " , str(correct)+"/"+str(count))
import MySql
import random

m = MySql.mysql()


#m.add_question("What is 1+1 ? ","2","3","4","5","2")
#m.add_question("What is love ?","KYB","BL","SL","AE","KYB")
#m.add_question("Who sings smells like teen spirit ? ","Kurt Cobain","Yuksel Bilgin","Johnny Cash","Kenan Dogulu","Kurt Cobain")
#m.add_question("Which one is not a programming language ? ","Python","Java","C++","HTML","HTML")
#m.add_question("Best programming comptetion site ? ","Hackerearth","Hackerrank","Hackerone","SoloLearn","Hackerearth")
#m.add_question("Which one is machine learning algorithm ? ","Decision Tree Algorithm","Kruskal Algorithm","Bubble Sort Algorithm","Huffman Algorithm","Decision Tree Algorithm")
#m.add_question("What is Parfume ? ","A programming language","Women name","Stuff for smelling good","Disease","Stuff for smelling good")

class Competitor():

    def __init__(self,nickname):
        self.nickname = nickname
        self.true_ans = 0



#Make random quizes is easy command
class Quiz():

    def __init__(self,qList,number_of_questions):
        create_quiz = set()
        while(len(create_quiz)<number_of_questions):
            create_quiz.add(random.choice(qList))
        #while loop gets random question's from given qList
        #we declared set because we don't want same question in quiz.
        self.qList = create_quiz


    def take_the_quiz(self):
        co = Competitor("jackie")
        count = 1
        for i in self.qList:
            print(str(count)+")",i)
            count+=1
            if i.answer == input():
                print("Congratulations True Answer\n")
                co.true_ans +=1
            else:
                print("Sorry False Answer\n")

        print("Winner : " + co.nickname +"\nTrue Answers :" ,co.true_ans)
    def __str__(self):

        print("""
        **********************************************************************************************************************************************
                                        WELCOME TO QUIZ NIGHTTTTT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


                                        **************************************************************

                                        """)

        count = 1
        for i in self.qList:
            print(str(count)+")",i)
            count+=1

        return ""


#Add list of questions to make quiz
quiz = Quiz(m.get_question(),7)
m.unlink()
print(quiz)

quiz.take_the_quiz()

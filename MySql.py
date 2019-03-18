import mysql.connector as MySQL


c =  MySQL.connect(user = 'user',password='password',auth_plugin="mysql_native_password")
cr = c.cursor()
cr.execute("CREATE DATABASE IF NOT EXISTS QuizMaker")
c.close()
try:
    con = MySQL.connect(user = 'user',password='password',auth_plugin="mysql_native_password",database='QuizMaker')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Answer(AnsID INT AUTO_INCREMENT PRIMARY KEY,Ans TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Question(QsID INT AUTO_INCREMENT PRIMARY KEY,Qs TEXT,QsA TEXT,QsB TEXT,QsC TEXT,QsD TEXT,AnsID INT,FOREIGN KEY (AnsID) REFERENCES Answer(AnsID))")
    #looks like we dont need competitor table.Comment line if we need it
    #cursor.execute("CREATE TABLE IF NOT EXISTS Competitor(CoID INT AUTO_INCREMENT PRIMARY KEY,Co VARCHAR(30))")

except MySQL.Error as err:
    print("Something went wrong: {}".format(err))


#Question's should in another python file
class Question():
    _counter = 0
    def __init__(self,question,qA,qB,qC,qD,answer):
        Question._counter +=1
        self.id = Question._counter
        self.question = question
        self.qA = qA
        self.qB = qB
        self.qC = qC
        self.qD = qD
        self.answer = answer

    def __str__(self):
        return self.question+"\n"+"A) "+self.qA +"\nB) "+self.qB+"\nC) " +self.qC+"\nD) "+self.qD +"\n "+"\n"


#mysql commands
class mysql():

    def __init__(self):
        self.con = MySQL.connect(user='root',password = "s0ulfly1978",auth_plugin="mysql_native_password",database = "QuizMaker")
        self.cursor = self.con.cursor()
        print("Don't forget to unlik mysql object. If you dont unlink it connection won't close!\n")

    def unlink(self):
        self.con.close()
        print("\n\nUnlinked. Connection closed now.")


    def add_question(self,question,qA,qB,qC,qD,answer):
        query = "INSERT INTO Answer (AnsID,Ans) VALUES (%s,%s)"
        self.cursor.execute(query,[None,answer])
        self.con.commit()
        print(self.cursor.rowcount , "Answer Record Inserted")

        query = "SELECT AnsID FROM Answer WHERE Ans='"+answer+"'"

        self.cursor.execute(query)
        ans_id = self.cursor.fetchall()


        query = "INSERT INTO Question (QsID,Qs,QsA,QsB,QsC,QsD,AnsID) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        value = (None,question,qA,qB,qC,qD,ans_id[0][0])
        self.cursor.execute(query,value)
        self.con.commit()

        print(self.cursor.rowcount , "Question Record Inserted")
        #unlink()

    def get_question(self):
        query = "SELECT Question.Qs,Question.QsA,Question.QsB,Question.QsC,Question.QsD,Answer.Ans FROM Question INNER JOIN Answer ON Question.AnsID=Answer.AnsID"
        self.cursor.execute(query)
        questionL = self.cursor.fetchall()
        questions = []
        for i in questionL:
            questions.append(Question(i[0],i[1],i[2],i[3],i[4],i[5]))

        return questions



#my = mysql()
#my.add_question("Mini mini bir kus","Konmustu","geceler","pencere","bos","Konmustu")
#my.unlink

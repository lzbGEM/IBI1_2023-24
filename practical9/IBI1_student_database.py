class students:# Define a class named 'students' to represent a student with various attributes
    def __init__(self,name,major,code_portfolio_score,group_project_score,exam_score):
        self.name=name
        self.major=major
        self.code_portfolio_score=code_portfolio_score
        self.group_project_score=group_project_score
        self.exam_score=exam_score
    def Print(self):# Method to print the student's information
        print(self.name,self.major, self.code_portfolio_score,self.group_project_score,self.exam_score)
# Create an instance of the 'students' class 
a=students("Li Zhibo","BMS",100,100,100)
a.Print()#use Print

    


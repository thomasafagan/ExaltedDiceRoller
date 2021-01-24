from random import randint
class output:
    def __init__(self, amountToRoll, doubles = 10, threshold = 7):
        self.dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
        self.successes = 0
        self.result = ""
        self.RollDice(amountToRoll, doubles, threshold)

    def RollDice(self, amountToRoll, doubles, threshold):
        for i in range (0,amountToRoll):
            temp=(randint(1,10))
        
            self.result+=str(temp)+", "
            self.dict[temp]=self.dict[temp]+1
            if(temp>=threshold):
                if(temp>=doubles):
                    self.successes+=2
                else:
                    self.successes+=1
        

        
    
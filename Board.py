
import random
from copy import copy, deepcopy
import string
import sys
# / *********************************************************************
#  * Name:  Michael D'Alessio
#      * Project:  Build up domino
#      * Date:  11/2014
# ********************************************************************* */

class Singleton:


    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
@Singleton
class Board:
    # /* *********************************************************************
# Function Name: __init__
# Purpose: To Inatilze data memebers 

#Variables:
        # elf.black_array, Array holding unshuffled deck
        # self.white_array,Array holding unshuffled deck
        # self.white_count , int holding white count
        # self.black_score , int holing black score
        # self.white_score , int holding white score
        # self.black_stack , list containing black stack
        # self.white_stack , list containing white stack
        # self.black_hand   , list containing black hand
        # self.white_hand , list containing whtie hand
        # self.white_boneyard, list containing shuffled deck
        # self.black_boneyard, list containing shuffled deck
        # self.white_rounds_won, int holding white rounds won
        # self.black_rounds_won , int holding black rounds won
# ********************************************************************* */
    def __init__(self):
        self.black_array=["B00", "B01", "B02", "B03", "B04", "B05", "B06", "B11", "B12", "B13", "B14", "B15", "B16", "B22", "B23", "B24", "B25", "B26", "B33", "B34", "B35", "B36", "B44", "B45", "B46", "B55", "B56", "B66"]
        self.white_array=["W00", "W01", "W02", "W03", "W04", "W05", "W06", "W11", "W12", "W13", "W14", "W15", "W16", "W22", "W23", "W24", "W25", "W26", "W33", "W34", "W35", "W36", "W44", "W45", "W46", "W55", "W56", "W66"]
        self.white_count = 0
        self.black_score = 0
        self.white_score = 0
        self.black_stack = []
        self.white_stack = []
        self.black_hand = []
        self.white_hand = []
        self.white_boneyard=[]
        self.black_boneyard=[]
        self.white_rounds_won = 0
        self.black_rounds_won = 0
    
    
    computer_output = "null"

    
# /* *********************************************************************
# Function Name: SHuffle Array
# Purpose: To Shuffle one array
# Parameters:
#             char x, which is either 'W' or 'B' to indicate which array it should shuffle.
# Algorithm:
#             1) Call lib function or shuffle arrays
# ********************************************************************* */

    def Shuffle_array(self,x):
        board=Board.Instance()
        if (x == 'B' or x == 'b'):
           random.shuffle(board.black_boneyard)
            
        elif (x == 'W' or x == 'w'):
            random.shuffle(board.white_boneyard)
            
        
    
#     /* *********************************************************************
# Function Name: Shuffle_arrays()
# Purpose: To shuffle both arrays
# Parameters: none

# Local Variables:

# Algorithm:
#            1) needed to call srand(time(NULL)) in not the above function or both shuffled arrays returned the same values.
# ********************************************************************* */

    def Shuffle_arrays(self):
        board=Board.Instance()
        board.Shuffle_array('B')
        board.Shuffle_array('W')
#     /* *********************************************************************
# Function Name: Draw Domino
# Purpose: To take an int from the above arrays
# Parameters:
#             int PLayer_count, is using one of the above counts to black_count/white_count to indicate which postion you should draw from.
# 			char Type, 'W' or 'B' to indicate which array
# Algorithm:
#                       1)add to white or black count
# 					  2)return the int in the postion of the above parameter.
# ********************************************************************* */

    def Draw_domino(self,Type):
        board=Board.Instance()
        if (Type == 'W' or Type == 'w'):
            return board.white_boneyard[0]
        if (Type == 'B' or Type == 'b'):
            return board.black_boneyard[0]
        else:
            return "0"
        
    # /* *********************************************************************
    # Function Name: Get_score_black
    # Purpose: Look for all strings in both stacks that start with 'B' or 'b' return pip value of all those strings.

    # Return Value: pip value of black in both stacks

    # Algorithm:
    #                       1) loop through the stack
    #                       2)look for at 0 postion of string 'B' or 'b'
    #                       3)replace b or B with 0
    #                       4) turn string into int
    #                       5)add the digits of the int with a while loop.
    #                       6)do this to both stacks
    # ********************************************************************* */
    def get_score_black(self):
        board=Board.Instance()
        total = 0
        for i in range(0,6):
            x = board.white_stack[i]
            if (x[0] == 'B'):
                p = x.replace(x[0], '0')
                value = int(p)
                while (value > 0):
                    total += value % 10
                    value /= 10
                
            

        
        for i in range(0,6):
            x = board.black_stack[i]
            if (x[0] == 'B'):
                p = x.replace(x[0], '0')
                value = int(p)
                while (value > 0):
                    total += value % 10
                    value /= 10
                
        return total
    
    # /* *********************************************************************
    # Function Name: Get_score_white
    # Purpose: Look for all strings in both stacks that start with 'W' or 'w' return pip value of all those strings.

    # Return Value: pip value of all white in both stacks

    # Algorithm:
    #                       1) loop through the stack
    #                       2)look for at 0 postion of string 'W' or 'w'
    #                       3)replace w or W with 0
    #                       4) turn string into int
    #                       5)add the digits of the int with a while loop.
    #                       6)do this to both stacks
    # ********************************************************************* */
    def get_score_white(self):
        board=Board.Instance()
        total = 0
        for i in range(0,6):
            x = board.white_stack[i]
            if (x[0] == 'W'):
                p = x.replace(x[0], '0')
                value = int(p)
                while (value > 0):
                    total += value % 10
                    value /= 10
                
            

        
        for i in range(0,6):
            x = board.black_stack[i]
            if (x[0] == 'W'):
                p = x.replace(x[0], '0')
                value = int(p)
                while (value > 0):
                    total += value % 10
                    value /= 10
        return total
#     /* *********************************************************************
# Function Name: deal_stack_white
# Purpose: Use draw domino fucntion to set white_stack[i] to a value
# ********************************************************************* */

    def deal_stack_white(self,count):
        board=Board.Instance()
        del board.white_stack[:]
        for i in range (count):
           board.white_stack.append( board.Draw_domino( 'W'))
           board.white_boneyard.pop(0)

        
    

#         /* *********************************************************************
# Function Name: deal_stack_black
# Purpose: Use draw domino fucntion to set black_stack[i] to a value
# ********************************************************************* */

    def deal_stack_black(self,count):
        board=Board.Instance()
        del board.black_stack[:]
        for i in range (count):
            board.black_stack.append(board.Draw_domino('B'))
            board.black_boneyard.pop(0)
        
    
   #  /* *********************************************************************
   # Function Name: deal_hand_white
   # Purpose: Use draw domino fucntion to set white_hand[i] to a value
   # ********************************************************************* */
    def deal_hand_white(self,count):
        board=Board.Instance()
        del board.white_hand[:] #empty out list
        for i in range (count):
            board.white_hand.append(board.Draw_domino( 'W'))
            board.white_boneyard.pop(0)

    # /* *********************************************************************
    #   Function Name: deal_hand_black
    #   Purpose: Use draw domino fucntion to set black_hand[i] to a value
    #   ********************************************************************* */
    def deal_hand_black(self,count):
        board=Board.Instance()
        del board.black_hand[:] #empty out list
        for i in range (count):
            board.black_hand.append(board.Draw_domino('B'))
            board.black_boneyard.pop(0)




#     /* *********************************************************************
# Function Name: addwhite_score
# Purpose: To be called in the load function, which caluclate the score and add it to the current score.
# Parameters:
#             int value, some value to add to score
# ********************************************************************* */


    def addwhite_score(self,value):
        board=Board.Instance()
        board.white_score += int(value)

    
   #  /* *********************************************************************
   # Function Name: addBlack_score
   # Purpose: To be called in the load function, which caluclate the score and add it to the current score.
   # Parameters:
   #             int value, some value to add to score
   # ********************************************************************* */
    def addblack_score(self,value):
        board=Board.Instance()
        board.black_score += int(value)
    
 


# /* *********************************************************************
# Function Name: set_white_stack
# Parameters: Count, Postion. String value, that will replace the current value
# Purpose: used in placing domino function to change the value of a stack string to value
# ********************************************************************* */

    def set_white_stack(self,count,value):
        board=Board.Instance()
        board.white_stack[count] = value
    

    # /* *********************************************************************
    # Function Name: set_black_stack
    # Parameters: Count, Postion. String value, that will replace the current value
    # Purpose: used in placing domino function to change the value of a stack string to value
    # ********************************************************************* */
    def set_black_stack(self,count,  value):
        board=Board.Instance()
        board.black_stack[count] = value
    


    
#     /* *********************************************************************
# Function Name: set_computer_output
# Purpose: set computer_output(a string to be called in main) to set a textview after computer goes.
# Parameters:
#              int a,Computer hand postion ,int  b:postion in the stack, char y: char to indicate which stack
# ********************************************************************* */

    def set_computer_output(self,a,  b, y) :
        board=Board.Instance()
        White_card = "null"
        Stack_card = "null"
        if (y == 'B'):
            White_card = board.Return_white_hand(a)
            Stack_card = board.return_black_stack(b)
        elif (y == 'W'):
            White_card = board.Return_white_hand(a)
            Stack_card = board.Return_white_stack(b)
        
        board.computer_output = "White placed: " + White_card + " on: " + Stack_card
    
#      /* *********************************************************************
# Function Name: getcomputer_output
# Purpose: return computer_output(a string to be called in main) to set a textview after computer goes.
# ********************************************************************* */

    def getComputer_output(self):
        board=Board.Instance()
        return board.computer_output
    
   #  /* *********************************************************************
   # Function Name: skip_computer_output()
   # Purpose: set computer_output(a string to be called in main) to set a textview after computer goes, to skip
   # ********************************************************************* */
    def skip_computer_output(self) :
        board=Board.Instance()
        board.computer_output = "Computer skipped"
    

    

#     /* *********************************************************************
# Function Name: Who_goes_first()
# Purpose: See who has higher tiles and goes first
# Return Value:  W= White goes first, B=Black goes first, N= None higher reshuffle decks try again.
# Local Variables:
#             W, digit value
#             B, digit value
# 			W_pip_value,total digits value
# 			B_pip_value, total digits value
# Algorithm:
#                       1)Before using place domino, check the array of ints white/black at postion 0.
# 					  2)Add the digits to the to W_pip_value or B_pip_value accordingly.
# 					  3)then Return W or B or N
# 					  4) this will be intrepreted in the game class, W= White goes first, B=Black goes first, N= None higher reshuffle decks try again.
# ********************************************************************* */
    def Who_goes_first(self) :
        board=Board.Instance()
        W_pip_value = 0
        B_pip_value = 0
        temp_B = board.white_boneyard[0]
        temp_W = board.black_boneyard[0]

        temp_B1 = temp_B.replace(temp_B[0], '0')
        temp_W1 = temp_W.replace(temp_W[0], '0')

        W = int(str(temp_W1))
        B = int(str(temp_B1))
        while (W):
            W_pip_value += W % 10
            W /= 10
        
        while (B):
            B_pip_value += B % 10
            B /= 10
        
        if (W_pip_value < B_pip_value):
            return "White"
        
        if (B_pip_value < W_pip_value):
            return "Black"  
        
        if (W_pip_value == B_pip_value):
            return "No"
        return "No"

    
#     /* *********************************************************************
# Function Name: return_Score_hand()
# Purpose: Get the pip value of a dominos in a hand
# Parameters:
#             char y, used to indicate which hand
# Algorithm:
#                       1)Loop through each domino at postion i

# 					  2)Replace the B or W with 0
# 					  3)Change string to int
# 					  4)While loop adds up digits
# ********************************************************************* */

    def return_score_hand(self,y):
        board=Board.Instance()
        total = 0
        if (y == 'W') :
            for i in range(0,len(board.white_hand)):
                if(len(board.white_hand)>0):
                    x = board.white_hand[i]
                    
                    if (x[0]=='W') :
                        p = x.replace(x[0], '0')
                        value = int(p)
                        while (value > 0):
                            total += value % 10
                            value /= 10
                    
                
            
        elif (y == 'B'):
         
            for i in range(0,len(board.black_hand)):
                if(len(board.black_hand)>0):
                    x = board.black_hand[i]

                    if (x[0]=='B') :
                        p = x.replace(x[0], '0')
                        value = int(p)
                        while (value > 0):
                            total += value % 10
                            value /= 10
        return total
    

# /* *********************************************************************
# Function Name: INC_Rounds
# Parameter: X is either W or B
# Purpose: Depending on X which will be W or B inc white_rounds or black_rounds respectively
# ********************************************************************* */

    def INC_Rounds(self,x) :
        board=Board.Instance()
        if (x == 'B' or x == 'b') :
            board.black_rounds_won+=1
        elif (x == 'W' or x == 'w'):
            board.white_rounds_won+=1
        
    

#     /* *********************************************************************
# Function Name: return_Rounds
# Parameter: x, to indicate wheter black or white
# Return: int of black/white_rounds_won
# ********************************************************************* */
    def Return_rounds(self,x):
        board=Board.Instance()
        if (x == 'B' or x == 'b') :
            return board.black_rounds_won
        elif (x == 'W' or x == 'w') :
            return board.white_rounds_won
        
        return 0
    

    # /* *********************************************************************
    #   Function Name: getWhite_score()
    #   Purpose: Return white_Score
    #   ********************************************************************* */
    def getWhite_score(self) :
        board=Board.Instance()
        return board.white_score
    
    # /* *********************************************************************
    #   Function Name: getBlack_score()
    #   Purpose: Return Black_Score
    #   ********************************************************************* */

    def getBlack_score(self) :
        board=Board.Instance()
        return board.black_score
    
    # /* *********************************************************************
    #       Function Name: SetScores
    #       Purpose: set scores back to zero
    #       ********************************************************************* */
    def setScores(self) :
        board=Board.Instance()
        board.white_score = 0
        board.black_score = 0
    
    # /* *********************************************************************
    #       Function Name: SetRounds
    #       Purpose: set Rounds back to zero
    #       ********************************************************************* */
    def setRounds(self):
        board=Board.Instance()
        board.white_rounds_won=0
        board.black_rounds_won=0
    



    
# /* *********************************************************************
# Function Name: SetBoneyards()
# Purpose: Set boneyards to the orginal unshuffled deck

# ********************************************************************* */
    def setBoneyards(self):
        board=Board.Instance()
        board.white_boneyard=copy(board.white_array)
        board.black_boneyard=copy(board.black_array)

#     /* *********************************************************************
# Function Name: load
# Purpose: To set all the data members with loaded data from file 
# Local Variables:
#             i, line number
#             fp, all data in file
#             line, current data for line 

# Algorithm:
#                      1)Loop through lines looking for specfic lines(i==1 ,etc)
#                     2) set data to line
#                     3) loop through removing punctuation from data 
#                     4) split the string, set data_list to string
#                      5)Remove first element from list (White stack, Black Boneyard,etc)
#                       6)set specfic data memeber to data_list
# ********************************************************************* */
    
    def Load(self,filename):
        board=Board.Instance()
        game=Game.Instance()
        fp = open(filename)
        for i, line in enumerate(fp):
            if i == 1:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)
                board.white_stack=data_list
                # print board.white_stack
            elif i == 2:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)
                board.white_boneyard=data_list
                # print board.white_boneyard
            elif i == 3:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)
                board.white_hand=data_list
                # print board.white_hand
            elif i == 4:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)
                if(len(data_list)>0):
                    board.white_score=int(data_list[0])
                #print "loaded white score",board.white_score
            elif i == 5:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)
                data_list.pop(0)
                if(len(data_list)>0):
                    board.white_rounds_won=int(data_list[0])
                # print board.white_rounds_won
            elif i == 8:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)
                board.black_stack=data_list
                # print board.black_stack
            elif i == 9:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)
                board.black_boneyard=data_list
                # print board.black_boneyard
            elif i == 10:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)
                board.black_hand=data_list
                # print board.white_hand
            elif i == 11:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)
                if(len(data_list)>0):
                    board.black_score=int(data_list[0])
                # print board.black_score
            elif i == 12:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)
                data_list.pop(0)
                if(len(data_list)>0):
                    board.black_rounds_won=int(data_list[0])
                # print board.black_rounds_won
            elif i == 14:
                data=line
                for c in string.punctuation:
                    data= data.replace(c,"")
                data_list=data.split()
                data_list.pop(0)

                if(len(data_list)>0):
                    game.Player_turn=data_list[0]
                # print game.Player_turn
            elif i > 14:
                break
        fp.close()

#     /* *********************************************************************
# Function Name: Save
# Purpose: Save to file specfic filename

# Local Variables:
        # WS=string holding white stack
        # BS=string holding black stack
        # BB=string holding black boneyard
        # WB=string holding white boneyard
        # BH=string holding black hand
        # WH=string white hand
        # WSS= int white_score
        # BSS=int black_score
        # WR=int white_rounds_won
        # BR=int black_rounds_won
# Algorithm:
#                      1)Write to file in with correct newlines(\n)
# ********************************************************************* */
    def Save(self,filename):
        board=Board.Instance()
        fw= open(filename, 'w+')
        WS=' '.join(board.white_stack)
        BS=' '.join(board.black_stack)
        BB=' '.join(board.black_boneyard)
        WB=' '.join(board.white_boneyard)
        BH=' '.join(board.black_hand)
        WH=' '.join(board.white_hand)
        WSS=board.white_score
        BSS=board.black_score
        WR=board.white_rounds_won
        BR=board.black_rounds_won

        fw.write("Computer"+ "\n")
        fw.write("   Stacks: "+WS+ "\n")
        fw.write("   Boneyard: "+WB+ "\n")
        fw.write("   Hand:  "+ WH +"\n")
        fw.write("   Score:  "+str(WSS) +"\n")
        fw.write("   Rounds Won:  "+ str(WR) +"\n")
        fw.write("\n")
        fw.write("Human: "+"\n")
        fw.write("   Stacks: "+WS+ "\n")
        fw.write("   Boneyard: "+BB+ "\n")
        fw.write("   Hand:  "+ BH +"\n")
        fw.write("   Score:  "+ str(BSS) +"\n")
        fw.write("   Rounds Won:  "+ str(BR) +"\n")
        fw.write("\n")
        fw.write("Turn: Human ")



@Singleton
class BoardView:
# /* *********************************************************************
# Function Name: UpdateBB()
# Purpose:Update a string containing the black boneyard
# local variable: a, string containing the entire black boneyard

# Algorithm:
#             1) Use regular expression to print list
#             2) concat with a " "
# ********************************************************************* */

    def UpdateBB(self):
        board=Board.Instance()
        
        a =  ' '.join(map(str, board.black_boneyard))
        print "BB: "+ (a)

    

    # /* *********************************************************************
# Function Name: UpdateBS()
# Purpose:Update a string containing the black stack
# Local variable: stackB, string containing the entire black stack


# Algorithm:
#             1) Use regular expression to print list
#             2) concat with a " "
# ********************************************************************* */
    def UpdateBS(self):
        board=Board.Instance()
        stackB =  ' '.join(map(str, board.black_stack))
        print "BS: "+(stackB)
    
#     /* *********************************************************************
# Function Name: UpdateBH()
# Purpose:Update a string containing the black hand
# local varaible: handB, string containing the entire black hand

# Algorithm:
#         1) Use regular expression to print list
#         2) concat with a " "
# ********************************************************************* */
    def UpdateBH(self):
        board=Board.Instance()
        handB =  ' '.join(map(str, board.black_hand))
        print "BH: " +(handB)
    
#     /* *********************************************************************
# Function Name: UpdateWS()
# Purpose:Update a string containing the white stack
# Local Variable: Stackw, String containing all of the white stack
# Algorithm:
#             1) Use regular expression to print list
#             2) concat with a " "
# ********************************************************************* */
    def UpdateWS(self) :
        board=Board.Instance()
        stackW =  ' '.join(map(str, board.white_stack))
        print "WS: "+ (stackW)
    
#     /* *********************************************************************
# Function Name: UpdateWB()
# Purpose:Update a string containing the white boneyard
# Local Varaible:BoneyardW, string containing the entire white boneyard

# Algorithm:
#         1) Use regular expression to print list
#         2) concat with a " "
# ********************************************************************* */
    def UpdateWB(self) :
        board=Board.Instance()
        BoneyardW =  ' '.join(map(str, board.white_boneyard))
        print "WB: "+(BoneyardW)
    
#     /* *********************************************************************
# Function Name: UpdateWH()
# Purpose:Update a string containing the white Hand
# Local Variable:handW, string containing the entire white hand

# Algorithm:
#         1) Use regular expression to print list
#         2) concat with a " "
# ********************************************************************* */
    def UpdateWH(self) :
        board=Board.Instance()
        handW =  ' '.join(map(str, board.white_hand))
        print "WH: "+ handW

    
#     /* *********************************************************************
# Function Name: UpdateView
# Purpose: Update the view of all stacks, hands, boneyards etc..
# ********************************************************************* */

    def UpdateView(self):
        board=Board.Instance()
        board1=BoardView.Instance()
        board1.UpdateBB()
        board1.UpdateBS()
        board1.UpdateBH()
        board1.UpdateWS()
        board1.UpdateWB()
        board1.UpdateWH()

        print "Black Rounds Won:", (int(board.Return_rounds('B')))
        print "White Rounds Won:",(int (board.Return_rounds('W')))


@Singleton
class Player:

#     /* *********************************************************************
# Function Name: Place Domino
# Purpose: Changes String in a stack to string in a hand.
# Parameters:
#             x, Hand 'B' or 'W'
#           hand_card, postion in hand ^
#           y, Stack 'B' or 'W'
#           stack_card, postion in stack ^
# Return Value: No return value
# Algorithm:
#              1) Checks x and y to see which hand and which stack to play to.
#             2) uses board function set_white/Black_stack to change to value of board function return_white/black_hand at postion hand_card(parameter)
#           3)if hand_card is =5 , set the 5th in hand_array to " "
#           4) if !=5, use board function move_array_hand, then set the 5th element in hand_array to " "
# ********************************************************************* */

    def place_domino(self,x, hand_card, y, stack_card) :
        board1=Board.Instance()
        if (x == 'W' or x == 'w') :
            if (y == 'W' or y == 'w') :
                if (hand_card == 5) :
                    board1.set_white_stack(stack_card, board1.white_hand[hand_card])
                    board1.white_hand.pop(hand_card)
                else :
                    board1.set_white_stack(stack_card, board1.white_hand[hand_card])
                    board1.white_hand.pop(hand_card)
                
            
            if (y == 'B' or y == 'b') :
                if (hand_card == 5) :
                    board1.set_black_stack(stack_card, board1.white_hand[hand_card])
                    board1.white_hand.pop(hand_card)
                else :
                    board1.set_black_stack(stack_card, board1.white_hand[hand_card])
                    board1.white_hand.pop(hand_card)
                
            
        elif (x == 'B' or x == 'b') :
            if (y == 'W' or y == 'w') :
                if (hand_card == 5) :
                    board1.set_white_stack(stack_card, board1.black_hand[hand_card])
                    board1.black_hand.pop(hand_card)
                else :
                    board1.set_white_stack(stack_card, board1.black_hand[hand_card])
                    board1.black_hand.pop(hand_card)
                
            elif (y == 'B' or y == 'b') :
                if (hand_card == 5) :
                    board1.set_black_stack(stack_card, board1.black_hand[hand_card])
                    board1.black_hand.pop(hand_card)
                else :
                    board1.set_black_stack(stack_card, board1.black_hand[hand_card])
                    board1.black_hand.pop(hand_card)

                
            
        
    

#     /* *********************************************************************
# Function Name: is_dominoHigher
# Purpose: To check if the pip value of the hand card is higher then that of the stack pip value
# Parameters:
#             x, Hand 'B' or 'W'
#           hand_card, postion in hand ^
#           y, Stack 'B' or 'W'
#           stack_card, postion in stack ^
# Return Value: 1 if higher,2 if equal, 0 if not higher.
# Local Variables:
#             a, pip value of hand array at postion hand_card(parameter)
#           b,pip value of stack array at postion stack_card(parameter)
# Algorithm:
#                       1) simply if then statements to determine which value is higher.
# ********************************************************************* */
    def is_dominoHigher(self,x, hand_card, y, stack_card) :
        player=Player.Instance()
        a = player.get_dominoValueHand(x, hand_card)
        b = player.get_dominoValueStack(y, stack_card)
        if (a > b) :
            return 1
        elif (a == b) :
            return 2
        else:
            return 0

    

#     /* *********************************************************************
# Function Name: get_dominoValueStack
# Purpose: To check if the pip value of the stack array at postion count
# Parameters:
#             x, stack 'B' or 'W'
#           count, postion in stack array ^

# Return Value: pip value aka total
# Local Variables:
#             total= total pip value of stack card
# Algorithm:
#                       1)Very simliar to board function,but instead of using for loop just returns stack at postion count.
#                     2) then turns char 'B' or 'W' to 0
#                     3) converts string of the black stack to a int.
#                     4) add the digits with while loop.
# ********************************************************************* */
    def get_dominoValueStack(self,x, count) :
        board1=Board.Instance()
        total = 0
        if (x == 'B' or x == 'b') :

            b = board1.black_stack[count]
            if(b is not None) :
                if (b[0] == 'B'or b[0] == 'W') :
                    p = b.replace(b[0], '0')
                    value = int(p)

                    while (value > 0) :
                        total += value % 10
                        value /= 10
                    
                
            
        
        if (x == 'w' or x == 'W') :
            b = board1.white_stack[count]
            if(b is not None ):
                if (b[0] == 'W'or b[0] == 'B') :
                    p = b.replace(b[0], '0')
                    value = int(p)
                    while (value > 0) :
                        total += value % 10
                        value /= 10
                    
                
            
        
        return total
    

    # /* *********************************************************************
    # Function Name: get_dominoValueHand
    # Purpose: To check if the pip value of the ahdn array at postion count
    # Parameters:
    #             x, hand 'B' or 'W'
    #             count, postion in hand array ^

    # Return Value: pip value aka total
    # Local Variables:
    #             total= total pip value of hand card
    # Algorithm:
    #                         1) use x to determine which hand.
    #                       2) then turns char 'B' or 'W' to 0
    #                       3) converts string of the black stack to a int.
    #                       4) add the digits with while loop.
    # ********************************************************************* */
    def get_dominoValueHand(self,x,count) :
        board1=Board.Instance()
        total = 0
        if (x == 'B' or x == 'b') :
            a = board1.black_hand[count]
            if (a[0] == 'B') :
                p = a.replace(a[0], '0')
                value =int(p)
                while (value > 0) :
                    total += value % 10
                    value /= 10

        
        if (x == 'w' or x == 'W') :
            a = board1.white_hand[count]
            if (a[0] == 'W') :
                p = a.replace(a[0], '0')
                value = int(p)
                while (value > 0) :
                    total += value % 10
                    value /= 10
        return total
    

    # /* * *********************************************************************
    # Function Name:is_dominoDoubleHand
    # Purpose: To check if a card in hand is a double
    # Parameters:
    # x, hand 'B' or 'W'
    # count, postion in hand array ^

    # Return Value:1 if double, 0 if not double.

    # Algorithm:
    #         1)use x to determine which hand.
    #         2)check the string y, with all known doubles, return 1 or 0
    # ********************************************************************* */
    def is_dominoDoubleHand(self,x,count) :
        board1=Board.Instance()
        if (x == 'w' or x == 'W') :
            y = board1.white_hand[count]
            if(y is not None) :
                if (y ==("W00")) :
                    return 1
                elif (y ==("W11")) :
                    return 1
                elif (y ==("W22")) :
                    return 1
                elif (y ==("W33")) :
                    return 1
                elif (y ==("W44")) :
                    return 1
                elif (y ==("W55")) :
                    return 1
                elif (y ==("W66")) :
                    return 1
                else :
                    return 0
                
            
        elif (x == 'B' or x == 'b') :
            y = board1.black_hand[count]
            if (y is not None) :
                if (y ==("B00")) :
                    return 1
                elif (y ==("B11")) :
                    return 1
                elif (y ==("B22")) :
                    return 1
                elif (y ==("B33")) :
                    return 1
                elif (y ==("B44")) :
                    return 1
                elif (y ==("B55")) :
                    return 1
                elif (y ==("B66")) :
                    return 1
                else :
                    return 0
        return 0

    # /* *********************************************************************
    # Function Name:is_dominoDoublestack
    # Purpose: To check if a card in stack is a double
    # Parameters:
    #             x, hand 'B' or 'W'
    #             count, postion in stack array ^

    # Return Value:1 if double, 0 if not double.

    # Algorithm:
    #                       1)use x to determine which stack.
    #                       2)check the string y, with all known doubles, return 1 or 0
    # ********************************************************************* */
    def is_dominoDoubleStack(self,x,count) :
        board1=Board.Instance()
        if (x == 'w' or x == 'W') :
            y = board1.white_stack[count]
            if (y ==("W00")) :
                return 1
            elif (y ==("W11")) :
                return 1
            elif (y ==("W22")) :
                return 1
            elif (y ==("W33")) :
                return 1
            elif (y ==("W44")) :
                return 1
            elif (y ==("W55")) :
                return 1
            elif (y ==("W66")) :
                return 1
            elif (y ==("B00")) :
                return 1
            elif (y ==("B11")) :
                return 1
            elif (y ==("B22")) :
                return 1
            elif (y ==("B33")) :
                return 1
            elif (y ==("B44")) :
                return 1
            elif (y ==("B55")) :
                return 1
            elif (y ==("B66")) :
                return 1
            else :
                return 0
            
        elif (x == 'B' or x == 'b') :
            y = board1.black_stack[count]
            if (y ==("B00")) :
                return 1
            elif (y ==("B11")) :
                return 1
            elif (y ==("B22")) :
                return 1
            elif (y ==("B33")) :
                return 1
            elif (y ==("B44")) :
                return 1
            elif (y ==("B55")) :
                return 1
            elif (y ==("B66")) :
                return 1
            elif (y ==("W00")) :
                return 1
            elif (y ==("W11")) :
                return 1
            elif (y ==("W22")) :
                return 1
            elif (y ==("W33")) :
                return 1
            elif (y ==("W44")) :
                return 1
            elif (y ==("W55")) :
                return 1
            elif (y ==("W66")) :
                return 1
            else :
                return 0
        return 0


@Singleton
class Computer () :
    computer_move="placed"

    
    # /* *********************************************************************
    # Function Name: PlaceDomino
    # Purpose: Place a domino for computer
    # Local Variables:
    #             x, Which stack the computer is going to place a domino to.
    #             i, postion in hand currently being test
    #             j, position in stack currently being tested
    # Algorithm:
    #                       1) Look for both stacks for dominos that start with B
    #             2) call "place" to place domino, return 1 if possible, 0 if not
    #             3) if no hand domino can be placed on a Black domino, repeat 1-2 but look for dominos that start with W
    # ********************************************************************* */
    def placeDomino(self):
        board=Board.Instance()
        computer=Computer.Instance()
        x="Black"
        board.skip_computer_output()
        for i in range(0,6):
            if (board.white_stack[i][0] == 'B') :
                x="White"
                for j in range(0,len(board.white_hand)):
                    if(computer.place(j,i,x)==1):
                        computer.computer_move="placed"
                        return 0
                    
            if(board.black_stack[i][0] == 'B'):
                x="Black"
                for j in range(0,len(board.white_hand)):
                    if(computer.place(j,i,x)==1):
                        computer.computer_move="placed"
                        return 0
        
        for i in range(0,6):
            if (board.white_stack[i][0] == 'W') :
                x="White"
                for j in range(0,len(board.white_hand)):
                    if(computer.place(j,i,x)==1):
                        computer.computer_move="placed"
                        return 0
                    
                

            
            if(board.black_stack[i][0] == 'W'):
                x="Black"
                for j in range(0,len(board.white_hand)):
                    if(computer.place(j,i,x)==1):
                        computer.computer_move="placed"
                        return 0
        computer.computer_move="skipped"
        print "Computer Skipped"
        return 0
    
# /* *********************************************************************
# Function Name: Place Domino
# Purpose: To check if a domino can be placed, and place it
# Local Variables:
#      a, the postion of  domino in your hand
#      b,postion of the domino on the stack you are playing to.
#      y, W or B depending on what stack you want to play to.
# Return Value:  return 1 if placed, 0 if cannot be palced
# Algorithm:
#            1)checks if domino your playing and the stack domino is a nondouble,if yes place domino through player function
#            2)checks if domino is double and stack domino is double, checks if player domino is higher through player function, if yes place domino.
#            3)lastly if the above to failed, just check if domino is higher if no dont play, if yes place domino.
# ********************************************************************* */


    def place(self, a, b,x) :
        player=Player.Instance()
        board=Board.Instance()
        computer=Computer.Instance()
        y='n'
        if (x ==("White")) :
            y = 'W'
        
        elif(x ==("Black")):
            y='B'
        

        if (y == 'W'  or  y == 'w' ) :
            if (player.is_dominoDoubleHand('W', a) == 1  and  player.is_dominoDoubleStack('W', b) != 1) :
                print "computer player", board.white_hand[a]," on ", board.white_stack[b]
                player.place_domino('W', a, 'W', b)
                return 1
            elif (player.is_dominoDoubleHand('W', a) == 1  and  player.is_dominoDoubleStack('W', b) == 1) :
                if (player.is_dominoHigher('W', a, 'W', b) == 1) :
                    print "computer player", board.white_hand[a]," on ", board.white_stack[b]
                    player.place_domino('W', a, 'W', b)
                    return 1
                
            elif (player.is_dominoHigher('W', a, 'W', b) == 1 or player.is_dominoHigher('W', a, 'W', b) == 2) :
                print "computer player",board.white_hand[a]," on ", board.white_stack[b]
                player.place_domino('W', a, 'W', b)
                return 1
            else :
                return 0
            

        elif (y == 'B'  or  y == 'b' ) :
            if (player.is_dominoDoubleHand('W', a) == 1  and  player.is_dominoDoubleStack('B', b) != 1) :
                print "computer player", board.white_hand[a]," on ", board.black_stack[b]
                player.place_domino('W', a, 'B', b)
                return 1
            elif (player.is_dominoDoubleHand('W', a) == 1  and  player.is_dominoDoubleStack('B', b) == 1) :
                if (player.is_dominoHigher('W', a, 'B', b) == 1) :
                    print "computer player", board.white_hand[a]," on ", board.black_stack[b]
                    player.place_domino('W', a, 'B', b)
                    return 1
                
            elif (player.is_dominoHigher('W', a, 'B', b) == 1 or player.is_dominoHigher('W', a, 'B', b) ==2) :
                print "computer player", board.white_hand[a]," on ", board.black_stack[b]
                player.place_domino('W', a, 'B', b)
                return 1
            else :
                return 0
        
        return 0
    

#     /* *********************************************************************
# Function Name: setHand_count
# Purpose: set hand count to x
# Algorithm:
#              1)set hand-count to x
# ********************************************************************* */
    def setHand_count(self,x):
        computer=Computer.Instance()
        computer.hand_count=x
    
#     /* *********************************************************************
# Function Name: get_Hand_count
# Purpose: return hand count
# Return: hand_count
# ********************************************************************* */
    def get_hand_count(self):
        computer=Computer.Instance()
        return hand_count
    

@Singleton
class Human():

    board=Board.Instance()

# /* *********************************************************************
# Function Name: Place
# Purpose: Place a domino from black hand to a stack

# Local Variables:
#      a, the postion of  domino in your hand
#      b,postion of the domino on the stack you are playing to.
#      y, W or B depending on what stack you want to play to.

# Algorithm:
#              1)Set a, b ,y to the spinners used to recieve them a(hand postion), b(stack postion), y(which stack)
#            3)checks if domino your playing and the stack domino is a nondouble,if yes place domino through player function
#            4)checks if domino is double and stack domino is double, checks if player domino is higher through player function, if yes place domino.
#            5)lastly if the above to failed, just check if domino is higher if no dont play, if yes place domino.
# ********************************************************************* */
    
    def place(self) :
        board=Board.Instance()
        human=Human.Instance()
        player=Player.Instance()
        y = 'n'
        y=(raw_input("Which stack do you want to play a domino to?(Computer, enter W. Human, enter B):"))
        
        if (y == 'W'  or  y == 'w') :
            a=int(raw_input("Which domino from your hand do you want to play?(Enter 1-"+str(len(board.black_hand))+"):"))
            if(a<=0  or a>len(board.black_hand)):
                print "not valid input"
                human.AskUser()
            a-=1
            b=int(raw_input("Which domino on the stack?(Enter 1-6):"))
            if(b<=0  or b>len(board.white_stack)):
                print "not valid input"
                human.AskUser()

            b-=1

            if (player.is_dominoDoubleHand('B', a) == 1 and player.is_dominoDoubleStack('W', b) != 1) :
                player.place_domino('B', a, 'W', b)



            elif (player.is_dominoDoubleHand('B', a) == 1 and player.is_dominoDoubleStack('W', b) == 1) :
                if (player.is_dominoHigher('B', a, 'W', b) == 1) :
                    player.place_domino('B', a, 'W', b)




                
            elif (player.is_dominoHigher('B', a, 'W', b) == 1 or player.is_dominoHigher('B', a, 'W', b) == 2) :
                player.place_domino('B', a, 'W', b)

            else:
                print "not valid move",  board.black_hand[a],board.white_stack[b]
                human.AskUser()

            

        elif (y == 'B'  or  y == 'b') :
            a=int(raw_input("Which domino from your hand do you want to play?(Enter 1-"+str(len(board.black_hand))+"):"))
            if(a<=0  or a>len(board.black_hand)):
                print "not valid input"
                human.AskUser()
            a-=1
            b=int(raw_input("Which domino on the stack?(Enter 1-6):"))
            if(b<=0  or b>len(board.white_stack)):
                print "not valid input"
                human.AskUser()

            b-=1

            if (player.is_dominoDoubleHand('B', a) == 1 and player.is_dominoDoubleStack('B', b) != 1) :
                player.place_domino('B', a, 'B', b)



            elif (player.is_dominoDoubleHand('B', a) == 1 and player.is_dominoDoubleStack('B', b) == 1) :
                if (player.is_dominoHigher('B', a, 'B', b) == 1) :
                    player.place_domino('B', a, 'B', b)


                
            elif (player.is_dominoHigher('B', a, 'B', b) == 1 or player.is_dominoHigher('B', a, 'B', b) ==2) :
                player.place_domino('B', a, 'B', b)

            else:
                print "not valid move",board.black_hand[a],board.black_stack[b]
                human.AskUser()
        else:
            print "not valid input"
            human.AskUser()


            
        
    
#     /* *********************************************************************
# Function Name: help
# Purpose: To check if a domino can be placed, and place it
# Local Variables:
#      a, the postion of  domino in your hand
#      b,postion of the domino on the stack you are playing to.
#      y, W or B depending on what stack you want to play to.
# Return Value:  return 1 if placed, 0 if cannot be placed
# Algorithm:
#            1)checks if domino your playing and the stack domino is a nondouble,if yes set help string accordingly
#            2)checks if domino is double and stack domino is double, checks if player domino is higher through player function, if yes set help string accordingly
#            3)lastly if the above to failed, just check if domino is higher if no dont play, if yes set help string accordingly.
#            4)If nothing can be done set help to SKIP

# ********************************************************************* */
    def help(self,a, b,x) :
        board=Board.Instance()
        player=Player.Instance()
        y = 'n'
        if (x=="White") :
            y = 'W'
        
        elif(x=="Black"):
            y='B'
        
        if (y == 'W'  or  y == 'w') :
            if (player.is_dominoDoubleHand('B', a) == 1 and player.is_dominoDoubleStack('W', b) != 1) :
                print "A good domino to play from your hand:"+board.black_hand[a]+" to the white stack domino:" +board.white_stack[b]
                return 1

            elif (player.is_dominoDoubleHand('B', a) == 1 and player.is_dominoDoubleStack('W', b) == 1) :
                if (player.is_dominoHigher('B', a, 'W', b) == 1) :
                    print "A good domino to play from your hand:"+board.black_hand[a]+" to the white stack domino:" +board.white_stack[b]
                    return 1
                
            elif (player.is_dominoHigher('B', a, 'W', b) == 1 or player.is_dominoHigher('B', a, 'W', b)== 2) :
                print "A good domino to play from your hand:"+board.black_hand[a]+" to the white stack domino:" +board.white_stack[b]
                return 1

            else :
                return 0
            

        elif (y == 'B'  or  y == 'b') :
            if (player.is_dominoDoubleHand('B', a) == 1 and player.is_dominoDoubleStack('B', b) != 1) :
                print "A good domino to play from your hand:"+board.black_hand[a]+" to the black stack domino:" +board.black_stack[b]
                return 1

            elif (player.is_dominoDoubleHand('B', a) == 1 and player.is_dominoDoubleStack('B', b) == 1) :
                if (player.is_dominoHigher('B', a, 'B', b) == 1) :
                    print "A good domino to play from your hand:"+board.black_hand[a]+" to the black stack domino:" +board.black_stack[b]
                    return 1

                
            elif (player.is_dominoHigher('B', a, 'B', b) == 1 or player.is_dominoHigher('B', a, 'B', b) ==2) :
                print "A good domino to play from your hand:"+board.black_hand[a]+" to the black stack domino:" +board.black_stack[b]
                return 1

            else :
                return 0
            
        
        return 0
    
#     /* *********************************************************************
# Function Name: RunHelp
# Purpose: Runs the above help function
# Local Variables:
#             x, Which stack the computer is going to place a domino to.
#             i, postion in hand currently being test
#             j, position in stack currently being tested
# Algorithm:
#             1) Look for both stacks for dominos that start with W
#             2) call "place" to place domino, return 1 if possible, 0 if not
#             3) if no hand domino can be placed on a Black domino, repeat 1-2 but look for dominos that start with B
# ********************************************************************* */
    def runHelp(self):
        board=Board.Instance()
        human=Human.Instance()
        x="White"
        for i in range(0,6):
            if (board.white_stack[i][0] == 'W') :
                x="White"
                for j in range(0,len(board.black_hand)):
                    if(human.help(j,i,x)==1):
                        return 1
                    
                

            if(board.black_stack[i][0] == 'W'):
                x="Black"
                for j in range(0,len(board.black_hand)):
                    if(human.help(j,i,x)==1):
                        return 1
                    
                
            
        
        for i in range(0,6):
            if (board.white_stack[i][0] == 'B') :
                x="White"
                for j in range(0,len(board.black_hand)):
                    if(human.help(j,i,x)==1):
                        return 1
                    
                

            
            if(board.black_stack[i][0] == 'B'):

                x="Black"
                for j in range(0,len(board.black_hand)):
                    if(human.help(j,i,x)==1):
                        return 1
                    
                
            
        return 0


    def AskUser(self):
        human=Human.Instance()
        computer=Computer.Instance()
        board=Board.Instance()
        try:
            print "Option 1:Place Domino"
            print "Option 2:Help"
            print "Option 3:Pass turn"
            print "Option 4:save game and quit"
            option=int(raw_input('Enter a number 1-4 corsponding to option:'))
            if (option==1):
                human.place()
            elif(option==2):
                if(human.runHelp()==0):
                     print "No moves, you should Skip"
                human.AskUser()
            elif(option==3 ):
                if(human.runHelp()==1):
                    print "You can still make a move"
                    human.AskUser()
                else:
                    print "you skipped"
                    computer.placeDomino()
            elif(option==4):
                filename=raw_input('Enter filename: ')
                board.Save(filename)
                sys.exit()

        except ValueError:
            print "Not a number"
            human.AskUser()


@Singleton
class Game:
    Player_turn=""
    board1=Board.Instance()

#     /* *********************************************************************
# Function Name: Start_game
# Purpose: Start the game
# Parameters:
#            new_or_not, indicates what way you are starting the game

# Algorithm:
#                       1)ON new, set the everything to zero, and use the function who_goes_first to see who goes first and deal out board.
#             2)Keep_going is at the end of the round where you do the same as on new, except dont restart rounds
#             3) else is for on load,checks if something already exists on the board, and deals out accordingly.
# ********************************************************************* */
    def Start_Game(self,new_or_not):
        board1=Board.Instance()
        game=Game.Instance()
        if(new_or_not=="new") :
            board1.setRounds()
            board1.setBoneyards()
            board1.Shuffle_arrays()
            board1.setScores()
            while (str(board1.Who_goes_first()) == "No"):
                print "Shuffled"
                board1.Shuffle_arrays()
            if (str(board1.Who_goes_first()) == "White") :
                board1.deal_stack_black(6)
                board1.deal_stack_white(6)
                board1.deal_hand_black(6)
                board1.deal_hand_white(6)
                game.Player_turn = "White"
            elif (str(board1.Who_goes_first()) == "Black") :
                board1.deal_stack_black(6)
                board1.deal_stack_white(6)
                board1.deal_hand_black(6)
                board1.deal_hand_white(6)
                game.Player_turn = "Black"
            
        elif(new_or_not=="keep_going"):
            board1.setBoneyards()
            board1.Shuffle_arrays()
            board1.setScores()

            if (board1.Who_goes_first() == "No") :
                print "Shuffled"
                board1.Shuffle_arrays()
            elif (board1.Who_goes_first() == "White") :
                board1.deal_stack_black(6)
                board1.deal_stack_white(6)
                board1.deal_hand_black(6)
                board1.deal_hand_white(6)
                game.Player_turn = "White"
            elif (board1.Who_goes_first() == "Black") :
                board1.deal_stack_black(6)
                board1.deal_stack_white(6)
                board1.deal_hand_black(6)
                board1.deal_hand_white(6)
                game.Player_turn = "Black"
            

        
        else :

            if(len(board1.black_hand)==0 and len(board1.white_hand)==0) :
                if (board1.Who_goes_first() == "No") :
                    print "Shuffled"
                    board1.white_boneyard.extend(board1.white_stack)
                    board1.black_boneyard.extend(board1.black_stack)
                    del board1.white_stack[:]
                    del board1.black_stack[:]
                    board1.Shuffle_arrays()
                    game.Start_Game("old")
                elif (board1.Who_goes_first() == "White") :
                    board1.deal_stack_black(6)
                    board1.deal_stack_white(6)
                    board1.deal_hand_black(6)
                    board1.deal_hand_white(6)
                    game.Player_turn ="White"
                elif (board1.Who_goes_first() == "Black") :
                    board1.deal_stack_black(6)
                    board1.deal_stack_white(6)
                    board1.deal_hand_black(6)
                    board1.deal_hand_white(6)
                    game.Player_turn = "Black"

            
        

    

# /* *********************************************************************
# Function Name: Play_game
# Paramter: Turn, current persons turn
# Purpose: if black set wait for input and set turn for white, if white call computer.playdomino and set turn to black.1

# ********************************************************************* */

    def PLay_Game(self,turn):
        board1=Board.Instance()
        if(turn=="Black"):
            if(User_turn=="Gone"):
               Player_turn="White"

           
       
        elif(turn=="White"):
           computer.placeDomino()
           Player_turn="Black"


       

   
    # /* *********************************************************************
    # Function Name: Finish_rounds
    # Purpose: To return a string that can be used by Main to make an alert appear, inc rounds after rounds, inc score after hands
    # Return Value: String used by main to tell user who won hand/round
    # Local Variables:
    #             x, Current BlackScore
    #             Y, current White Score
    # Algorithm:
    #              1) Get the current scores(dominos on stack), minus any dominos still left in the hands(temp_x,temp_y)
    #             2) Add to total score, set x and y to this new score
    #             3)if x is greater than y, and the boneyard is empty(end of tourny) inc rounds and set score to zero)
    #             4)else return string to the user telling them the won the round
    #             5)if with y>x repeat 3-4 inc white_rounds, return string etc..
    #             6) if y==x return "tie"
    # ********************************************************************* */
    def Finish_round(self) :
        board1=Board.Instance()
        temp_x = board1.get_score_black()
        x =((temp_x)- (board1.return_score_hand('B')))
        temp_y = board1.get_score_white()
        y =((temp_y)-(board1.return_score_hand('W')))
        board1.addblack_score(x)
        board1.addwhite_score(y)
        x = board1.getBlack_score()
        y = board1.getWhite_score()

        if (x > y) :
              board1.INC_Rounds('B')
              board1.setScores()
              print  "You won the round! with a score of " , x , " to the computers:" , y 
       
        if (y > x) :
               board1.INC_Rounds('W')
               board1.setScores()
               print "Computer won the round! with a score of " ,y ," to your: " ,x 
           

       
        elif(y==x):
            print "Tie!"
       
   



@Singleton
class Tournament():

        # /* *********************************************************************
    # Function Name: CallGame
    # Purpose: Start and implement the Tournament 
    # Local Variables:
    #            option, input of the user
    # Algorithm:
    #              1) Ask the User if the want to load or start a new game
    #             2) If new game call game.start_game("new") and PlayTourny
    #             3) if old game ask user for filename, call board load , then game.start_game("old")
    # ********************************************************************* */

    def Callgame(self):
        computer=Computer.Instance()
        board1=BoardView.Instance()
        human=Human.Instance()
        game=Game.Instance()
        board=Board.Instance()
        print "Welcome to Michael D'Alessio's Domino Game"
        print "1) Do you want to play a new game?"
        print "2)Do you want to load a game"
        option=int(raw_input("Enter 1-2:  "))
        if(option ==1 ):
            game.Start_Game("new")
            board1.UpdateView()
            if(game.Player_turn=="White"):
                computer.placeDomino()
                board1.UpdateView()
            tournament.PlayTourny()
        if(option==2):
            filename=(raw_input("Enter a filename with .txt: "))
            board.Load(filename)
            board1.UpdateView()
            game.Start_Game("old")
            board1.UpdateView()
            if(game.Player_turn=="Computer"):
                computer.placeDomino()
                board1.UpdateView()
            tournament.PlayTourny()

        else:
            tournament.Callgame()

    # /* *********************************************************************
    # Function Name: Alert
    # Purpose: Called at the end of the round  
    # Local Variables:
    #            option1, input of the user
    # Algorithm:
    #              1) Ask the User if they want to stop playing or keep playing
    #             2) if keep playing, check the state of the game(boneyard size) and deal cards out or start_game accordingly 
    #             3) If stop playing check who has won more rounds and annouce winner
    # ********************************************************************* */

    def Alert(self):
        board=Board.Instance()
        board1=BoardView.Instance()
        option1=int(raw_input("1)Keep Going \n2)Stop playing and end tournament \nEnter 1-2:  "))
        if (option1==1):
            if (len(board.black_boneyard) >6 ) :
                board.deal_hand_black(6)
                board.deal_hand_white(6)
                board1.UpdateView()
            elif (len(board.black_boneyard) ==4 ) :
                board.deal_hand_black(4)
                board.deal_hand_white(4)
                board1.UpdateView()
            elif(len(board.black_boneyard) ==0) :
                game.Start_Game("keep_going")
                board1.UpdateView()
                tournament.PlayTourny()
        elif(option1==2):
            if (board.Return_rounds('B') > board.Return_rounds('W')) :
                print ("You win the tourny")
            elif (board.Return_rounds('B') < board.Return_rounds('W')) :

                print ("Computer wins")
            else :
                print ("Rounds the same, Tie Tournament!")
        else:
            tournament.Alert()

          # /* *********************************************************************
    # Function Name: PlayTourny
    # Purpose: Gameplay of the tournamnet 
    # Algorithm:
    #              1) Keep playing while users have cards
    #             2) if both users cant make move call tournament alert
    # ********************************************************************* */


    def PlayTourny(self):
            board=Board.Instance()
            human=Human.Instance()
            board1=BoardView.Instance()
            computer=Computer.Instance()
            game=Game.Instance()
            while ((len(board.white_hand)>0 or len(board.black_hand)>0)):
                human.AskUser()
                board1.UpdateView()
                computer.placeDomino()
                board1.UpdateView()
                if(len(board.black_hand)==0) or len(board.white_hand)==0 :
                    game.Finish_round()
                    tournament.Alert()
                elif(human.runHelp()==0 and computer.computer_move=="skipped"):
                    game.Finish_round()
                    tournament.Alert()
     

    







if __name__ == "__main__":
    tournament=Tournament.Instance()
    tournament.Callgame()




    



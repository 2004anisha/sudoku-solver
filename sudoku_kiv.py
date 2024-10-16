import pygame
import sys

s1 = [[],[],[],[],[],[],[],[],[]]
s2 = [[],[],[],[],[],[],[],[],[]]
s3 = [[],[],[],[],[],[],[],[],[]]
s4 = [[],[],[],[],[],[],[],[],[]]
s5 = [[],[],[],[],[],[],[],[],[]]
s6 = [[],[],[],[],[],[],[],[],[]]
s7 = [[],[],[],[],[],[],[],[],[]]
s8 = [[],[],[],[],[],[],[],[],[]]
s9 = [[],[],[],[],[],[],[],[],[]]

s = [s1,s2,s3,s4,s5,s6,s7,s8,s9] #Structure to store possibilites 

box1 = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
box2 = [[3,0],[4,0],[5,0],[3,1],[4,1],[5,1],[3,2],[4,2],[5,2]]
box3 = [[6,0],[7,0],[8,0],[6,1],[7,1],[8,1],[6,2],[7,2],[8,2]]
box4 = [[0,3],[1,3],[2,3],[0,4],[1,4],[2,4],[0,5],[1,5],[2,5]]
box5 = [[3,3],[4,3],[5,3],[3,4],[4,4],[5,4],[3,5],[4,5],[5,5]]
box6 = [[6,3],[7,3],[8,3],[6,4],[7,4],[8,4],[6,5],[7,5],[8,5]]
box7 = [[0,6],[1,6],[2,6],[0,7],[1,7],[2,7],[0,8],[1,8],[2,8]]
box8 = [[3,6],[4,6],[5,6],[3,7],[4,7],[5,7],[3,8],[4,8],[5,8]]
box9 = [[6,6],[7,6],[8,6],[6,7],[7,7],[8,7],[6,8],[7,8],[8,8]]

boxy = [box1,box2,box3,box4,box5,box6,box7,box8,box9]#Keep track of boxes 
""""
g1 = [0,0,0,0,0,0,0,0,0]
g2 = [0,0,0,0,0,0,0,0,0]
g3 = [0,0,0,0,0,0,0,0,0]
g4 = [0,0,0,0,0,0,0,0,0]
g5 = [0,0,0,0,0,0,0,0,0]
g6 = [0,0,0,0,0,0,0,0,0]
g7 = [0,0,0,0,0,0,0,0,0]
g8 = [0,0,0,0,0,0,0,0,0]
g9 = [0,0,0,0,0,0,0,0,0]
g = [g1,g2,g3,g4,g5,g6,g7,g8,g9]
"""
def is_it_solved(g): #checks if all the grid has any empty values 
        flag = True
        for x in g:# goind through every row in g
                for y in x: #goind through every item in specified row x
                        if y == 0 : # if an empty spot is found the flag us marked false else it remains true
                                flag = False
        if flag == True:
                return (True) # if there is nothing fornd returns true 

        else:
                return (False) # if an empty spot is found returns false


def find_box(x,y):
    for i in boxy:#finds the right box from the list of boxes 
        for j in i:#goes through evert element in every box to check if it contains it 
            if [x,y] ==j:
                return(i) #adds the right box in b 

def clear_s(s): #clears all values of s 
    for i in range(9): #going through every row 
        for j in range(9):#going through every item in row 
            s[i][j] = [] #removing any value found

def get_row(g,x):#gets the row of the cell
    return (g[x]) 
    
def get_col(g,y):# gets coloumn of the cell
    list = []
    for i in range(9):# goes through each row and adds the yth element to the list 
        n = g[i][y]
        list.append(n)
    return (list)

def get_box(g,x,y):
    for i in boxy:#finds the right box from the list of boxes 
        for j in i:#goes through evert element in every box to check if it contains it 
            if [x,y] ==j:
                b = i#adds the right box in b 
    list = []
    for i in b:#goes through each item in the list of boxes. The list contains locations. Adds the value from each location in list 
        list.append(g[i[0]][i[1]])
    return (list)


def get_row_s(s,x):#gets all the s values for a row 
    return (s[x])

def get_col_s(s,y):#gets all the s values for a coloumn in a list 
    list = []
    for i in range(9):# goes through each row in s and adds the yth element to the list 
        n = s[i][y]
        list.append(n)
    return (list)

def get_box_s(s,x,y):#gets all the values of s from a box
    for i in boxy:#finds the right box from the list of boxes 
        for j in i:#goes through evert element in every box to check if it contains it 
            if [x,y] ==j:
                b = i#adds the right box in b 
    list = []
    for i in b:#goes through each item in the list of boxes. The list contains locations. Adds the s value from each location in list 
        list.append(s[i[0]][i[1]])
    return (list)

def three_row(s):
    for x in range(9):#goes through every row in s 
        for y in range(9):#goes through every coloumn in s 
            if len(s[x][y])==2 :#checks if any cells have exactly 2 possibilities 
                flag = False #indicates if there are any other cell exactly the same as the first in the same row
                coordinate = []#holds the location of the second cell 
                for i in range(9):#checking if there are any other cells which are the same in the same row 
                    if (s[x][y] == s[x][i]) and (y != i):#checking if the two cells are the same values and not the same location
                        coordinate = [x,i]#adding the coordinate 
                        flag = True #indictaing there is a change 
                if flag:#making change if required 
                    for i in range(9):#going through every item in the same row 
                        if (i !=y ) and (i!=coordinate[1]):#making sure not to change two initial cells 
                            if s[x][y][0] in s[x][i]:#checking if value one is in the list
                                s[x][i].remove(s[x][y][0])#if it is in the list removing it 
                            if s[x][y][1] in s[x][i]:#checking of value 2 is in the list 
                                s[x][i].remove(s[x][y][1])#if it is removing it
                    if find_box(x,y) == find_box(x,coordinate[1]):#checking if both are in the same box 
                        for i in find_box(x,y):#if they are in the same box, going through every location in box  
                           if (i != [x,y] ) and (i!=coordinate):#making sure not to change two initial cells 
                                if s[x][y][0] in s[i[0]][i[1]]:#checking if value one is in the list
                                    s[i[0]][i[1]].remove(s[x][y][0])#if it is in the list removing it
                                    
                                if s[x][y][1] in s[i[0]][i[1]]:#checking of value 2 is in the list 
                                    s[i[0]][i[1]].remove(s[x][y][1])#if it is removing it
                                
                    
    return(s)

def three_col(s):
    for x in range(9):#goes through every row in s    
        for y in range(9):#goes through every coloumn in s 
            if len(s[x][y])==2 :#checks if any cells have exactly 2 possibilities 
                flag = False #indicates if there are any other cell exactly the same as the first in the same row
                coordinate = []#holds the location of the second cell 
                for i in range(9):#checking if there are any other cells which are the same in the same row
                    if (s[x][y] == s[i][y]) and (x != i):#checking if the two cells are the same values and not the same location
                        coordinate = [i,y]#adding the coordinate 
                        flag = True#indictaing there is a change 
                if flag:#making change if required 
                    for i in range(9):#going through every item in the same coloumn 
                        if (i !=x ) and (i!=coordinate[0]):#making sure not to change two initial cells 
                            if s[x][y][0] in s[i][y]:#checking if value one is in the list
                                s[i][y].remove(s[x][y][0])#if it is in the list removing it 
                            if s[x][y][1] in s[i][y]:#checking of value 2 is in the list 
                                s[i][y].remove(s[x][y][1])#if it is removing it
                                      
                    if find_box(x,y) == find_box(coordinate[0],y):#checking if both are in the same box 
                        for i in find_box(x,y):#if they are in the same box, going through every location in box  
                            if (i != [x,y] ) and (i!=coordinate):#making sure not to change two initial cells 
                                if s[x][y][0] in s[i[0]][i[1]]:#checking if value one is in the list
                                    s[i[0]][i[1]].remove(s[x][y][0])#if it is in the list removing it 
                                if s[x][y][1] in s[i[0]][i[1]]:#checking of value 2 is in the list 
                                    s[i[0]][i[1]].remove(s[x][y][1])#if it is removing it
    return(s)


def add_s(g,s): #populates s
        for x in range(9):#going through every row in x 
                for y in range(9):#going through evry coloumn in x 
                        if g[x][y] == 0:#checks if cell in empty 
                                for n in range(9):#going through each possible number  in the grid 
                                        if (n+1) not in get_row(g,x):#checks if this number is not in the same row 
                                                if (n+1) not in get_col(g,y):#checks to see in number is not in same colomn 
                                                        if (n+1) not in get_box(g,x,y):#checks to see if number is not in same box 
                                                                if (n+1) not in s[x][y]:#checks to see if number is not already there in s 
                                                                        s[x][y].append((n+1))#adds the number

                        else:
                                #del s[x][y][:] #if there is already a number there, this clears the cell 
                                s[x][y].append(0)#and adds a #to indicate its been filled

       
        three_row(s)
        three_col(s)
        
        return (s)




def one(g,s):#the first round of checking. sees if there is any cell in s which has only one possibility
        
        flag =False #flag to see if there are any changes to the grid 
        for x in range(9):#goes through every row in s
                for y in range(9):#goes through every coloumn in s
                        if len(s[x][y])== 1:#checks if the length is 1
                                if s[x][y][0] != 0: #checks if the length is not 1 because it is empty
                                        n = s[x][y][0]#puts the value of s x,y in n 
                                        g[x][y] = n #putting n in the actual grid
                                        
                                        #s[x][y].clear() #removing the value from s 
                                        #s[x][y].append(0)#replacing it to indicate it is full 
                                        flag = True#shows a change has occured
                    
        return(flag,g)#returning if or not a change has occured

def one_hint(g,s):#the first round of checking. sees if there is any cell in s which has only one possibility
        
        flag =False #flag to see if there are any changes to the grid 
        for x in range(9):#goes through every row in s
                for y in range(9):#goes through every coloumn in s
                        if len(s[x][y])== 1:#checks if the length is 1
                                if s[x][y][0] != 0: #checks if the length is not 1 because it is empty
                                        n = s[x][y][0]#puts the value of s x,y in n 
                                        flag = True#shows a change has occured
                                        return(flag,x,y,n)
                    
        return(flag,g)#returning if or not a change has occured 


def two(g,s):
        flag = False #checks to see if there are any changes made 
        for x in range(9):#goes through all the rows 
                for y in range(9):#goes through all the coloumns 
                        cell = g[x][y]#gets the value 
                        if cell == 0:#only proceeds with the part if this cell is empty 
                                cell_s = s[x][y]#gets the values of s for this cell
                                flag_s = False#indicates if a particular number in cell_s is present only once in a row/coloumn/box 
                                i_permanent = 0
                                for i in cell_s:#going through every element in cell_s
                                        counter_r = 0#keeps track of the number of times i is present in row
                                        counter_c = 0#^for coloumn
                                        counter_b = 0#^for box 
                                        for r in get_row_s(s,x):#going through every element in the row 
                                                if i in r:#checks if the element is present in every element of row(also lists)
                                                        counter_r +=1#if it is present it incriments by 1 
                                            
                                                if counter_r ==1:#if it is only present once(in s[x][y]) then uses the placeholder
                                                        i_permanent = i
                                                        flag_s = True#indicates a change needs to be made 
                                        
                                        for c in get_col_s(s,y):#going through every element in the coloumn 
                                                if i in c:#checks if the element is present in every element of coloumn(also lists)
                                                        counter_c +=1#if it is present it incriments by 1 
                                                if counter_c ==1:#if it is only present once(in s[x][y]) then uses the placeholder
                                                        i_permanent = i
                                                        flag_s = True #indicates a change needs to be made

                                        for b in get_box_s(s,x,y):#going through every element in the box 
                                                if i in b:#checks if the element is present in every element of box(also lists)
                                                        counter_b +=1#if it is present it incriments by 1 
                                                if counter_b ==1:#if it is only present once(in s[x][y]) then uses the placeholder
                                                        i_permanent = i
                                                        flag_s = True#indicates a change needs to be made
                                
                                if flag_s: #if the flag indicates that a change needs to be made 
                                        g[x][y] = i_permanent#the value is changed in the grid 
                                        #clear_s(s)#all the values of s are erased
                                        #add_s(g,s)#all the values are rewritted because the change would have changed posibilities too
                                        flag = True#indicates a change was made to the grid
        return(flag,g)

def two_hint(g,s):
        flag = False #checks to see if there are any changes made 
        for x in range(9):#goes through all the rows 
                for y in range(9):#goes through all the coloumns 
                        cell = g[x][y]#gets the value 
                        if cell == 0:#only proceeds with the part if this cell is empty 
                                cell_s = s[x][y]#gets the values of s for this cell
                                flag_s = False#indicates if a particular number in cell_s is present only once in a row/coloumn/box 
                                i_permanent = 0
                                for i in cell_s:#going through every element in cell_s
                                        counter_r = 0#keeps track of the number of times i is present in row
                                        counter_c = 0#^for coloumn
                                        counter_b = 0#^for box 
                                        for r in get_row_s(s,x):#going through every element in the row 
                                                if i in r:#checks if the element is present in every element of row(also lists)
                                                        counter_r +=1#if it is present it incriments by 1 
                                            
                                                if counter_r ==1:#if it is only present once(in s[x][y]) then uses the placeholder
                                                        i_permanent = i
                                                        flag_s = True#indicates a change needs to be made 
                                        
                                        for c in get_col_s(s,y):#going through every element in the coloumn 
                                                if i in c:#checks if the element is present in every element of coloumn(also lists)
                                                        counter_c +=1#if it is present it incriments by 1 
                                                if counter_c ==1:#if it is only present once(in s[x][y]) then uses the placeholder
                                                        i_permanent = i
                                                        flag_s = True #indicates a change needs to be made

                                        for b in get_box_s(s,x,y):#going through every element in the box 
                                                if i in b:#checks if the element is present in every element of box(also lists)
                                                        counter_b +=1#if it is present it incriments by 1 
                                                if counter_b ==1:#if it is only present once(in s[x][y]) then uses the placeholder
                                                        i_permanent = i
                                                        flag_s = True#indicates a change needs to be made
                                
                                if flag_s: #if the flag indicates that a change needs to be made 
                                        flag = True#indicates a change was made to the grid
                                        return(flag,x,y,i_permanent)
        return(flag,g)


def is_valid(g):#Determins if the grid is solvaable 
    flag = True
    box1 = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
    box2 = [[3,0],[4,0],[5,0],[3,1],[4,1],[5,1],[3,2],[4,2],[5,2]]
    box3 = [[6,0],[7,0],[8,0],[6,1],[7,1],[8,1],[6,2],[7,2],[8,2]]
    box4 = [[0,3],[1,3],[2,3],[0,4],[1,4],[2,4],[0,5],[1,5],[2,5]]
    box5 = [[3,3],[4,3],[5,3],[3,4],[4,4],[5,4],[3,5],[4,5],[5,5]]
    box6 = [[6,3],[7,3],[8,3],[6,4],[7,4],[8,4],[6,5],[7,5],[8,5]]
    box7 = [[0,6],[1,6],[2,6],[0,7],[1,7],[2,7],[0,8],[1,8],[2,8]]
    box8 = [[3,6],[4,6],[5,6],[3,7],[4,7],[5,7],[3,8],[4,8],[5,8]]
    box9 = [[6,6],[7,6],[8,6],[6,7],[7,7],[8,7],[6,8],[7,8],[8,8]]

    boxy = [box1,box2,box3,box4,box5,box6,box7,box8,box9]

    for x in g:#Going through each row in grid 
        st = []
        for y in x:#Going through each col in grid 
            if y !=0:#If cell not empty 
                if y in st:#If number is already in the same row, grid invalid 
                    flag = False
                    return(False)
                else:#Creating a list of numbers already in the row 
                    st.append(y)
    for i in range (9):
        st=[]
        for j in range(9):
            if g[j][i] !=0:#Checking if it is in the same col 
                if g[j][i] in st:
                    flag = False#Gird invalid if number in col
                    return False
                else:
                    st.append(g[j][i])#Creating list of numbers already in col 

    for i in boxy: #Checking if number in same box 
        st = []
        for j in i: 
            if g[j[0]][j[1]] !=0:#if number in same box, grid invalid 
                if g[j[0]][j[1]] in st:
                    flag = False
                    return False
                else:
                    st.append(g[j[0]][j[1]])

    return(flag)




def input():#Screen for inputing the sudoku grid 

    WIDTH = 550#window size 
    background_color = (251,247,245)
    original_grid_element_color = (52, 31, 151)
    buffer = 5

    smallfont = pygame.font.SysFont('Corbel',35) 
    color_light = (170,170,170) 
    # dark shade of the button 
    color_dark = (100,100,100) 


    g1 = [0,0,0,0,0,0,0,0,0]
    g2 = [0,0,0,0,0,0,0,0,0]
    g3 = [0,0,0,0,0,0,0,0,0]
    g4 = [0,0,0,0,0,0,0,0,0]
    g5 = [0,0,0,0,0,0,0,0,0]
    g6 = [0,0,0,0,0,0,0,0,0]
    g7 = [0,0,0,0,0,0,0,0,0]
    g8 = [0,0,0,0,0,0,0,0,0]
    g9 = [0,0,0,0,0,0,0,0,0]
    grid = [g1,g2,g3,g4,g5,g6,g7,g8,g9]

    grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]#Copying grid into different format 

    def insert(win, position):#What happens when a number needs to be inserted 
        i,j = position[1], position[0]#Position of the cell 
        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        if i>10 or i<0 or j>10 or j<0:#Checking if input cell is valid 
            return
        while True:
            for event in pygame.event.get():#If quit, program stops 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:#If a key is pressed 
                    if(event.key == 48): #checking with 0
                        grid[i-1][j-1] = event.key - 48#putting 0 on the grid to indicate blank space  
                        pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        pygame.display.update()#Adding to GUI
                        return
                    if(0 < event.key - 48 <10):  #We are checking for valid input
                        pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        value = myfont.render(str(event.key-48), True, (0,0,0))#The number pressed on keyboard 
                        win.blit(value, (position[0]*50 +15, position[1]*50))#Putting it on the GUI
                        grid[i-1][j-1] = event.key - 48#adding to the grid 
                        pygame.display.update()
                        return
                    return
            


    def main():    
        
        win = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption("Sudoku")
        win.fill(background_color)
        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        text_done = smallfont.render('Done' , True , (255,255,255))
        for i in range(0,10):#Drawing the grid
            if(i%3 == 0):#Making thicker lines every third line to show boxes 
                pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
                pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )#Drawing lines 
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
        pygame.display.update()
        
        for i in range(0, len(grid[0])):#Checking what cells are already filled and adding that to the grid 
            for j in range(0, len(grid[0])):
                if(0 < grid[i][j]<10):
                    value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                    win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
        pygame.display.update()
                
            
        while True: 
            mouse = pygame.mouse.get_pos() 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    #mouse = pygame.mouse.get_pos() 
                    if WIDTH-140 <= mouse[0] <= WIDTH and WIDTH-40 <= mouse[1] <= WIDTH: 
                        #If done button is pressed, value is returned 
                        return(grid)
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:#If button is pressed on grid 
                    #mouse = pygame.mouse.get_pos() 
                    mouse = pygame.mouse.get_pos() 
                    insert(win, (mouse[0]//50, mouse[1]//50))#Inserts number on grid 
                
                if event.type == pygame.QUIT:#If user wants to quit 
                    pygame.quit()
                    return
            

            if WIDTH-140 <= mouse[0] <= WIDTH and WIDTH-40<= mouse[1] <= WIDTH: #Button, different colour on differnt part of screen
                pygame.draw.rect(win,color_light,[WIDTH-140,WIDTH-40,140,40]) 
            else:
                pygame.draw.rect(win,color_dark,[WIDTH-140,WIDTH-40,140,40]) #Hover effect, changes colour when the mouse is over the button 


            win.blit(text_done , (WIDTH-140, WIDTH-40))#Adding text on to of bitton 
            pygame.display.update() 

    main()
    return(grid)
    #return([[8, 0, 0, 0, 5, 2, 0, 0, 0], [0, 0, 3, 8, 4, 6, 0, 7, 5], [0, 7, 5, 9, 0, 1, 0, 0, 0], [0, 5, 1, 3, 0, 4, 6, 0, 0], [0, 8, 6, 5, 2, 0, 0, 1, 7], [2, 9, 4, 1, 0, 0, 0, 8, 3], [0, 1, 0, 4, 7, 0, 0, 0, 0], [4, 0, 7, 2, 9, 5, 0, 0, 8], [5, 0, 0, 6, 0, 8, 0, 4, 9]])

def solution(g,s):#Solves grid 
    
        #print (*g, "g", sep = "\n")
        #print("\n")
        #print (*s, "s", sep = "\n")
        #print("\n")
        if is_it_solved(g):#checks if it has been solved. If it is true the program ends by returning the value otherwise the program continues 
                return g

        else:
                clear_s(s)#clears s
                add_s(g,s)#re populates s
                #print (*s, "sa", sep = "\n")
                #print("\n")
                one_flag = one(g,s)#runs the first algorithm on g and s 

                if one_flag[0]:#if any changes occur because of one reruns the program
                        g = one_flag[1]
                        solution(g,s)
                two_flag = two(g,s)#runs second algorithm
                #print (*s, "s", sep = "\n")
                #print("\n")
                if two_flag[0]:#if changes were made
                        g = two_flag[1]
                        solution(g,s)#runs program again
                if is_it_solved(one_flag[1]):#checks if it has been solved. If it is true the program ends by returning the value otherwise the program continues 
                        return one_flag[1]
                if is_it_solved(two_flag[1]):#checks if it has been solved. If it is true the program ends by returning the value otherwise the program continues 
                        return two_flag[1]
                
        if is_it_solved(g):#checks if it has been solved. If it is true the program ends by returning the value otherwise the program continues 
                return g
        clear_s(s)#clears s
        add_s(g,s)#re populates s
        g = one(g,s)
        
        g = g[1]

        #print (*g, "g", sep = "\n")
        #print("\n")

        solution(g,s)

    

def hint(g):#What happens when user asks for hint 
        clear_s(s)#clears s
        add_s(g,s)#re populates s
        one_flag = one_hint(g,s)#returns value of hint 
        if one_flag[0]:
                return one_flag
        two_flag = two_hint(g,s)#Returns value of hint 
        if two_flag[0]:
            return two_flag
        start()
    

def solve_win(complete, original):#Screen once the solve button has been pressed 
    WIDTH = 550
    background_color = (251,247,245)
    original_grid_element_color = (52, 31, 151)
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    smallfont = pygame.font.SysFont('Corbel',35) 
    color_light = (170,170,170) 
    # dark shade of the button 
    color_dark = (100,100,100) 
   
    buffer = 5
    text_home = smallfont.render('home' , True , (255,255,255))
    for i in range(0,10):
        if(i%3 == 0):#Drawing grid again 
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
    
    for i in range(0, len(original[0])):#Adding the numbers originally in the grid in different colour 
        for j in range(0, len(original[0])):#Numbers originallly in grid 
            if(0<original[i][j]<10):
                value = myfont.render(str(original[i][j]), True, (0,0,0))
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
            elif (0<complete[i][j]<10) :#Numbers in comppleted grid added 
                value = myfont.render(str(complete[i][j]), True, (255,0,255))
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))

    pygame.display.update()
    while True: 
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos() 
                if WIDTH-140 <= mouse[0] <= WIDTH and WIDTH-40 <= mouse[1] <= WIDTH: 
                    start()#Goes back to home is button is pressed 
                    
            if event.type == pygame.QUIT:#Quits when user quits 
                pygame.quit()
                return

        if WIDTH-140 <= mouse[0] <= WIDTH and WIDTH-40<= mouse[1] <= WIDTH: #Button, different color when mouse over it 
            pygame.draw.rect(win,color_light,[WIDTH-140,WIDTH-40,140,40]) 
        else:
            pygame.draw.rect(win,color_dark,[WIDTH-140,WIDTH-40,140,40]) #Colour of button when mouse not there 


        win.blit(text_home , (WIDTH-140, WIDTH-40))#Adding text to button 
        pygame.display.update() 
    


def write(g):#When user is solving the grid 
    smallfont = pygame.font.SysFont('Corbel',35) 
    color_light = (170,170,170) 
    # dark shade of the button 
    color_dark = (100,100,100) 
    WIDTH = 550
    background_color = (251,247,245)
    original_grid_element_color = (52, 31, 151)
    hint_grid_element_color = (255, 0, 0)
    largefont = pygame.font.SysFont('Corbel',50) 

    buffer = 5
    color = (255,255,255) 

    text_done = smallfont.render('Done' , True , (255,255,255))
    


    grid = g
    grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
    
    def insert(win, position):#When user wants to add something to grid 
        i,j = position[1], position[0]#Position of cell 
        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        
        if i>=10 or i<=0 or j>=10 or j<=0:
            gridcheck = 12#Invalid grid 
            return
        else:
            gridcheck = grid_original[i-1][j-1]#checking if the value of cell is 0
        

        while True:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:#quits when user quits 
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if(gridcheck != 0):#Not continuing if cell is not 0
                        return
                    if(event.key == 48): #checking with 0
                        grid[i-1][j-1] = event.key - 48#Emptying grid 
                        pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        pygame.display.update()#Deleting value 
                        return
                    if(0 < event.key - 48 <10):  #We are checking for valid input
                        pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        value = myfont.render(str(event.key-48), True, original_grid_element_color)
                        gr = grid
                        gr[i-1][j-1] = event.key - 48#Making new grid with added value 
                        if is_valid(gr):
                            win.blit(value, (position[0]*50 +15, position[1]*50))
                            grid[i-1][j-1] = event.key - 48#Checking if the new grid is valid with input 
                            pygame.display.update()#Updating if true 
                            return
                        else:#Indicating wrong input with red button 
                            pygame.draw.rect(win,(255,0,0),[0,0,35,35]) 
                            pygame.display.update()
                            pygame.time.delay(2000)
                            pygame.draw.rect(win,background_color,[0,0,35,35]) 
                            pygame.display.update()
                            return


                    return
            


    def main_a():    
        pygame.init()
        win = pygame.display.set_mode((WIDTH, WIDTH))
        pygame.display.set_caption("Sudoku")
        win.fill(background_color)
        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        text_solve = smallfont.render('solve' , True , (255,255,255))
        text_hint = smallfont.render('hint' , True , (255,255,255))
        
        for i in range(0,10):#Drawing grid 
            if(i%3 == 0):
                pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
                pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
        pygame.display.update()
        
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid[0])):#Adding values already in there 
                if(0<grid[i][j]<10):
                    value = myfont.render(str(grid[i][j]), True, (0,0,0))
                    win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
        pygame.display.update()
                
            
        while True: 
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                
                   
                    
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    insert(win, (mouse[0]//50, mouse[1]//50))#If a cell is left clicked 

                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos() 
                    if WIDTH-140 <= mouse[0] <= WIDTH and WIDTH-40 <= mouse[1] <= WIDTH: 
                        answer = solution(grid,s) #if the solve button is pressed, answer is recieved 
                        
                        if answer == False:#If answer is not there, program restarts 
                            start()
                        else:
                            solve_win(answer,grid_original)#Goes to solved page if it is a valid grid 

                       
                    if 0 <= mouse[0] <= 140 and WIDTH-40<= mouse[1] <= WIDTH: #If hint button is pressed 
                        hint_a = hint(grid) #Calls hint fucnction if button is pressed 
                        
                        if hint_a[0]:#Checking if there is a hint 
                
                            value = myfont.render(str(hint_a[3]), True, hint_grid_element_color)
                            grid[hint_a[1]][hint_a[2]] = hint_a[3]
                            win.blit(value, ((hint_a[2]+1)*50 + 15, (hint_a[1]+1)*50 ))#Adds hint value to the grid in different colour 
                            #grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
                            pygame.display.update()
                        elif hint_a[0] == None:#If there is no hint, program restarts 
                            start()
                             
                            
                        else:
                            win.fill((0,0,0))#Checking if grid is invalid 
                            win.blit(largefont.render('INVALID' , True , color) , (width/3,width/3)) 
                            pygame.display.update() 
                            pygame.time.delay(5000)
                            start()
                            

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if is_it_solved(grid):#If grid is solved, redicts to new page and restarts program 
                win.fill((0,0,0))
                win.blit(largefont.render('You win' , True , color) , (WIDTH/3,WIDTH/3)) 
                pygame.display.update() 
                pygame.time.delay(3500)
                start()

            if WIDTH-140 <= mouse[0] <= WIDTH and WIDTH-40<= mouse[1] <= WIDTH: #Button and hover effect 
                pygame.draw.rect(win,color_light,[WIDTH-140,WIDTH-40,140,40]) 
            else:
                pygame.draw.rect(win,color_dark,[WIDTH-140,WIDTH-40,140,40])

            if 0 <= mouse[0] <= 140 and WIDTH-40<= mouse[1] <= WIDTH: 
                pygame.draw.rect(win,color_light,[0,WIDTH-40,140,40]) 
            else:
                pygame.draw.rect(win,color_dark,[0,WIDTH-40,140,40]) 


            win.blit(text_solve , (WIDTH-140, WIDTH-40))#Adding texts to button 
            win.blit(text_hint , (0, WIDTH-40))
            pygame.display.update() 
       
    main_a()
    return(grid)


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
        #the function that adds text to the screen 
    words = [word.split(' ') for word in text.splitlines()]
    # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    return()


def instructions(text):#The function which is a new screen and has a home button 
    SIZE = WIDTH, HEIGHT = (1024, 720)
    FPS = 30
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 30)
    color_light = (170,170,170) 
    # dark shade of the button 
    color_dark = (100,100,100)
    smallfont = pygame.font.SysFont('Corbel',35)
    text_home = smallfont.render('Home' , True , (255,255,255))
     

    while True:
        dt = clock.tick(30) / 1000
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Quits when it wuits 
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                    #If home button is pressed, program restarts 
                if 550-140 <= mouse[0] <= 550 and 550-40 <= mouse[1] <= 550:
                    start()
                                    
            screen.fill(pygame.Color('white'))#Setting screen 
            blit_text(screen, text, (20, 20), font)#Adding text to the screen(Instructions 
            if 550-140 <= mouse[0] <= 550 and 550-40 <= mouse[1] <= 550: #Drawing button with hover effect 
                pygame.draw.rect(screen,color_light,[550-140,550-40,140,40])
            else:
                pygame.draw.rect(screen,color_dark,[550-140,550-40,140,40])


            screen.blit(text_home ,(550-140,550-40))#Adding text to button 
            pygame.display.update()


def start():
    pygame.init()
    # initializing the constructor 
    pygame.init() 
    # screen resolution 
    res = (650,650) 
    # opens up a window 
    screen = pygame.display.set_mode(res) 
    # white color 
    color = (255,255,255) 
    # light shade of the button 
    color_light = (170,170,170) 
    # dark shade of the button 
    color_dark = (100,100,100) 
    # stores the width of the 
    # screen into a variable 
    width = screen.get_width() 
    # stores the height of the 
    # screen into a variable 
    height = screen.get_height() 
    clock = pygame.time.Clock()
    # defining a font 
    smallfont = pygame.font.SysFont('Corbel',35) 
    largefont = pygame.font.SysFont('Corbel',50)
    # rendering a text written in 
    # this font 

    
    text_quit = smallfont.render('Quit' , True , color)
    
    text_start= smallfont.render('Start' , True , color) 
    text_instruction= smallfont.render('Instructions' , True , color) 
    clear_s(s)

    text = "Each Sudoku is on a grid of 9 by 9 spaces. Each row,column and box is supposed to be filled exactly once with" \
            "the numbers 1-9, without repeating any numbers.\nWhen you press start, you can input any puzzle you are not able to solve." \
            "Once you have filled up the grid, press done to play. If you input a wrong number, a red box will indicate your mistake. Press " \
            "Hint if you are stuck and solve if you would like the solution"
    
    while True: 
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                pygame.quit() 
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONUP: 
                #if the mouse is clicked on the 
                # button the game is terminated 
                if width/2 <= mouse[0] <= width/2+150 and height/2 <= mouse[1] <= height/2+40: 
                    pygame.quit()
                elif width/2 <= mouse[0] <= width/2+150 and height/3 <= mouse[1] <= height/3+40:
                        instructions(text)
                    
                elif width/2 <= mouse[0] <= width/2+150 and height/4 <= mouse[1] <= height/4+40:
                    grid = input()
                    if is_valid(grid):
                        #sample = [[8, 0, 0, 0, 5, 4, 0, 0, 0], [0, 0, 3, 8, 4, 6, 0, 7, 5], [0, 7, 5, 9, 0, 1, 0, 0, 0], [0, 5, 1, 3, 0, 4, 6, 0, 0], [0, 8, 6, 5, 2, 0, 0, 1, 7], [2, 9, 4, 1, 0, 0, 0, 8, 3], [0, 1, 0, 4, 7, 0, 0, 0, 0], [4, 0, 7, 2, 9, 5, 0, 0, 8], [5, 0, 0, 6, 0, 8, 0, 4, 9]]
                        #write(grid)
                        write(grid)
                    else:
                        screen.fill((0,0,0))
                        screen.blit(largefont.render('INVALID' , True , color) , (width/3,width/3)) 
                        pygame.display.update() 
                        pygame.time.delay(3500)
                        start()

                        pygame.display.update() 

        screen.fill((60,25,60)) 
              
            # stores the (x,y) coordinates into 
            # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
              
            # if mouse is hovered on a button it 
            # changes to lighter shade 
        if width/2 <= mouse[0] <= width/2+150 and height/2 <= mouse[1] <= height/2+40: 
            pygame.draw.rect(screen,color_light,[width/2,height/2,150,40]) 
        elif width/2 <= mouse[0] <= width/2+150 and height/4 <= mouse[1] <= height/4+40:
            pygame.draw.rect(screen,color_light,[width/2,height/4,150,40])
        elif width/2 <= mouse[0] <= width/2+150 and height/3 <= mouse[1] <= height/3+40:
            pygame.draw.rect(screen,color_light,[width/2,height/3,150,40])
        else: 
            pygame.draw.rect(screen,color_dark,[width/2,height/2,150,40]) 
            pygame.draw.rect(screen,color_dark,[width/2,height/4,150,40])
            pygame.draw.rect(screen,color_dark,[width/2,height/3,150,40])
            
          
        # superimposing the text onto our button 
        screen.blit(text_quit , (width/2+50,height/2)) 
        screen.blit(text_start , (width/2+50,height/4))
        screen.blit(text_instruction ,(width/2,height/3))
         
        # updates the frames of the game 
        pygame.display.update() 

start()


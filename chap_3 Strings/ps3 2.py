#program to fill in a letter templet given below with name and date
#letter =''' Dear <|name|>
#            yor are selected!
#             <|date|>
name = input("enter your name:")
date = input("Enter the date:")

letter = ''' 
             Dear <|name|> 
             you are selected!
             <|date|>
         '''
print(letter.replace('<|name|>', name).replace('<|date|>', date))








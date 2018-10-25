#koment
import os
from random import *

def main():          
    message='''The classic Sudoku game involves a grid of 81 squares. 
The grid is divided into nine blocks, each containing nine squares. 
The rules of the game are simple: 
each of the nine blocks has to contain all the numbers 1-9 within its squares. 
Each number can only appear once in a row, column or box.

To enter a number select a row then a column and the number of your choice.
At any moment you can check your board by entering [0].
Have fun and good luck!'''

    def random_chart_generator():
        with open('sudoku.csv', 'r') as file:
            lines = file.readlines()
            os.system('clear')
            print(f'{message}')
            choice=input('''Enter a number between 1 and 1000000 to play the chart of your choice \nor press[0] to play a random chart: ''')
            while choice.isalpha():
                choice=input('Wrong input! Enter a number between 1 and 1000000: ') 
            while int(choice) <0 or int(choice)>1000000:
                choice=input('Wrong input! Enter a number between 1 and 1000000: ') 
            if choice =='0':
                chart_number= randint(1,1000000)
            else:
                chart_number=int(choice)
            random_line = lines[chart_number]
            return random_line, chart_number



    #dzieli stringa na liste 2 stringowiiii
    def sort_lines(string_to_split):
            chart_list = string_to_split.split(',')
            return chart_list


    def convert_listofstr_to_listoflists(listofstrings,n):
            filled_in_list=[['']*9 for num in range(9)]
            for chatr in range(2):
                for list in range(9):
                        for letter in range(9):
                                filled_in_list[list][letter]=listofstrings[n][list+letter+(list*8)]    
            return filled_in_list

    chart, chart_number=random_chart_generator()
    sorted_charts = sort_lines(chart)
    display_list=convert_listofstr_to_listoflists(sorted_charts,0)
    templet=convert_listofstr_to_listoflists(sorted_charts,1)       
    all_numbers=('1','2','3','4','5','6','7','8','9','0')

    def show_list(g):
        print(f'{white_on_black()}  1 2 3 4 5 6 7 8 9 {end_col()}')
        for i in range(3):
            for d in range(1):
                print(f'{white_on_black()}{i+1} {end_col()}{red()}{" ".join(g[d+i][0:3])}{end_col()} {" ".join(g[d+i][3:6])} {red()}{" ".join(g[d+i][6:9])}{end_col()}')
        for i in range(3,6):
            for d in range(1):
                print(f'{white_on_black()}{i+1} {end_col()}{" ".join(g[d+i][0:3])} {red()}{" ".join(g[d+i][3:6])}{end_col()} {" ".join(g[d+i][6:9])}' )
        for i in range(6,9):
            for d in range(1):
                print(f'{white_on_black()}{i+1} {end_col()}{red()}{" ".join(g[d+i][0:3])}{end_col()} {" ".join(g[d+i][3:6])} {red()}{" ".join(g[d+i][6:9])}{end_col()}' )

    def red():
        return '\33[31m\033[1m' 

    def white_on_black():
        return '\33[7m'

    def end_col():
        return '\033[0m'

    



    def stop_game():
        if display_list == templet:
            print('\nYou Win!\n')
            show_list(templet)
            play_again = input("To try again press [y] or any other key to exit: ")
        else:
            print('\nYou Lose!\n')
            show_list(display_list)
            print('\nCorrect sudoku is:\n')
            show_list(templet)
            play_again = input("To try again press [y] or any other key to exit: ")
        if play_again == "y":
            os.system('clear')
            
            return main()


    def add_new_number():
        all_numbers=('1','2','3','4','5','6','7','8','9','0')
        os.system('clear')
        print(f'Sudoku chart number: {chart_number}\n') 
        show_list(display_list)
        x = input('Enter row number or press[0] to check: ')
        while x not in all_numbers:
            x = input('Wrong Input! Enter row number or press[0] to check: ')
        if x == '0':
            stop_game()
        else:
            y = input('Enter column number or press[0] to check: ') 
            while y not in all_numbers:
                y = input('Wrong Input! Enter column number or press[0] to check: ')
            if y== '0':
                
                stop_game()
            else:
                new_number = input('Enter a number: ')
                while new_number not in all_numbers:
                    new_number = input('Wrong Input! Enter a number or press[0] to check: ')
                if new_number== '0':
                    stop_game()
                else:
                    display_list[int(x)-1][int(y)-1] = new_number
                    return(add_new_number())
        
    add_new_number()    
main()




# kolory oznaczen kolumn i rzedow DONE!
# mozliwosc wprowadzenia tylko od 1 do 9 na kazdym etapie DONE!
# try - except?
# opis + zasady - tylko przy pierwszym wyswietleniu oraz po try again
# prezentacja - screen'y, filmik BANG!
# tabelka
# random board
# functions, reduce the code length

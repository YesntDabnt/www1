#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <stdio.h>


#define CLEAR_BUFFER while(getchar() != '\n');

#define BOARD_SIZE 15
#define CHAIN 5
#define PLAYER 'X'
#define COMPUTER 'O'

void init_board(char board[BOARD_SIZE][BOARD_SIZE], int size);
void print_board(char board[BOARD_SIZE][BOARD_SIZE], int size);
void print_stats(int player_wins, int draws, int computer_wins);
void update_stats(int result, int *player_wins, int *draws, int *computer_wins);
void print_result(int result);
int next_turn(int turn);
int winner(char board[BOARD_SIZE][BOARD_SIZE], int size, int turn, int *result);
void player(char board[BOARD_SIZE][BOARD_SIZE], int size, int *row, int *col);
void computer(char board[BOARD_SIZE][BOARD_SIZE], int size, int *row, int *col);
int play_again();

int main(int argc, char *argv[]){
    int play, size, turn, row, col, result;
    int player_wins, draws, computer_wins;
    char board[BOARD_SIZE][BOARD_SIZE];
    
    size = BOARD_SIZE;
    play = 1;
    player_wins = 0;
    draws = 0;
    computer_wins = 0;
    
    while(play){
        printf("G O M O K U \n");
        init_board(board, size);
        print_stats(player_wins, draws, computer_wins);
        print_board(board, size);

        turn = 1;
        while(winner(board, size, turn, &result)){
            if(next_turn(turn)){
                player(board, size, &row, &col);
                board[row][col] = PLAYER;
            }
            else{
                computer(board, size, &row, &col);
                board[row][col] = COMPUTER;
            }
            print_stats(player_wins, draws, computer_wins);
            print_board(board, size);
            turn++;
        }
        update_stats(result, &player_wins, &draws, &computer_wins);
        print_result(result);
        play=play_again();
    }
    
    return 0;
}

void init_board(char board[BOARD_SIZE][BOARD_SIZE], int size){
    for(int row = 0; row < size; row++){
        for(int col = 0; col < size; col++){
            board[row][col] = '+';
        }
    }
}

void print_board(char board[BOARD_SIZE][BOARD_SIZE], int size){

    printf(" --------------------------------------------------------------- \n");
    for(int row = 0; row < size; row++){
        printf("|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |\n");
        printf("|");
        for(int col=0;col < size; col++){
            printf("---%c", board[row][col]);
        }
        printf("---|\n");
        }
    printf("|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |\n");
    printf(" --------------------------------------------------------------- \n");
}

void print_stats(int player_wins, int draws, int computer_wins){
    printf("PLAYER: %d\n", player_wins);
    printf("DRAWS: %d\n", draws);
    printf("COMPUTER: %d\n", computer_wins);
}

void player(char board[BOARD_SIZE][BOARD_SIZE], int size, int *row, int *col){
    do{
        do{
            printf("row: ");
            scanf("%d", row);
            
        }while(*row < 0 || *row >= size);
        do{
            printf("col: ");
            scanf("%d", col);
        }while(*col < 0 || *col >= size);
    } while(board[*row][*col] == COMPUTER || board[*row][*col] == PLAYER);
}

void update_stats(int result, int*player_wins, int*draws, int*computer_wins){
    if (result==1)
    {
       ++*player_wins;
    }
    else if(result==2)
    {
        ++*computer_wins;
    }
    else if(result==-1)
    {
        ++*draws;
    }
    else {
        printf("something went wrong");
    }
}

void print_result(int result){
    if(result==1){
        printf("PLAYER WINS!");
    }
    else if(result==2)
    {
        printf("COMPUTER WINS!");
    }
    else if(result==-1)
    {
        printf("DRAW!");
    }
}
int next_turn(int turn){
    return (turn % 2);
}

int winner(char board[BOARD_SIZE][BOARD_SIZE], int size, int turn, int *result){
    int sum = 1;
    int counter = 0;
    *result = 0;
    
    for(int row=0; row < size; row++){
        for(int col=0; col < size; col++){
            if(board[row][col] == PLAYER){
                for(int i=row; i<row + CHAIN && board[i][col] == board[i + 1][col]; i++){
                    sum++;
                }
                if(sum == CHAIN){
                    *result = 1;
                }
                else {
                    sum = 1;
                }
                for(int i=col; i<col + CHAIN && board[row][i] == board[row][i+1]; i++){
                    sum++;
                }
                if(sum == CHAIN){
                    *result = 1; 
                }
                else {
                    sum = 1;
                }
                counter++;
            }
            else if(board[row][col] == COMPUTER){
                for(int i=row; i< row + CHAIN && board[i][col] == board[i+1][col]; i++){
                    sum++;
                }
                if(sum == CHAIN){
                    *result = 2;
                }
                else {
                    sum = 1;
                }
                for(int i=col; i<col + CHAIN && board[row][i] == board[row][i+1]; i++){
                    sum++;
                }
                if(sum == CHAIN){
                    *result = 2; 
                }
                else {
                    sum = 1;
                }
                counter++;
            }
        }
    }
    if(counter == 215){
       *result = -1;
    }
    
    if(*result == 0){
        return 1;
    } else {
        return 0;
    }
}

void computer(char board[BOARD_SIZE][BOARD_SIZE], int size, int *row, int *col){
    do{
        srand(time(NULL));
        *row = rand() % size;
        *col = rand() % size;
    }while(board[*row][*col] == PLAYER || board[*row][*col] == COMPUTER);
}

int play_again(){
    char answer;
    int x;

    do{
        printf("Do you want to play again? (y/n) \n");
        CLEAR_BUFFER
        scanf("%c", &answer);

        if(answer == 'y'){
            x = 1;
        }
        else if(answer == 'n'){
            x = 0;
        }
        else {
            printf("Wrong input! Please try again.");
        }
    } while(answer != 'y' && answer != 'n');

    return x;
}
gomoku.c
Displaying gomoku.c.
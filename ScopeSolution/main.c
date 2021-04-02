#include <math.h>
#include <stdio.h>
#include <stdbool.h>

#include "tests.h"


int global1 = 10;
double global2 = 25;

typedef struct hobby {
    char * description;
    int yearsPracticed;
    int nerdFactor;
    bool maxLevelAchieved;
    float moneyExpendedOnHappiness;
} Hobby;

int multiply(int a, int b) {
    return a * b;
}

void newVersionOfHobbyReleased(Hobby * hobby) {
    hobby->maxLevelAchieved = false;
    hobby->moneyExpendedOnHappiness = hobby->moneyExpendedOnHappiness + 1000;
}

int main(void) {
    /*
        Types of Scope:
        1. File or Global Scope: These include variables and other identifiers
              that are global and are visible throughout a given file
        2. Block Scope: Scope as defined by opening and closing curly braces - {}.
              Identifiers defined within the curly braces are local to the block
        4. Function Scope: Begins a the opening of a function and closes at the
              end of it.
    */

    // Global Scope 1
    // - Update the code below to set global to a new value

    // v------Write code below--------v
    global1 = 15;
    // ^-------Write code above-------^
    globalTest1(global1);

    // Global Scope 2
    // - Uncomment the code between the update lines below. What do you
    //     expect the second printf to say?
    // - Pass the test by successfully setting global2 to the square root
    //     of 1,089

    // v------Update code below--------v
    printf("global2 %.0f\n", global2);
    double global2 = sqrt(1089);
    printf("global2 %.0f\n", global2);

    // ^-------Update code above-------^
    globalTest2(global2);

    // Block Scope
    // - Examine the code below - what do you think these will print?
    // - Uncomment the printfs to see if you were right!
    // - To pass the test, update the code so the final value of y is
    // -   equal to 42
    {
        int x = 10, y = 20;
        {
            //printf("x = %d, y = %d\n", x, y);
            {
                int y = 40;
                x++;
                y++;

                //printf("x = %d, y = %d\n", x, y);
            }
            //printf("x = %d, y = %d\n", x, y); // <--This final y should print 42
        }
        y = 42;
        blockTest(y);
    }

    // Function Scope 1
    // - The function "multiply" currently doesn't seem to be doing us much good -
    //     what happens to the values of a and b when they are passed into muliply?
    // - Update the multiply function and the code below so that result contains the
    //     expected value
    int a = 52, b = 26;

    // v------Update code below--------v
    //int result;
    int result = multiply(a, b);

    // ^-------Update code above-------^
    functionTest1(result);

    // Function Scope 2
    // - Check out the function referenced below - if you uncomment the printf,
    //     will the struct have been changed?
    // - Update the signature of newVersionOfHobbyReleased and the code below
    //     to pass the test

    Hobby hobby = { "Favorite Video Game", 6, 100, true, 1000 };

    newVersionOfHobbyReleased(&hobby);

    printf("New value of expenditure: $%.2f\n", hobby.moneyExpendedOnHappiness);
    functionTest2(hobby.moneyExpendedOnHappiness);


}
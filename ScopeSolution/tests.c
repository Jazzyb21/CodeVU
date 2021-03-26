#include <stdio.h>

#include "tests.h"

void globalTest1(int globalVar) {
    printf("Global Test 1: ");
    if (globalVar == 10) {
        printf("\033[0;31mFailed: Value is still 10\033[0m\n");
        return;
    }
    printf("\033[0;32mPassed\033[0m\n");
}

void globalTest2(double globalVar) {
    printf("Global Test 2: ");
    if (globalVar != 33) {
        printf("\033[0;31mFailed: Value is not the sqrt of 1,089\033[0m\n");
        return;
    }
    printf("\033[0;32mPassed\033[0m\n");
}

void blockTest(int blockVar) {
    printf("Block Scope Test: ");
    if (blockVar != 42) {
        printf("\033[0;31mFailed: Value is != 42\033[0m\n");
        return;
    }
    printf("\033[0;32mPassed\033[0m\n");
}

void functionTest1(int result) {
    printf("Function Scope Test 1: ");
    if (result != 1352) {
        printf("\033[0;31mFailed: Value is != a * b\033[0m\n");
        return;
    }
    printf("\033[0;32mPassed\033[0m\n");
}

void functionTest2(float result) {
    printf("Function Scope Test 2: ");
    if (result != 2000) {
        printf("\033[0;31mFailed: Value is != 2000\033[0m\n");
        return;
    }
    printf("\033[0;32mPassed\033[0m\n");
}
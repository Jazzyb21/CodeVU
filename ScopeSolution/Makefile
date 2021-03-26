play : main.o tests.o
	cc -o play main.o tests.o -L. -lcs50
	
tests.o : tests.c tests.h
	cc -c tests.c

main.o : main.c
	cc -c main.c

clean :
	@rm -f *.o
	@rm -f play
	@echo Clean as a whistle!

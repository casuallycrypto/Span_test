# Span coding test

This coding assessment is a ranking application, which takes in either manually typed text input or a file name, and then returns a sorted ranking table. The rules are set out below:

The rules
In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0 points.
If two or more teams have the same number of points, they should have the same rank and be
printed in alphabetical order (as in the tie for 3rd place in the sample data).


Sample input:
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0

Expected output:
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts

To run this test, in your terminal use:

"python3 ranking_table.py" and follow the prompts

To run the test file in your terminal use:
"pyhon3 tests.py" 

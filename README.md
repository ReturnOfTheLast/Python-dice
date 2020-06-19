# Python-dice
A python dice module

## Usage
The module can be loaded by `import dice` in a python shell or python script

The module has 4 methods:
1. roll (`roll(dCount, dSides)`)

Rolls `dCount` number of `dSides` sided dice

2. multiRoll (`multiRoll([[dCount_1, dSides_1], [dCount_2, dSides_2], ...])`)

Rolls multiple different sided dice

3. calculateAverage (`calculateAverage(dCount, dSides)`)

Calculates the average of a roll

4. calculateMultiAverage (`calculateMultiAverage([[dCount_1, dSides_1], [dCount_2, dSides_2], ...])`)

Calculates the average of multiple rolls


All methods have the option to supress messages by passing `quiet=True` as an additional argument 
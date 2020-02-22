# kenken-partition

This is a simple Python script to help you solve your KenKen puzzles.

This assumes your default Python is Python 3.

Examples:
```
$ ./partition.py 10+ in 3 from 1-6
Max-repeat  Numbers
     1      [1, 3, 6]
     1      [1, 4, 5]
     2      [2, 2, 6]
     1      [2, 3, 5]
     2      [2, 4, 4]
     2      [3, 3, 4]

$ ./partition.py 72x in 3 from 1-6
Max-repeat  Numbers
     2      [2, 6, 6]
     1      [3, 4, 6]
```

Here's the docstring:
```
    Usage:

        ./partition.py [clue] in [num squares] from [range]

        [clue] can be, eg, 150x or 10+ or 4-

        [num squares] is an integer

        [range] is an inclusive integer range, eg, 1-4, 1-6, 3-7
        
    For example:

        ./partition.py 150x in 3 from 1-6

            Prints out all 3-square multiplicative partitions of 150 using the
            numbers 1-6.

    The requirement of the delimiter words "in" and "from" is designed to help
    you remember the order and meaning of the arguments.
```

README.template

## Project Number/Title 

* Authors: Rory Long, Riley Turner, Michelle Nguyen
* Group name: UG_Group89

## Overview

This program implements parallel merge sort using the pthread library. 
It extends the original merge sort algorithm by creating multiple threads to sort subarrays in parallel, 
allowing faster sorting on multi-core systems. 

## Manifest

mergesort.c – Has the functions to implement serial and parallel merge sort, including merge(), my_mergesort(), parallel_mergesort(), and buildArgs().
mergesort.h – Header file defining global variables, functions, and the struct argument used for thread arguments.
test-mergesort.c – Testing program that generates a random array and measures sorting performance.

## Building the project

1. You must have a C compiler with pthread support
2. From the project folder, run: make (This will compile the code and produce the executable file "test-mergesort")

## Features and usage

- Single-threaded merge sort: When the cutoff is set to 0, the program uses standard recursive merge sort.
- Parallel merge sort: When the cutoff is greater than 0, the program creates threads up to the specified level to sort subarrays concurrently.

To run the executeable use the format below:
./test-mergesort <input size> <cutoff level> <seed>

Input Parameters 
- input size – number of elements in the array
- cutoff level – maximum recursion level to create threads
- seed – random seed for array generation

## Testing

This section should detail how you tested your code. Simply stating "I ran
it a few times and it seems to work" is not sufficient. Your testing needs
to be detailed here.

## Known Bugs

List known bugs that you weren't able to fix (or ran out of time to fix).

## Reflection and Self Assessment

Discuss the issues you encountered during development and testing. What
problems did you have? What did you have to research and learn on your own?
What kinds of errors did you get? How did you fix them?

What parts of the project did you find challenging? Is there anything that
finally "clicked" for you in the process of working on this project? How well
did the development and testing process go for you?

## Sources Used

If you used any sources outside of the textbook, you should list them here. 
If you looked something up on stackoverflow.com or you use help from AI, and 
fail to cite it in this section, it will be considered plagiarism and dealt 
with accordingly. So be safe CITE!

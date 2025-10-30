README.template

## Project Number/Title 

* Authors: Rory Long, Riley Turner, Michelle Nguyen
* Group name: UG_Group89

## Overview

This program implements parallel merge sort using the `pthread` library. 
It extends the original merge sort algorithm by creating multiple threads to sort subarrays in parallel, 
allowing faster sorting on multi-core systems. 

## Manifest

* `mergesort.c` - Has the functions to implement serial and parallel merge sort, including merge(), my_mergesort(), parallel_mergesort(), and buildArgs().

* `mergesort.h` – Header file defining global variables, functions, and the struct argument used for thread arguments.

* `test-mergesort.c` – Testing program that generates a random array and measures sorting performance.

## Building the project

### Required libraries/ software
1. `pthread` library
2. `gcc/clang` C compiler

### Building the project 
1. From the project folder `./comp2002-os-mergesort`, run: `make`. This will compile the code and produce the executable file `test-mergesort`.
2. Run the test: `./test-mergesort <input size> <cutoff level> <seed>`. Details on the input parameters are found in the [next section](#features-and-usage)

## Features and usage

### Program usage
To run the executeable use the format below:
`./test-mergesort <input size> <cutoff level> <seed>`

Input Parameters 
- `input size` – number of elements in the array
- `cutoff level` – maximum recursion level to create threads
- `seed` – seed for random array generation

### Summary of program main features
- When the `cutoff` is set to 0, the program uses standard recursive merge sort. The output shows the runtime of **single-threaded merge sort**.

- When the `cutoff` is greater than 0, the program creates threads up to the specified level (derived from `cutoff`) to sort subarrays concurrently. The output shows the runtime of **parallel merge sort**.
    > Note: the number of threads is `2**cutoff` in this case.

## Testing

### Running our test `.py` code
1. Make sure you are in our project folder `./comp2002-os-mergesort`
2. Create a new environment if you have not done so: `python -m venv ./test/.venv`
3. Activate `source ./test/.venv/bin/activate` (for MacOS/Linux)
4. Use our requirements.txt to install dependencies: `pip install -r ./test/requirements.txt`
Our dependencies in requirements.txt include
* Pandas
* Matplotlib
5. (1) Run our first script to generate a csv, summarising the results of all runs: 
 `python ./test/create_test_csv.py`
    * Go to this script to adjust the inputs you want to run in the batch: inputs, cutoffs and seeds.
    * Output is a csv file with the name "results_{datetime}.csv" in the ./test/results folder.
6. (2.1) To see the table png of the result, run `python ./test/create_table.py`. This will run the latest created csv file. You can also change the csv file directly in this file.
7. (2.2) To see the scatter plot of the result, run `python ./test/create_plots.py`. 
* This will run the latest created csv file. 
* To select the control, edit this script.

### Record of our past testing results and discussion

[Placeholder] Attach the images, tables with meaningful results here
[Discussion] Discuss the key insights from these results

## Known Bugs

[Placeholder] List known bugs that you weren't able to fix (or ran out of time to fix).
* Too many threads -> program crashes???

## Reflection and Self Assessment

Discuss the issues you encountered during development and testing. What
problems did you have? What did you have to research and learn on your own?
What kinds of errors did you get? How did you fix them?

What parts of the project did you find challenging? Is there anything that
finally "clicked" for you in the process of working on this project? How well did the development and testing process go for you?

## Sources Used

If you used any sources outside of the textbook, you should list them here. 
If you looked something up on stackoverflow.com or you use help from AI, and 
fail to cite it in this section, it will be considered plagiarism and dealt 
with accordingly. So be safe CITE!

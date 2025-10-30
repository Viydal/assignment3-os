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
> Note: the number of threads is `2^cutoff` in this case.

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

**Discuss the issues you encountered during development and testing**

_Development_:

- When the group initially began to construct a solution for this project, there was some confusion in relation to the usage of the `args` struct and its components. It wasn't immediately clear as to what the left and right pointers represented, but with some further research and testing this confusion quickly subsided.
- While developing the `merge` function, the group found that some iterators did not appropriately take into account their position relative to the end of the array. This caused several out-of-bounds errors that were quickly addressed.

_Testing_:

- The testing process initially lacked automation, requiring multiple manual executions for performance and correctness checks. To address this, a testing script was developed to streamline the process by automatically executing numerous variations of the main program, collating timing data, generating visualisations, and ensuring proper functionality in the most extreme cases.

**What problems did you have?**

- The group did not face any major issues throughout the course of this project, with the only minor issue being that of availability. Attempting to schedule a time for the group to communicate ideas and clarify expectations was the only real difficulty.

**What did you have to research and learn on your own?**

- Although the topic of merge sort is familiar, the group felt it necessary to do some minor revision on the core concepts and logic.
- The group needed to do some research in relation to the usage of threads to ensure the `parallel merge sort` function ran as anticipated.

**What kinds of errors did you get? How did you fix them?**

- The group ran into one minor issue in the development of the codebase, with that being in how some iterators did not appropriately take into account their position relative to the end of the array. To identify and fix this issue, a visualisation of the programming logic was produced and execution flow was tracked.

**What parts of the project did you find challenging?**

- Producing a testing script to more efficiently orchestrate testing was the most challenging aspect of this project. This was difficult because the script was required to be produced in such a way that it could execute many different variations of the main executable, collating the results and producing the relevant visualistion material.

**Is there anything that finally "clicked" for you in the process of working on this project?**

- Everything in this project functioned exactly as the group expected, there were no **eureka** moments unfortunately. One group member did express their satisfaction at the realisation a testing script could be produced to automate testing, this was the closest the group came to having a **eureka** moment.

**How well did the development and testing process go for you?**

- The developmental process was extremely efficient, with the entire programming portion of the project requiring the better part of an hour. The testing process was similarly expeditious, with testing requiring approximately two hours of dedicated efforts.

## Sources Used

If you used any sources outside of the textbook, you should list them here. 
If you looked something up on stackoverflow.com or you use help from AI, and 
fail to cite it in this section, it will be considered plagiarism and dealt 
with accordingly. So be safe CITE!

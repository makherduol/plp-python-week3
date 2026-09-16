# Week 3 Assignment: Conditions and Loops

## Description
This repository contains solutions for the Week 3 assignment covering Python control flow, loops, and debugging.

## Files
* `grade_reporter.py`: Loops through student scores, computes letter grades using `if/elif/else`, tracks pass/fail metrics, and calculates the rounded average score.
* `bug_hunt.py`: Fixes three syntax, type, and logical bugs in a `while` loop program that sums numbers from 1 to 5.

## Bug Reflection
The hardest bug to find in Part B was the logical off-by-one condition (`count < 5`). Because Python executed the program without raising any error messages, the issue wasn't immediately flagged by the interpreter. I knew something was wrong because the output printed `10` instead of the expected correct total of `15`, indicating that the loop was terminating before processing the number `5`.

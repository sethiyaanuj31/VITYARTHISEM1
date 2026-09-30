# Project Statement: Personal Expense Tracker

**Student:** Anuj Sethiya
**Registration No.:** 26MIM10240
**Semester:** 1

## Problem Statement

Many students and individuals do not keep a record of their daily spending. Paper notes get lost, and spreadsheets or mobile apps feel too heavy for quick entries. As a result, people cannot easily answer simple questions such as:

- How much have I spent in total?
- How much have I spent on a particular category, such as food or travel?
- What was my biggest and smallest expense?
- How much did I spend in each month?

There is a need for a small, fast and easy-to-use tool that records each expense in a few seconds and answers these questions instantly, without any setup beyond Python itself.

## Scope of the Project

### In Scope

- Adding an expense with its date, category, amount and a short summary
- Viewing all recorded expenses
- Calculating the total expense
- Searching and totalling expenses by category (case-insensitive)
- Finding the highest and the lowest expense
- Generating a month-wise summary (MM-YYYY)
- A menu-driven command-line interface that repeats until the user exits

### Out of Scope (current version)

- Permanent storage: expenses are kept in memory and are lost when the program exits
- Editing or deleting expenses
- Validation of date and amount input
- Graphical or web interface
- Multiple users, login or budgeting alerts

## Target Users

- **Students** who manage a monthly allowance and want to see where their money goes
- **Individuals** who want a quick, simple record of daily expenses
- **Python beginners** looking for a practical example of lists, dictionaries, loops and functions

## High-Level Features

| No. | Feature | Description |
|-----|---------|-------------|
| 1 | Add Expense | Record date (DD-MM-YYYY), category, amount and summary |
| 2 | View Expenses | Display every expense with a serial number |
| 3 | Total Expense | Show the sum of all expenses |
| 4 | Search by Category | Show the total spent in a given category |
| 5 | Highest Expense | Find and display the largest single expense |
| 6 | Lowest Expense | Find and display the smallest single expense |
| 7 | Monthly Summary | Show month-wise spending totals |
| 8 | Exit | Close the application |

## Technology

- Python 3.6 or higher (core language only, no external libraries)
- Git and GitHub for version control

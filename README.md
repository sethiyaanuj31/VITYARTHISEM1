# 💰 Personal Expense Tracker

A simple, beginner-friendly command-line application written in Python to record and analyse your daily expenses. It uses only core Python, with no external libraries needed.

## Features

- **Add Expense**: record the date, category, amount, and a short summary
- **View Expenses**: list every expense entered in the current session
- **Total Expense**: see the sum of all expenses
- **Search by Category**: get the total spent in a given category (case-insensitive)
- **Highest Expense**: find your single largest expense
- **Lowest Expense**: find your single smallest expense
- **Monthly Summary**: view month-wise spending totals (`MM-YYYY`)

## Requirements

- Python 3.6 or higher

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/personal-expense-tracker.git
   cd personal-expense-tracker
   ```

2. **Run the program**

   ```bash
   python expense_tracker.py
   ```

   > Replace `expense_tracker.py` with the actual name of your file.

## Usage

When you run the program, you will see this menu:

```
Personal Expense Tracker
1. Add Expense
2. View Expenses
3. View Total Expense
4. Search by Category
5. Find Highest Expense
6. Find Lowest Expense
7. Monthly Summary
8. Exit
Enter your choice:
```

Type the number of the option you want and press Enter.

### Example Session

```
Enter your choice: 1
Add Expense
Enter date (DD-MM-YYYY): 15-09-2026
Enter category: Food
Enter amount: 250
Enter summary: Lunch with friends
Expense added successfully.

Enter your choice: 3
Total Expense: Rs. 250.0

Enter your choice: 7
Month-wise totals:
09-2026 : Rs. 250.0
```

## Input Format

| Field    | Format / Notes                                   |
|----------|--------------------------------------------------|
| Date     | `DD-MM-YYYY` (required for the monthly summary)  |
| Category | Any text, e.g. `Food`, `Travel`, `Bills`         |
| Amount   | A number, e.g. `250` or `99.50`                  |
| Summary  | A short description of the expense               |

## How It Works

Each expense is stored as a Python dictionary inside a list:

```python
{
    "date": "15-09-2026",
    "category": "Food",
    "amount": 250.0,
    "summary": "Lunch with friends"
}
```

The program loops over this list to calculate totals, find the highest and lowest values, and group spending by month.

## Limitations

- Expenses are stored **in memory only**, so data is lost when the program exits.
- No input validation yet: entering a non-numeric amount will crash the program, and the date format is not checked.

## Future Improvements

- [ ] Save and load expenses from a CSV or JSON file
- [ ] Validate date and amount input
- [ ] Edit and delete expenses
- [ ] Filter expenses by date range
- [ ] Export reports

## Contributing

Suggestions and improvements are welcome! Feel free to fork the repository and open a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Anuj**

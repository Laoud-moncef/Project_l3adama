# Project l3adama: Betting Tracker & Dashboard

## Description
A local-to-cloud automated tracking system for sports betting. This project allows for rapid local data entry via Linux terminal commands, processes the financial data using Python, and automatically generates an interactive, searchable HTML dashboard hosted on GitHub Pages.

## Data Structure
Data is stored locally in plain text CSV files to ensure fast appending and easy manual correction if necessary.

**1. bets.csv**
Tracks individual bet slips.
* Columns: `Date, Code, Outcome, Payout, Teams, Input`
* Outcomes: Pending, Won, Lost, Refund

**2. bank.csv**
Tracks the overall betting fund pool.
* Columns: `Date, Amount, Type, Note`
* Types: Injection, Cashout

## Project Files
* `bets.csv` / `bank.csv`: Raw data storage.
* `dashboard.py`: The backend Python script (Pandas/Jinja2) that calculates totals and structures the data.
* `template.html`: The frontend structural skeleton.
* `index.html`: The final generated webpage.
* `setup.sh`: The Bash script containing the custom terminal commands (sourced to `.bashrc`).

## Terminal Commands
These commands are restricted to execute only within the project directory:
* `log_bet`: Appends a new slip to `bets.csv`.
* `log_bank`: Appends a funding injection to `bank.csv`.
* `log_cashout`: Appends a withdrawal to `bank.csv`.
* `update_bet`: Uses stream editing to update a slip's outcome and payout.
* `publish_logs`: Manually triggers the Python build and Git push (also scheduled via cron at midnight).

## HTML Dashboard Design
The dashboard is a static HTML file upgraded with the DataTables JavaScript library. 
* **Hierarchy:** Grouped by Date (Main Row: Daily totals/Input/Slips) -> Expandable child rows (Individual bet slip details).
* **Features:** Searchable text, sortable columns, and specific columns (like Bank Balance and Input) maskable via CSS classes.

## Development Roadmap
1. **Backend (Python):** Write `dashboard.py` to parse CSVs, calculate bank balance/daily totals, and prepare the data structures.
2. **Frontend (HTML/JS):** Build `template.html` with DataTables integration and CSS masking.
3. **Deployment (Git Bridge):** Set up the local-to-remote Git pipeline and GitHub Pages hosting.
4. **Data Entry (Bash):** Code the terminal commands to automate logging and updating the CSV files.
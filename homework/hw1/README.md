# HW1 - Client Message Visualization Program

**Course:** Tech.UB.27.002 Spring 2026  
**Professor:** Guthrie Collin

## Overview

This program helps visualize client messaging data by creating horizontal histograms. It allows users to input client names and their daily message counts, then displays two visualizations:

1. Total messages sent per client
2. Total messages sent per day of the week

## Requirements

- Python 3.x

## Usage

Run the program from the command line:

```bash
python hw1.py
```

### Running the Program

When prompted, enter any key (except 't') to run the main program:

1. Enter the total number of clients (minimum 5)
2. For each client, enter:
   - Client name
   - 7 space-separated integers representing messages for each day (Sunday through Saturday)
3. View the generated histograms

### Running Unit Tests

When prompted, enter `t` to run all unit tests:

```
Enter 't' if you want to run the tests: t
OK: Total 12 tests passed
```

## Sample Output

```
-------------------------
Number of Messages per Client
-------------------------
Alice   :****************************
Bob     :*********
Charlie :*******

-------------------------
Number of Messages per Day
-------------------------
Sunday    :**
Monday    :****
Tuesday   :******
Wednesday :********
Thursday  :**********
Friday    :************
Saturday  :**************
```

## Program Structure

| Function | Description |
|----------|-------------|
| `read_input()` | Collects and validates user input for client names and daily message counts |
| `aggregate_by_client(data)` | Sums total messages per client |
| `aggregate_by_day(data)` | Sums total messages per day of the week |
| `draw_histogram(data)` | Generates a horizontal histogram string from aggregated data |

## Unit Tests

Each function includes three test cases following the common/edge/special pattern:

| Function | Common | Edge | Special |
|----------|--------|------|---------|
| `read_input` | 5 clients, normal values | All zeros for a client | Large message counts |
| `aggregate_by_client` | Multiple clients | Single client | Empty dictionary |
| `aggregate_by_day` | Multiple clients | Zero messages on some days | Empty dictionary |
| `draw_histogram` | Multiple items | Zero value | Empty dictionary |
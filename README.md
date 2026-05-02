# Tech-UB 27: Programming & Algorithms using Python

Coursework for **NYU Stern School of Business — Tech-UB 27.002**, Spring 2026.

**Author:** Yuri Chentsov
**Instructor:** Professor Guthrie Collin
**Schedule:** Mon & Wed, 9:30 – 10:45 AM (Jan 21 – Mar 9, 2026)

This repository collects the homework assignments for the course. Each assignment is a self-contained Python program built around a shared *Address Book* theme, progressing from procedural code through OOP, sorting/searching algorithms, and finally graph traversal.

## Topics covered

- Object-oriented programming (classes, dunder methods, encapsulation)
- Core data structures — lists, dicts, sets, stacks, queues, hashmaps, trees, graphs
- Algorithms — searching, sorting (merge sort), recursion, BFS, Big-O analysis
- Multi-file programs and Git version control
- Program design, unit testing, and debugging

## Repository structure

```
Programming-Algorithms-Python/
├── homework/
│   ├── hw1/   Client message visualization (procedural Python, histograms)
│   ├── hw2/   Address Book v1 — OOP, duplicate detection, merge
│   ├── hw3/   Address Book v2 — recursive merge sort and search
│   └── hw4/   Address Book v3 — graphs and BFS up to 3rd degree
├── .gitignore
└── README.md
```

Each homework folder contains its own README explaining what to run and how the code is organized.

## Homework summary

| HW  | Topic                              | Highlights                                                                 | Entry point                                  |
| --- | ---------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------- |
| hw1 | Client message visualization       | Input validation, aggregation, ASCII histograms, 12 unit tests             | `python message-tracker.py`                  |
| hw2 | Address Book (OOP basics)          | `Contact` and `AddressBook` classes, `__str__` / `__eq__`, merge contacts  | `python main.py` (or `python test.py`)       |
| hw3 | Address Book + sorting / searching | Recursive merge sort by name/email/phone (descending), exact-match search  | `python algo_demo.py`, `python algo_test.py` |
| hw4 | Address Book + social graph        | Adjacency list of edges, BFS to enumerate 1st / 2nd / 3rd-degree contacts  | `python social_demo.py`                      |

## Requirements

- Python 3.10 or newer (developed against 3.13)
- No third-party packages — everything uses the Python standard library (`unittest`, `collections`, `sys`)

A virtual environment isn't strictly required, but it's good practice:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
```

## Running an assignment

Each homework is independent. Open a terminal in the folder for the homework you want to run:

```bash
cd homework/hw3
python algo_demo.py        # demo
python algo_test.py        # unit tests
```

See the per-homework `README.md` (or `README.txt` for hw2) for details on inputs, expected output, and which file to run.

## Git workflow

Most commits in this repo were made from the command line. The `.gitignore` excludes Python bytecode, virtual environments, IDE settings, and OS metadata, so day-to-day development doesn't pollute the index.

## Academic integrity

All assignment logic was written and reviewed by the student. Where AI assistance was used (Claude Code), it is documented in each homework's README under the "LLM Usage" section, per the course's expectations.

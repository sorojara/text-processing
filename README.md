# Mine Dwarf

This project is a text processing library/CLI for text based applications development. It includes file management and NLP capabilities.

## Stack

This is a pure Python project which use libraries like nltk for NLP purposes.

## Infrastructure

### mine_dwarf.py
Implements the CLI functions to wrap the core.py public functions.

### core.py
This file defines all the exposable functions available for CLI. It is the main consumer of all the other modules. 

### file.py
File management functions (open as string, lines, sorted lines, etc).

### shape.py
Text shape functions (tokenize, wrapping, etc).

### calc.py
Any mathematical related functions.

### nlp.py
Any general Natural Language Processing methods.

### title.py
Different Title printing (Easter Egg).

### variables.py
General usage variables to avoid convoluted code files.

## Objectives

- [x] Create Basic Project
- [x] Add CLI functionality
- [x] Add File Management
- [ ] Add Unit Testing
- [ ] Add Deep Text Processing
- [ ] Add NLP
- [ ] Define CLI command list
- [ ] Create CLI commands
- [ ] Configure as Package
- [ ] Add CI/CD

## Brainstorm

- Sentiment analysis
- Filters
- SOLID refactor
    - Class usage
    - Inheritance
- Move to PyCharm
- Add Linting

## Installation

**TODO**

## Dev Environment

Install the requirements listed in requirements.txt **(WIP)**

## Usage

TODO

## Examples

TODO
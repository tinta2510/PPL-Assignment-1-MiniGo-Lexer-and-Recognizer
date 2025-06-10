# PPL-Assignment-1-MiniGo-Lexer-and-Recognizer
## Overview
This project is the first assignment for the Principles of Programming Languages (CO3005) course at HCMC University of Technology (VNU-HCM). The overall goal  of assignments in this course is to implement a simplified version of the Go programming language, named MiniGo.

The first assignment's objective is to implement a lexer and parser for MiniGo using ANTLR4. The lexer will tokenize the input source code, while the parser will build an abstract syntax tree (AST) from the tokens produced by the lexer.

The project is built using [ANTLR 4.9.2](https://www.antlr.org/), Python 3.12, and Java.

## Other Components of MiniGo compiler
Other components of the MiniGo project will be implemented in subsequent assignments, including:
- **Assignment 2**: Implementing an abstract syntax tree generator for MiniGo. https://github.com/tinta2510/PPL-Assignment-2-MiniGo-AST-Generation
- **Asssignment 3**: Implementing a static checker for MiniGo. https://github.com/tinta2510/PPL-Assignment-3-MiniGo-Static-Checker
- **Assignment 4**: Implementing a code generator for MiniGo. https://github.com/tinta2510/PPL-Assignment-4-Code-Generator

## Environment Setup
1. **Install Java (JDK)**  
   Ensure `java` is available in your terminal. If not, install it from:  
   https://www.oracle.com/java/technologies/downloads/

2. **Install Python 3.12.x**  
   Download: https://www.python.org/

3. **Install ANTLR 4.9.2**  
   - Download: https://www.antlr.org/download/antlr-4.9.2-complete.jar  
   - Set environment variable `ANTLR_JAR` to the path of this JAR.

4. **Install ANTLR runtime for Python**  
   ```bash
   pip install antlr4-python3-runtime==4.9.2

5. **Start and test the current Lexer and Parser**
Change current directory to ./src where there is file run.py
Run `python run.py gen` to generate the ANTLR4 lexer and parser files.
Run `python run.py test LexerSuite` to test the lexer.
Run `python run.py test ParserSuite` to test the parser.

## Project Files
- `MiniGo.g4`: ANTLR grammar file defining MiniGo tokens and grammar rules.
- `LexerSuite.py`: Contains 100 lexer test cases to validate token definitions.
- `ParserSuite.py`: Contains 100 parser test cases to validate grammar recognition.

## Features
- Full support for MiniGo’s lexical tokens: identifiers, literals, operators, keywords, comments, etc.
- Grammar rules for declarations, expressions, functions, structs, interfaces, loops, conditionals, etc.
- Custom exceptions:
  - `ErrorToken`: Raised for unrecognized tokens.
  - `UnclosedString`: Raised for unterminated string literals.
  - `IllegalEscapeInString`: Raised for illegal escape sequences in string literals.
  
*Note:* Find more details in the `docs/MiniGo Spec 1.0.2.pdf` and `docs/MiniGo Spec 1.0.2.md` files.
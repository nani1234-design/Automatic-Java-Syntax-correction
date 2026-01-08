Java Syntax Automatic Correction Tool

This project implements an automatic Java syntax correction system using fundamental compiler design concepts such as lexical analysis and parsing. The tool reads Java source code, analyzes it in multiple stages, detects common syntax issues, and regenerates corrected Java code.

The primary goal of this project is to demonstrate how compiler construction techniques can be applied to real-world programming tools. Rather than relying on a full Java compiler, the system focuses on identifying and correcting frequently occurring syntax errors such as missing semicolons and unmatched braces.

---

## Project Overview

The system processes Java source code through a structured pipeline. It first performs lexical analysis to break the source code into tokens. These tokens are then examined using parsing and rule-based validation techniques to identify syntax inconsistencies. Once errors are detected, an automatic correction module applies predefined correction rules and regenerates syntactically valid Java code.

This approach reflects the core stages of a compiler while keeping the implementation lightweight and easy to understand for academic and learning purposes.

---

## Workflow

1. The input Java source code is read from a file.
2. Lexical analysis is performed to tokenize the source code into meaningful elements such as keywords, identifiers, operators, and separators.
3. The token stream is passed to a parser that applies syntax validation rules.
4. Common syntax errors are identified, including missing semicolons and unmatched braces.
5. A correction module automatically fixes the detected errors using rule-based logic.
6. The corrected Java source code is regenerated and written to a new output file.

This step-by-step pipeline ensures clarity and separation of responsibilities between different phases of the system.

---

## Technology and Design

The project is implemented in Python to focus on algorithmic clarity rather than language-specific complexity. Python enables rapid prototyping of lexical and parsing logic while accurately representing compiler design principles.

The system is modular, with separate components for tokenization, parsing, correction, and orchestration. This design allows future extensions such as grammar-based parsing, improved error recovery, and support for additional Java syntax rules.

---

## Project Structure

java-syntax-auto-corrector/
│
├── src/
│ ├── lexer.py # Lexical analysis and tokenization
│ ├── parser.py # Syntax validation and parsing rules
│ ├── corrector.py # Automatic syntax correction logic
│ └── main.py # Entry point and pipeline execution
│
├── samples/
│ ├── input.java # Java source code with syntax errors
│ └── corrected.java # Auto-generated corrected output
│
├── README.md

Rohith D

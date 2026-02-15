# Copilot Instructions for This Codebase

## Overview
This workspace is a collection of Python scripts and exercises for a data science curriculum. It is organized by module and topic, with each folder containing example programs, model answers, and student tasks. The codebase is educational and modular, with each script typically self-contained.

## Key Patterns and Conventions
- **File Naming:**
  - Scripts are named for their function or topic (e.g., `holiday.py`, `calc_app.py`, `inventory.py`).
  - Model answers are often suffixed with `model answer.py` or `Model_answer.py`.
  - Data files use `.txt` and are named to match their related script (e.g., `inventory.txt` for `inventory.py`).
- **Data Handling:**
  - Scripts like `inventory.py` and `calc_app.py` read from and write to `.txt` files in the same directory.
  - Data files are simple CSV or line-based text, with headers where appropriate.
- **OOP Examples:**
  - Object-oriented scripts (e.g., `inventory.py`, `album_management.py`) define classes at the top, followed by functions for data manipulation and user interaction.
- **User Input:**
  - Most scripts are interactive, using `input()` for user data.
  - Error handling is basic, with `try/except` blocks for input validation.

## Developer Workflows
- **Running Scripts:**
  - Run scripts directly with Python 3: `python3 scriptname.py`.
  - No build system or dependency management is required; all scripts use the Python standard library.
- **Testing:**
  - There is no formal test suite. To test, run scripts and verify output manually.
- **Debugging:**
  - Debug by running scripts and reading printed output or error messages.

## Project Structure
- **Modules:**
  - Folders are named by module/topic (e.g., `M03T07 - OOP - Synthesis`).
  - Each module contains code files and sometimes subfolders for further organization.
- **Key Files:**
  - `inventory.py`/`inventory.txt`: OOP inventory management example.
  - `holiday.py`: Holiday cost calculator with function decomposition.
  - `calc_app.py`/`equations.txt`: Simple calculator with persistent history.
  - `album_management.py`: OOP and list manipulation example.

## AI Agent Guidance
- **When adding new scripts:**
  - Follow the naming and data handling conventions above.
  - Place related `.txt` data files in the same directory as the script.
- **When updating OOP examples:**
  - Keep class definitions at the top, followed by functions, then script logic.
- **When creating exercises:**
  - Use clear, descriptive filenames and comments to indicate the learning objective.

## Examples
- To add a new inventory item, update both `inventory.py` and `inventory.txt`.
- To add a new module, create a folder with the pattern `MxxTyy - Topic/` and place scripts inside.

---
For questions or unclear conventions, review similar scripts in the relevant module or ask for clarification.

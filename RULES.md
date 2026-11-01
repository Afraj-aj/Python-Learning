# Project Rules: Python Notes & Screenshots

## Rule 1: Read This File First
**Whenever you are asked to do a task, you MUST read this file first before doing any work.**
This file defines the conventions for the entire project. Follow it exactly.

---

## Rule 2: Root Directory
The project root is `C:\Users\Afraj\Python Learning`.

Files allowed at root:
- `Tutorial01.py` - Main Python script
- `.gitignore` - Ignores large files (images, videos, etc.) from git
- `README.md` - Project overview (optional)
- This rules file (`RULES.md`)

No other files or folders at root except `Python Notes & Screenshots/`.

**Example of correct root structure:**
```
C:\Users\Afraj\Python Learning\
├── Tutorial01.py
├── .gitignore
├── RULES.md
└── Python Notes & Screenshots\
```

---

## Rule 3: Main Notes Folder
**Location:** `Python Notes & Screenshots/`

This is the single parent folder for all notes and screenshots.

Subfolders are created for each major topic. Each topic gets its own folder.

**Example:**
```
Python Notes & Screenshots/
├── Variables/
├── Numbers/
├── Strings/
├── Type Conversion/
├── Conditionals/
└── Loops/
```

---

## Rule 4: Topic Folders
Each major topic gets a dedicated folder under `Python Notes & Screenshots/`.

Existing topic folders:
- `Variables/`
- `Numbers/`
- `Strings/`
- `Type Conversion/`
- `Conditionals/`
- `Loops/`

Sub-topics get nested folders under their parent topic:
- `Strings/String Methods/`
- `Strings/Escape Sequences/`
- `Strings/Formatted Strings/`

**Example of nested structure:**
```
Python Notes & Screenshots/
└── Strings/
    ├── Strings.txt
    ├── String Methods/
    │   └── String Methods.txt
    ├── Escape Sequences/
    │   └── Escape Sequences.txt
    └── Formatted Strings/
        └── Formatted Strings.txt
```

---

## Rule 5: Note Files
Every folder MUST contain a `.txt` note file.

**Naming convention:**
- The file name MUST match the folder name exactly.
- File extension is `.txt`.
- Example: `String Methods/String Methods.txt`

**Content format:**
- Title on line 1, followed by `=` underline (same length as title)
- Blank line
- Section headers (topic name), followed by `-------` underline
- Blank line
- Content with 4-space indentation for method/function descriptions
- Method signatures aligned with 8+ spaces of padding for readability

**Example of a well-formatted note file:**
```
String Methods
=============

Case Manipulation Methods
-------------------------
    upper():    Converts a string to all uppercase characters.
    lower():    Converts a string to all lowercase characters.
    title():    Capitalizes the first letter of every word in the string.

Whitespace Management
---------------------
    strip():    Trims whitespace from both the beginning and end of a string.
    lstrip():   Removes whitespace specifically from the left (beginning) side.
    rstrip():   Removes whitespace specifically from the right (end) side.
```

---

## Rule 6: Screenshots
Screenshots are stored in their corresponding topic folder alongside the note file.

**Naming:** Use the default screenshot naming (e.g., `Screenshot 2026-10-25 205631.png`).

**Git:** All image files are ignored via `.gitignore` and will not be committed.

**Example of a folder with both note and screenshot:**
```
String Methods/
├── String Methods.txt
└── Screenshot 2026-10-25 205631.png
```

---

## Rule 7: When Adding New Content
When you receive notes for a new topic:

1. Read this file first.
2. Check if a folder exists for the topic.
3. If the folder does not exist, create it.
4. Create the `.txt` note file with the name matching the folder.
5. Format the content following Rule 5.
6. Place any associated screenshots in the same folder.

**Example workflow:**
- User provides notes on "Dictionaries"
- Step 1: Read RULES.md
- Step 2: Check `Python Notes & Screenshots/Dictionaries/` - does not exist
- Step 3: Create `Python Notes & Screenshots/Dictionaries/`
- Step 4: Create `Python Notes & Screenshots/Dictionaries/Dictionaries.txt`
- Step 5: Format content per Rule 5
- Step 6: Place any screenshots in the same folder

---

## Rule 8: File Organization Summary
```
Python Notes & Screenshots/
├── Variables/
│   └── Variables.txt
├── Numbers/
│   └── Numbers.txt
├── Type Conversion/
│   └── Type Conversion.txt
├── Conditionals/
│   ├── Conditionals.txt
│   ├── Comparison Operators/
│   │   └── Comparison Operators.txt
│   ├── Conditional Statements/
│   │   └── Conditional Statements.txt
│   ├── Ternary Operator/
│   │   └── Ternary Operator.txt
│   ├── Logical Operators/
│   │   └── Logical Operators.txt
│   ├── Short-circuit Evaluations/
│   │   └── Short-circuit Evaluations.txt
│   └── Chaining Comparison Operators/
│       └── Chaining Comparison Operators.txt
├── Loops/
│   ├── Loops.txt
│   ├── For Loops/
│   │   └── For Loops.txt
│   ├── For..Else/
│   │   └── For..Else.txt
│   ├── Nested Loops/
│   │   └── Nested Loops.txt
│   ├── Iterables/
│   │   └── Iterables.txt
│   ├── While Loops/
│   │   └── While Loops.txt
│   └── Infinite Loops/
│       └── Infinite Loops.txt
└── Strings/
    ├── Strings.txt
    ├── String Methods/
    │   └── String Methods.txt
    ├── Escape Sequences/
    │   └── Escape Sequences.txt
    └── Formatted Strings/
        └── Formatted Strings.txt
```

---

## Rule 9: Examples in Notes
Every note file should include practical code examples to help understand the concept.

**Why examples?**
- They bridge theory and practice
- They show real-world usage
- They make notes more helpful when reviewing

**Example of a note with examples:**
```
Variables
=========

Purpose
-------
Used to store data in the computer's memory. A variable acts as a label
referencing a specific memory location.

Example:
    age = 25
    name = "Alice"
    height = 5.9
    is_student = True
```

**When writing examples:**
- Use 4-space indentation to match the note format
- Keep examples simple and focused
- Show the concept in action, not just the definition
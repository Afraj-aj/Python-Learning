# Project Rules: Python Notes & Screenshots

## Rule 1: Read This File First
**Whenever you are asked to do a task, you MUST read this file first before doing any work.**
This file defines the conventions for the entire project. Follow it exactly.

---

## Rule 2: Root Directory
The project root is `C:\Users\Afraj\Python Learning`.

Files and folders currently at root:
- `Tutorial01.py` - Python practice script
- `Star Tutorial.py` - Star-pattern practice script
- `.gitignore` - Ignores large files (images, videos, etc.) from git
- `README.md` - Optional project overview
- `RULES.md` - Repository conventions
- `.kombai/` - Hidden local workspace settings (may be empty)
- `Python Notes & Screenshots/` - Learning notes and screenshots

This is a reference inventory, not a substitute for checking the actual
workspace. Update it when intentional root-level files or folders are added,
removed, or renamed.

**Example of correct root structure:**
```
C:\Users\Afraj\Python Learning\
├── Tutorial01.py
├── Star Tutorial.py
├── .gitignore
├── RULES.md
├── .kombai\
└── Python Notes & Screenshots\
```
An optional `README.md` may also be placed at the root.

---

## Rule 3: Main Notes Folder
**Location:** `Python Notes & Screenshots/`

This is the single parent folder for all notes and screenshots.

Subfolders are created for each major topic. Each topic gets its own folder.

**Example:**
```
Python Notes & Screenshots/
├── Variables/
├── Receiving Input/
├── Numbers/
├── Strings/
├── Type Conversion/
├── Conditionals/
├── Loops/
├── Lists/
├── Tuples/
└── Functions/
```

---

## Rule 4: Topic Folders
Each major topic gets a dedicated folder under `Python Notes & Screenshots/`.

Current topic folders (check the workspace for the authoritative structure):
- `Variables/`
- `Receiving Input/`
- `Numbers/`
- `Strings/`
- `Type Conversion/`
- `Conditionals/`
- `Loops/`
- `Lists/`
- `Dictionaries/`
- `Tuples/`
- `Functions/`

Sub-topics get nested folders under their parent topic:
- `Numbers/Operator Precedence/`
- `Strings/String Methods/`
- `Strings/Escape Sequences/`
- `Strings/Formatted Strings/`
- `Conditionals/Exercise/`
- `Lists/List Methods/`
- `Loops/The range() Function/`

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
Every topic folder under `Python Notes & Screenshots/` must contain a `.txt`
note file. Hidden local workspace folders are not topic folders.

**Naming convention:**
- The file name MUST match the folder name exactly.
- File extension is `.txt`.
- Example: `String Methods/String Methods.txt`

**Content format:**
- Title on line 1, followed by an `=` underline matching the title length
- Blank line
- Section headers (topic name), followed by `-------` underline
- Blank line
- Content with 4-space indentation for method/function descriptions
- Method signatures aligned with 8+ spaces of padding for readability

**Example of a well-formatted note file:**
```
String Methods
==============

Case Manipulation Methods
-------------------------
    upper():    Converts a string to all uppercase characters.
    lower():    Converts a string to all lowercase characters.
    title():    Returns a title-cased string; apostrophe handling may be
                unexpected for names.

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

**Git:** Untracked images with the listed extensions are ignored via
`.gitignore`. This does not remove files that Git already tracks.

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
The tree below is a reference snapshot. Check the actual workspace before
creating, moving, or removing folders, and update this summary when the
organization intentionally changes.

```
Python Notes & Screenshots/
├── Variables/
│   └── Variables.txt
├── Receiving Input/
│   └── Receiving Input.txt
├── Numbers/
│   ├── Numbers.txt
│   └── Operator Precedence/
│       └── Operator Precedence.txt
├── Type Conversion/
│   └── Type Conversion.txt
├── Conditionals/
│   ├── Conditionals.txt
│   ├── Comparison Operators/
│   │   └── Comparison Operators.txt
│   ├── Conditional Statements/
│   │   └── Conditional Statements.txt
│   ├── Exercise/
│   │   └── Exercise.txt
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
│   ├── Infinite Loops/
│   │   └── Infinite Loops.txt
│   └── The range() Function/
│       └── The range() Function.txt
├── Lists/
│   ├── Lists.txt
│   └── List Methods/
│       └── List Methods.txt
├── Dictionaries/
│   └── Dictionaries.txt
├── Tuples/
│   └── Tuples.txt
├── Functions/
│   ├── Functions.txt
│   ├── Defining Functions/
│   │   └── Defining Functions.txt
│   ├── Arguments/
│   │   └── Arguments.txt
│   ├── Types of Functions/
│   │   └── Types of Functions.txt
│   ├── Keyword Arguments/
│   │   └── Keyword Arguments.txt
│   ├── Default Arguments/
│   │   └── Default Arguments.txt
│   └── xargs/
│       └── xargs.txt
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
Used to give a value a name. In Python, a variable name refers to an object;
assignment binds a name to that object.

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

---

## Rule 10: Complete Concept Coverage
For every function, method, operator, or language feature explained in a note:

- When a function or method is introduced or mentioned for the first time,
  define it in beginner-friendly language: what it does, why or when it is
  useful, and a simple example of how to use it.
- Define new technical terms and concepts before relying on them. For example,
  explain that a dictionary is a collection that stores values under keys,
  then show a small example and when that structure is useful.
- Explain signature notation that may be unfamiliar (such as `/` for
  positional-only parameters) in plain language. Make clear which parts are
  documentation notation and which parts are actually typed in a call.
- Cover its documented forms, parameters/options, defaults, and return value or result.
- Explain relevant side effects, mutability, boundary behavior, and common errors.
- Include examples for each meaningfully different form or behavior, including
  optional arguments and important edge cases.
- When a concept has too many possible input values to list individually,
  explain the general rule and demonstrate representative values and boundaries.
  State the scope of the note rather than implying that a few examples cover
  every possible input.
- Keep explanations appropriate to the note's learning level; this rule does
  not require reproducing the entire Python language or library reference.

For example, a complete beginner-level explanation of string slicing should
cover omitted start/stop values, positive and negative indexes and steps,
out-of-range bounds, the exclusive stop, and invalid steps such as zero.

---

## Rule 11: Accuracy and Example Verification
- Use accurate Python terminology and describe behavior based on the language
  or library documentation, not guesses.
- If behavior depends on a Python version or implementation, name the relevant
  version or implementation and avoid presenting it as universal behavior.
- Check runnable examples when practical. Confirm their output and any
  demonstrated exceptions; show expected output or errors when that helps
  learners understand the result.
- Do not present an example as tested unless it has actually been run. If it
  cannot be run, keep it simple and review it carefully for correctness.
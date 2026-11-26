## Daily Learnings Over the Course of This Project

### Days 1–2: Strings, Lists & Input Validation

- **Slicing:** Negative step slicing (`s[::-1]`) reverses strings/lists by flipping default start/stop bounds.
- **Cleaning & Splitting:** Used `.strip()` to clean whitespace and `.split(maxsplit=1)` to split text into at most two parts (e.g., separating `/command` from the prompt).
- **Input Validation:** Combined `while` loops with `any(char.isalnum() ...)` to reject blank or special-character-only inputs.

### Day 3: Lists & Dictionaries (Chat Memory)

- Practiced dictionary lookups (`.get()` with defaults to avoid `KeyError`), tuple unpacking with `.items()`, and navigating nested list/dict API structures (`response["choices"][0]["message"]["content"]`).

### Day 4: Functions & Error Handling

- Revised function argument types:
  1. **Default:** `def prntN(name, age=22):` — uses `22` if `age` is omitted.
  2. **Positional:** `prntN("sabhya", 22)` — argument order matters.
  3. **Keyword:** `prntN(age=22, name="sabhya")` — matched by parameter name.
  4. **Variable-length:** `*args` (collects extra positional args as a tuple) and `**kwargs` (collects extra keyword args as a dict).
- **Fault Tolerance:** Used `try / except` blocks to safely catch missing keys or invalid user inputs without crashing.

### Day 5: Workspace Hygiene & JSON Persistence

- **Why `.env` and `.venv` are in `.gitignore` (kept out of GitHub):**
  - `.env` keeps secret API keys private so they aren't leaked publicly or abused for unauthorized API charges.
  - `.venv` avoids uploading thousands of OS-specific library files; dependencies are tracked cleanly via `requirements.txt` instead.
- **JSON Module:**
  - `json.load(f)` → Reads a `.json` file into a Python dict/list.
  - `json.dump(data, f)` → Writes a Python dict/list into a `.json` file.
  - `json.loads(str)` → Parses a raw JSON string into a Python dict/list.
  - `json.dumps(data)` → Converts a Python dict/list into a JSON-formatted string.

# 🧠 Recursive Memory Architecture (RMA) - Complete Simulator

**A pure Python implementation of hierarchical recursive memory structures**

> Memory as a recursive tree, not a flat array

---

## 📚 Documentation

| File | Description |
|------|-------------|
| **[QUICKSTART.md](QUICKSTART.md)** | ⚡ **START HERE** - Get running in 30 seconds |
| **[RMA_README.md](RMA_README.md)** | Complete documentation, API reference, examples |

---

## 🛠️ Core Files

### 1. `rma_simulator.py` (8.2 KB)
**The main implementation**

Classes:
- `MemoryBlock` - Node in the recursive tree
- `RecursiveMemory` - High-level interface

Features:
- Set/get values via paths
- Search by value or key
- Tree traversal (up/down)
- Statistics & export

**Usage:**
```python
from rma_simulator import RecursiveMemory
memory = RecursiveMemory()
memory.set("path.to.value", "data")
```

**Run demo:**
```bash
python rma_simulator.py
```

---

### 2. `rma_advanced_examples.py` (8.5 KB)
**Real-world usage examples**

Examples included:
- 📚 Knowledge graphs
- 💬 Conversation memory
- 📁 Filesystem simulation
- ⚙️ State machines
- 🧠 Semantic/episodic memory
- 💾 JSON export/import
- ⬆️ Parent traversal
- ⚡ Performance benchmarks

**Run all examples:**
```bash
python rma_advanced_examples.py
```

---

### 3. `rma_repl.py` (6.2 KB)
**Interactive command-line interface**

Commands:
- `set <path> <value>` - Store data
- `get <path>` - Retrieve data
- `search <value>` - Find by value
- `search-key <key>` - Find by key
- `display` - Show tree
- `stats` - Show statistics
- `export [file]` - Export to JSON
- `help` - Show help

**Start REPL:**
```bash
python rma_repl.py
```

**Example session:**
```
RMA> set thoughts.AI.RML recursive memory rocks
RMA> get thoughts.AI.RML
RMA> display
RMA> stats
```

---

### 4. `rma_visualize.py` (6.8 KB)
**Beautiful ASCII tree visualizations**

Visualization types:
- 🌳 Traditional tree (vertical)
- 🌲 Horizontal layout
- 📋 Compact leaf view
- 📊 Depth histogram

**Run visualizations:**
```bash
python rma_visualize.py
```

---

### 5. `test_rma.py` (7.8 KB)
**Comprehensive test suite**

18 tests covering:
- Basic operations (set/get/delete)
- Path syntax (list/dot notation)
- Search functionality
- Tree operations (depth/count)
- Parent references
- Export/import
- Edge cases
- Unicode support

**Run tests:**
```bash
python test_rma.py
```

**Expected output:**
```
✅ All tests passed!
📊 RESULTS: 18 passed, 0 failed
```

---

## 🎯 Quick Commands Reference

| What you want to do | Command |
|---------------------|---------|
| **Get started** | `python rma_simulator.py` |
| **See advanced examples** | `python rma_advanced_examples.py` |
| **Play interactively** | `python rma_repl.py` |
| **See visualizations** | `python rma_visualize.py` |
| **Run tests** | `python test_rma.py` |
| **Read quick guide** | Open `QUICKSTART.md` |
| **Read full docs** | Open `RMA_README.md` |

---

## 💡 Core Concepts

### What is Recursive Memory?

**Traditional memory:**
```python
data[0] = "value"  # Flat, index-based
```

**Recursive memory:**
```python
memory["thoughts"]["AI"]["RML"] = "value"  # Hierarchical, semantic
```

### Key Features

| Feature | Description |
|---------|-------------|
| 🌳 **Hierarchical** | Tree structure, not flat array |
| 🔍 **Searchable** | Find by value or key name |
| 📍 **Path-based** | Use semantic paths: `a.b.c` |
| 🔄 **Bi-directional** | Traverse up (parent) or down (children) |
| 📊 **Introspective** | Query depth, count, structure |
| 💾 **Exportable** | Convert to/from JSON |
| 🚀 **Dynamic** | Grows on demand |

---

## 📖 Example Use Cases

### 1. AI Agent Memory
```python
memory.set("context.user.intent", "search")
memory.set("context.conversation.history", [...])
memory.set("context.current_task.status", "in_progress")
```

### 2. Configuration System
```python
memory.set("config.app.theme", "dark")
memory.set("config.features.export.enabled", True)
memory.set("config.database.host", "localhost")
```

### 3. Knowledge Graph
```python
memory.set("concepts.AI.definition", "artificial intelligence")
memory.set("concepts.AI.related", ["ML", "robotics"])
memory.set("relationships.AI.requires", "mathematics")
```

### 4. State Machine
```python
memory.set("states.idle.transitions.start", "active")
memory.set("states.active.transitions.pause", "paused")
memory.set("current.state", "idle")
```

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Python files** | 5 |
| **Documentation files** | 3 |
| **Total lines of code** | ~1,271 |
| **Total size** | ~45 KB |
| **Tests** | 18 (all passing ✅) |
| **Dependencies** | 0 (pure Python) |

---

## 🚀 Getting Started in 3 Steps

### Step 1: Run the basic demo (30 seconds)
```bash
python rma_simulator.py
```

### Step 2: Try the interactive REPL (2 minutes)
```bash
python rma_repl.py
```
Then type:
```
set example.hello world
get example.hello
display
```

### Step 3: Read the docs (5 minutes)
Open `QUICKSTART.md` or `RMA_README.md`

---

## 🎓 Learning Path

| Level | What to do | Time |
|-------|------------|------|
| **Beginner** | Run `rma_simulator.py`, read `QUICKSTART.md` | 5 min |
| **Intermediate** | Explore `rma_repl.py`, try examples | 15 min |
| **Advanced** | Study `rma_advanced_examples.py`, read code | 30 min |
| **Expert** | Extend the code, add features | ∞ |

---

## 🔧 API Quick Reference

### RecursiveMemory

```python
memory = RecursiveMemory()

# Store
memory.set(path, value)              # path = list or "dot.string"

# Retrieve
value = memory.get(path)             # Returns value or None

# Delete
success = memory.delete(path)        # Returns True/False

# Search
paths = memory.search(value)         # Find by value
paths = memory.search_key(key)       # Find by key name

# Display
memory.display(show_paths=False)     # Print tree

# Analyze
stats = memory.stats()               # Get statistics
data = memory.export()               # Export to dict
```

---

## 🌟 Why RMA?

| Reason | Explanation |
|--------|-------------|
| **Semantic** | Paths have meaning: `user.profile.name` |
| **Flexible** | Grows dynamically as needed |
| **Searchable** | Find data by content or structure |
| **Navigable** | Traverse relationships easily |
| **Introspective** | Query its own structure |
| **Simple** | Pure Python, zero dependencies |
| **Educational** | Learn recursion & tree algorithms |

---

## 📝 File Manifest

```
.
├── INDEX.md                      ← You are here
├── QUICKSTART.md                 ← Start here (quick guide)
├── RMA_README.md                 ← Full documentation
│
├── rma_simulator.py              ← Core implementation
├── rma_advanced_examples.py      ← Usage examples
├── rma_repl.py                   ← Interactive shell
├── rma_visualize.py              ← Tree visualizations
└── test_rma.py                   ← Test suite
```

---

## 🎯 Next Steps

1. **Quick start**: `python rma_simulator.py`
2. **Interactive**: `python rma_repl.py`
3. **Learn more**: Read `QUICKSTART.md`
4. **Deep dive**: Read `RMA_README.md`
5. **Extend it**: Add your own features!

---

## 💬 Philosophy

> "Traditional memory is a library with no organization system.
> Recursive memory is a library with a hierarchical catalog.
> Both store books, but only one lets you find them."

**Memory should be:**
- Structured (not flat)
- Semantic (not arbitrary)
- Navigable (not opaque)
- Introspective (not black-box)

**That's RMA.**

---

**Built with ❤️ in pure Python**

*No dependencies. No complexity. Just recursive elegance.* 🧠

---

## 🏁 TL;DR

```bash
# Run this:
python rma_simulator.py

# Then this:
python rma_repl.py

# Then read:
QUICKSTART.md
```

**You now have a complete recursive memory system in < 40KB of Python code.**

🚀 **Go build something amazing!**

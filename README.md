# 🧠 Recursive Memory Architecture (RMA)

> A pure Python implementation of hierarchical recursive memory structures — zero dependencies, just elegant code.

[![Tests](https://img.shields.io/badge/tests-18%20passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.6%2B-blue)]()
[![License](https://img.shields.io/badge/license-Public%20Domain-green)]()
[![Lines of Code](https://img.shields.io/badge/lines%20of%20code-~1271-blue)]()

## 🎯 What is RMA?

**Recursive Memory Architecture** is a memory model where:

- 🧱 **Memory blocks** contain values and spawn child blocks dynamically
- 🌳 **Hierarchical structure** - tree-based, not flat arrays
- 📍 **Path-based access** - semantic navigation via `thoughts.AI.RML`
- 🔄 **Bi-directional** - traverse up (parent) or down (children)
- 🔍 **Searchable** - query by value or key structure

Think: **Memory = recursive tree, not flat array**

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/renaissancebro/recursive-memory-architecture.git
cd recursive-memory-architecture

# Run the demo (30 seconds)
python rma_simulator.py

# Try the interactive REPL
python rma_repl.py

# Run tests
python test_rma.py
```

## 📚 Usage Example

```python
from rma_simulator import RecursiveMemory

# Create memory
memory = RecursiveMemory()

# Store values using paths
memory.set(["thoughts", "AI", "RML"], "recursive memory rocks")
memory.set("emotions.fear", "predictive error signal")

# Retrieve values
value = memory.get("thoughts.AI.RML")
print(value)  # "recursive memory rocks"

# Search
results = memory.search("recursive memory rocks")
print(results)  # [['thoughts', 'AI', 'RML']]

# Display the tree
memory.display()
```

**Output:**
```
🧠 Recursive Memory Structure:
==================================================
[root] = 'root'
  [thoughts] = None
    [AI] = None
      [RML] = 'recursive memory rocks'
  [emotions] = None
    [fear] = 'predictive error signal'
==================================================
```

## 🎮 Interactive REPL

```bash
$ python rma_repl.py

RMA> set thoughts.idea great concept
✓ Set thoughts.idea = 'great concept'

RMA> get thoughts.idea
📖 thoughts.idea = 'great concept'

RMA> display
🧠 Recursive Memory Structure:
==================================================
[root] = 'root'
  [thoughts] = None
    [idea] = 'great concept'
==================================================

RMA> stats
📊 Memory Statistics:
  Total nodes:     3
  Maximum depth:   2
  Direct children: 1
  Root has value:  True
```

## 📦 What's Included

| File | Description | Size |
|------|-------------|------|
| **`rma_simulator.py`** | Core implementation | 8.2 KB |
| **`rma_advanced_examples.py`** | Real-world examples & benchmarks | 8.5 KB |
| **`rma_repl.py`** | Interactive command-line interface | 6.2 KB |
| **`rma_visualize.py`** | ASCII tree visualizations | 6.8 KB |
| **`test_rma.py`** | Comprehensive test suite | 7.8 KB |
| **Documentation** | INDEX.md, QUICKSTART.md, RMA_README.md | ~20 KB |

**Total: ~1,271 lines of Python, ~45 KB, zero external dependencies**

## ✨ Features

- ✅ **Hierarchical memory** - Tree-based structure
- ✅ **Path-based access** - Dot notation or list syntax
- ✅ **Dynamic growth** - Nodes created on demand
- ✅ **Search & query** - Find by value or key
- ✅ **Bi-directional traversal** - Parent and child navigation
- ✅ **Tree visualization** - 4 different styles
- ✅ **Statistics** - Depth, count, structure analysis
- ✅ **JSON export** - Serialize to/from dict
- ✅ **Interactive REPL** - Explore live
- ✅ **Well-tested** - 18 tests, 100% passing
- ✅ **Zero dependencies** - Pure Python 3.6+

## 🚀 Examples

### Knowledge Graph
```python
memory.set("concepts.mathematics.algebra.definition", "study of symbols")
memory.set("concepts.physics.quantum.definition", "discrete energy")
definitions = memory.search_key("definition")
```

### Conversation Memory
```python
memory.set("conversation.session_001.user.name", "Alice")
memory.set("conversation.session_001.messages.msg_1.text", "Hello!")
```

### State Machine
```python
memory.set("states.idle.transitions.start", "processing")
memory.set("states.processing.transitions.complete", "done")
memory.set("current.state", "idle")
```

### Filesystem Simulation
```python
memory.set("filesystem.home.user.documents.notes.txt", "meeting notes")
memory.set("filesystem.home.user.code.main.py", "print('hello')")
```

## 📊 Benchmarks

Performance comparison (1000 operations):

| Operation | RMA | Flat Dict | Ratio |
|-----------|-----|-----------|-------|
| Write | ~1.3ms | ~0.2ms | 7x slower |
| Read | ~0.8ms | ~0.2ms | 5x slower |

**Trade-off:** RMA is slower but provides hierarchical structure, semantic paths, relationships, and dynamic growth.

## 🧪 Testing

```bash
$ python test_rma.py

============================================================
🧪 RECURSIVE MEMORY ARCHITECTURE TEST SUITE
============================================================

Testing basic set/get... ✓
Testing dot notation... ✓
Testing value overwrite... ✓
Testing delete... ✓
Testing search by value... ✓
Testing search by key... ✓
... (12 more tests)

============================================================
📊 RESULTS: 18 passed, 0 failed out of 18 tests
✅ All tests passed!
============================================================
```

## 📖 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[RMA_README.md](RMA_README.md)** - Complete documentation
- **[INDEX.md](INDEX.md)** - Project navigation and overview

## 🎓 Use Cases

- 🧠 **AI/ML memory systems** - Agent context and knowledge
- 📊 **Configuration management** - Nested settings
- 🗂️ **Knowledge graphs** - Conceptual relationships
- ⚙️ **State machines** - Workflow modeling
- 📁 **Hierarchical data** - File systems, organizations
- 💬 **Conversation context** - Dialogue history
- 🧬 **Semantic memory** - Facts and episodes

## 💡 Philosophy

> "Traditional memory is a library with no organization system.
> Recursive memory is a library with a hierarchical catalog.
> Both store books, but only one lets you find them."

**Memory should be:**
- **Structured** (not flat)
- **Semantic** (not arbitrary)
- **Navigable** (not opaque)
- **Introspective** (not black-box)

**That's RMA.**

## 🔧 API Reference

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

## 🤝 Contributing

This is a minimal, educational implementation. Ideas for extensions:

- 🗺️ Graph visualization (graphviz)
- 💾 Persistence (pickle/JSON files)
- 🔍 Query DSL (SQL-like syntax)
- 🧮 Memory compression
- ⚡ Indexing for faster search
- 🔄 Version control for memory
- 🌐 Distributed memory

## 📝 License

**Public Domain** - Use, modify, share freely.

## 🙏 Credits

Inspired by the concept of recursive memory logic and hierarchical knowledge representation.

---

**Built with ❤️ in pure Python — no dependencies, no complexity, just recursive elegance.**

🧠 *"Recursion is the universe thinking about itself."*

---

## 🏁 TL;DR

```bash
git clone https://github.com/renaissancebro/recursive-memory-architecture.git
cd recursive-memory-architecture
python rma_simulator.py
```

**You now have a complete recursive memory system in < 40KB of Python code.**

🚀 **Go build something amazing!**

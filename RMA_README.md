# 🧠 Recursive Memory Architecture (RMA) Simulator

A pure Python implementation of hierarchical recursive memory structures — no external dependencies, just clean, minimal code.

## 🎯 What is RMA?

Recursive Memory Architecture is a memory model where:

- **Memory blocks (nodes)** contain values
- Each block can **dynamically spawn child blocks**
- You can **traverse, grow, and query** the structure recursively
- Memory is accessed via **paths**, not flat addresses

Think: 🧱 **Memory = a recursive tree, not a flat array**

## 📦 Files

- **`rma_simulator.py`** - Core RMA implementation with `MemoryBlock` and `RecursiveMemory` classes
- **`rma_advanced_examples.py`** - Advanced usage examples (knowledge graphs, benchmarks, etc.)
- **`rma_repl.py`** - Interactive REPL for exploring RMA structures

## 🚀 Quick Start

### Basic Usage

```python
from rma_simulator import RecursiveMemory

# Initialize memory
memory = RecursiveMemory()

# Set values using paths
memory.set(["thoughts", "AI", "RML"], "recursive memory rocks")
memory.set(["emotions", "fear"], "predictive error signal")

# Alternative dot notation
memory.set("thoughts.philosophy.epistemology", "knowledge structures")

# Retrieve values
value = memory.get(["thoughts", "AI", "RML"])
print(value)  # "recursive memory rocks"

# Display the entire tree
memory.display()

# Search for values
results = memory.search("recursive memory rocks")
for path in results:
    print(" -> ".join(path))

# Get statistics
stats = memory.stats()
print(f"Total nodes: {stats['total_nodes']}")
print(f"Max depth: {stats['max_depth']}")
```

### Run the Demo

```bash
python rma_simulator.py
```

### Run Advanced Examples

```bash
python rma_advanced_examples.py
```

### Interactive REPL

```bash
python rma_repl.py
```

## 🎮 REPL Commands

| Command | Description | Example |
|---------|-------------|---------|
| `set` | Set a value at a path | `set thoughts.idea great concept` |
| `get` | Get a value at a path | `get thoughts.idea` |
| `delete` | Delete a path | `delete thoughts.idea` |
| `search` | Search for a value | `search great concept` |
| `search-key` | Search for a key name | `search-key idea` |
| `display` | Show the memory tree | `display` or `display --paths` |
| `stats` | Show memory statistics | `stats` |
| `export` | Export to JSON | `export` or `export file.json` |
| `clear` | Clear all memory | `clear` |
| `help` | Show help | `help` or `help <command>` |
| `exit` | Exit the REPL | `exit` or `quit` |

## 📚 Advanced Examples

### 1. Knowledge Graph

```python
memory.set("concepts.mathematics.algebra.definition", "study of symbols")
memory.set("concepts.physics.quantum.definition", "discrete energy")
definitions = memory.search_key("definition")
```

### 2. Conversation Memory

```python
memory.set("conversation.session_001.user.name", "Alice")
memory.set("conversation.session_001.messages.msg_1.text", "Hello!")
```

### 3. Filesystem Simulation

```python
memory.set("filesystem.home.user.documents.notes.txt", "meeting notes")
memory.set("filesystem.home.user.code.main.py", "print('hello')")
```

### 4. State Machine

```python
memory.set("states.idle.transitions.start", "processing")
memory.set("states.processing.transitions.complete", "done")
memory.set("current.state", "idle")
```

### 5. Semantic Memory

```python
memory.set("semantic.animals.dog.properties.legs", 4)
memory.set("episodic.2024_03_15.event", "saw a dog")
```

## 🔧 Core API

### RecursiveMemory Class

| Method | Description |
|--------|-------------|
| `set(path, value)` | Set value at path (creates nodes as needed) |
| `get(path)` | Get value at path |
| `delete(path)` | Delete node at path |
| `search(value)` | Find all paths with matching value |
| `search_key(key)` | Find all paths containing key |
| `display(show_paths=False)` | Display tree structure |
| `stats()` | Get memory statistics |
| `export()` | Export to nested dict |

### MemoryBlock Class (Lower Level)

| Method | Description |
|--------|-------------|
| `add_child(name, value)` | Add child node |
| `get_path(path)` | Traverse to path |
| `set_value(path, value)` | Set value at path |
| `get_value(path)` | Get value at path |
| `get_depth()` | Get max depth |
| `count_nodes()` | Count total nodes |
| `get_full_path()` | Get path from root |
| `to_dict()` | Convert to dict |

## 📊 Benchmarks

Comparison with flat dictionary (1000 operations):

| Operation | Recursive Memory | Flat Dict | Ratio |
|-----------|-----------------|-----------|-------|
| Write | ~1.3ms | ~0.2ms | ~7x slower |
| Read | ~0.8ms | ~0.2ms | ~5x slower |

**Trade-off:** RMA is slower but provides:
- Hierarchical structure
- Parent/child relationships
- Path-based queries
- Dynamic growth
- Semantic organization

## 💡 Use Cases

- **Knowledge graphs** - Represent conceptual relationships
- **Conversation context** - Store dialogue history hierarchically
- **State machines** - Model states and transitions
- **Configuration systems** - Nested settings
- **Semantic memory** - Organize facts and episodes
- **File systems** - Simulate directory structures
- **Neural architectures** - Prototype memory systems

## 🧪 Features Demonstrated

✅ Dynamic recursive memory growth
✅ Path-based access (dot notation or list)
✅ Value search
✅ Key search
✅ Parent traversal (backreferences)
✅ Tree visualization
✅ Depth and node counting
✅ JSON export
✅ Memory statistics
✅ Interactive REPL
✅ Benchmarks vs flat structures

## 🔮 Future Enhancements

| Feature | Description |
|---------|-------------|
| 🗺️ Visualization | Use graphviz to plot memory structure |
| 💾 Persistence | Save/load from disk |
| 🔍 Query language | SQL-like queries for memory |
| 🧮 Compression | Detect and merge duplicate subtrees |
| ⚡ Indexing | Speed up searches with indices |
| 🔄 Versioning | Track changes over time |
| 🌐 Distributed | Share memory across processes |
| 🧬 Genetic ops | Crossover/mutation for evolution |

## 📖 Learning Resources

This simulator demonstrates:

1. **Recursive data structures** - Trees that reference themselves
2. **Dynamic memory** - Growing structures at runtime
3. **Path-based addressing** - Navigate via semantic paths
4. **Parent-child relationships** - Bidirectional references
5. **Tree algorithms** - Traversal, search, depth calculation

## 🎓 Philosophy

> "Memory is not a flat buffer. It's a recursive, self-referential structure where meaning emerges from relationships, not addresses."

Traditional memory: `array[index] = value`
Recursive memory: `memory["thoughts"]["AI"]["RML"] = value`

The latter preserves **semantic structure** and **relationships**.

## 🤝 Contributing Ideas

Want to extend this? Try:

- Implement graph visualization
- Add persistence (pickle/JSON)
- Build a query DSL
- Create memory pruning algorithms
- Implement attention mechanisms
- Add temporal versioning
- Build neural network integration

## 📝 License

Public domain. Use, modify, share freely.

---

**Built with ❤️ in pure Python — no dependencies, no complexity, just recursive elegance.**

🧠 *"Recursion is the universe thinking about itself."*

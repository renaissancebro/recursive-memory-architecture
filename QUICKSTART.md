# 🚀 Recursive Memory Architecture - Quick Start

## What You Have

A complete **Recursive Memory Architecture (RMA)** simulator in pure Python — no dependencies needed!

## Files Overview

| File | Purpose | Size |
|------|---------|------|
| `rma_simulator.py` | Core implementation | 8.2K |
| `rma_advanced_examples.py` | Advanced examples & benchmarks | 8.5K |
| `rma_repl.py` | Interactive REPL | 6.2K |
| `rma_visualize.py` | Tree visualizations | 6.8K |
| `test_rma.py` | Test suite (18 tests) | 6.5K |
| `RMA_README.md` | Full documentation | 7.0K |

**Total: ~43KB of pure Python code**

## Try It Now!

### 1. Run the Basic Demo (30 seconds)

```bash
python rma_simulator.py
```

**What you'll see:**
- Memory tree creation
- Value retrieval
- Search functionality
- Statistics

### 2. Run Advanced Examples (1 minute)

```bash
python rma_advanced_examples.py
```

**What you'll see:**
- Knowledge graphs
- Conversation memory
- Filesystem simulation
- State machines
- Semantic memory
- JSON export
- Parent traversal
- Performance benchmarks

### 3. Play Interactively (as long as you want!)

```bash
python rma_repl.py
```

**Try these commands:**
```
set thoughts.AI.RML recursive memory rocks
get thoughts.AI.RML
display
search recursive
search-key AI
stats
help
```

### 4. See Beautiful Visualizations

```bash
python rma_visualize.py
```

**What you'll see:**
- ASCII tree visualization
- Horizontal tree layout
- Compact leaf view
- Depth histogram

### 5. Run Tests (verify everything works)

```bash
python test_rma.py
```

All 18 tests should pass ✅

## Code Examples

### Example 1: Basic Usage

```python
from rma_simulator import RecursiveMemory

memory = RecursiveMemory()

# Set values
memory.set(["thoughts", "AI", "RML"], "recursive memory rocks")
memory.set("emotions.fear", "predictive error signal")

# Get values
value = memory.get("thoughts.AI.RML")
print(value)  # "recursive memory rocks"

# Search
results = memory.search("recursive memory rocks")
print(results)  # [['thoughts', 'AI', 'RML']]

# Display tree
memory.display()
```

### Example 2: Knowledge Graph

```python
memory = RecursiveMemory()

# Build knowledge
memory.set("animals.dog.legs", 4)
memory.set("animals.dog.sound", "bark")
memory.set("animals.cat.legs", 4)
memory.set("animals.cat.sound", "meow")

# Query
all_dogs = memory.search_key("dog")
four_legged = memory.search(4)
```

### Example 3: State Machine

```python
memory = RecursiveMemory()

# Define states
memory.set("states.idle.next", "processing")
memory.set("states.processing.next", "done")
memory.set("current.state", "idle")

# Query current state
current = memory.get("current.state")
next_state = memory.get(f"states.{current}.next")
```

## Key Features

✅ **Zero dependencies** - Pure Python 3
✅ **Hierarchical structure** - Tree-based memory
✅ **Path-based access** - Use dot notation or lists
✅ **Dynamic growth** - Create nodes on the fly
✅ **Search & query** - Find by value or key
✅ **Parent traversal** - Navigate up the tree
✅ **Statistics** - Depth, count, structure analysis
✅ **Export/Import** - JSON serialization
✅ **Well-tested** - 18 comprehensive tests
✅ **Interactive REPL** - Explore live
✅ **Beautiful visualizations** - ASCII art trees

## Common Use Cases

### 🧠 AI/ML Memory Systems
```python
memory.set("context.conversation.user.intent", "search")
memory.set("context.conversation.history.msg_1", "Hello")
```

### 📊 Configuration Management
```python
memory.set("config.app.theme", "dark")
memory.set("config.features.export.enabled", True)
```

### 🗂️ Hierarchical Data
```python
memory.set("filesystem.home.documents.file.txt", "content")
memory.set("org.team.engineering.lead", "Alice")
```

### 🎯 State Machines
```python
memory.set("workflow.step1.next", "step2")
memory.set("workflow.step2.next", "complete")
```

## Performance Notes

From benchmarks (1000 operations):
- **Write**: ~1.3ms (7x slower than flat dict)
- **Read**: ~0.8ms (5x slower than flat dict)

**Trade-off**: Slower but provides:
- Semantic structure
- Relationship modeling
- Hierarchical queries
- Dynamic growth

## Next Steps

1. **Read the full docs**: `RMA_README.md`
2. **Study examples**: `rma_advanced_examples.py`
3. **Experiment in REPL**: `python rma_repl.py`
4. **Build something**: Use RMA in your project!

## Philosophy

> Traditional memory: `array[0] = value`
>
> Recursive memory: `memory["thoughts"]["AI"]["RML"] = value`

The latter preserves **semantic relationships** and **hierarchical structure**.

## Questions?

- Check `RMA_README.md` for detailed docs
- Read the source code — it's clean & commented
- Run examples to see real usage patterns
- Use the REPL to experiment

---

**Built in pure Python. No magic. Just recursive elegance. 🧠**

*"Recursion is the universe thinking about itself."*

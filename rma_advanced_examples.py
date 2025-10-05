"""
Advanced examples for the Recursive Memory Architecture simulator.
Demonstrates benchmarking, complex queries, and practical applications.
"""

from rma_simulator import RecursiveMemory, MemoryBlock
import time
import json


def example_knowledge_graph():
    """Build a knowledge graph using recursive memory."""
    print("\n" + "="*60)
    print("📚 Example 1: Knowledge Graph")
    print("="*60)

    memory = RecursiveMemory()

    # Build a conceptual knowledge graph
    memory.set("concepts.mathematics.algebra.definition", "study of mathematical symbols")
    memory.set("concepts.mathematics.algebra.uses", ["cryptography", "physics", "ML"])
    memory.set("concepts.mathematics.calculus.definition", "study of change")
    memory.set("concepts.mathematics.calculus.inventor", "Newton/Leibniz")

    memory.set("concepts.physics.quantum.definition", "discrete energy levels")
    memory.set("concepts.physics.quantum.key_principle", "uncertainty")
    memory.set("concepts.physics.classical.definition", "deterministic mechanics")

    memory.set("relationships.mathematics.connects_to", "physics")
    memory.set("relationships.physics.foundation", "mathematics")

    memory.display()

    print("\n🔍 Query: Find all definitions")
    definitions = memory.search_key("definition")
    for path in definitions:
        value = memory.get(path)
        print(f"  {' -> '.join(path)}: {value}")


def example_conversation_memory():
    """Simulate conversation/dialogue memory."""
    print("\n" + "="*60)
    print("💬 Example 2: Conversation Memory")
    print("="*60)

    memory = RecursiveMemory()

    # Store conversation context
    memory.set("conversation.session_001.user.name", "Alice")
    memory.set("conversation.session_001.user.intent", "learn RML")
    memory.set("conversation.session_001.messages.msg_1.speaker", "user")
    memory.set("conversation.session_001.messages.msg_1.text", "What is RML?")
    memory.set("conversation.session_001.messages.msg_2.speaker", "assistant")
    memory.set("conversation.session_001.messages.msg_2.text", "Recursive Memory Logic")

    memory.set("conversation.session_002.user.name", "Bob")
    memory.set("conversation.session_002.user.intent", "debug code")

    memory.display()

    print("\n📊 Statistics:")
    stats = memory.stats()
    print(f"  Total conversation nodes: {stats['total_nodes']}")
    print(f"  Memory depth: {stats['max_depth']}")


def example_hierarchical_filesystem():
    """Simulate a file system structure."""
    print("\n" + "="*60)
    print("📁 Example 3: Hierarchical Filesystem")
    print("="*60)

    memory = RecursiveMemory()

    # Build file system
    memory.set("filesystem.home.user.documents.notes.txt", "content: meeting notes")
    memory.set("filesystem.home.user.documents.reports.pdf", "content: Q4 report")
    memory.set("filesystem.home.user.code.python.main.py", "content: print('hello')")
    memory.set("filesystem.home.user.code.python.utils.py", "content: utilities")
    memory.set("filesystem.home.user.code.rust.main.rs", "content: fn main() {}")

    memory.display()

    print("\n🔍 Find all Python files:")
    python_files = memory.search_key("python")
    for path in python_files:
        print(f"  /{'/'.join(path)}")


def example_state_machine():
    """Model a state machine with recursive states."""
    print("\n" + "="*60)
    print("⚙️  Example 4: State Machine")
    print("="*60)

    memory = RecursiveMemory()

    # Define states and transitions
    memory.set("states.idle.description", "waiting for input")
    memory.set("states.idle.transitions.start", "processing")
    memory.set("states.processing.description", "working on task")
    memory.set("states.processing.transitions.complete", "done")
    memory.set("states.processing.transitions.error", "failed")
    memory.set("states.done.description", "task completed")
    memory.set("states.failed.description", "error occurred")
    memory.set("states.failed.transitions.retry", "processing")

    memory.set("current.state", "idle")

    memory.display()


def benchmark_vs_dict():
    """Compare recursive memory vs flat dictionary."""
    print("\n" + "="*60)
    print("⚡ Benchmark: Recursive Memory vs Flat Dict")
    print("="*60)

    n = 1000

    # Benchmark recursive memory
    memory = RecursiveMemory()
    start = time.time()
    for i in range(n):
        memory.set(f"data.category_{i % 10}.item_{i}.value", i)
    rma_write_time = time.time() - start

    start = time.time()
    for i in range(n):
        _ = memory.get(f"data.category_{i % 10}.item_{i}.value")
    rma_read_time = time.time() - start

    # Benchmark flat dictionary
    flat_dict = {}
    start = time.time()
    for i in range(n):
        flat_dict[f"data.category_{i % 10}.item_{i}.value"] = i
    dict_write_time = time.time() - start

    start = time.time()
    for i in range(n):
        _ = flat_dict.get(f"data.category_{i % 10}.item_{i}.value")
    dict_read_time = time.time() - start

    print(f"\n📝 Writing {n} values:")
    print(f"  Recursive Memory: {rma_write_time*1000:.2f}ms")
    print(f"  Flat Dictionary:  {dict_write_time*1000:.2f}ms")
    print(f"  Ratio: {rma_write_time/dict_write_time:.2f}x")

    print(f"\n📖 Reading {n} values:")
    print(f"  Recursive Memory: {rma_read_time*1000:.2f}ms")
    print(f"  Flat Dictionary:  {dict_read_time*1000:.2f}ms")
    print(f"  Ratio: {rma_read_time/dict_read_time:.2f}x")

    print(f"\n📊 Memory structure stats:")
    stats = memory.stats()
    print(f"  Total nodes: {stats['total_nodes']}")
    print(f"  Max depth: {stats['max_depth']}")


def example_semantic_memory():
    """Build semantic/episodic memory structure."""
    print("\n" + "="*60)
    print("🧠 Example 5: Semantic Memory")
    print("="*60)

    memory = RecursiveMemory()

    # Semantic knowledge
    memory.set("semantic.animals.dog.properties.legs", 4)
    memory.set("semantic.animals.dog.properties.sound", "bark")
    memory.set("semantic.animals.dog.category", "mammal")
    memory.set("semantic.animals.cat.properties.legs", 4)
    memory.set("semantic.animals.cat.properties.sound", "meow")
    memory.set("semantic.animals.bird.properties.legs", 2)
    memory.set("semantic.animals.bird.properties.can_fly", True)

    # Episodic memory (specific events)
    memory.set("episodic.2024_03_15.event", "saw a dog in park")
    memory.set("episodic.2024_03_15.emotion", "joy")
    memory.set("episodic.2024_03_15.location", "central park")

    memory.display()

    print("\n🔍 Query: Find all animals with 4 legs")
    # This demonstrates the limitation - we'd need to traverse manually
    animals = memory.search(4)
    print(f"  Found {len(animals)} entries with value '4':")
    for path in animals:
        if "properties" in path and "legs" in path:
            animal_name = path[2]  # Extract animal name
            print(f"    - {animal_name}")


def example_json_export():
    """Export memory to JSON."""
    print("\n" + "="*60)
    print("💾 Example 6: JSON Export/Import")
    print("="*60)

    memory = RecursiveMemory()

    memory.set("config.app.name", "RMA Simulator")
    memory.set("config.app.version", "1.0.0")
    memory.set("config.features.search", True)
    memory.set("config.features.export", True)

    # Export to dict
    exported = memory.export()

    # Pretty print JSON
    print("\n📤 Exported structure:")
    print(json.dumps(exported, indent=2))


def example_parent_traversal():
    """Demonstrate upward traversal using parent references."""
    print("\n" + "="*60)
    print("⬆️  Example 7: Parent Traversal")
    print("="*60)

    memory = RecursiveMemory()

    memory.set("thoughts.deep.nested.idea", "bottom value")

    # Get the deepest node
    node = memory.root.get_path(["thoughts", "deep", "nested", "idea"])

    print("\n🔄 Traversing upward from deepest node:")
    current = node
    level = 0
    while current is not None:
        path = current.get_full_path()
        path_str = " -> ".join(path) if path else "root"
        print(f"  Level {level}: {path_str} = '{current.value}'")
        current = current.parent
        level += 1


def main():
    """Run all advanced examples."""
    print("\n🚀 RECURSIVE MEMORY ARCHITECTURE - ADVANCED EXAMPLES")
    print("="*60)

    example_knowledge_graph()
    example_conversation_memory()
    example_hierarchical_filesystem()
    example_state_machine()
    example_semantic_memory()
    example_json_export()
    example_parent_traversal()
    benchmark_vs_dict()

    print("\n" + "="*60)
    print("✅ All examples complete!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()

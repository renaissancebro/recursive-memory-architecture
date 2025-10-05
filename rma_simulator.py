"""
Recursive Memory Architecture (RMA) Simulator
A pure Python implementation of hierarchical recursive memory structures.
"""

class MemoryBlock:
    """
    A node in the recursive memory tree.
    Each block can store a value and spawn child blocks dynamically.
    """

    def __init__(self, value=None, parent=None, name=None):
        self.value = value
        self.children = {}
        self.parent = parent
        self.name = name

    def add_child(self, name, value=None):
        """Add a child memory block."""
        child = MemoryBlock(value=value, parent=self, name=name)
        self.children[name] = child
        return child

    def get_path(self, path):
        """
        Traverse memory via path.
        Example: ['thoughts', 'ideas', 'RML']
        Returns the node at that path, or None if not found.
        """
        node = self
        for key in path:
            if key not in node.children:
                return None
            node = node.children[key]
        return node

    def set_value(self, path, value):
        """Set value at a recursive memory path, creating nodes as needed."""
        node = self
        for key in path:
            if key not in node.children:
                node.add_child(key)
            node = node.children[key]
        node.value = value

    def get_value(self, path):
        """Get value at a path, or None if not found."""
        node = self.get_path(path)
        return node.value if node else None

    def delete_path(self, path):
        """Delete a node at the given path."""
        if len(path) == 0:
            return False

        parent_path = path[:-1]
        key = path[-1]

        parent = self.get_path(parent_path) if parent_path else self
        if parent and key in parent.children:
            del parent.children[key]
            return True
        return False

    def search(self, value):
        """Search for all nodes with a given value. Returns list of paths."""
        results = []
        self._search_recursive(value, [], results)
        return results

    def _search_recursive(self, value, current_path, results):
        """Helper for recursive search."""
        if self.value == value:
            results.append(current_path.copy())

        for key, child in self.children.items():
            child._search_recursive(value, current_path + [key], results)

    def search_key(self, key_name):
        """Find all paths that contain a specific key."""
        results = []
        self._search_key_recursive(key_name, [], results)
        return results

    def _search_key_recursive(self, key_name, current_path, results):
        """Helper for recursive key search."""
        for key, child in self.children.items():
            new_path = current_path + [key]
            if key == key_name:
                results.append(new_path)
            child._search_key_recursive(key_name, new_path, results)

    def get_depth(self):
        """Calculate maximum depth of memory tree."""
        if not self.children:
            return 0
        return 1 + max(child.get_depth() for child in self.children.values())

    def count_nodes(self):
        """Count total number of nodes in subtree."""
        count = 1  # Count self
        for child in self.children.values():
            count += child.count_nodes()
        return count

    def get_full_path(self):
        """Get the full path from root to this node."""
        path = []
        node = self
        while node.parent is not None:
            if node.name:
                path.insert(0, node.name)
            node = node.parent
        return path

    def display(self, level=0, show_paths=False):
        """Display the memory tree structure."""
        indent = "  " * level
        display_value = f"'{self.value}'" if self.value else "None"

        if show_paths and self.name:
            path = " -> ".join(self.get_full_path())
            print(f"{indent}[{self.name}] = {display_value} (path: {path})")
        elif self.name:
            print(f"{indent}[{self.name}] = {display_value}")
        else:
            print(f"{indent}- {display_value}")

        for child in self.children.values():
            child.display(level + 1, show_paths)

    def to_dict(self):
        """Convert memory structure to nested dictionary."""
        result = {"value": self.value}
        if self.children:
            result["children"] = {
                key: child.to_dict()
                for key, child in self.children.items()
            }
        return result

    def stats(self):
        """Get statistics about the memory structure."""
        return {
            "total_nodes": self.count_nodes(),
            "max_depth": self.get_depth(),
            "direct_children": len(self.children),
            "has_value": self.value is not None
        }


class RecursiveMemory:
    """
    Main interface for the Recursive Memory Architecture.
    Provides high-level operations on the memory tree.
    """

    def __init__(self):
        self.root = MemoryBlock(value="root", name="root")

    def set(self, path, value):
        """Set a value at a path."""
        if isinstance(path, str):
            path = path.split('.')
        self.root.set_value(path, value)

    def get(self, path):
        """Get a value at a path."""
        if isinstance(path, str):
            path = path.split('.')
        return self.root.get_value(path)

    def delete(self, path):
        """Delete a node at a path."""
        if isinstance(path, str):
            path = path.split('.')
        return self.root.delete_path(path)

    def search(self, value):
        """Search for all occurrences of a value."""
        return self.root.search(value)

    def search_key(self, key):
        """Search for all paths containing a key."""
        return self.root.search_key(key)

    def display(self, show_paths=False):
        """Display the entire memory tree."""
        print("\n🧠 Recursive Memory Structure:")
        print("=" * 50)
        self.root.display(show_paths=show_paths)
        print("=" * 50)

    def stats(self):
        """Get overall memory statistics."""
        return self.root.stats()

    def export(self):
        """Export memory structure as nested dict."""
        return self.root.to_dict()


def demo():
    """Demonstration of the Recursive Memory Architecture."""

    print("🧠 Recursive Memory Architecture Simulator")
    print("=" * 60)

    # Initialize memory
    memory = RecursiveMemory()

    # Set deeply nested values
    print("\n📝 Setting values in recursive memory...")
    memory.set(["thoughts", "AI", "RML"], "recursive memory rocks")
    memory.set(["thoughts", "AI", "alignment"], "emotion is logic")
    memory.set(["thoughts", "philosophy", "epistemology"], "knowledge structures")
    memory.set(["emotions", "fear"], "predictive error signal")
    memory.set(["emotions", "joy"], "goal achievement signal")
    memory.set(["sensory", "vision", "color"], "wavelength perception")
    memory.set(["sensory", "vision", "depth"], "binocular disparity")

    # Alternative syntax using dot notation
    memory.set("actions.speak.intent", "communicate ideas")
    memory.set("actions.move.purpose", "navigate space")

    print("✓ Values set successfully")

    # Display memory tree
    memory.display()

    # Retrieve specific values
    print("\n🔍 Retrieving specific values:")
    rml_value = memory.get(["thoughts", "AI", "RML"])
    print(f"  thoughts -> AI -> RML: '{rml_value}'")

    fear_value = memory.get("emotions.fear")
    print(f"  emotions.fear: '{fear_value}'")

    # Search functionality
    print("\n🔎 Search for value 'emotion is logic':")
    results = memory.search("emotion is logic")
    for path in results:
        print(f"  Found at: {' -> '.join(path)}")

    print("\n🔎 Search for all paths containing 'AI':")
    key_results = memory.search_key("AI")
    for path in key_results:
        print(f"  Found at: {' -> '.join(path)}")

    # Statistics
    print("\n📊 Memory Statistics:")
    stats = memory.stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")

    # Demonstrate deletion
    print("\n🗑️  Deleting path: emotions.fear")
    memory.delete("emotions.fear")
    memory.display()

    print("\n✅ Simulation complete!")


if __name__ == "__main__":
    demo()

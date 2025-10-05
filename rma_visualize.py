"""
ASCII Visualization for Recursive Memory Architecture
Creates beautiful tree visualizations without external dependencies.
"""

from rma_simulator import RecursiveMemory


def tree_visualize(memory, max_depth=None, show_values=True):
    """
    Create an ASCII tree visualization of the memory structure.

    Args:
        memory: RecursiveMemory instance
        max_depth: Maximum depth to display (None for unlimited)
        show_values: Whether to show node values
    """

    def _build_tree(node, prefix="", is_last=True, depth=0, path_name="root"):
        """Recursively build the ASCII tree."""
        if max_depth and depth >= max_depth:
            return

        # Determine the branch characters
        branch = "└── " if is_last else "├── "

        # Format the node
        value_str = ""
        if show_values and node.value is not None:
            # Truncate long values
            val = str(node.value)
            if len(val) > 40:
                val = val[:37] + "..."
            value_str = f" = '{val}'"

        # Print the current node
        print(f"{prefix}{branch}{path_name}{value_str}")

        # Prepare prefix for children
        if is_last:
            new_prefix = prefix + "    "
        else:
            new_prefix = prefix + "│   "

        # Process children
        children = list(node.children.items())
        for i, (key, child) in enumerate(children):
            is_last_child = (i == len(children) - 1)
            _build_tree(child, new_prefix, is_last_child, depth + 1, key)

    print("\n" + "="*70)
    print("🌳 RECURSIVE MEMORY TREE VISUALIZATION")
    print("="*70 + "\n")
    _build_tree(memory.root, "", True, 0, "root")
    print("\n" + "="*70 + "\n")


def horizontal_tree(memory, max_width=80):
    """
    Create a horizontal tree layout (left to right).
    """

    def _get_max_depth(node, depth=0):
        """Calculate maximum depth."""
        if not node.children:
            return depth
        return max(_get_max_depth(child, depth + 1)
                   for child in node.children.values())

    def _build_layers(node, depth=0, layers=None):
        """Build layers for horizontal display."""
        if layers is None:
            layers = {}

        if depth not in layers:
            layers[depth] = []

        name = node.name if node.name else "root"
        value = f"={node.value}" if node.value else ""
        layers[depth].append(f"{name}{value}")

        for child in node.children.values():
            _build_layers(child, depth + 1, layers)

        return layers

    print("\n" + "="*70)
    print("🌲 HORIZONTAL MEMORY TREE")
    print("="*70 + "\n")

    layers = _build_layers(memory.root)
    max_depth = max(layers.keys())

    for depth in range(max_depth + 1):
        indent = "  " * depth
        arrow = "→ " if depth > 0 else ""
        nodes = layers.get(depth, [])

        # Show up to 5 nodes per layer, then summarize
        if len(nodes) <= 5:
            print(f"{indent}{arrow}[{', '.join(nodes)}]")
        else:
            shown = ', '.join(nodes[:5])
            print(f"{indent}{arrow}[{shown}, ... +{len(nodes)-5} more]")

    print("\n" + "="*70 + "\n")


def compact_view(memory):
    """
    Create a compact path view showing all leaf nodes.
    """

    def _find_leaves(node, current_path=None):
        """Find all leaf nodes with their paths."""
        if current_path is None:
            current_path = []

        leaves = []

        if not node.children:  # Leaf node
            path_str = ".".join(current_path) if current_path else "root"
            value = node.value if node.value else "(empty)"
            leaves.append((path_str, value))
        else:
            for key, child in node.children.items():
                leaves.extend(_find_leaves(child, current_path + [key]))

        return leaves

    print("\n" + "="*70)
    print("📋 COMPACT VIEW (Leaf Nodes Only)")
    print("="*70 + "\n")

    leaves = _find_leaves(memory.root)

    if not leaves:
        print("  (empty memory)")
    else:
        # Find max path length for alignment
        max_path_len = max(len(path) for path, _ in leaves)

        for path, value in sorted(leaves):
            # Truncate long values
            val_str = str(value)
            if len(val_str) > 50:
                val_str = val_str[:47] + "..."

            print(f"  {path:<{max_path_len}} → {val_str}")

    print("\n" + "="*70 + "\n")


def depth_histogram(memory):
    """
    Show a histogram of nodes by depth.
    """

    def _count_by_depth(node, depth=0, counts=None):
        """Count nodes at each depth."""
        if counts is None:
            counts = {}

        counts[depth] = counts.get(depth, 0) + 1

        for child in node.children.values():
            _count_by_depth(child, depth + 1, counts)

        return counts

    print("\n" + "="*70)
    print("📊 DEPTH HISTOGRAM")
    print("="*70 + "\n")

    counts = _count_by_depth(memory.root)
    max_count = max(counts.values())

    for depth in sorted(counts.keys()):
        count = counts[depth]
        bar_length = int((count / max_count) * 40)
        bar = "█" * bar_length
        print(f"  Depth {depth}: {bar} ({count} nodes)")

    print("\n" + "="*70 + "\n")


def demo():
    """Demonstrate different visualization styles."""

    # Create sample memory
    memory = RecursiveMemory()

    # Build a rich example
    memory.set("system.core.cpu", "ARM64")
    memory.set("system.core.memory", "16GB")
    memory.set("system.peripherals.display", "Retina")
    memory.set("system.peripherals.keyboard", "Magic Keyboard")
    memory.set("system.peripherals.trackpad", "Force Touch")

    memory.set("user.profile.name", "Alice")
    memory.set("user.profile.role", "Developer")
    memory.set("user.preferences.theme", "dark")
    memory.set("user.preferences.editor", "vim")
    memory.set("user.recent.files", "[main.py, utils.py, test.py]")
    memory.set("user.recent.commands", "['build', 'test', 'deploy']")

    memory.set("app.state.current", "idle")
    memory.set("app.state.last_error", "None")
    memory.set("app.features.search.enabled", True)
    memory.set("app.features.export.enabled", True)
    memory.set("app.features.sync.enabled", False)

    # Show different visualizations
    print("\n🎨 RECURSIVE MEMORY ARCHITECTURE VISUALIZATIONS")
    print("="*70)

    # 1. Traditional tree
    tree_visualize(memory, show_values=True)

    # 2. Horizontal layout
    horizontal_tree(memory)

    # 3. Compact leaf view
    compact_view(memory)

    # 4. Depth histogram
    depth_histogram(memory)

    # Show stats
    stats = memory.stats()
    print("📈 OVERALL STATISTICS")
    print("="*70)
    print(f"  Total nodes:     {stats['total_nodes']}")
    print(f"  Maximum depth:   {stats['max_depth']}")
    print(f"  Direct children: {stats['direct_children']}")
    print("="*70 + "\n")


if __name__ == "__main__":
    demo()

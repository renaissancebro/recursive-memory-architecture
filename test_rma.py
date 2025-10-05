"""
Test suite for Recursive Memory Architecture
Run with: python test_rma.py
"""

from rma_simulator import RecursiveMemory, MemoryBlock


def test_basic_set_get():
    """Test basic set and get operations."""
    print("Testing basic set/get... ", end="")
    memory = RecursiveMemory()

    memory.set(["a", "b", "c"], "value")
    result = memory.get(["a", "b", "c"])

    assert result == "value", f"Expected 'value', got {result}"
    print("✓")


def test_dot_notation():
    """Test dot notation path syntax."""
    print("Testing dot notation... ", end="")
    memory = RecursiveMemory()

    memory.set("x.y.z", "test")
    result = memory.get("x.y.z")

    assert result == "test", f"Expected 'test', got {result}"
    print("✓")


def test_overwrite():
    """Test overwriting existing values."""
    print("Testing value overwrite... ", end="")
    memory = RecursiveMemory()

    memory.set("path", "old")
    memory.set("path", "new")
    result = memory.get("path")

    assert result == "new", f"Expected 'new', got {result}"
    print("✓")


def test_delete():
    """Test delete operation."""
    print("Testing delete... ", end="")
    memory = RecursiveMemory()

    memory.set("a.b.c", "value")
    assert memory.get("a.b.c") == "value"

    success = memory.delete("a.b.c")
    assert success, "Delete should return True"

    result = memory.get("a.b.c")
    assert result is None, f"Expected None after delete, got {result}"
    print("✓")


def test_search_value():
    """Test search by value."""
    print("Testing search by value... ", end="")
    memory = RecursiveMemory()

    memory.set("path1.a", "target")
    memory.set("path2.b", "target")
    memory.set("path3.c", "other")

    results = memory.search("target")

    assert len(results) == 2, f"Expected 2 results, got {len(results)}"
    print("✓")


def test_search_key():
    """Test search by key."""
    print("Testing search by key... ", end="")
    memory = RecursiveMemory()

    memory.set("a.target.x", "val1")
    memory.set("b.target.y", "val2")
    memory.set("c.other.z", "val3")

    results = memory.search_key("target")

    assert len(results) == 2, f"Expected 2 results, got {len(results)}"
    print("✓")


def test_depth():
    """Test depth calculation."""
    print("Testing depth calculation... ", end="")
    memory = RecursiveMemory()

    memory.set("a", "val")
    assert memory.root.get_depth() == 1

    memory.set("a.b.c.d.e", "deep")
    assert memory.root.get_depth() == 5
    print("✓")


def test_count_nodes():
    """Test node counting."""
    print("Testing node count... ", end="")
    memory = RecursiveMemory()

    memory.set("a", "val")
    memory.set("b", "val")
    memory.set("c.d", "val")

    # root + a + b + c + d = 5
    stats = memory.stats()
    assert stats['total_nodes'] == 5, f"Expected 5 nodes, got {stats['total_nodes']}"
    print("✓")


def test_parent_reference():
    """Test parent references."""
    print("Testing parent references... ", end="")
    memory = RecursiveMemory()

    memory.set("a.b.c", "value")
    node_c = memory.root.get_path(["a", "b", "c"])

    assert node_c.parent is not None, "Node should have parent"
    assert node_c.parent.name == "b", f"Parent should be 'b', got {node_c.parent.name}"
    print("✓")


def test_full_path():
    """Test getting full path."""
    print("Testing full path retrieval... ", end="")
    memory = RecursiveMemory()

    memory.set("x.y.z", "value")
    node = memory.root.get_path(["x", "y", "z"])

    path = node.get_full_path()
    assert path == ["x", "y", "z"], f"Expected ['x', 'y', 'z'], got {path}"
    print("✓")


def test_export():
    """Test export to dict."""
    print("Testing export... ", end="")
    memory = RecursiveMemory()

    memory.set("a.b", "value")
    exported = memory.export()

    assert "children" in exported, "Export should have children"
    assert "a" in exported["children"], "Export should contain 'a'"
    print("✓")


def test_empty_get():
    """Test getting non-existent paths."""
    print("Testing non-existent path... ", end="")
    memory = RecursiveMemory()

    result = memory.get("does.not.exist")
    assert result is None, f"Expected None, got {result}"
    print("✓")


def test_mixed_types():
    """Test storing different value types."""
    print("Testing mixed types... ", end="")
    memory = RecursiveMemory()

    memory.set("int", 42)
    memory.set("str", "text")
    memory.set("bool", True)
    memory.set("list", [1, 2, 3])
    memory.set("dict", {"key": "val"})

    assert memory.get("int") == 42
    assert memory.get("str") == "text"
    assert memory.get("bool") is True
    assert memory.get("list") == [1, 2, 3]
    assert memory.get("dict") == {"key": "val"}
    print("✓")


def test_unicode():
    """Test unicode support."""
    print("Testing unicode... ", end="")
    memory = RecursiveMemory()

    memory.set("emoji", "🧠💡🔥")
    memory.set("chinese", "记忆")
    memory.set("arabic", "ذاكرة")

    assert memory.get("emoji") == "🧠💡🔥"
    assert memory.get("chinese") == "记忆"
    assert memory.get("arabic") == "ذاكرة"
    print("✓")


def test_deep_nesting():
    """Test very deep nesting."""
    print("Testing deep nesting... ", end="")
    memory = RecursiveMemory()

    # Create a 20-level deep path
    path = [f"level_{i}" for i in range(20)]
    memory.set(path, "deep_value")

    result = memory.get(path)
    assert result == "deep_value", f"Expected 'deep_value', got {result}"
    assert memory.root.get_depth() == 20
    print("✓")


def test_intermediate_nodes():
    """Test that intermediate nodes are created without values."""
    print("Testing intermediate nodes... ", end="")
    memory = RecursiveMemory()

    memory.set("a.b.c", "value")

    # Intermediate nodes should exist but have None values
    assert memory.get("a") is None
    assert memory.get("a.b") is None
    assert memory.get("a.b.c") == "value"
    print("✓")


def test_delete_nonexistent():
    """Test deleting non-existent path."""
    print("Testing delete non-existent... ", end="")
    memory = RecursiveMemory()

    success = memory.delete("does.not.exist")
    assert not success, "Delete should return False for non-existent path"
    print("✓")


def test_search_empty():
    """Test search on empty memory."""
    print("Testing search on empty memory... ", end="")
    memory = RecursiveMemory()

    results = memory.search("anything")
    assert len(results) == 0, f"Expected 0 results, got {len(results)}"
    print("✓")


def run_all_tests():
    """Run all test functions."""
    print("\n" + "="*60)
    print("🧪 RECURSIVE MEMORY ARCHITECTURE TEST SUITE")
    print("="*60 + "\n")

    test_functions = [
        test_basic_set_get,
        test_dot_notation,
        test_overwrite,
        test_delete,
        test_search_value,
        test_search_key,
        test_depth,
        test_count_nodes,
        test_parent_reference,
        test_full_path,
        test_export,
        test_empty_get,
        test_mixed_types,
        test_unicode,
        test_deep_nesting,
        test_intermediate_nodes,
        test_delete_nonexistent,
        test_search_empty,
    ]

    passed = 0
    failed = 0

    for test_func in test_functions:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"✗ FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ ERROR: {e}")
            failed += 1

    print("\n" + "="*60)
    print(f"📊 RESULTS: {passed} passed, {failed} failed out of {passed + failed} tests")

    if failed == 0:
        print("✅ All tests passed!")
    else:
        print(f"❌ {failed} test(s) failed")

    print("="*60 + "\n")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)

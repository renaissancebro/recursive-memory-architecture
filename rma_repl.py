#!/usr/bin/env python3
"""
Interactive REPL for Recursive Memory Architecture
Explore and manipulate recursive memory structures interactively.
"""

from rma_simulator import RecursiveMemory
import json
import sys


class RMLREPL:
    """Interactive Read-Eval-Print Loop for RMA."""

    def __init__(self):
        self.memory = RecursiveMemory()
        self.commands = {
            'set': self.cmd_set,
            'get': self.cmd_get,
            'delete': self.cmd_delete,
            'search': self.cmd_search,
            'search-key': self.cmd_search_key,
            'display': self.cmd_display,
            'stats': self.cmd_stats,
            'export': self.cmd_export,
            'clear': self.cmd_clear,
            'help': self.cmd_help,
            'exit': self.cmd_exit,
            'quit': self.cmd_exit,
        }

    def cmd_set(self, args):
        """Set a value at a path. Usage: set <path> <value>"""
        if len(args) < 2:
            print("❌ Usage: set <path> <value>")
            return
        path = args[0]
        value = ' '.join(args[1:])
        self.memory.set(path, value)
        print(f"✓ Set {path} = '{value}'")

    def cmd_get(self, args):
        """Get a value at a path. Usage: get <path>"""
        if len(args) < 1:
            print("❌ Usage: get <path>")
            return
        path = args[0]
        value = self.memory.get(path)
        if value is not None:
            print(f"📖 {path} = '{value}'")
        else:
            print(f"❌ Path not found: {path}")

    def cmd_delete(self, args):
        """Delete a path. Usage: delete <path>"""
        if len(args) < 1:
            print("❌ Usage: delete <path>")
            return
        path = args[0]
        if self.memory.delete(path):
            print(f"✓ Deleted {path}")
        else:
            print(f"❌ Path not found: {path}")

    def cmd_search(self, args):
        """Search for a value. Usage: search <value>"""
        if len(args) < 1:
            print("❌ Usage: search <value>")
            return
        value = ' '.join(args)
        results = self.memory.search(value)
        if results:
            print(f"🔍 Found {len(results)} result(s):")
            for path in results:
                print(f"  → {' -> '.join(path)}")
        else:
            print(f"❌ No results found for: {value}")

    def cmd_search_key(self, args):
        """Search for a key. Usage: search-key <key>"""
        if len(args) < 1:
            print("❌ Usage: search-key <key>")
            return
        key = args[0]
        results = self.memory.search_key(key)
        if results:
            print(f"🔍 Found {len(results)} path(s) containing '{key}':")
            for path in results:
                print(f"  → {' -> '.join(path)}")
        else:
            print(f"❌ No paths found containing: {key}")

    def cmd_display(self, args):
        """Display the memory tree. Usage: display [--paths]"""
        show_paths = '--paths' in args
        self.memory.display(show_paths=show_paths)

    def cmd_stats(self, args):
        """Show memory statistics. Usage: stats"""
        stats = self.memory.stats()
        print("\n📊 Memory Statistics:")
        print(f"  Total nodes:     {stats['total_nodes']}")
        print(f"  Maximum depth:   {stats['max_depth']}")
        print(f"  Direct children: {stats['direct_children']}")
        print(f"  Root has value:  {stats['has_value']}")

    def cmd_export(self, args):
        """Export memory as JSON. Usage: export [filename]"""
        exported = self.memory.export()
        json_str = json.dumps(exported, indent=2)

        if args:
            filename = args[0]
            try:
                with open(filename, 'w') as f:
                    f.write(json_str)
                print(f"✓ Exported to {filename}")
            except Exception as e:
                print(f"❌ Error writing file: {e}")
        else:
            print(json_str)

    def cmd_clear(self, args):
        """Clear all memory. Usage: clear"""
        self.memory = RecursiveMemory()
        print("✓ Memory cleared")

    def cmd_help(self, args):
        """Show help. Usage: help [command]"""
        if args:
            cmd_name = args[0]
            if cmd_name in self.commands:
                cmd_func = self.commands[cmd_name]
                print(f"\n{cmd_func.__doc__}")
            else:
                print(f"❌ Unknown command: {cmd_name}")
        else:
            print("\n🧠 Recursive Memory Architecture - Interactive REPL")
            print("="*60)
            print("\nAvailable commands:")
            for name, func in sorted(self.commands.items()):
                doc = func.__doc__.split('.')[0] if func.__doc__ else ""
                print(f"  {name:12s} - {doc}")
            print("\nType 'help <command>' for detailed usage.")
            print("="*60)

    def cmd_exit(self, args):
        """Exit the REPL. Usage: exit"""
        print("\n👋 Goodbye!")
        sys.exit(0)

    def run(self):
        """Start the REPL."""
        print("🧠 Recursive Memory Architecture - Interactive REPL")
        print("="*60)
        print("Type 'help' for available commands, 'exit' to quit")
        print("="*60 + "\n")

        # Add some example data
        self.memory.set("example.greeting", "Hello, RMA!")
        self.memory.set("example.info", "Type 'display' to see the memory tree")
        print("💡 Loaded example data. Type 'display' to see it.\n")

        while True:
            try:
                line = input("RMA> ").strip()

                if not line:
                    continue

                parts = line.split()
                cmd = parts[0].lower()
                args = parts[1:]

                if cmd in self.commands:
                    self.commands[cmd](args)
                else:
                    print(f"❌ Unknown command: {cmd}. Type 'help' for available commands.")

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! (Use 'exit' or Ctrl+D to quit)")
                continue
            except EOFError:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")


def main():
    """Entry point."""
    repl = RMLREPL()
    repl.run()


if __name__ == "__main__":
    main()

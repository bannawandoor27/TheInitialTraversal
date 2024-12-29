# TheInitialTraversal

> Because code, like us, thrives on connection.

TheInitialTraversal helps you understand how your code pieces fit together. It gently maps the relationships between your files, turning complex codebases into something we can all understand - a story of connected parts.

## Getting Started

1. Bring the code home:
   ```bash
   git clone https://github.com/bannawandoor27/TheInitialTraversal.git
   cd TheInitialTraversal
   ```

2. Make friends with the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Let Tree-sitter settle in:
   ```bash
   cd tree_sitter
   python build.py
   ```

## The Good Part

Map your world:
```bash
python scripts/preprocess_codebase.py --codebase target_codebases/rosterly_pegasus_backend
```

See the connections:
```bash
python scripts/visualize_graph.py --output graph.png
```

Ask questions:
```bash
python main.py --query "What modules does manage.py depend on?"
```

## Why This Matters

Your code is more than just files in folders. It's a community of modules working together, each one helping the others do their part. TheInitialTraversal helps you see these relationships, making it easier to understand and care for your codebase.

Think of it as a friendly guide who knows all the paths through your code's neighborhood.

---

_Made with care for those who write code_
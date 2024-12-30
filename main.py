from parsers.tree_builder import build_tree_structure
from parsers.import_resolver import resolve_imports
from utils.file_manager import save_tree_to_file, load_tree_from_file

TARGET_CODEBASE_DIR = "target_codebases/"
OUTPUT_PICKLE_FILE = "tree_structure.pkl"

if __name__ == "__main__":
    print("Building tree structure...")
    tree = build_tree_structure(TARGET_CODEBASE_DIR)

    print("Resolving imports...")
    resolve_imports(tree)

    print("Saving tree structure...")
    save_tree_to_file(tree, OUTPUT_PICKLE_FILE)

    print("Tree structure created and saved successfully.")

import os
from tree_sitter import Language

def load_tree_sitter_languages():
    """
    Builds and loads Tree-sitter grammars.
    """
    Language.build_library(
        # Path to the compiled shared libray
        "build/tree-sitter-languages.so",
        # Paths to the grammar repositories
        [
            "tree-sitter-python",
            "tree-sitter-javascript",
            # TODO : Add more languages here
        ],
    )
    return {
        "python": Language("build/tree-sitter-languages.so", "python"),
        "javascript": Language("build/tree-sitter-languages.so", "javascript"),
    }

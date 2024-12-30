import pickle

def save_tree_to_file(tree, file_path):
    """
    Saves the tree structure to a pickle file.
    """
    with open(file_path, "wb") as f:
        pickle.dump(tree, f)
    print(f"Tree structure saved to {file_path}.")

def load_tree_from_file(file_path):
    """
    Loads the tree structure from a pickle file.
    """
    with open(file_path, "rb") as f:
        return pickle.load(f)

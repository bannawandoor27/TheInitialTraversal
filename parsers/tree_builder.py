import os
from utils.tree_node import TreeNode

def build_tree_structure(dir_path, parent=None, current_id="0"):
    """
    Recursively builds a tree structure of the target codebase.
    """
    root = TreeNode(
        name=os.path.basename(dir_path) or dir_path,
        node_type="directory",
        path=dir_path,
        parent=parent,
        id=current_id,
    )

    for idx, item in enumerate(sorted(os.listdir(dir_path))):
        item_path = os.path.join(dir_path, item)
        child_id = f"{current_id}-{idx + 1}"

        #### If the item is a directory, recursively build its tree
        if os.path.isdir(item_path):
            child_node = build_tree_structure(item_path, root, child_id)
            root.add_child(child_node)
        else:
            #### Create a leaf node for files
            root.add_child(
                TreeNode(
                    name=item,
                    node_type="file",
                    path=item_path,
                    parent=root,
                    id=child_id,
                )
            )
    return root

import os

def get_folder_tree(folder_path, indent=""):
    try:
        items = sorted(os.listdir(folder_path))
    except PermissionError:
        print(f"{indent}[Permission Denied] {folder_path}")
        return
    
    items = [item for item in items if (item != "venv" or item !=".git")]
    
    for i, item in enumerate(items):
        item_path = os.path.join(folder_path, item)
        is_last = (i == len(items) - 1)
        connector = "└──" if is_last else "├──"
        print(f"{indent}{connector} {item}")
        
        if os.path.isdir(item_path):
            new_indent = indent + ("    " if is_last else "│   ")
            get_folder_tree(item_path, new_indent)

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    print(folder_path)
    get_folder_tree(folder_path)

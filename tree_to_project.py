import os

def clean_line(line):
    return line.split("#")[0].rstrip()

def is_node(line):
    return "├──" in line or "└──" in line

def extract_depth_and_name(line):
    if "├──" in line:
        idx = line.index("├──")
        name = line[idx + 3:].strip()
    else:
        idx = line.index("└──")
        name = line[idx + 3:].strip()

    depth = idx // 4
    return depth, name

def is_file(name):
    return "." in name and not name.endswith("/")

def parse_tree(lines):
    stack = []
    root = None

    for raw in lines:
        line = clean_line(raw)

        # skip pure visual lines
        if line.strip() in {"", "│"}:
            continue

        # ROOT (no ├── / └── yet)
        if root is None and not is_node(line):
            root = line.strip().rstrip("/")
            os.makedirs(root, exist_ok=True)
            stack.append((0, root))
            continue

        # ignore anything that isn't a real node
        if not is_node(line):
            continue

        depth, name = extract_depth_and_name(line)

        while stack and stack[-1][0] >= depth + 1:
            stack.pop()

        parent = stack[-1][1]
        path = os.path.join(parent, name)

        if is_file(name):
            open(path, "a", encoding="utf-8").close()
        else:
            os.makedirs(path, exist_ok=True)

        stack.append((depth + 1, path))


def main():
    print("📁 Paste directory structure (ENTER twice to finish):\n")

    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)

    parse_tree(lines)
    print("\n✅ Directory structure created correctly!")


if __name__ == "__main__":
    main()

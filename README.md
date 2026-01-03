---

# Tree to Project

A lightweight Python CLI tool that creates a full directory and file structure by parsing a pasted tree diagram.

This tool is useful when you already have a project structure written as text (for example from ChatGPT, documentation, or a README) and want to instantly generate it on your local machine.

---

## Features

* Create folders and files from a tree diagram
* Supports standard `tree`-style output (`├──`, `└──`, `│`)
* Ignores comments and visual spacer lines
* Works with trees copied from:

  * ChatGPT
  * GitHub READMEs
  * Documentation
  * Terminal `tree` command
* No dependencies (Python standard library only)

---

## Requirements

* Python 3.x

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
```

No additional installation is required.

---

## Usage

Run the script:

```bash
python tree_to_project.py
```

You will be prompted to paste a directory structure.

Paste the tree diagram and press **ENTER twice** to finish.

---

## Input Example (Generic)

You can paste **any valid tree diagram**, for example:

```
my-project/
│
├── src/
│   ├── main.py
│   ├── utils.py
│   └── config.py
│
├── tests/
│   └── test_main.py
│
├── README.md
└── requirements.txt
```

Comments (after `#`) and visual lines (`│`) are ignored automatically.

---

## Output

The script will create the following structure on disk:

```
my-project/
├── src/
│   ├── main.py
│   ├── utils.py
│   └── config.py
├── tests/
│   └── test_main.py
├── README.md
└── requirements.txt
```

* Folders are created automatically
* Files are created as empty files
* Existing folders/files are not overwritten

---

## Supported Tree Formats

The tool supports trees that:

* Start with a root folder (`project-name/`)
* Start directly with `├── project-name`
* Use standard spacing and connectors

Example:

```
├── website
│   ├── index.html
│   ├── css
│   │   └── style.css
│   └── js
│       └── app.js
```

---

## Real-World Use Cases

### 1. Create project structure from ChatGPT output

When ChatGPT suggests a project layout as a tree diagram, paste it directly into this tool to instantly generate the structure locally.

### 2. Recreate folder structure from documentation

Many READMEs and technical documents describe folder structures using tree diagrams. This tool converts those diagrams into real folders and files.

### 3. Quickly bootstrap new projects

Instead of manually creating folders and files, define the structure once as text and generate it in seconds.

### 4. Teaching and learning

Useful for:

* Programming tutorials
* Assignments
* Demonstrating project architecture
* Preparing starter templates for students

---

## Limitations

* Files are created empty (no boilerplate code)
* Tree diagrams must follow a readable hierarchical format
* Existing files and folders are not modified or deleted

---

## Author

Created by **Soumya Kushwah**
A simple developer utility for turning tree diagrams into real projects.

---

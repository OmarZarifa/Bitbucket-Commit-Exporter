# Bitbucket Commit Exporter

A simple Python CLI tool that fetches commit history from any Bitbucket repository and exports it into a Word document (`.docx`).

---

## 🔧 Features

- Fetch latest commits via the Bitbucket 2.0 REST API  
- Prompt interactively (or via flags) for:
  - Bitbucket username  
  - Workspace/user (repo owner)  
  - Repository slug  
  - App password  
- Export commits into a neatly formatted Word document  
- Configurable number of commits to fetch  
- Modular design (`bitbucket_api.py`, `doc_writer.py`, `main.py`)  

---

## ⚙️ Prerequisites

- Bitbucket account
- App password (not your regular password)
- Repository access permissions

**How to create an App Password:**
1. Go to Bitbucket Settings → App passwords
2. Create a new app password with "Repositories: Read" permissions
3. Copy the generated password (you won't see it again)

---

## 📋 Requirements

- Python 3.7+
- requests
- python-docx

---

## 🚀 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/OmarZarifa/Bitbucket-Commit-Exporter.git
   cd Bitbucket-Commit-Exporter
   ```

2. **Create & activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

Run the tool:
```bash
python src/main.py
```

The tool will prompt you for:
- **Bitbucket username** - Your Bitbucket account username
- **Workspace/user** - The owner of the repository (workspace name or username)
- **Repository slug** - The repository name (e.g., "my-project" from "workspace/my-project")
- **App password** - Your Bitbucket app password (not your regular password)
- **Number of commits** - How many recent commits to fetch (default: 10)

### Example Output

The tool will create a `commits.docx` file containing:
- Commit hash
- Author name and email
- Commit date
- Commit message
- Files changed

---

## 📁 Project Structure

```
src/
├── main.py           # CLI entrypoint and user interaction
├── bitbucket_api.py  # Bitbucket API integration
└── doc_writer.py     # Word document generation
```

---

## 📄 License

MIT © Omar Zarifa
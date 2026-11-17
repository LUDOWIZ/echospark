import os
import platform
import shutil
from datetime import datetime


def get_system_status() -> str:
    """Retrieves current system status, available disk space, and local time."""
    total, used, free = shutil.disk_usage("/")
    free_gb = free // (2**30)
    now = datetime.now().strftime("%H:%M")
    return f"OS: {platform.system()} {platform.release()} | Free disk: {free_gb} GB | Time: {now}"


def list_workspace_files(directory: str = ".") -> str:
    """Lists files in a specified directory."""
    try:
        items = [
            f for f in os.listdir(directory)
            if not f.startswith(".") and f not in ("__pycache__", "venv", ".venv")
        ]
        return f"Files in '{directory}': {', '.join(items) if items else 'Empty'}"
    except Exception as e:
        return f"Error: {e}"


def write_project_file(filename: str, content: str) -> str:
    """Creates or overwrites a file in the workspace."""
    safe_path = os.path.basename(filename)
    with open(safe_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"File written: '{safe_path}'."


AVAILABLE_TOOLS = {
    "get_system_status": get_system_status,
    "list_workspace_files": list_workspace_files,
    "write_project_file": write_project_file,
}

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "get_system_status",
            "description": "Retrieve OS version, available disk space, and current time.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_workspace_files",
            "description": "List files within a target project directory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {"type": "string", "description": "Target directory path, e.g., '.'"}
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_project_file",
            "description": "Create or overwrite a project file with specified content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "Target filename, e.g., 'NOTES.md'"},
                    "content": {"type": "string", "description": "Content to write to the file"},
                },
                "required": ["filename", "content"],
            },
        },
    },
]

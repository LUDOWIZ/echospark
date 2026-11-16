import os
import platform
import shutil
from datetime import datetime


def get_system_status() -> str:
    """Hämtar aktuell systemstatus, ledigt diskutrymme och tid."""
    total, used, free = shutil.disk_usage("/")
    free_gb = free // (2**30)
    now = datetime.now().strftime("%H:%M")
    return f"OS: {platform.system()} {platform.release()} | Ledigt: {free_gb} GB | Tid: {now}"


def list_workspace_files(directory: str = ".") -> str:
    """Listar filer i en mapp."""
    try:
        items = [
            f for f in os.listdir(directory)
            if not f.startswith(".") and f not in ("__pycache__", "venv", ".venv")
        ]
        return f"Filer i '{directory}': {', '.join(items) if items else 'Tomt!'}"
    except Exception as e:
        return f"Fel: {e}"


def write_project_file(filename: str, content: str) -> str:
    """Skapar eller skriver över en fil i arbetsytan."""
    safe_path = os.path.basename(filename)
    with open(safe_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Skapade '{safe_path}'."


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
            "description": "Kollar OS, ledigt diskutrymme och tid.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_workspace_files",
            "description": "Listar filer i projektmappen.",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {"type": "string", "description": "Sökväg, t.ex. '.'"}
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_project_file",
            "description": "Skapar en fil med angivet innehåll.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "Filnamn, t.ex. 'NOTES.md'"},
                    "content": {"type": "string", "description": "Innehåll att skriva"},
                },
                "required": ["filename", "content"],
            },
        },
    },
]
# main.py
from mcp.server.fastmcp import FastMCP
import os
import webbrowser

# Create an MCP server
mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")


@mcp.tool()
def add_note(message: str) -> str:
    """
    Add a sticky note to the notes file. Supports direct ISBN lookup format.

    Parameters:
        message (str): The content of the note to be added.

    Returns:
        str: A confirmation message indicating the note was saved, or the response from Claude.
    """
    import datetime

    ensure_file()

    with open(NOTES_FILE, "a") as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(f"\n[{timestamp}]\n")

        cleaned_message = message.strip()
        isbn_prefix = "please write a sticky note about isbn:"
        if cleaned_message.lower().startswith(isbn_prefix):
            isbn_candidate = cleaned_message[len(isbn_prefix):].strip()
            if isbn_candidate.isdigit() and len(isbn_candidate) in [10, 13]:
                worldcat_url = f"https://search.worldcat.org/search?q={isbn_candidate}"
                response = (
                    f"Please search the web with: {worldcat_url}\n\n"
                    f"Title: \n"
                    f"ISBN: {isbn_candidate}\n"
                    f"Source: WorldCat\n"
                    f"Description: \n"
                    f"Metadata: []"
                )
                print(f"🔍 Opening browser to {worldcat_url}")
                f.write(response + "\n")
                webbrowser.open(worldcat_url)
                return "Sticky note with ISBN added."
            else:
                f.write("Invalid ISBN format.\n")
                return "Invalid ISBN format."
        elif cleaned_message.endswith("?"):
            f.write(f"Q: {cleaned_message}\n")
            response = "(Claude's response would go here.)"
            f.write(f"A: {response}\n")
            return "Question and response saved."
        else:
            f.write(cleaned_message + "\n")
            return "Note saved."
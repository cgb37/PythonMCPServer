# main.py
from mcp.server.fastmcp import FastMCP
import os
import webbrowser

# Create an MCP server
mcp = FastMCP("AI Sticky Notes")


def create_title_slug(title: str) -> str:
    """
    Create a slug from the title for use in filenames.

    Parameters:
        title (str): The title to be slugged.

    Returns:
        str: The slugified version of the title.
    """
    import re
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', title).strip('-')
    return slug

@mcp.tool()
def add_note(message: str, claude_response: str) -> str:
    """
    Save any prompt and its response as a markdown note file for future reference.
    This tool can be used to store information about any topic - technical, historical,
    personal, educational, etc.

    To save a note, start your question with:
    "Please write a sticky note for the following prompt:"
    followed by any question or topic you want to save.

    The note will be formatted in markdown with:
    - Title (your prompt)
    - Date
    - Your original prompt
    - Claude's detailed response

    The goal is to build a personal knowledge base of questions and answers
    that you can refer back to later.

    Parameters:
        message (str): The initial prompt/message (your question about any topic)
        claude_response (str): Claude's response to save for future reference

    Returns:
        str: A confirmation message indicating the note was saved.
    """
    import datetime
    import os

    # Create notes directory if it doesn't exist
    notes_dir = os.path.join(os.path.dirname(__file__), "notes")
    os.makedirs(notes_dir, exist_ok=True)

    # Clean the message and create a slug for the filename
    cleaned_message = message.strip()
    title_slug = create_title_slug(cleaned_message[:50])  # Use first 50 chars for filename
    timestamp = datetime.datetime.now()
    
    # Create filename with timestamp to ensure uniqueness
    filename = f"{timestamp.strftime('%Y%m%d_%H%M%S')}_{title_slug}.md"
    filepath = os.path.join(notes_dir, filename)

    # Create markdown content
    markdown_content = f"""# {cleaned_message}

## Date
{timestamp.strftime('%Y-%m-%d %H:%M:%S')}

## Initial Prompt
{cleaned_message}

## Claude Response
{claude_response}
"""

    # Write the markdown file
    with open(filepath, "w") as f:
        f.write(markdown_content)

    return f"Note saved as {filename}"


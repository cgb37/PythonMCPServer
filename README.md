# PythonMCPServer

## Requirements

**uv**
An extremely fast Python package and project manager, written in Rust.
- https://docs.astral.sh/uv/


```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

To enable shell autocompletion for uv commands

```shell
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
```


**MCP Python SDK**

- https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file



```shell
uv init .

uv add "mcp[cli]"


uv run mcp install main.py
```


**Example mcp tools**

```python
# Add an addition tool
@mcp.tool("add")
def add(a: int, b: int) -> int:
    """
    Add two numbers

    Parameters:
        a (int): The first number
        b (int): The second number

    Returns:
        int: The sum of the two numbers
    """
    print(f"🛠️ Tool 'add' invoked with a={a}, b={b}")
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```
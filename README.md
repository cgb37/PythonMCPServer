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

**To create a new project**

```shell
uv init .

uv venv

source .venv/bin/activate

uv add "mcp[cli]"

uv run mcp install main.py
```

**Install after cloning**

```shell
uv venv

source .venv/bin/activate

uv add "mcp[cli]"

uv run mcp install main.py
```


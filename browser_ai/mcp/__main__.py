"""Entry point for running MCP server as a module.

Usage:
    python -m browser_ai.mcp
"""

import asyncio

from browser_ai.mcp.server import main

if __name__ == '__main__':
	asyncio.run(main())

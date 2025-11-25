# MCP Servers Guide

Model Context Protocol (MCP) servers extend Droid capabilities.

## What is MCP?

MCP allows Droid to connect to external tools and services:
- Web search
- Documentation lookup
- Browser automation
- Custom integrations

## Recommended MCP Servers

### Tavily (Web Search)
Best for `/research` command.

**Capabilities**:
- Web search
- Content extraction
- News search

**Setup**:
```json
// ~/.factory/mcp.json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["-y", "@tavily/mcp-server"],
      "env": {
        "TAVILY_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Context7 (Documentation)
Official documentation lookup.

**Capabilities**:
- Framework docs
- Library references
- API documentation

### Playwright (Browser)
Browser automation and testing.

**Capabilities**:
- Web scraping
- UI testing
- Screenshot capture

**Setup**:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-playwright"]
    }
  }
}
```

## Configuration

### Location
MCP servers are configured in:
- `~/.factory/mcp.json` (global)
- `.factory/mcp.json` (project)

### Format
```json
{
  "mcpServers": {
    "server-name": {
      "command": "command-to-run",
      "args": ["arg1", "arg2"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```

## Managing Servers

### List Servers
In Droid CLI:
```
/mcp
```

### Add Server
Edit `~/.factory/mcp.json` and restart Droid.

### Remove Server
Delete the entry from `mcp.json` and restart.

## Integration with Commands

| Command | Benefits with MCP |
|---------|-------------------|
| `/research` | Tavily for web search |
| `/implement` | Context7 for docs |
| `/test` | Playwright for E2E |
| `/analyze` | Various for insights |

## Best Practices

1. **Only add what you need** - Each server uses resources
2. **Secure API keys** - Don't commit to git
3. **Restart after changes** - MCP loads on startup
4. **Check server status** - Use `/mcp` to verify

## Troubleshooting

### Server not connecting?
- Check command path
- Verify API keys
- Look at Droid logs

### Server errors?
- Update to latest version
- Check server documentation
- Restart Droid CLI

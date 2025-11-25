# Quick Start Guide

Get SuperDroid up and running in minutes.

## Prerequisites

- [Factory Droid CLI](https://docs.factory.ai) installed
- Terminal access

## Installation

### Option 1: Clone and Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/Frexxis/SuperDroid.git
cd SuperDroid

# Run installation script
./install.sh
```

### Option 2: Manual Installation

```bash
# Clone the repository
git clone https://github.com/Frexxis/SuperDroid.git
cd SuperDroid

# Copy commands to Factory
cp -r .factory/commands/* ~/.factory/commands/

# Copy droids to Factory
cp -r .factory/droids/* ~/.factory/droids/
```

## Post-Installation

1. **Restart Droid CLI** to load new commands

2. **Enable Custom Droids**:
   - Run `/settings` in Droid CLI
   - Find "Custom Droids" option
   - Enable it

3. **Verify Installation**:
   ```
   /help
   ```

## Your First Commands

### Try a slash command:
```
/research "how to implement JWT authentication"
```

### Use a droid:
```
Use the security-engineer droid to review my authentication code
```

### Get help:
```
/help implement
```

## Next Steps

- Read [Commands Guide](../user-guide/commands.md) for all 30 commands
- Read [Droids Guide](../user-guide/droids.md) for all 16 droids
- Copy `AGENTS.md` to your project for customization

## Troubleshooting

### Commands not appearing?
- Restart Droid CLI
- Check `~/.factory/commands/` has the files

### Droids not working?
- Enable custom droids in `/settings`
- Check `~/.factory/droids/` has the files

### Need more help?
- Open an issue: https://github.com/Frexxis/SuperDroid/issues

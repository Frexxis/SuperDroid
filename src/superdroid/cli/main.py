"""
SuperDroid CLI Main Entry Point

Provides command-line interface for SuperDroid operations.
"""

import sys
from pathlib import Path

import click

from superdroid import __version__


@click.group()
@click.version_option(version=__version__, prog_name="SuperDroid")
def main():
    """
    SuperDroid - AI-enhanced development framework for Factory Droid CLI

    30 slash commands, 20 specialized droids, 7 behavioral modes.
    Inspired by SuperClaude Framework.
    """
    pass


@main.command()
@click.option(
    "--target",
    default="~/.factory/commands/sd",
    help="Installation directory (default: ~/.factory/commands/sd)",
)
@click.option(
    "--force",
    is_flag=True,
    help="Force reinstall if commands already exist",
)
@click.option(
    "--list",
    "list_only",
    is_flag=True,
    help="List available commands without installing",
)
def install(target: str, force: bool, list_only: bool):
    """
    Install SuperDroid commands to Factory Droid CLI

    Installs all slash commands (/sd:research, /sd:implement, etc.) to your
    ~/.factory/commands/sd directory so you can use them as /sd:command in Droid CLI.

    Examples:
        superdroid install
        superdroid install --force
        superdroid install --list
    """
    from .install_commands import (
        install_commands,
        install_droids,
        install_modes,
        list_available_commands,
        list_installed_commands,
    )

    if list_only:
        available = list_available_commands()
        installed = list_installed_commands()

        click.echo("📋 Available Commands:")
        for cmd in sorted(available):
            status = "✅ installed" if cmd in installed else "⬜ not installed"
            click.echo(f"   /{cmd:20} {status}")

        click.echo(f"\nTotal: {len(available)} available, {len(installed)} installed")
        return

    target_path = Path(target).expanduser()

    click.echo(f"📦 Installing SuperDroid Framework to ~/.factory/...")
    click.echo()

    # Install commands
    success1, msg1 = install_commands(target_path=target_path, force=force)
    click.echo(msg1)

    # Install droids
    success2, msg2 = install_droids(force=force)
    click.echo(msg2)

    # Install modes
    success3, msg3 = install_modes(force=force)
    click.echo(msg3)

    if not (success1 and success2 and success3):
        sys.exit(1)

    click.echo()
    click.echo("✅ SuperDroid Framework installed successfully!")
    click.echo()
    click.echo("Next steps:")
    click.echo("  1. Restart Droid CLI to load new commands")
    click.echo("  2. Enable custom droids: /settings → Custom Droids → On")
    click.echo("  3. Try: /sd:help")


@main.command()
@click.option(
    "--verbose",
    is_flag=True,
    help="Show detailed diagnostic information",
)
def doctor(verbose: bool):
    """
    Check SuperDroid installation health

    Verifies:
        - Commands installed correctly
        - Droids installed correctly
        - Modes installed correctly
        - Factory CLI directory exists
    """
    from .doctor import run_doctor

    click.echo("🔍 SuperDroid Doctor\n")

    results = run_doctor(verbose=verbose)

    for check in results["checks"]:
        status_symbol = "✅" if check["passed"] else "❌"
        click.echo(f"{status_symbol} {check['name']}")

        if verbose and check.get("details"):
            for detail in check["details"]:
                click.echo(f"    {detail}")

    click.echo()
    total = len(results["checks"])
    passed = sum(1 for check in results["checks"] if check["passed"])

    if passed == total:
        click.echo("✅ SuperDroid is healthy!")
    else:
        click.echo(f"⚠️  {total - passed}/{total} checks failed")
        sys.exit(1)


@main.command()
@click.option(
    "--target",
    default="~/.factory/commands",
    help="Installation directory",
)
def update(target: str):
    """
    Update SuperDroid to latest version

    Re-installs all commands, droids, and modes.
    """
    from .install_commands import install_commands, install_droids, install_modes

    target_path = Path(target).expanduser()

    click.echo(f"🔄 Updating SuperDroid to version {__version__}...")
    click.echo()

    success1, msg1 = install_commands(target_path=target_path, force=True)
    click.echo(msg1)

    success2, msg2 = install_droids(force=True)
    click.echo(msg2)

    success3, msg3 = install_modes(force=True)
    click.echo(msg3)

    if not (success1 and success2 and success3):
        sys.exit(1)

    click.echo()
    click.echo("✅ SuperDroid updated successfully!")


@main.command()
def version():
    """Show SuperDroid version"""
    click.echo(f"SuperDroid version {__version__}")


@main.command()
def info():
    """Show SuperDroid framework information"""
    click.echo(f"""
🤖 SuperDroid Framework v{__version__}

Transform Factory Droid CLI into a structured development platform.

📊 Statistics:
   • 30 Slash Commands
   • 20 Specialized Droids
   • 7 Behavioral Modes

🔗 Links:
   • GitHub: https://github.com/Frexxis/SuperDroid
   • Inspired by: SuperClaude Framework

📦 Installation:
   superdroid install        Install all components
   superdroid doctor         Check installation health
   superdroid install --list List available commands
""")


if __name__ == "__main__":
    main()

"""
SuperDroid Command Installation

Installs slash commands, droids, and modes to Factory Droid CLI directories.
"""

import shutil
from pathlib import Path
from typing import Tuple, List, Set
import importlib.resources


def get_package_root() -> Path:
    """Get the root directory of the installed package."""
    import superdroid
    
    # First check: .factory inside the package (wheel install)
    package_dir = Path(superdroid.__file__).parent
    factory_in_package = package_dir / ".factory"
    if factory_in_package.exists():
        return package_dir
    
    # Second check: .factory in project root (dev install)
    project_root = package_dir.parent.parent
    factory_in_root = project_root / ".factory"
    if factory_in_root.exists():
        return project_root
    
    # Fallback: try to find .factory relative to this file
    current = Path(__file__).parent
    for _ in range(5):
        factory_path = current / ".factory"
        if factory_path.exists():
            return current
        current = current.parent
    
    raise FileNotFoundError("Could not find SuperDroid .factory directory")


def list_available_commands() -> List[str]:
    """List all available commands in the package."""
    try:
        package_root = get_package_root()
        commands_dir = package_root / ".factory" / "commands"
        if commands_dir.exists():
            return [f.stem for f in commands_dir.glob("*.md")]
    except:
        pass
    return []


def list_installed_commands() -> Set[str]:
    """List commands currently installed in Factory CLI."""
    factory_commands = Path.home() / ".factory" / "commands"
    if factory_commands.exists():
        return {f.stem for f in factory_commands.glob("*.md")}
    return set()


def install_commands(
    target_path: Path = None,
    force: bool = False
) -> Tuple[bool, str]:
    """
    Install SuperDroid commands to Factory CLI.
    
    Args:
        target_path: Directory to install commands (default: ~/.factory/commands)
        force: Overwrite existing commands
        
    Returns:
        Tuple of (success, message)
    """
    if target_path is None:
        target_path = Path.home() / ".factory" / "commands"
    
    target_path = Path(target_path).expanduser()
    target_path.mkdir(parents=True, exist_ok=True)
    
    try:
        package_root = get_package_root()
        source_dir = package_root / ".factory" / "commands"
        
        if not source_dir.exists():
            return False, f"❌ Source commands not found: {source_dir}"
        
        installed = 0
        skipped = 0
        
        for cmd_file in source_dir.glob("*.md"):
            dest_file = target_path / cmd_file.name
            
            if dest_file.exists() and not force:
                skipped += 1
                continue
            
            shutil.copy2(cmd_file, dest_file)
            installed += 1
        
        msg = f"✅ Commands: {installed} installed"
        if skipped > 0:
            msg += f", {skipped} skipped (use --force to overwrite)"
        
        return True, msg
        
    except Exception as e:
        return False, f"❌ Failed to install commands: {e}"


def install_droids(force: bool = False) -> Tuple[bool, str]:
    """
    Install SuperDroid droids to Factory CLI.
    
    Args:
        force: Overwrite existing droids
        
    Returns:
        Tuple of (success, message)
    """
    target_path = Path.home() / ".factory" / "droids"
    target_path.mkdir(parents=True, exist_ok=True)
    
    try:
        package_root = get_package_root()
        source_dir = package_root / ".factory" / "droids"
        
        if not source_dir.exists():
            return False, f"❌ Source droids not found: {source_dir}"
        
        installed = 0
        skipped = 0
        
        for droid_file in source_dir.glob("*.md"):
            dest_file = target_path / droid_file.name
            
            if dest_file.exists() and not force:
                skipped += 1
                continue
            
            shutil.copy2(droid_file, dest_file)
            installed += 1
        
        msg = f"✅ Droids: {installed} installed"
        if skipped > 0:
            msg += f", {skipped} skipped"
        
        return True, msg
        
    except Exception as e:
        return False, f"❌ Failed to install droids: {e}"


def install_modes(force: bool = False) -> Tuple[bool, str]:
    """
    Install SuperDroid modes to Factory CLI.
    
    Args:
        force: Overwrite existing modes
        
    Returns:
        Tuple of (success, message)
    """
    target_path = Path.home() / ".factory" / "modes"
    target_path.mkdir(parents=True, exist_ok=True)
    
    try:
        package_root = get_package_root()
        source_dir = package_root / ".factory" / "modes"
        
        if not source_dir.exists():
            return True, "ℹ️  Modes: source not found, skipping"
        
        installed = 0
        skipped = 0
        
        for mode_file in source_dir.glob("*.md"):
            dest_file = target_path / mode_file.name
            
            if dest_file.exists() and not force:
                skipped += 1
                continue
            
            shutil.copy2(mode_file, dest_file)
            installed += 1
        
        msg = f"✅ Modes: {installed} installed"
        if skipped > 0:
            msg += f", {skipped} skipped"
        
        return True, msg
        
    except Exception as e:
        return False, f"❌ Failed to install modes: {e}"

"""
SuperDroid Command Installation

Installs slash commands, droids, and modes to Factory Droid CLI directories.
"""

import shutil
import sys
from pathlib import Path
from typing import Tuple, List, Set, Optional

# Debug mode - set to True to see detailed path info
DEBUG = False


def debug_print(msg: str):
    """Print debug message if DEBUG is enabled."""
    if DEBUG:
        print(f"[DEBUG] {msg}")


def get_factory_source_dir() -> Optional[Path]:
    """
    Find the .factory directory in the installed package.
    Tries multiple methods to ensure cross-platform compatibility.
    """
    import superdroid
    
    # Method 1: Check inside package directory (wheel install)
    package_dir = Path(superdroid.__file__).parent
    factory_path = package_dir / ".factory"
    debug_print(f"Method 1 - Package dir: {package_dir}")
    debug_print(f"Method 1 - .factory exists: {factory_path.exists()}")
    if factory_path.exists():
        return factory_path
    
    # Method 2: Check site-packages structure
    # Sometimes installed as superdroid/.factory
    site_packages = package_dir.parent
    for possible in [
        site_packages / "superdroid" / ".factory",
        site_packages / ".factory",
    ]:
        debug_print(f"Method 2 - Checking: {possible}")
        if possible.exists():
            return possible
    
    # Method 3: Check relative to this file (dev install)
    current = Path(__file__).resolve().parent
    for _ in range(6):
        factory_path = current / ".factory"
        debug_print(f"Method 3 - Checking: {factory_path}")
        if factory_path.exists():
            return factory_path
        current = current.parent
    
    # Method 4: Try importlib.resources (Python 3.9+)
    try:
        if sys.version_info >= (3, 9):
            from importlib.resources import files
            pkg_files = files("superdroid")
            factory_path = Path(str(pkg_files)) / ".factory"
            debug_print(f"Method 4 - importlib.resources: {factory_path}")
            if factory_path.exists():
                return factory_path
    except Exception as e:
        debug_print(f"Method 4 failed: {e}")
    
    # Method 5: Search in sys.path
    for path in sys.path:
        for possible in [
            Path(path) / "superdroid" / ".factory",
            Path(path) / ".factory",
        ]:
            if possible.exists():
                debug_print(f"Method 5 - Found in sys.path: {possible}")
                return possible
    
    return None


def get_package_root() -> Path:
    """Get the .factory directory. Raises error with debug info if not found."""
    factory_dir = get_factory_source_dir()
    
    if factory_dir is None:
        import superdroid
        error_msg = f"""
❌ Could not find SuperDroid .factory directory!

Debug info:
  - Python version: {sys.version}
  - Package location: {Path(superdroid.__file__).parent}
  - This file: {Path(__file__)}
  - sys.path: {sys.path[:3]}...

Please report this issue at:
  https://github.com/Frexxis/SuperDroid/issues
"""
        raise FileNotFoundError(error_msg)
    
    # Return parent of .factory for backward compatibility
    return factory_dir.parent


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
        return {f.stem for f in factory_commands.glob("sd-*.md")}
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
    
    Installs to both:
    - ~/.factory/droids/ (global)
    - ./.factory/droids/ (project, if .factory exists)
    
    Args:
        force: Overwrite existing droids
        
    Returns:
        Tuple of (success, message)
    """
    # Target paths
    global_path = Path.home() / ".factory" / "droids"
    project_path = Path.cwd() / ".factory" / "droids"
    
    # Always install to global
    target_paths = [global_path]
    
    # Also install to project if .factory exists there
    if (Path.cwd() / ".factory").exists():
        target_paths.append(project_path)
    
    try:
        package_root = get_package_root()
        source_dir = package_root / ".factory" / "droids"
        
        if not source_dir.exists():
            return False, f"❌ Source droids not found: {source_dir}"
        
        total_installed = 0
        total_skipped = 0
        locations = []
        
        for target_path in target_paths:
            target_path.mkdir(parents=True, exist_ok=True)
            installed = 0
            skipped = 0
            
            for droid_file in source_dir.glob("*.md"):
                dest_file = target_path / droid_file.name
                
                if dest_file.exists() and not force:
                    skipped += 1
                    continue
                
                shutil.copy2(droid_file, dest_file)
                installed += 1
            
            total_installed += installed
            total_skipped += skipped
            if installed > 0:
                locations.append(str(target_path))
        
        msg = f"✅ Droids: {total_installed} installed"
        if total_skipped > 0:
            msg += f", {total_skipped} skipped"
        if len(locations) > 1:
            msg += f" (global + project)"
        
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

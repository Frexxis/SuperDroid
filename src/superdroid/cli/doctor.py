"""
SuperDroid Doctor

Health check for SuperDroid installation.
"""

from pathlib import Path
from typing import Dict, List, Any


def run_doctor(verbose: bool = False) -> Dict[str, Any]:
    """
    Run health checks for SuperDroid installation.
    
    Args:
        verbose: Include detailed information
        
    Returns:
        Dictionary with check results
    """
    checks = []
    
    # Check 1: Factory directory exists
    factory_dir = Path.home() / ".factory"
    check = {
        "name": "Factory CLI directory",
        "passed": factory_dir.exists(),
        "details": []
    }
    if verbose:
        check["details"].append(f"Path: {factory_dir}")
        check["details"].append(f"Exists: {factory_dir.exists()}")
    checks.append(check)
    
    # Check 2: Commands installed
    commands_dir = factory_dir / "commands" / "sd"
    command_count = len(list(commands_dir.glob("*.md"))) if commands_dir.exists() else 0
    check = {
        "name": f"Commands installed ({command_count}/30)",
        "passed": command_count >= 25,  # Allow some flexibility
        "details": []
    }
    if verbose:
        check["details"].append(f"Path: {commands_dir}")
        check["details"].append(f"Count: {command_count}")
        if command_count < 30:
            check["details"].append("Run 'superdroid install' to install missing commands")
    checks.append(check)
    
    # Check 3: Droids installed
    droids_dir = factory_dir / "droids"
    droid_count = len(list(droids_dir.glob("*.md"))) if droids_dir.exists() else 0
    check = {
        "name": f"Droids installed ({droid_count}/20)",
        "passed": droid_count >= 15,
        "details": []
    }
    if verbose:
        check["details"].append(f"Path: {droids_dir}")
        check["details"].append(f"Count: {droid_count}")
    checks.append(check)
    
    # Check 4: Modes installed
    modes_dir = factory_dir / "modes"
    mode_count = len(list(modes_dir.glob("*.md"))) if modes_dir.exists() else 0
    check = {
        "name": f"Modes installed ({mode_count}/7)",
        "passed": mode_count >= 5,
        "details": []
    }
    if verbose:
        check["details"].append(f"Path: {modes_dir}")
        check["details"].append(f"Count: {mode_count}")
    checks.append(check)
    
    # Check 5: Settings file exists
    settings_file = factory_dir / "settings.json"
    check = {
        "name": "Factory settings file",
        "passed": settings_file.exists(),
        "details": []
    }
    if verbose:
        check["details"].append(f"Path: {settings_file}")
        if not settings_file.exists():
            check["details"].append("Run 'droid' to create settings file")
    checks.append(check)
    
    # Check 6: Custom droids enabled (if settings exists)
    custom_droids_enabled = False
    if settings_file.exists():
        try:
            import json
            with open(settings_file) as f:
                settings = json.load(f)
                custom_droids_enabled = settings.get("enableCustomDroids", False)
        except:
            pass
    
    check = {
        "name": "Custom droids enabled",
        "passed": custom_droids_enabled,
        "details": []
    }
    if verbose:
        check["details"].append(f"Enabled: {custom_droids_enabled}")
        if not custom_droids_enabled:
            check["details"].append("Enable via /settings → Custom Droids → On")
    checks.append(check)
    
    return {"checks": checks}


def print_doctor_report(results: Dict[str, Any]):
    """Print a formatted doctor report."""
    print("🔍 SuperDroid Doctor\n")
    
    for check in results["checks"]:
        status = "✅" if check["passed"] else "❌"
        print(f"{status} {check['name']}")
        
        for detail in check.get("details", []):
            print(f"    {detail}")
    
    print()
    total = len(results["checks"])
    passed = sum(1 for c in results["checks"] if c["passed"])
    
    if passed == total:
        print("✅ SuperDroid is healthy!")
    else:
        print(f"⚠️  {total - passed}/{total} checks failed")

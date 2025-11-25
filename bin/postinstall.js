#!/usr/bin/env node

/**
 * SuperDroid Post-Install Script
 * 
 * Automatically installs commands, droids, and modes after npm install.
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const FACTORY_DIR = path.join(os.homedir(), '.factory');
const COMMANDS_DIR = path.join(FACTORY_DIR, 'commands');
const DROIDS_DIR = path.join(FACTORY_DIR, 'droids');
const MODES_DIR = path.join(FACTORY_DIR, 'modes');

const PACKAGE_ROOT = path.join(__dirname, '..');
const SOURCE_COMMANDS = path.join(PACKAGE_ROOT, '.factory', 'commands');
const SOURCE_DROIDS = path.join(PACKAGE_ROOT, '.factory', 'droids');
const SOURCE_MODES = path.join(PACKAGE_ROOT, '.factory', 'modes');

function ensureDir(dir) {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
}

function copyFiles(sourceDir, targetDir) {
    if (!fs.existsSync(sourceDir)) {
        return 0;
    }
    
    ensureDir(targetDir);
    
    let count = 0;
    const files = fs.readdirSync(sourceDir).filter(f => f.endsWith('.md'));
    
    for (const file of files) {
        const sourcePath = path.join(sourceDir, file);
        const targetPath = path.join(targetDir, file);
        
        // Don't overwrite existing files during postinstall
        if (!fs.existsSync(targetPath)) {
            fs.copyFileSync(sourcePath, targetPath);
            count++;
        }
    }
    
    return count;
}

console.log('\n🤖 SuperDroid Framework - Post-Install\n');

try {
    const cmdCount = copyFiles(SOURCE_COMMANDS, COMMANDS_DIR);
    const droidCount = copyFiles(SOURCE_DROIDS, DROIDS_DIR);
    const modeCount = copyFiles(SOURCE_MODES, MODES_DIR);
    
    console.log(`✅ Installed: ${cmdCount} commands, ${droidCount} droids, ${modeCount} modes`);
    console.log('\nNext steps:');
    console.log('  1. Restart Droid CLI');
    console.log('  2. Enable custom droids: /settings → Custom Droids → On');
    console.log('  3. Try: /sd-help\n');
} catch (err) {
    console.log('⚠️  Auto-install skipped. Run "superdroid install" manually.\n');
}

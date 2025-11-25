#!/usr/bin/env node

/**
 * SuperDroid CLI
 * 
 * AI-enhanced development framework for Factory Droid CLI.
 * 30 slash commands, 20 specialized droids, 7 behavioral modes.
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const VERSION = '1.0.2';
const FACTORY_DIR = path.join(os.homedir(), '.factory');
const COMMANDS_DIR = path.join(FACTORY_DIR, 'commands', 'sd');
const DROIDS_DIR = path.join(FACTORY_DIR, 'droids');
const MODES_DIR = path.join(FACTORY_DIR, 'modes');

// Get package root directory
const PACKAGE_ROOT = path.join(__dirname, '..');
const SOURCE_COMMANDS = path.join(PACKAGE_ROOT, '.factory', 'commands');
const SOURCE_DROIDS = path.join(PACKAGE_ROOT, '.factory', 'droids');
const SOURCE_MODES = path.join(PACKAGE_ROOT, '.factory', 'modes');

function ensureDir(dir) {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
}

function copyFiles(sourceDir, targetDir, force = false) {
    if (!fs.existsSync(sourceDir)) {
        return { installed: 0, skipped: 0, error: `Source not found: ${sourceDir}` };
    }
    
    ensureDir(targetDir);
    
    let installed = 0;
    let skipped = 0;
    
    const files = fs.readdirSync(sourceDir).filter(f => f.endsWith('.md'));
    
    for (const file of files) {
        const sourcePath = path.join(sourceDir, file);
        const targetPath = path.join(targetDir, file);
        
        if (fs.existsSync(targetPath) && !force) {
            skipped++;
            continue;
        }
        
        fs.copyFileSync(sourcePath, targetPath);
        installed++;
    }
    
    return { installed, skipped, error: null };
}

function install(force = false) {
    console.log('📦 Installing SuperDroid Framework...\n');
    
    // Install commands
    const cmdResult = copyFiles(SOURCE_COMMANDS, COMMANDS_DIR, force);
    if (cmdResult.error) {
        console.log(`❌ Commands: ${cmdResult.error}`);
    } else {
        let msg = `✅ Commands: ${cmdResult.installed} installed`;
        if (cmdResult.skipped > 0) msg += `, ${cmdResult.skipped} skipped`;
        console.log(msg);
    }
    
    // Install droids
    const droidResult = copyFiles(SOURCE_DROIDS, DROIDS_DIR, force);
    if (droidResult.error) {
        console.log(`❌ Droids: ${droidResult.error}`);
    } else {
        let msg = `✅ Droids: ${droidResult.installed} installed`;
        if (droidResult.skipped > 0) msg += `, ${droidResult.skipped} skipped`;
        console.log(msg);
    }
    
    // Install modes
    const modeResult = copyFiles(SOURCE_MODES, MODES_DIR, force);
    if (modeResult.error) {
        console.log(`ℹ️  Modes: ${modeResult.error}`);
    } else {
        let msg = `✅ Modes: ${modeResult.installed} installed`;
        if (modeResult.skipped > 0) msg += `, ${modeResult.skipped} skipped`;
        console.log(msg);
    }
    
    console.log('\n✅ SuperDroid Framework installed successfully!\n');
    console.log('Next steps:');
    console.log('  1. Restart Droid CLI to load new commands');
    console.log('  2. Enable custom droids: /settings → Custom Droids → On');
    console.log('  3. Try: /sd:help\n');
}

function list() {
    console.log('📋 Available Commands:\n');
    
    if (!fs.existsSync(SOURCE_COMMANDS)) {
        console.log('❌ Source commands not found');
        return;
    }
    
    const available = fs.readdirSync(SOURCE_COMMANDS)
        .filter(f => f.endsWith('.md'))
        .map(f => f.replace('.md', ''));
    
    const installed = fs.existsSync(COMMANDS_DIR) 
        ? new Set(fs.readdirSync(COMMANDS_DIR).filter(f => f.endsWith('.md')).map(f => f.replace('.md', '')))
        : new Set();
    
    for (const cmd of available.sort()) {
        const status = installed.has(cmd) ? '✅ installed' : '⬜ not installed';
        console.log(`   /${cmd.padEnd(20)} ${status}`);
    }
    
    console.log(`\nTotal: ${available.length} available, ${installed.size} installed`);
}

function doctor() {
    console.log('🔍 SuperDroid Doctor\n');
    
    let passed = 0;
    let failed = 0;
    
    // Check Factory directory
    if (fs.existsSync(FACTORY_DIR)) {
        console.log('✅ Factory CLI directory');
        passed++;
    } else {
        console.log('❌ Factory CLI directory not found');
        failed++;
    }
    
    // Check commands
    const cmdCount = fs.existsSync(COMMANDS_DIR) 
        ? fs.readdirSync(COMMANDS_DIR).filter(f => f.endsWith('.md')).length 
        : 0;
    if (cmdCount >= 25) {
        console.log(`✅ Commands installed (${cmdCount}/30)`);
        passed++;
    } else {
        console.log(`❌ Commands installed (${cmdCount}/30)`);
        failed++;
    }
    
    // Check droids
    const droidCount = fs.existsSync(DROIDS_DIR)
        ? fs.readdirSync(DROIDS_DIR).filter(f => f.endsWith('.md')).length
        : 0;
    if (droidCount >= 15) {
        console.log(`✅ Droids installed (${droidCount}/20)`);
        passed++;
    } else {
        console.log(`❌ Droids installed (${droidCount}/20)`);
        failed++;
    }
    
    // Check modes
    const modeCount = fs.existsSync(MODES_DIR)
        ? fs.readdirSync(MODES_DIR).filter(f => f.endsWith('.md')).length
        : 0;
    if (modeCount >= 5) {
        console.log(`✅ Modes installed (${modeCount}/7)`);
        passed++;
    } else {
        console.log(`❌ Modes installed (${modeCount}/7)`);
        failed++;
    }
    
    console.log();
    if (failed === 0) {
        console.log('✅ SuperDroid is healthy!');
    } else {
        console.log(`⚠️  ${failed}/${passed + failed} checks failed`);
    }
}

function showHelp() {
    console.log(`
🤖 SuperDroid CLI v${VERSION}

Usage: superdroid <command> [options]

Commands:
  install [--force]   Install commands, droids, and modes
  list                List available commands
  doctor              Check installation health
  update              Update to latest version (same as install --force)
  version             Show version
  help                Show this help message

Examples:
  superdroid install          Install SuperDroid Framework
  superdroid install --force  Force reinstall
  superdroid list             List all commands
  superdroid doctor           Health check

More info: https://github.com/Frexxis/SuperDroid
`);
}

function showVersion() {
    console.log(`SuperDroid version ${VERSION}`);
}

// Parse arguments
const args = process.argv.slice(2);
const command = args[0] || 'help';
const force = args.includes('--force') || args.includes('-f');

switch (command) {
    case 'install':
        install(force);
        break;
    case 'update':
        install(true);
        break;
    case 'list':
    case '--list':
        list();
        break;
    case 'doctor':
        doctor();
        break;
    case 'version':
    case '--version':
    case '-v':
        showVersion();
        break;
    case 'help':
    case '--help':
    case '-h':
    default:
        showHelp();
        break;
}

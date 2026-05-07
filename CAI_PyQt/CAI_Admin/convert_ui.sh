#!/bin/bash

# Get the absolute path of the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Define paths relative to the script's location
UI_DIR="$SCRIPT_DIR/UI"
OUT_DIR="$SCRIPT_DIR/App"

# Ensure the output directory exists
mkdir -p "$OUT_DIR"

echo "Running UI & Resource conversion..."
echo "Location: $SCRIPT_DIR"
echo "------------------------------------------------"

# 1. Convert .ui files from the UI folder
if [ -d "$UI_DIR" ]; then
    for ui_file in "$UI_DIR"/*.ui; do
        [ -e "$ui_file" ] || continue
        
        filename=$(basename "$ui_file" .ui)
        pyside6-uic "$ui_file" -o "$OUT_DIR/$filename.py"
        
        if [ $? -eq 0 ]; then
            echo "✅ UI Converted: UI/$filename.ui -> App/$filename.py"
        else
            echo "❌ UI Failed: $filename.ui"
        fi
    done
else
    echo "⚠️  Warning: UI directory not found at $UI_DIR"
fi

# 2. Convert resource.qrc from the script's location
QRC_FILE="$SCRIPT_DIR/resources.qrc"

if [ -f "$QRC_FILE" ]; then
    # Standard naming: resources.qrc becomes resources_rc.py
    pyside6-rcc "$QRC_FILE" -o "$SCRIPT_DIR/resources_rc.py"
    
    if [ $? -eq 0 ]; then
        echo "📦 QRC Compiled: resources.qrc -> App/resources_rc.py"
    else
        echo "❌ QRC Failed: resource.qrc"
    fi
else
    echo "ℹ️  No resource.qrc found in $SCRIPT_DIR"
fi

echo "------------------------------------------------"
echo "Done! All components are up to date."
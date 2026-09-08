#!/usr/bin/env bash
set -e

TRAINER_DIR="$1"
PYTHON="${2:-python3}"
SRC="$TRAINER_DIR/process.cpp"
BIN="$TRAINER_DIR/process"

# matplotlib is imported by common.py; force a headless backend so it does not
# try to open a window from inside the request handler
MPLBACKEND=Agg "$PYTHON" "$TRAINER_DIR/test.py"

if [ ! -x "$BIN" ] || [ "$SRC" -nt "$BIN" ]; then
	c++ -std=c++17 -O2 -o "$BIN" "$SRC"
fi

"$BIN" "$TRAINER_DIR"

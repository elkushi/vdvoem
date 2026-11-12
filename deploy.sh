#!/usr/bin/env bash
# Rebuild and publish to GitHub Pages.
# Uses the gh token over HTTPS: this machine's SSH key is not registered with
# GitHub, and a global insteadOf rewrites https -> ssh, so the URL is passed
# explicitly here rather than stored in the remote.
set -e
cd "$(dirname "$0")"
python3 build.py
git add -A
git commit -q -m "${1:-update}" || echo "nothing to commit"
git push "https://x-access-token:$(gh auth token)@github.com/elkushi/vdvoem.git" main:main
echo "→ https://elkushi.github.io/vdvoem/"

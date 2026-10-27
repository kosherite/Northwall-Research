#!/usr/bin/env bash
# Build _site/ and publish it to the gh-pages branch. Used by both workflows.
set -euo pipefail
python tools/build_site.py
cd _site
git init -q -b gh-pages
git config user.name "northwall-site-bot"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add -A
git commit -qm "Site build $(date -u +%Y-%m-%dT%H:%MZ)"
git push -fq "https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" gh-pages

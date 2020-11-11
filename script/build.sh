#!/bin/bash

# Exit if any statement returns a non-true return value.
set -e

# Go to the project's root directory.
cd "$(dirname "$0")/.."

script/bootstrap.sh

echo "==> Generating Keymaps..."
for pyfile in Keymaps/*.py; do
    exec "$pyfile" > "${pyfile%.py}"
done

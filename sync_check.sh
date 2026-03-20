#!/bin/bash
# Move to the project directory
cd ~/Documents/Project_l3adama || exit

# Check if there are any changes in the CSV files or others
if [[ -n $(git status --porcelain) ]]; then
    echo "Changes detected. Publishing..."
    # Load your aliases so the function is available
    source ~/.bash_aliases
    # Run the function we just made
    publish_dashboard
else
    echo "No changes. Skipping update."
fi

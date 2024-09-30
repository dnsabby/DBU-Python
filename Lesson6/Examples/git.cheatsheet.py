"""
Git and GitHub Cheat Sheet

This cheat sheet provides a quick reference to the most common Git commands and GitHub workflows.
It's formatted in Python using comment blocks for easy viewing in code editors like Visual Studio Code.

Table of Contents:
- Getting Started
- Configuration
- Creating Repositories
- Staging and Committing
- Branching and Merging
- Viewing History
- Undoing Changes
- Working with Remote Repositories
- GitHub Specific Commands
- Additional Tips
"""

# Getting Started
# ---------------

# Check Git version
# Command: git --version

# Initialize a new Git repository
# Command: git init

# Clone an existing repository
# Command: git clone <repository_url>

# Example:
# git clone https://github.com/username/repository.git

# Configuration
# -------------

# Set global username and email
# Command:
# git config --global user.name "Your Name"
# git config --global user.email "youremail@example.com"

# Check configuration settings
# Command: git config --list

# Creating Repositories
# ---------------------

# Create a new local repository
# Command: git init

# Add a remote repository
# Command: git remote add origin <repository_url>

# Example:
# git remote add origin https://github.com/username/repository.git

# Staging and Committing
# ----------------------

# Check the status of your files
# Command: git status

# Add files to the staging area
# Command:
# git add <file_name>           # Add a specific file
# git add .                     # Add all files in the current directory

# Commit changes with a message
# Command: git commit -m "Your commit message"

# Shortcut to add all changes and commit
# Command: git commit -am "Your commit message"
# Note: Only works for files already tracked by Git

# Branching and Merging
# ---------------------

# List all branches
# Command: git branch

# Create a new branch
# Command: git branch <branch_name>

# Switch to a branch
# Command: git checkout <branch_name>

# Create and switch to a new branch
# Command: git checkout -b <branch_name>

# Merge a branch into the current branch
# Command: git merge <branch_name>

# Delete a branch
# Command:
# git branch -d <branch_name>        # Delete a merged branch
# git branch -D <branch_name>        # Force delete an unmerged branch

# Viewing History
# ---------------

# View commit history
# Command: git log

# View a summary of the commit history
# Command: git log --oneline --graph --all

# Show changes between commits
# Command: git diff                 # Show unstaged changes
# git diff --staged                 # Show staged changes
# git diff <commit1> <commit2>      # Show changes between commits

# Undoing Changes
# ---------------

# Unstage a file
# Command: git reset HEAD <file_name>

# Revert changes in a file to the last commit
# Command: git checkout -- <file_name>

# Amend the last commit
# Command: git commit --amend -m "New commit message"

# Reset to a previous commit
# Command:
# git reset --soft <commit_hash>     # Keep changes staged
# git reset --mixed <commit_hash>    # Unstage changes (default)
# git reset --hard <commit_hash>     # Discard changes

# Working with Remote Repositories
# --------------------------------

# List remote repositories
# Command: git remote -v

# Fetch changes from the remote repository
# Command: git fetch

# Pull changes from the remote repository and merge
# Command: git pull

# Push changes to the remote repository
# Command: git push origin <branch_name>

# Push all branches to the remote repository
# Command: git push --all origin

# Remove a remote repository
# Command: git remote remove <remote_name>

# GitHub Specific Commands
# ------------------------

# Forking a Repository
# - Fork a repository using the GitHub web interface

# Creating a Pull Request
# - Push your branch to your forked repository
# - Go to GitHub and create a pull request from your branch

# Setting Upstream for a Forked Repository
# Command:
# git remote add upstream <original_repository_url>

# Example:
# git remote add upstream https://github.com/original_owner/repository.git

# Synchronizing Your Fork
# Fetch and merge changes from the upstream repository
# Commands:
# git fetch upstream
# git merge upstream/main       # If the main branch is named 'main'

# Alternatively, rebase your changes
# Commands:
# git fetch upstream
# git rebase upstream/main

# Additional Tips
# ---------------

# Viewing the commit history of a file
# Command: git log -- <file_name>

# Show who changed each line in a file
# Command: git blame <file_name>

# Stashing Changes
# Save uncommitted changes for later
# Command: git stash

# List stashed changes
# Command: git stash list

# Apply stashed changes
# Command: git stash apply

# Delete stashed changes
# Command: git stash drop

# Apply and delete stashed changes
# Command: git stash pop

# Ignoring Files
# Create a .gitignore file and add patterns of files to ignore

# Example .gitignore content:
# ---------------------------
# # Ignore all .log files
# *.log

# # Ignore node_modules directory
# node_modules/

# Aliases
# -------

# Set up Git command aliases
# Commands:
# git config --global alias.co checkout
# git config --global alias.br branch
# git config --global alias.ci commit
# git config --global alias.st status

# Now you can use:
# git co      # Instead of git checkout
# git br      # Instead of git branch
# git ci      # Instead of git commit
# git st      # Instead of git status

# Tagging
# -------

# Create a new tag
# Command: git tag <tag_name>

# Create an annotated tag
# Command: git tag -a <tag_name> -m "Tag message"

# List all tags
# Command: git tag

# Push tags to remote repository
# Command: git push origin --tags

# Deleting a tag
# Command:
# git tag -d <tag_name>             # Delete locally
# git push origin :refs/tags/<tag_name>   # Delete from remote

# Working with Submodules
# -----------------------

# Add a submodule
# Command: git submodule add <repository_url> <path>

# Initialize and update submodules
# Command:
# git submodule init
# git submodule update

# Clone a repository with submodules
# Command: git clone --recurse-submodules <repository_url>

# Git Log Formatting
# ------------------

# Pretty log with graph and branches
# Command:
# git log --oneline --decorate --graph --all

# Example Aliases for Pretty Log
# Command:
# git config --global alias.lg "log --color --graph --pretty=format:'%C(red)%h%C(reset) - %C(bold blue)%d%C(reset) %s %C(green)(%cr) %C(bold green)<%an>%C(reset)' --abbrev-commit"

# Now you can use:
# git lg

# Reset vs. Revert vs. Checkout
# -----------------------------

# git reset
# - Moves the branch pointer to a specified commit
# - Can modify the staging area and working directory depending on options (--soft, --mixed, --hard)

# git revert
# - Creates a new commit that undoes changes from a previous commit
# - Safe for public branches

# git checkout
# - Switches branches or restores working tree files

# Deleting Remote Branches
# ------------------------

# Delete a remote branch
# Command: git push origin --delete <branch_name>
# Alternative:
# Command: git push origin :<branch_name>

# Changing the Last Commit Message
# --------------------------------

# Amend the last commit message
# Command: git commit --amend -m "New commit message"

# Be cautious if the commit has been pushed to a remote repository

# Squashing Commits
# -----------------

# Interactive rebase to squash commits
# Command: git rebase -i HEAD~<number_of_commits>

# In the editor, change 'pick' to 'squash' for commits you want to squash

# Force push after rebasing (if necessary)
# Command: git push --force

# Be cautious when rewriting history, especially on shared branches

# Additional Resources
# --------------------

# Official Git Documentation: https://git-scm.com/doc
# GitHub Guides: https://guides.github.com/
# Pro Git Book: https://git-scm.com/book/en/v2

"""
End of Git and GitHub Cheat Sheet
"""
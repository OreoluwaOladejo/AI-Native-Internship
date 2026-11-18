# Week 8: Git, GitHub and Formal Collaboration

## Overview
This week I practised working the way professional teams do on GitHub: tracking a task with an issue, making changes on a separate branch, opening a pull request, getting a peer review, and merging.

## What's in This Folder
- `README.md`: this file
- `.gitignore`: tells Git which files to leave out of the repository
(The `.env` file is included in `.gitignore` because it may contain sensitive information such as API keys, database credentials, and secret configuration values. Excluding it helps prevent these secrets from being accidentally uploaded to GitHub.)
- `screenshots/`: evidence of the issue, pull request and review

## Workflow I Followed
1. **Issue:** I created an issue describing the task. [link to your issue]
2. **Branch:** I created the branch `docs/week-8-readme` so I didn't change `main` directly.
3. **Commits:** I committed my changes with clear messages,  `docs: add Week 8 README and gitignore`.
4. **Pull request:** I opened a pull request from my branch into `main`, linked to the issue. [link to your PR]
5. **Peer review:** [friend's GitHub username] reviewed the pull request and left a comment. [link to the comment]
6. **Merge:** After the review, I merged the pull request into `main`, which closed the issue.

## About the .gitignore
I added a `.gitignore` file so that these are never uploaded:
- `__pycache__/`: Python's automatically generated cache files
- `.env`: files that may hold private settings or keys
- `.vscode/`: my editor's personal settings

## Issue Link

[View Week 8 Issue](https://github.com/OreoluwaOladejo/AI-Native-Internship/issues/1)

## Commit Message Style
I used short, specific commit messages that clearly describe each change:
- `docs: add Week 8 README and gitignore`
- `docs: add pull request link to README`

## Peer Review

My pull request was reviewed by isagoch.
Feedback received:
The reviewer suggested including a brief explanation of why environment files should be excluded using `.gitignore`.
Response:
I updated the README to explain that `.env` files may contain sensitive information such as API keys and database credentials, which should not be exposed publicly.

## Evidence

## Evidence

- **GitHub Issue:** [View Issue #1](https://github.com/OreoluwaOladejo/AI-Native-Internship/issues/1)
- **Pull Request:** [View Pull Request #2](https://github.com/OreoluwaOladejo/AI-Native-Internship/pull/2)
- **Peer Reviewer:** [@isagoch](https://github.com/isagoch)

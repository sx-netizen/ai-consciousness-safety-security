# GitHub Setup — ACSS First Release

1. Sign in at https://github.com/new (or connect GitHub to ChatGPT for assisted repository work).
2. Repository owner: preferably a distinct ACSS organization when available; otherwise a temporary personal account repository, transferable later.
3. Repository name: `ai-consciousness-safety-security` (subject to availability).
4. Visibility: **Public**. Description: `Independent, open research on AI consciousness, agency, safety and security.`
5. Create an **empty** repository (do not initialize with auto README, license, or .gitignore if uploading this package by git).
6. Extract the ZIP and, in a terminal inside the `acss-research` folder, run:

```bash
git init
git branch -M main
git add .
git commit -m "Initialize ACSS independent research initiative"
git remote add origin https://github.com/OWNER/ai-consciousness-safety-security.git
git push -u origin main
```

Replace `OWNER` with the actual username or organization. If the repository is already initialized, follow its current merge/upload process instead of overwriting it.

**Before publication:** check the three founding principles, verify the preprint URL, decide future code/data/text licenses separately, and ensure no private drafts or identifying submission-review documents are included.

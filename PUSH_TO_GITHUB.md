# 🚀 How to Push This Project to GitHub

Follow these steps to upload your Mental Health Chatbot to GitHub.

## Prerequisites

- GitHub account ([Sign up here](https://github.com/join))
- Git installed ([Download here](https://git-scm.com/downloads))

---

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the **"+"** icon → **"New repository"**
3. Fill in the details:
   - **Repository name**: `mental-health-chatbot` (or your preferred name)
   - **Description**: "AI-powered mental health support chatbot built with Gradio and Hugging Face"
   - **Visibility**: Choose Public or Private
   - **DON'T** initialize with README (we already have one)
4. Click **"Create repository"**

---

## Step 2: Initialize Local Git Repository

Open Command Prompt/Terminal in your project folder:

```bash
cd c:\Users\Lenovo\Downloads\chatbot
```

Initialize Git:

```bash
git init
```

---

## Step 3: Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Step 4: Add Files to Git

```bash
# Add all files (except those in .gitignore)
git add .

# Check what will be committed
git status
```

**Important**: Make sure `.env` is NOT listed (it should be ignored)

---

## Step 5: Commit Changes

```bash
git commit -m "Initial commit: Mental Health Chatbot with Gradio and Hugging Face"
```

---

## Step 6: Connect to GitHub

Replace `yourusername` with your actual GitHub username:

```bash
git remote add origin https://github.com/yourusername/mental-health-chatbot.git
```

---

## Step 7: Push to GitHub

```bash
# For first push
git branch -M main
git push -u origin main
```

Enter your GitHub credentials when prompted.

---

## Step 8: Verify on GitHub

1. Go to your repository: `https://github.com/yourusername/mental-health-chatbot`
2. Verify all files are uploaded
3. Check that README.md is displaying properly
4. Verify `.env` is NOT uploaded (security!)

---

## 🎉 Done! Your Project is Live!

Now you can:
- ⭐ Add topics/tags to your repo (gradio, ai, mental-health, chatbot)
- 📝 Edit repository description and website
- 🔗 Share your project link
- 📊 Enable GitHub Pages (if desired)

---

## Making Updates Later

When you make changes:

```bash
# 1. Check what changed
git status

# 2. Add changes
git add .

# 3. Commit with a message
git commit -m "Description of what you changed"

# 4. Push to GitHub
git push
```

---

## Common Issues & Solutions

### Issue: `.env` file uploaded accidentally

```bash
# Remove from Git but keep locally
git rm --cached .env
git commit -m "Remove .env from tracking"
git push
```

Then add `.env` to `.gitignore` if not already there.

### Issue: Authentication failed

**Option A: Use Personal Access Token (Recommended)**
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` scope
3. Use token as password when pushing

**Option B: Use GitHub CLI**
```bash
# Install GitHub CLI first
gh auth login
```

### Issue: Push rejected

```bash
# Pull latest changes first
git pull origin main --rebase
git push
```

---

## Repository Enhancements

### Add Topics/Tags
1. Go to your repo on GitHub
2. Click ⚙️ next to "About"
3. Add topics: `ai`, `chatbot`, `mental-health`, `gradio`, `huggingface`, `python`

### Add Social Preview Image
1. Create a nice 1280x640px image
2. Settings → Social preview → Upload image

### Enable Discussions
- Settings → Features → Check "Discussions"

### Add Repository Website
- Settings → Website → Add: `https://yourusername.github.io/mental-health-chatbot`

---

## Next Steps

✅ Add a `CODE_OF_CONDUCT.md` (optional)  
✅ Create GitHub Issues for future features  
✅ Add a project board for tracking tasks  
✅ Set up GitHub Actions for CI/CD (optional)  
✅ Write a blog post about your project  
✅ Share on social media  

---

## Example Repository URL Structure

After pushing, your project will be available at:

```
https://github.com/yourusername/mental-health-chatbot
```

Clone URL for others:
```
https://github.com/yourusername/mental-health-chatbot.git
```

---

## Security Checklist Before Pushing

- [ ] `.env` is in `.gitignore`
- [ ] No API keys in code
- [ ] No passwords in files
- [ ] `.env.example` has placeholder values only
- [ ] Sensitive data removed from all files

---

**Your Mental Health Chatbot is now on GitHub! 🎊**

Share it with the community and help others! 💚

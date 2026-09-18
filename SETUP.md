# Setup Guide

This guide will help you set up the Mental Health Chatbot on your local machine.

## Prerequisites

- **Python 3.7+**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Hugging Face Account**: [Sign up](https://huggingface.co/join)

## Step-by-Step Setup

### 1. Get Your Hugging Face API Token

1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Click **"New token"**
3. Name it (e.g., "Mental Health Chatbot")
4. Select **"Read"** permission
5. Click **"Generate token"**
6. Copy the token (you'll need it in step 4)

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/mental-health-chatbot.git
cd mental-health-chatbot
```

### 3. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

**Option A: Create .env file manually**
```bash
# Create .env file
echo HF_TOKEN=your_token_here > .env
```

**Option B: Copy from example**
```bash
cp .env.example .env
# Then edit .env and add your token
```

Your `.env` file should look like:
```
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 6. Run the Application

**Windows Quick Start:**
```bash
run.bat
```

**Manual Start:**
```bash
python app.py
```

### 7. Access the Chatbot

Open your browser and go to:
```
http://127.0.0.1:7860
```

## Troubleshooting

### Issue: Python not found
```bash
# Windows: Add Python to PATH or use full path
C:\Python311\python.exe app.py

# macOS/Linux: Use python3
python3 app.py
```

### Issue: pip not found
```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
python3 -m pip install -r requirements.txt
```

### Issue: Permission denied
```bash
# macOS/Linux: Make sure venv is activated
chmod +x venv/bin/activate
source venv/bin/activate
```

### Issue: Module not found
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Issue: API Authentication Error
- Verify your HF_TOKEN in .env file
- Make sure token has "Read" permission
- Check for extra spaces in .env file

## Verification

Test if everything works:

1. ✅ Virtual environment activated
2. ✅ Dependencies installed
3. ✅ .env file created with valid token
4. ✅ Server starts without errors
5. ✅ Browser shows chatbot interface
6. ✅ Chatbot responds to messages

## Next Steps

- Customize system prompts in the UI
- Adjust parameters for better responses
- Read [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Check [README.md](README.md) for advanced features

## Getting Help

- Check [Issues](https://github.com/yourusername/mental-health-chatbot/issues)
- Read [FAQ section](#faq)
- Open a new issue with detailed information

## FAQ

**Q: Can I use this without internet?**
A: No, it requires internet to access Hugging Face API.

**Q: Is my data stored?**
A: No conversation data is stored by default.

**Q: Can I change the AI model?**
A: Yes, edit the model name in `app.py`.

**Q: How much does it cost?**
A: The Hugging Face Inference API has a free tier.

**Q: Can I deploy this online?**
A: Yes, see deployment options in README.md.

---

**Need more help? Open an issue!** 🚀

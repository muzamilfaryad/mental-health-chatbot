# ⚡ Quick Start Guide

Get your Mental Health Chatbot running in 5 minutes!

## For Windows Users

### 🎯 Super Quick Start

1. **Get Hugging Face Token**: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. **Edit `.env` file**: Add your token
   ```
   HF_TOKEN=your_token_here
   ```
3. **Double-click `run.bat`**
4. **Open browser**: http://127.0.0.1:7860

Done! 🎉

---

## For macOS/Linux Users

```bash
# 1. Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Create .env file
echo "HF_TOKEN=your_token_here" > .env

# 3. Run
python app.py

# 4. Open http://127.0.0.1:7860
```

---

## First Time Setup (Detailed)

### Step 1: Get Your Token
1. Sign up at [Hugging Face](https://huggingface.co/join)
2. Go to [Settings → Tokens](https://huggingface.co/settings/tokens)
3. Create new token with "Read" access
4. Copy the token

### Step 2: Configure
```bash
# Create .env file in project root
HF_TOKEN=hf_YourActualTokenHere
```

### Step 3: Install
```bash
# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Run
```bash
# Windows
python app.py

# macOS/Linux
python3 app.py
```

### Step 5: Use
Open: **http://127.0.0.1:7860**

---

## Example Questions to Try

- "I'm feeling stressed. What can I do?"
- "Give me tips for better sleep"
- "How do I build confidence?"
- "What are some mindfulness exercises?"

---

## Customization

In the web interface, adjust:
- **System Message**: Change bot personality
- **Temperature**: 0.1 (focused) to 4.0 (creative)
- **Max Tokens**: Response length (default: 512)
- **Top-p**: Response diversity (default: 0.95)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Python not found" | Install Python 3.7+ |
| "Module not found" | Run `pip install -r requirements.txt` |
| "API error" | Check HF_TOKEN in .env |
| "Connection error" | Check internet connection |

---

## Need More Help?

📖 Read [SETUP.md](SETUP.md) for detailed instructions  
🐛 Report issues on GitHub  
💬 Check [README.md](README.md) for full documentation

---

**Happy Chatting! 🧠💚**

# 🧠 Mental Health Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Gradio](https://img.shields.io/badge/Gradio-6.28.0-orange.svg)
![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**An AI-powered mental health support chatbot built with Gradio and Hugging Face's Qwen model.**

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## 📖 About

Mental Health Chatbot is an intelligent conversational AI designed to provide supportive, empathetic responses for mental health and wellness queries. Built using state-of-the-art language models, this chatbot offers:

- 💬 Real-time conversational support
- 🎯 Mental health guidance and coping strategies
- 🌟 Positive reinforcement and motivation
- 🔒 Privacy-focused local deployment

> **Disclaimer:** This chatbot is for informational purposes only and is not a replacement for professional mental health services. If you're experiencing a mental health crisis, please contact a licensed professional or emergency services.

---

## ✨ Features

- 🤖 **Advanced AI Model**: Powered by Qwen 2.5 (72B parameters) for intelligent conversations
- 🎨 **Beautiful UI**: Clean, intuitive Gradio interface
- ⚙️ **Customizable Parameters**: Adjust temperature, max tokens, and system prompts
- 🔄 **Streaming Responses**: Real-time message generation
- 📊 **Conversation History**: Maintains context throughout the chat
- 🌐 **Easy Deployment**: Simple setup with virtual environment
- 🔐 **Secure**: Environment-based API token management

---

## 🚀 Demo

![Chatbot Demo](https://via.placeholder.com/800x400/4A90E2/FFFFFF?text=Mental+Health+Chatbot+Demo)

### Example Interactions:

**User:** "Give me tips for building confidence"

**Bot:** Provides comprehensive, actionable advice including:
- Setting achievable goals
- Positive self-talk techniques
- Mindfulness practices
- Physical wellness tips
- And more...

---

## 🛠️ Tech Stack

- **Frontend**: [Gradio](https://gradio.app/) - Interactive web interface
- **AI Model**: [Qwen 2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) via Hugging Face Inference API
- **Backend**: Python 3.11+
- **Environment Management**: python-dotenv
- **Deployment**: Local server with optional cloud deployment

---

## 📋 Prerequisites

Before you begin, ensure you have:

- Python 3.7 or higher
- pip (Python package manager)
- A Hugging Face account and API token ([Get one here](https://huggingface.co/settings/tokens))

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mental-health-chatbot.git
cd mental-health-chatbot
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
HF_TOKEN=your_huggingface_token_here
```

Replace `your_huggingface_token_here` with your actual Hugging Face API token.

---

## 🎮 Usage

### Quick Start (Windows)

Simply double-click `run.bat` to start the chatbot automatically!

### Manual Start

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run the application
python app.py
```

### Access the Chatbot

Once running, open your browser and navigate to:

```
http://127.0.0.1:7860
```

### Customization Options

In the web interface, you can adjust:

- **System Message**: Define the chatbot's personality and behavior
- **Max Tokens**: Control response length (default: 512)
- **Temperature**: Adjust creativity (0.1-4.0, default: 0.7)
- **Top-p**: Control randomness (0.1-1.0, default: 0.95)

---

## 📁 Project Structure

```
mental-health-chatbot/
│
├── app.py                      # Main application file
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── .gitignore                 # Git ignore file
├── run.bat                     # Windows quick-start script
├── README.md                   # Project documentation
├── Mental_Health_FAQ.csv       # FAQ dataset (optional)
└── venv/                       # Virtual environment (auto-generated)
```

---

## 🔧 Configuration

### Changing the AI Model

Edit `app.py` to use a different Hugging Face model:

```python
client = InferenceClient("your-preferred-model", token=hf_token)
```

### Customizing System Prompts

Modify the default system message in `app.py`:

```python
gr.Textbox(value="Your custom system message here", label="System message")
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Ideas for Contribution:
- 🎨 Improve UI/UX design
- 📊 Add conversation analytics
- 🌍 Multi-language support
- 📱 Mobile responsiveness
- 🔊 Voice interaction features
- 📈 Sentiment analysis

---

## 🐛 Troubleshooting

### Common Issues:

**Problem**: `ModuleNotFoundError: No module named 'gradio'`
```bash
Solution: pip install -r requirements.txt
```

**Problem**: `BadRequestError: The requested model is not supported`
```bash
Solution: Check your HF_TOKEN in .env file and ensure you have API access
```

**Problem**: Chatbot returns error on input
```bash
Solution: Verify your internet connection and Hugging Face API status
```

---

## 📊 Dataset

The project includes `Mental_Health_FAQ.csv` with common mental health questions and answers. You can extend the chatbot's capabilities by integrating this dataset.

---

## 🔒 Privacy & Security

- ✅ All conversations happen through Hugging Face's secure API
- ✅ API tokens are stored securely in `.env` (not committed to Git)
- ✅ No conversation data is stored permanently by default
- ⚠️ For production use, implement proper data encryption and compliance measures

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the inference API
- [Gradio](https://gradio.app/) for the amazing UI framework
- [Qwen Team](https://huggingface.co/Qwen) for the powerful language model
- All contributors and supporters of this project

---

## 📞 Contact & Support

- 💬 Open an [Issue](https://github.com/yourusername/mental-health-chatbot/issues) for bug reports
- ⭐ Star this repo if you find it helpful!
- 🔗 Share with others who might benefit

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/mental-health-chatbot&type=Date)](https://star-history.com/#yourusername/mental-health-chatbot&Date)

---

<div align="center">

**Made with ❤️ for mental health awareness**

[⬆ Back to Top](#-mental-health-chatbot)

</div>

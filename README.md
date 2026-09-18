<div align="center">

# 🧠 Mental Health Chatbot

### AI-Powered Mental Health Support Assistant

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-6.28+-FF6F00?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app/)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Qwen%202.5-FFD21E?style=for-the-badge)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

<img src="https://raw.githubusercontent.com/muzamilfaryad/mental-health-chatbot/main/.github/demo.gif" alt="Demo" width="700"/>

*An intelligent conversational AI designed to provide supportive, empathetic responses for mental health and wellness queries.*

</div>

---

## 📖 About

Mental Health Chatbot is a compassionate AI assistant that offers mental health support and wellness guidance through natural conversations. Built with cutting-edge AI technology, it provides:

- 💬 Real-time conversational support
- 🎯 Evidence-based coping strategies
- 🌟 Positive reinforcement and motivation
- 🛡️ Private and secure interactions

> **⚠️ Important Disclaimer**  
> This chatbot is for informational and educational purposes only. It is not a substitute for professional mental health services, diagnosis, or treatment. If you're experiencing a mental health crisis, please contact a licensed healthcare provider or emergency services immediately.
>
> 🆘 **Crisis Resources:**
> - **National Suicide Prevention Lifeline (US):** 988
> - **Crisis Text Line:** Text HOME to 741741
> - **International Association for Suicide Prevention:** [https://www.iasp.info/resources/Crisis_Centres/](https://www.iasp.info/resources/Crisis_Centres/)

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🤖 Powered by Advanced AI
- Built on **Qwen 2.5-72B-Instruct** model
- Contextual understanding of conversations
- Empathetic and supportive responses
- Real-time streaming responses

</td>
<td width="50%">

### 🎨 User-Friendly Interface
- Clean, intuitive Gradio UI
- Mobile-responsive design
- Conversation history maintained
- Easy parameter customization

</td>
</tr>
<tr>
<td width="50%">

### ⚙️ Highly Customizable
- Adjustable response creativity
- Configurable token limits
- Custom system prompts
- Temperature and sampling controls

</td>
<td width="50%">

### 🔐 Privacy & Security
- Secure API token management
- Local deployment option
- No conversation logging
- Environment-based configuration

</td>
</tr>
</table>

---

## 🎬 Demo

### Example Conversations

<details>
<summary><b>💪 Building Confidence</b></summary>

**User:** "Give me tips for building confidence"

**Bot:** Provides comprehensive advice including:
- Setting achievable goals
- Practicing positive self-talk
- Facing fears gradually
- Celebrating small wins
- Physical wellness strategies
- And more actionable tips...

</details>

<details>
<summary><b>😰 Managing Stress</b></summary>

**User:** "I'm feeling stressed lately. What can I do?"

**Bot:** Offers practical coping strategies:
- Breathing exercises
- Time management techniques
- Mindfulness practices
- Physical activity recommendations
- Work-life balance tips

</details>

<details>
<summary><b>😴 Improving Sleep</b></summary>

**User:** "How can I improve my sleep quality?"

**Bot:** Suggests evidence-based sleep hygiene:
- Sleep schedule optimization
- Bedroom environment setup
- Pre-sleep routines
- Diet and exercise timing
- Screen time management

</details>

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.7+** - [Download](https://www.python.org/downloads/)
- **Hugging Face Account** - [Sign Up](https://huggingface.co/join) (Free)

### Installation

```bash
# Clone the repository
git clone https://github.com/muzamilfaryad/mental-health-chatbot.git
cd mental-health-chatbot

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your Hugging Face token
```

### Get Your Hugging Face Token

1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Click **"New token"**
3. Select **"Read"** permission
4. Copy the token and add it to `.env`:

```env
HF_TOKEN=hf_your_token_here
```

### Run the Application

```bash
python app.py
```

Open your browser and navigate to **http://127.0.0.1:7860**

**Windows Users:** Simply double-click `run.bat` for automatic setup and launch!

---

## 🎮 Usage

### Basic Configuration

Once the app is running, you can customize these parameters:

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| **System Message** | Define bot personality and behavior | Friendly & empathetic | Custom text |
| **Max Tokens** | Maximum response length | 512 | 1-2048 |
| **Temperature** | Response creativity (lower = focused, higher = creative) | 0.7 | 0.1-4.0 |
| **Top-p** | Response diversity control | 0.95 | 0.1-1.0 |

### Example Questions to Try

- "I'm feeling anxious about an upcoming presentation. How can I calm down?"
- "What are some effective mindfulness exercises for beginners?"
- "How do I maintain a healthy work-life balance?"
- "Can you suggest strategies for dealing with burnout?"
- "What are some ways to improve my self-esteem?"

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | [Gradio](https://gradio.app/) - Interactive web UI framework |
| **AI Model** | [Qwen 2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) - State-of-the-art LLM |
| **API** | [Hugging Face Inference API](https://huggingface.co/inference-api) |
| **Language** | Python 3.11+ |
| **Config Management** | python-dotenv |

---

## 📁 Project Structure

```
mental-health-chatbot/
├── 📄 app.py                    # Main application
├── 📄 requirements.txt          # Dependencies
├── 📄 .env.example             # Environment template
├── 📄 run.bat                   # Windows quick-start
├── 📄 README.md                 # Documentation
├── 📄 LICENSE                   # MIT License
├── 📄 CONTRIBUTING.md           # Contribution guidelines
├── 📊 Mental_Health_FAQ.csv     # FAQ dataset
└── 📁 venv/                     # Virtual environment
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

### Ideas for Contribution

- 🌍 Add multi-language support
- 📊 Implement conversation analytics
- 🎨 Create additional UI themes
- 🔊 Add voice interaction
- 📱 Improve mobile responsiveness
- 🧪 Add comprehensive testing

---

## 🐛 Troubleshooting

<details>
<summary><b>Module not found error</b></summary>

```bash
pip install --upgrade -r requirements.txt
```
</details>

<details>
<summary><b>API Authentication Error</b></summary>

- Verify `HF_TOKEN` in `.env` file
- Ensure token has "Read" permission
- Check for extra spaces or quotes in `.env`
</details>

<details>
<summary><b>Port already in use</b></summary>

Change the port in `app.py`:
```python
demo.launch(server_port=7861)  # Use different port
```
</details>

<details>
<summary><b>Slow responses</b></summary>

- Check internet connection
- Try reducing `max_tokens` to 256
- Lower `temperature` to 0.5 for faster processing
</details>

For more issues, check [open issues](https://github.com/muzamilfaryad/mental-health-chatbot/issues) or create a new one.

---

## 📊 Roadmap

- [ ] Multi-language support (Spanish, French, Arabic, etc.)
- [ ] Voice input/output capabilities
- [ ] Sentiment analysis integration
- [ ] Conversation export (PDF/CSV)
- [ ] Mobile app version
- [ ] Integration with mental health resources database
- [ ] Personalized user profiles
- [ ] Group chat support features

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) - For providing the Inference API and model hosting
- [Qwen Team](https://huggingface.co/Qwen) - For the powerful Qwen 2.5 language model
- [Gradio](https://gradio.app/) - For the amazing UI framework
- All contributors and mental health advocates supporting this project

---

## 📞 Support & Contact

- 💬 **Issues:** [GitHub Issues](https://github.com/muzamilfaryad/mental-health-chatbot/issues)
- 📧 **Email:** muzamilfaryad@gmail.com
- 🌟 **Star this repo** if you find it helpful!

---

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=muzamilfaryad/mental-health-chatbot&type=Date)](https://star-history.com/#muzamilfaryad/mental-health-chatbot&Date)

---

<div align="center">

### Made with ❤️ for Mental Health Awareness

**Remember:** It's okay to ask for help. You're not alone. 💚

[⬆ Back to Top](#-mental-health-chatbot)

</div>

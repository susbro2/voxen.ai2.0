# 🤖 Voxen2.0 AI Assistant

A conversational AI assistant built with Streamlit and Transformers, featuring a modern UI and intelligent responses.

## ✨ Features

- **AI Chat Interface**: Powered by GPT-2 for intelligent conversations
- **Modern UI**: Clean, responsive design with Streamlit
- **Sample Questions**: Quick access to common queries
- **Chat History**: Persistent conversation memory
- **Real-time Responses**: Fast AI-powered responses

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd voxen2
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   - Local: http://localhost:8501
   - Network: http://your-ip:8501

## 🌐 Deployment Options

### 1. Streamlit Cloud (Recommended - Free)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Deploy!

### 2. Heroku

1. **Create Procfile**
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Deploy**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### 3. Railway

1. **Connect GitHub repository**
2. **Auto-deploy on push**
3. **Get live URL**

### 4. Docker

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build and run**
   ```bash
   docker build -t voxen2 .
   docker run -p 8501:8501 voxen2
   ```

## 📁 Project Structure

```
voxen2/
├── app.py                 # Main Streamlit application
├── config/
│   └── settings.py        # Configuration settings
├── models/
│   ├── voxen_model.py     # AI model wrapper
│   └── chat_model.py      # Chat functionality
├── utils/
│   ├── math_utils.py      # Mathematical utilities
│   ├── text_processing.py # Text processing
│   └── visualization.py   # Visualization tools
├── ui/
│   └── components.py      # UI components
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit configuration
└── README.md             # This file
```

## ⚙️ Configuration

### Model Settings
Edit `config/settings.py` to change:
- AI model (GPT-2, DialoGPT, etc.)
- Response length
- Temperature
- UI theme

### Environment Variables
- `OPENAI_API_KEY`: For OpenAI models (optional)
- `HUGGINGFACE_TOKEN`: For Hugging Face models (optional)

## 🔧 Customization

### Change AI Model
```python
# In config/settings.py
MODEL_CONFIG = {
    "default_model": "gpt2",  # Change to any Hugging Face model
    "voxen_model": "gpt2",
    "max_length": 1000,
    "temperature": 0.7,
    "do_sample": True,
}
```

### Add New Features
1. Create new modules in `utils/`
2. Add UI components in `ui/components.py`
3. Update main app in `app.py`

## 📊 Performance

- **Model Size**: ~548MB (GPT-2)
- **Memory Usage**: ~2GB RAM
- **Response Time**: 1-3 seconds
- **Concurrent Users**: 10-50 (depending on deployment)

## 🛠️ Troubleshooting

### Common Issues

1. **Model loading slow**
   - Use smaller models (DialoGPT-small)
   - Check internet connection

2. **Memory errors**
   - Reduce model size
   - Use CPU instead of GPU

3. **Deployment issues**
   - Check requirements.txt
   - Verify Python version (3.8+)

## 📝 License

MIT License - feel free to use and modify!

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

- Create an issue on GitHub
- Check the documentation
- Review troubleshooting section

---

**Made with ❤️ using Streamlit and Transformers** 
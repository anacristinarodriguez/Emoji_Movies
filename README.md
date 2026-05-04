# Emoji Movies 🎬

An intelligent movie recommendation system that suggests films based on emoji inputs using AI and the OMDB API.

## Features

✨ **Emoji-Based Recommendations** - Get movie suggestions by simply entering emojis that describe the mood or genre you're looking for

🔐 **User Authentication** - Secure login and registration system with JWT token-based authentication

🤖 **AI-Powered** - Uses Groq's LLM API to interpret emoji inputs and generate creative movie recommendations

🎥 **Movie Information** - Integrates with OMDB API to fetch detailed movie information including plot, poster, and ratings

💾 **Preference Tracking** - Saves user preferences and recommendation history to a SQLite database

## Tech Stack

- **Backend**: FastAPI (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: JWT tokens with python-jose
- **AI/ML**: Groq API (llama-3.1-8b-instant model)
- **External APIs**: OMDB API for movie data
- **Frontend**: HTML, CSS, JavaScript
- **Server**: Uvicorn ASGI server

## Prerequisites

- Python 3.9+
- pip (Python package manager)
- API Keys:
  - [Groq API Key](https://console.groq.com) - for AI-powered recommendations
  - [OMDB API Key](http://www.omdbapi.com/apikey.aspx) - for movie data

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Emoji_Movies.git
   cd Emoji_Movies
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt --break-system-packages
   ```

3. **Create a `.env` file** in the project root:
   ```bash
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   echo "OMDB_API_KEY=your_omdb_api_key_here" >> .env
   echo "SECRET_KEY=your_secret_key_here" >> .env
   ```

   **Important**: 
   - Get your **GROQ_API_KEY** from [console.groq.com](https://console.groq.com)
   - Get your **OMDB_API_KEY** from [omdbapi.com](http://www.omdbapi.com/apikey.aspx) and activate it
   - Generate a random **SECRET_KEY** for JWT token signing

4. **Initialize the database** (if needed)
   ```bash
   python create_db.py
   ```

## Running the Application

1. **Start the development server**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the application**
   - Open your browser and go to: **http://localhost:8000**
   - You should see the login page

3. **Create an account and start getting recommendations!**

## Project Structure

```
Emoji_Movies/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app initialization
│   ├── models.py            # SQLAlchemy database models
│   ├── database.py          # Database configuration
│   ├── utils.py             # Utility functions
│   ├── routes/
│   │   ├── auth.py          # Authentication endpoints
│   │   └── recommend.py     # Movie recommendation endpoint
│   ├── schemas/
│   │   └── recommend.py     # Pydantic request/response schemas
│   ├── services/
│   │   └── groq.py          # Groq API integration
│   ├── static/
│   │   ├── index.html       # Login page
│   │   ├── watch.html       # Recommendation page
│   │   ├── login.js         # Login form logic
│   │   └── src/             # CSS and assets
│   └── __pycache__/
├── movies.db                # SQLite database
├── create_db.py             # Database initialization script
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not in repo)
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and receive JWT token

### Recommendations
- `POST /recommend/` - Get movie recommendation based on emojis
  - **Headers**: `Authorization: Bearer <token>`
  - **Body**: `{"emojis": "🎬🌙😢"}`
  - **Response**: Movie title, description, and poster image

## Usage Example

1. **Register/Login**: Create an account at http://localhost:8000
2. **Enter Emojis**: Go to the watch page and input emojis like:
   - 🎬🌙😢 → Movie about sadness at night
   - 🚀🌌⚡ → Sci-fi action movie
   - 😂🎉🎊 → Comedy party movie
3. **Get Recommendations**: The app will suggest a movie and show its details

## Troubleshooting

### "Invalid API Key" Error
- **For Groq**: Verify your API key is correct and active at https://console.groq.com
- **For OMDB**: Make sure to activate your key via the email link from omdbapi.com

### "Model decommissioned" Error
- Groq regularly updates available models. Check available models at: https://console.groq.com/docs/models
- Update the model name in `app/routes/recommend.py` and `app/services/groq.py`

### Database Errors
- Delete `movies.db` and run `python create_db.py` to reinitialize

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Paula Rodriguez - [@prodriguezdiaz](https://github.com/prodriguezdiaz)

## Acknowledgments

- [Groq](https://www.groq.com/) - For the fast LLM API
- [OMDB API](http://www.omdbapi.com/) - For movie data
- [FastAPI](https://fastapi.tiangolo.com/) - For the web framework

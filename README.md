# TrendLab

Project about trends and user interactions.

## Setup and run

### Python + pip

1. Create virtual environment
```cmd
python -m venv .venv
```

2. Activate venv
```cmd
./.venv/Scripts/Activate
```

3. Install dependencies
```cmd
pip install -r requirements.txt
```

4. Create environment variables
```cmd
cp .env.example .env
```

5. Edit environment variables (notepad, nano, vim)
```cmd
notepad .env
```

6. Run the app
```cmd
flask run
```

### UV

1. Create venv
```cmd
uv venv .venv
```

2. Create environment variables
```cmd
cp .env.example .env
```

3. Edit environment variables (notepad, nano, vim)
```cmd
notepad .env
```

4. Install dependencies
```cmd
uv sync
```

5. Run the app
```cmd
flask run --debug
```

## Config explanation

```.env
SECRET_KEY =            # String, used for security by flask to protect sessions
DATABASE_URL=           # URL String, must be "driver+another_driver:///path" or "driver+another_driver://host:port/database_name"
```

For more help - `flask --help`
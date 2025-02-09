FROM python:3.12.2

# Install system dependencies
RUN apt-get update && apt-get install -y \
    qtbase5-dev \
    qtchooser \
    qt5-qmake \
    qtbase5-dev-tools \
    build-essential \
    python3-dev \
    libgl1-mesa-glx \
    wget \
    unzip \
    xvfb \
    libglib2.0-0 \
    libnss3 \
    libxcb1-dev \
    libx11-xcb-dev \
    libxcb-icccm4-dev \
    libxcb-image0-dev \
    libxcb-keysyms1-dev \
    libxcb-randr0-dev \
    libxcb-render-util0-dev \
    libxcb-xinerama0-dev \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "fetch_tweets:app", "--reload"]

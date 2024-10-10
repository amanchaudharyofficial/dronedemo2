FROM python:3.10.12


#Working directory
WORKDIR /app


# Create a directory for logs
RUN mkdir -p /app/logs



COPY vosk-model-hi-0.22 /app/vosk-model-hi-0.22
COPY vosk-model-en-in-0.5 /app/vosk-model-en-in-0.5
COPY data.json /app/data.json

# Set permissions for the logs directory (optional)
RUN chmod 777 /app/logs

# Update package index and install required packages
RUN apt-get update \
    && apt-get install -y \
       libasound-dev \
       portaudio19-dev \
       libportaudio2 \
       libportaudiocpp0 \
       ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install numpy \
    && pip install vosk \
    && pip install pipwin \
    && pip install pyaudio \
    && pip install speechrecognition
RUN apt-get update \
    && apt-get install -y jackd


# Add your application files
ADD main.py .
ADD subMain.py .
ADD sender.py .
ADD reciever.py .
ADD logger.py .
ADD IndianEnglishModel.py .
ADD json_handler.py .
ADD constant_struct.py .


# Example: Print contents of a file inside 'folder_name' inside the container
RUN ls -l /
RUN pwd

# Set environment variable for real-time scheduling
ENV SCHED_FIFO_POLICY=true

# Define the command to run your application
#CMD ["jackd", "-d", "alsa", "-d", "hw:0", "-r", "44100"]
CMD ["python3", "main.py"]


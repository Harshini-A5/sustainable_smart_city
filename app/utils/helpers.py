import os
from datetime import datetime

def save_uploaded_file(uploaded_file, save_dir="uploads"):
    """
    Save an uploaded file to a local directory.

    Args:
        uploaded_file (UploadedFile): File uploaded from Streamlit
        save_dir (str): Directory to save files

    Returns:
        str: Full path to the saved file
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    file_path = os.path.join(save_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path


def log_event(event_type, message, log_file="logs/app.log"):
    """
    Log application events to a file with timestamps.

    Args:
        event_type (str): Type of event (e.g., "INFO", "ERROR")
        message (str): Description of the event
        log_file (str): Path to the log file
    """
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {event_type.upper()}: {message}\n"
    
    with open(log_file, "a") as f:
        f.write(log_line)

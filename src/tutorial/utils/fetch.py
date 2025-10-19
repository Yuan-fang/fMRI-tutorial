# src/utils/fetch.py
import re
import gdown
import zipfile
from pathlib import Path

def fetch_dataset(url: str, data_dir: Path, zip_name: str = "data.zip") -> Path:
    """
    Download and extract a dataset from a Google Drive link if not already present.

    Parameters
    ----------
    url : str
        The full Google Drive link (e.g. 
        "https://drive.google.com/file/d/1WTZWuMePRJ9VMIl67M7a5EHhJxBmX21O/view?usp=sharing")
    data_dir : Path
        Directory where the data should be stored.
    zip_name : str, optional
        Temporary filename for the downloaded ZIP file (default: "data.zip").

    Returns
    -------
    Path
        Path to the extracted data directory (data_dir / "data").
    """
    zip_path = data_dir / zip_name
    raw_dir = data_dir / "data"
    raw_dir.mkdir(parents=True, exist_ok=True)

    if any(raw_dir.iterdir()):
        print(f"Data already present: {raw_dir}")
        return raw_dir

    # Extract file ID from a full Google Drive link
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
    if not match:
        raise ValueError("Invalid Google Drive link format.")
    file_id = match.group(1)
    download_url = f"https://drive.google.com/uc?id={file_id}"

    try:
        print(f"Downloading from {download_url} ...")
        gdown.download(download_url, str(zip_path), quiet=False)
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(raw_dir)
        zip_path.unlink()  # remove zip after extraction
        print(f"Downloaded and extracted to {raw_dir}")
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        if zip_path.exists():
            zip_path.unlink()
        raise

    return raw_dir
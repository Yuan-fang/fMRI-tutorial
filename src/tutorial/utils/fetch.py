
from pathlib import Path
import urllib.request

def fetch_url(url: str, out_path: str):
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {url} -> {out}")
    urllib.request.urlretrieve(url, out)
    return str(out)

def fetch_gdrive(file_id: str, out_path: str):
    import gdown  # %pip -q install gdown in the notebook first
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    gdown.download(id=file_id, output=str(out), quiet=False)
    return str(out)

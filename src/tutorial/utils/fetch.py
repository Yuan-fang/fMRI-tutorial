# src/utils/fetch.py
import re
import shutil
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
        Path to the extracted data directory (data_dir).
    """
    zip_path = data_dir / zip_name

    try:
        # download the zip file
        print(f"Downloading from {url} ...")
        gdown.download(url, str(zip_path), quiet=False)
        
        # create a temporary extraction directory
        tmp_extract = data_dir / "_tmp_extract"
        tmp_extract.mkdir(exist_ok=True)

        # extract the zip file to the temporary directory
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(tmp_extract)

        # Move all extracted files to the data directory (flatten if there's a top-level folder)
        extracted_items = list(tmp_extract.iterdir())

        # right after extraction
        def _is_macos_junk(p: Path) -> bool:
             n = p.name
             return (
                  n == "__MACOSX" or
                  n == ".DS_Store" or
                  n.startswith("._")
                  )

        # filter out junk before inspecting / moving
        extracted_items = [p for p in tmp_extract.iterdir() if not _is_macos_junk(p)]

        if len(extracted_items) == 1 and extracted_items[0].is_dir():
            # If there's a single top-level folder, move its contents up
            for item in extracted_items[0].iterdir():
                shutil.move(str(item), str(data_dir))
        else:
            # Otherwise move everything directly
            for item in extracted_items:
                shutil.move(str(item), str(data_dir))
        
        # Cleanup
        shutil.rmtree(tmp_extract)

        zip_path.unlink()  # remove zip after extraction
        print(f"Downloaded and extracted to {data_dir}")
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        if zip_path.exists():
            zip_path.unlink()
        raise

    return data_dir

# fMRI Analysis in Colab — Minimal 6‑Session Course

A clean, lightweight template for teaching fMRI analysis with **Google Colab** — no local installs.  
Each session is a separate notebook with:
- a tiny **install cell** (per‑session, in Colab’s VM),
- a clear **example** section,
- **interactive practice** blocks (YOUR CODE HERE),
- an **outputs** cell for saving results.

> **How students run this**  
> 1) Click the **Open in Colab** badge next to a session.  
> 2) Do **File → Save a copy in Drive**.  
> 3) Run from top to bottom.  
> 4) Submit the Drive link or the `outputs/` artifacts.

## Sessions
- [Session 01 — Basics / GLM (template)](notebooks/session01.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USER/REPO/blob/main/notebooks/session01.ipynb)
- [Session 02 — Confounds & Design (template)](notebooks/session02.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USER/REPO/blob/main/notebooks/session02.ipynb)
- [Session 03 — Group GLM (template)](notebooks/session03.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USER/REPO/blob/main/notebooks/session03.ipynb)
- [Session 04 — Decoding / MVPA (template)](notebooks/session04.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USER/REPO/blob/main/notebooks/session04.ipynb)
- [Session 05 — Connectivity (template)](notebooks/session05.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USER/REPO/blob/main/notebooks/session05.ipynb)
- [Session 06 — RSA / Advanced (template)](notebooks/session06.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USER/REPO/blob/main/notebooks/session06.ipynb)

> Replace `USER/REPO` above after you upload to GitHub.

## Data hosting (recommended options)
- **OSF**: free, citable, good for folders.  
- **Hugging Face Datasets**: programmatic and versioned.  
- **Zenodo**: citable DOI for a release snapshot.  
- **Google Drive (public links)**: simplest; stable enough for class.

Put your data URLs in `data/urls.yml` and use the helper in `utils/fetch.py` to download.

## Minimal workflow for class
- Share **view-only** link to a session notebook (or the GitHub page with Colab badge).
- Students **Save a copy in Drive** and run the install cell once per session.
- During class, have students paste their **Drive links** into a roster (Sheet) or use Classroom.
- You open links and **comment inline** while they work.

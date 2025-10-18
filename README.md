
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
- [Session 01 — Basics / GLM (template)](notebooks/session01.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yuan-fang/fMRI-tutorial/blob/main/notebooks/session01_Data.ipynb)
- [Session 02 — Confounds & Design (template)](notebooks/session02.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yuan-fang/fMRI-tutorial/blob/main/notebooks/session02_Preprocessing.ipynb)
- [Session 03 — Group GLM (template)](notebooks/session03.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yuan-fang/fMRI-tutorial/blob/main/notebooks/session03_GLM.ipynb)
- [Session 04 — Decoding / MVPA (template)](notebooks/session04.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yuan-fang/fMRI-tutorial/blob/main/notebooks/session04_Group.ipynb)


## Data hosting 
- **Google Drive (public links)**

Put your data URLs in `data/urls.yml` and use the helper in `utils/fetch.py` to download.

## Minimal workflow for class
- Share **view-only** link to a session notebook (or the GitHub page with Colab badge).
- Students **Save a copy in Drive** and run the install cell once per session.
- During class, have students paste their **Drive links** into a roster (Sheet) or use Classroom.
- You open links and **comment inline** while they work.

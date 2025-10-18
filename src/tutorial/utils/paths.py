# src/utils/paths.py
from pathlib import Path
import glob
from bids import BIDSLayout

class PathManager:
    def __init__(self, BIDSlayout: BIDSLayout, deriv_base: str | Path, pipeline: str):
        """
        BIDSlayout: project layout
        deriv_base: root data output folder
        Pipeline: the type of analysis
        """
        self.L = BIDSlayout
        self.deriv_base = Path(deriv_base).resolve()
        self.pipeline = pipeline

    def create_path(self, src: str | Path, *, proc: str, suffix: str, extension=".nii.gz", datatype_hint=None):
        
        """
        Create a derivative path by inheriting entities from a raw BIDSlayout object.

        src: source file path from the raw BIDS dataset. e.g., func/sub-01_ses-01_task-rest_run-01_bold.nii.gz
        proc: processing label. e.g., "preproc", "smoothed"
        suffix: suffix for the output file. e.g., "bold", "T1w"
        extension: file extension. e.g., ".nii.gz", ".json"
        datatype_hint: if the source file is not in a raw datatype folder (e.g., func, anat), provide a hint here
        Returns: Path object

        """
        ent = self.L.parse_file_entities(str(src))
        sub = ent.get("subject"); ses = ent.get("session")
        task = ent.get("task"); run = ent.get("run")
        # pick datatype: prefer raw datatype, else hint, else func
        dt = ent.get("datatype") or datatype_hint or "func"

        out_dir = self.deriv_base / self.pipeline 

        if sub: out_dir /= f"sub-{sub}"
        if ses: out_dir /= f"ses-{ses}"
        out_dir /= dt
        out_dir.mkdir(parents=True, exist_ok=True)

        parts = []
        if sub:  parts.append(f"sub-{sub}")
        if ses:  parts.append(f"ses-{ses}")
        if task: parts.append(f"task-{task}")
        if run:  parts.append(f"run-{run}")
        if proc: parts.append(f"proc-{proc}")
        fname = "_".join(parts) + f"_{suffix}{extension}"
        return out_dir / fname

    def find_path(self, *, subject=None, session=None, task=None, run=None, proc=None, suffix=None, extension=None):
        """
        Quick keyword/glob finder.

        subject: subject label or glob pattern
        session: session label or glob pattern
        task: task label or glob pattern
        run: run number or glob pattern
        proc: processing label or glob pattern
        suffix: suffix or glob pattern
        extension: file extension or glob pattern
        Returns: list of Path objects

        """
        root = self.deriv_base / self.pipeline
        pats = [f"sub-*"]
        if session: pats.append(f"ses-{session}")
        # search both anat/func/etc
        candidates = []
        for dt in ("func","anat","dwi","fmap","perf"):
            p = root / "/".join(pats) / dt
            for matched_path in map(Path, glob.glob(str(p))):
                candidates.extend(matched_path.rglob("*"))
        hits = []
        for f in candidates:
            if not f.is_file(): continue
            ent = self.L.parse_file_entities(str(f))
            if subject and ent.get("subject") != str(subject):   continue
            if session and ent.get("session") != str(session):   continue
            if task and ent.get("task") != str(task):            continue
            if run and str(ent.get("run")) not in {str(run), f"{int(run):02d}"}: continue
            if proc and ent.get("proc") != str(proc):            continue
            if suffix and ent.get("suffix") != str(suffix):      continue
            if extension and ent.get("extension") != str(extension): continue
            hits.append(f)
        return sorted(hits)

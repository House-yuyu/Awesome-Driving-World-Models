#!/usr/bin/env python3
"""Generate paper tables and badges from data/papers.yaml; use --check to verify.

Only the PAPERS_START/PAPERS_END block and the two metadata badges are generated.
Unknown categories and duplicate papers fail validation instead of being omitted.
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Install with: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
START_MARKER = "<!-- PAPERS_START -->"
END_MARKER = "<!-- PAPERS_END -->"
CODE_STATUSES = {"released", "partial", "unreleased", "repository-only", "data-only"}
PUBLICATION_STATUSES = {"published", "accepted", "preprint"}
SECTIONS = [
    ("survey", "Surveys & Perspectives", 1,
     "Cross-domain world-model reviews.",
     ["Work","Paper","Focus","Venue","Resources"]),
    ("foundations", "Foundations & General World Models", 1,
     "Latent dynamics and general predictive world representation learning.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("interactive", "Interactive Worlds & Games", 1,
     "Controllable generated interactive environments and playable simulations.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("robotics", "Robotics & Embodied World Models", 1,
     "Robot-action-conditioned video, imagined state and model-based policies.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("medical", "Medical & Biological World Models", 1,
     "Patient, disease, imaging and cell-state forecasting or simulation.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("social", "Social & Multi-Agent World Models", 1,
     "Social-state transitions and related agent simulation systems.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("physics", "Physics, Weather & Scientific World Models", 1,
     "Learned physical and geophysical dynamical systems.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("video-spatial", "Video & Spatial World Models", 1,
     "Predictive and controllable representations of visual worlds.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("bench-general", "General World-Model Benchmarks", 1,
     "Evaluation across action fidelity, physical consistency and geometry.",
     ["Benchmark","Paper","Evaluation Focus","Venue","Resources"]),
    ("generative", "Driving: Generative & Explicit-State Models", 2,
     "RGB, LiDAR, occupancy and future-geometry driving worlds.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("latent", "Driving: Latent & Planning-Oriented Models", 2,
     "Future latent states and world-model-based driving plans.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("world-action", "Driving: World-Action & Action-Aligned Models", 2,
     "Driving models that couple predictive states to actions.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("jepa", "Driving: JEPA & Predictive Representations", 2,
     "Driving predictive representation and joint-embedding methods.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("vla-world", "Driving: World-Model-Enhanced VLA", 2,
     "Driving VLA using future world states or features.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("vla-general", "Driving: Selected General VLA (Context)", 2,
     "Related driving VLA references, not necessarily world models.",
     ["Model","Paper","Key Idea","Venue","Resources"]),
    ("benchmark", "Driving: Benchmarks & Simulation", 2,
     "Driving simulation and evaluation protocols.",
     ["Benchmark","Paper","Evaluation Focus","Venue","Resources"]),
]
CATEGORIES = {section[0] for section in SECTIONS}
PARENTS = {
    "generative": ("Autonomous Driving World Models", "Autonomous driving is one application of world models, including generation, latent prediction, world-action, JEPA, VLA and benchmarks."),
}


def valid_url(value):
    parsed = urlsplit(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def load_catalog(path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("papers"), list) or not data["papers"]:
        raise ValueError("Catalog must contain a non-empty papers list")
    if data.get("schema_version") != 2:
        raise ValueError("Expected schema_version: 2")
    date.fromisoformat(str(data["updated_date"]))
    seen_models, seen_titles, seen_links, seen_ids = set(), set(), set(), set()
    for paper in data["papers"]:
        for key in ("model", "title", "paper_url", "year", "venue", "category", "focus"):
            if not paper.get(key):
                raise ValueError(f"Missing {key}: {paper.get('model', '<unnamed>')}")
        if paper["category"] not in CATEGORIES:
            raise ValueError(f"Unknown category {paper['category']}: {paper['model']}")
        if type(paper["year"]) is not int or not 1900 <= paper["year"] <= 2100:
            raise ValueError(f"Invalid year: {paper['model']}")
        if paper.get("publication_status", "published") not in PUBLICATION_STATUSES:
            raise ValueError(f"Invalid publication_status: {paper['model']}")
        if paper.get("code_status", "released") not in CODE_STATUSES:
            raise ValueError(f"Invalid code_status: {paper['model']}")
        for key in ("published_date", "verified_date", "added_date"):
            if paper.get(key):
                date.fromisoformat(str(paper[key]))
        for key in ("paper_url", "code_url", "project_url", "publication_url"):
            if paper.get(key) and not valid_url(paper[key]):
                raise ValueError(f"Invalid {key}: {paper['model']}")
        for resource in paper.get("resources", []):
            if not resource.get("label") or not valid_url(resource.get("url", "")):
                raise ValueError(f"Invalid resource: {paper['model']}")
        for source in paper.get("sources", []):
            if not valid_url(source):
                raise ValueError(f"Invalid source: {paper['model']}")
        model = paper["model"].casefold()
        title = re.sub(r"\W+", "", paper["title"].casefold())
        link = paper["paper_url"].rstrip("/")
        arxiv_id = paper.get("arxiv_id", "")
        if arxiv_id and not re.fullmatch(r"\d{4}\.\d{4,5}", arxiv_id):
            raise ValueError(f"Invalid arxiv_id: {paper['model']}")
        if (model in seen_models or title in seen_titles or link in seen_links
                or (arxiv_id and arxiv_id in seen_ids)):
            raise ValueError(f"Duplicate paper: {paper['model']}")
        if "arxiv.org/abs/" in link and arxiv_id and not re.search(rf"/{re.escape(arxiv_id)}(?:v\d+)?$", link):
            raise ValueError(f"arxiv_id does not match paper_url: {paper['model']}")
        seen_models.add(model)
        seen_titles.add(title)
        seen_links.add(link)
        if arxiv_id:
            seen_ids.add(arxiv_id)
    return data


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def venue_cell(paper):
    text = f"{paper['venue']} {paper['year']}"
    if paper.get("publication_status") == "accepted":
        text += " (accepted)"
    if paper.get("publication_url"):
        return f"[{cell(text)}]({paper['publication_url']})"
    return cell(text)


def resource_cell(paper):
    links, seen_urls = [], set()

    def add(label, url, note=""):
        if url and url not in seen_urls:
            links.append(f"[{cell(label)}]({url}){note}")
            seen_urls.add(url)

    status = paper.get("code_status", "released")
    label = ("Data" if status == "data-only" else
             "Repository" if status in {"unreleased", "repository-only"} else "Code")
    note = " (code pending)" if status == "unreleased" else " (partial)" if status == "partial" else ""
    add(label, paper.get("code_url"), note)
    add("Project", paper.get("project_url"))
    for resource in paper.get("resources", []):
        add(resource["label"], resource["url"])
    return " · ".join(links) or "—"


def build_table(papers, headers):
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for paper in papers:
        row = [f"**{cell(paper['model'])}**", f"[{cell(paper['title'])}]({paper['paper_url']})",
               cell(paper["focus"]), venue_cell(paper), resource_cell(paper)]
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def generate_papers_section(papers):
    lines = [START_MARKER, ""]
    emitted = 0
    for category, heading, level, description, headers in SECTIONS:
        group = [p for p in papers if p["category"] == category]
        if not group:
            continue
        # Stable sorting retains YAML order when year and first-posted date tie.
        group.sort(key=lambda p: (p["year"], str(p.get("published_date", ""))), reverse=True)
        if category in PARENTS:
            parent, intro = PARENTS[category]
            lines.extend([f"# {parent}", "", intro, ""])
        lines.extend([f"{'#' * level} {heading}", "", description, "",
                      build_table(group, headers), "", "---", ""])
        emitted += len(group)
    if emitted != len(papers):
        raise ValueError("Not all catalog papers were rendered")
    lines = lines[:-2]
    lines.extend([END_MARKER, ""])
    return "\n".join(lines)


def render_readme(content, catalog):
    starts = list(re.finditer(rf"(?m)^{re.escape(START_MARKER)}$", content))
    ends = list(re.finditer(rf"(?m)^{re.escape(END_MARKER)}$", content))
    if len(starts) != 1 or len(ends) != 1 or starts[0].end() >= ends[0].start():
        raise ValueError("README must contain exactly one pair of paper markers")
    prefix = content[:starts[0].start()]
    suffix = content[ends[0].end():]
    result = prefix + generate_papers_section(catalog["papers"]) + "\n" + suffix.lstrip("\n")
    result, count = re.subn(r"https://img\.shields\.io/badge/papers-\d+-blue",
                           f"https://img.shields.io/badge/papers-{len(catalog['papers'])}-blue", result)
    if count != 1:
        raise ValueError("README must contain exactly one papers badge")
    updated = str(catalog["updated_date"]).replace("-", "--")
    result, count = re.subn(r"https://img\.shields\.io/badge/last%20updated-[\d-]+-brightgreen",
                           f"https://img.shields.io/badge/last%20updated-{updated}-brightgreen", result)
    if count != 1:
        raise ValueError("README must contain exactly one last-updated badge")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate metadata and fail if README needs regeneration")
    args = parser.parse_args(argv)
    try:
        catalog = load_catalog(ROOT / "data/papers.yaml")
        path = ROOT / "README.md"
        current = path.read_text(encoding="utf-8")
        expected = render_readme(current, catalog)
        if args.check:
            if current != expected:
                sys.exit("README.md is out of date. Run python scripts/generate_readme.py")
            print(f"Validated {len(catalog['papers'])} unique papers; README.md is up to date.")
        else:
            path.write_text(expected, encoding="utf-8")
            print(f"Generated {len(catalog['papers'])} papers across {len(CATEGORIES)} categories.")
    except (KeyError, TypeError, ValueError, OSError, yaml.YAMLError) as error:
        sys.exit(f"Error: {error}")


if __name__ == "__main__":
    main()


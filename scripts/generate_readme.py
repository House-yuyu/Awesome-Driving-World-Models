#!/usr/bin/env python3
"""
Generate README.md paper tables from data/papers.yaml.

Usage:
    python scripts/generate_readme.py

The script only updates the content between the markers:
    <!-- PAPERS_START -->
    <!-- PAPERS_END -->

All other content in README.md is preserved.
"""

import os
import sys

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
PAPERS_YAML = os.path.join(REPO_ROOT, "data", "papers.yaml")
README_MD = os.path.join(REPO_ROOT, "README.md")

# Markers
START_MARKER = "<!-- PAPERS_START -->"
END_MARKER = "<!-- PAPERS_END -->"

# Category order (top-level)
CATEGORY_ORDER = [
    "Surveys & Perspectives",
    "Driving World Models",
    "Representation Learning",
    "Related Work",
]

# Subcategory order per category
SUBCATEGORY_ORDER = {
    "Driving World Models": [
        "Generative World Models",
        "Latent / Predictive World Models",
        "World-Action Models",
    ],
    "Representation Learning": [
        "JEPA-based Methods",
    ],
    "Related Work": [
        "Embodied / Robotics World Models",
        "General Video World Models",
    ],
}

# Table column headers
TABLE_HEADERS = ["Model", "Title", "Focus", "Venue", "Resources"]


def load_papers(yaml_path):
    """Load and validate papers from YAML file."""
    if not os.path.exists(yaml_path):
        print(f"Error: {yaml_path} not found")
        sys.exit(1)

    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not data or "papers" not in data:
        print("Error: YAML file does not contain a 'papers' key")
        sys.exit(1)

    papers = data["papers"]
    print(f"Loaded {len(papers)} papers from {os.path.basename(yaml_path)}")

    # Basic validation
    required_fields = ["title", "year", "venue", "category", "focus"]
    for i, paper in enumerate(papers):
        for field in required_fields:
            if field not in paper or paper[field] is None:
                print(f"Warning: Paper #{i+1} missing required field '{field}'")
                if field == "focus":
                    paper[field] = ""
                elif field == "tags":
                    paper[field] = []

    return papers


def group_papers(papers):
    """Group papers by category and subcategory.

    Returns a dict like:
    {
        "Category 1": {
            "": [paper1, paper2],  # no subcategory
            "Subcategory A": [paper3],
        },
        ...
    }
    """
    grouped = {}

    for paper in papers:
        cat = paper.get("category", "Uncategorized")
        subcat = paper.get("subcategory", "") or ""

        if cat not in grouped:
            grouped[cat] = {}
        if subcat not in grouped[cat]:
            grouped[cat][subcat] = []

        grouped[cat][subcat].append(paper)

    # Sort each group by year descending, then preserve YAML order within same year
    for cat in grouped:
        for subcat in grouped[cat]:
            grouped[cat][subcat].sort(key=lambda p: -p.get("year", 0))

    return grouped


def format_venue_short(venue, year):
    """Format venue + year as short string like 'arXiv '26'."""
    year_short = str(year)[-2:] if year else "??"
    if venue and venue.lower() == "arxiv":
        return f"arXiv '{year_short}"
    elif venue:
        return f"{venue} '{year_short}"
    return f"'{year_short}"


def format_resources(paper):
    """Format resource links as a string."""
    links = []
    if paper.get("code_url"):
        links.append(f"[Code]({paper['code_url']})")
    if paper.get("project_url"):
        links.append(f"[Project]({paper['project_url']})")

    if links:
        return " ".join(links)
    return "—"


def format_title_cell(paper):
    """Format title cell: linked if paper_url exists, plain text otherwise."""
    title = paper.get("title", "Untitled")
    paper_url = paper.get("paper_url", "")
    if paper_url:
        return f"[{title}]({paper_url})"
    return title


def format_model_cell(paper):
    """Format model name cell (bold)."""
    model = paper.get("model", "")
    if model:
        return f"**{model}**"
    return "—"


def build_table(papers):
    """Build a markdown table from a list of papers."""
    lines = []

    # Header
    header = "| " + " | ".join(TABLE_HEADERS) + " |"
    lines.append(header)

    # Separator
    sep = "| " + " | ".join(["---"] * len(TABLE_HEADERS)) + " |"
    lines.append(sep)

    # Rows
    for paper in papers:
        model = format_model_cell(paper)
        title = format_title_cell(paper)
        focus = paper.get("focus", "—")
        venue = format_venue_short(paper.get("venue", ""), paper.get("year", ""))
        resources = format_resources(paper)

        row = f"| {model} | {title} | {focus} | {venue} | {resources} |"
        lines.append(row)

    return "\n".join(lines)


def generate_contents(grouped):
    """Generate the Contents section."""
    lines = []
    lines.append("## Contents")
    lines.append("")

    for cat in CATEGORY_ORDER:
        if cat not in grouped:
            continue
        anchor = cat.lower().replace(" ", "-").replace("&", "").replace("/", "-").replace("--", "-")
        lines.append(f"- [{cat}](#{anchor})")

        subcats = grouped[cat]
        subcat_order = SUBCATEGORY_ORDER.get(cat, [])
        for subcat in subcat_order:
            if subcat and subcat in subcats and subcats[subcat]:
                sub_anchor = subcat.lower().replace(" ", "-").replace("/", "-").replace("&", "").replace("--", "-")
                lines.append(f"  - [{subcat}](#{sub_anchor})")

    lines.append("")
    return "\n".join(lines)


def generate_papers_section(papers):
    """Generate the full papers section markdown."""
    grouped = group_papers(papers)

    lines = []
    lines.append(START_MARKER)
    lines.append("")

    # Contents
    lines.append(generate_contents(grouped))

    # Generate each category
    for cat in CATEGORY_ORDER:
        if cat not in grouped:
            continue

        subcats = grouped[cat]
        subcat_order = SUBCATEGORY_ORDER.get(cat, [])

        # Category heading
        lines.append(f"## {cat}")
        lines.append("")

        # Papers without subcategory
        if "" in subcats and subcats[""]:
            lines.append(build_table(subcats[""]))
            lines.append("")

        # Subcategories
        for subcat in subcat_order:
            if subcat not in subcats or not subcats[subcat]:
                continue

            lines.append(f"### {subcat}")
            lines.append("")
            lines.append(build_table(subcats[subcat]))
            lines.append("")

    lines.append(END_MARKER)
    lines.append("")

    return "\n".join(lines)


def update_readme(readme_path, new_section):
    """Replace the content between markers in README.md.

    The function matches from START_MARKER through END_MARKER plus any
    following blank lines, ensuring idempotent output across multiple runs.
    """
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found")
        sys.exit(1)

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    if START_MARKER not in content:
        print(f"Error: START_MARKER '{START_MARKER}' not found in README.md")
        sys.exit(1)
    if END_MARKER not in content:
        print(f"Error: END_MARKER '{END_MARKER}' not found in README.md")
        sys.exit(1)

    # Find start position (beginning of START_MARKER line)
    start_idx = content.index(START_MARKER)

    # Find end position: end of END_MARKER line, plus any trailing blank lines
    end_marker_start = content.index(END_MARKER)
    end_idx = end_marker_start + len(END_MARKER)

    # Consume trailing newlines after END_MARKER up to the next non-empty line
    # so repeated runs don't accumulate extra blank lines
    while end_idx < len(content) and content[end_idx] in ('\n', '\r'):
        end_idx += 1
    # Put back exactly one newline so the next section starts after a blank line
    if end_idx < len(content):
        end_idx -= 1  # leave one newline before next content

    # Replace section
    new_content = content[:start_idx] + new_section + content[end_idx:]

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("README.md updated successfully.")


def main():
    print("=" * 60)
    print("README Generator — Table Mode")
    print("=" * 60)
    print()

    # Load papers
    papers = load_papers(PAPERS_YAML)
    print()

    # Count by category
    grouped = group_papers(papers)
    print("Generating paper tables...")
    for cat in CATEGORY_ORDER:
        if cat not in grouped:
            continue
        total = sum(len(ps) for ps in grouped[cat].values())
        print(f"  {cat}: {total} papers")
    print()

    # Generate section
    papers_section = generate_papers_section(papers)

    # Update README
    update_readme(README_MD, papers_section)
    print()
    print("Done!")


if __name__ == "__main__":
    main()

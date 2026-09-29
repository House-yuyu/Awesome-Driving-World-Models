#!/usr/bin/env python3
"""
Generate README.md paper list from data/papers.yaml.

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
    print(f"Loaded {len(papers)} papers from {yaml_path}")

    # Basic validation
    required_fields = ["title", "year", "venue", "category", "tags", "summary"]
    for i, paper in enumerate(papers):
        for field in required_fields:
            if field not in paper or paper[field] is None:
                print(f"Warning: Paper #{i+1} missing required field '{field}'")
                if field == "tags":
                    paper[field] = []
                elif field == "summary":
                    paper[field] = ""

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


def format_paper_entry(paper):
    """Format a single paper entry as markdown."""
    title = paper.get("title", "Untitled")
    year = paper.get("year", "?")
    venue = paper.get("venue", "")
    paper_url = paper.get("paper_url", "")
    code_url = paper.get("code_url", "")
    project_url = paper.get("project_url", "")
    tags = paper.get("tags", [])
    summary = paper.get("summary", "")

    lines = []

    # Title line: **Title** — *Venue, Year*
    title_line = f"- **{title}**"
    if venue and year:
        title_line += f" — *{venue}, {year}*"
    elif year:
        title_line += f" — *{year}*"
    lines.append(title_line)

    # Links line: [Paper] [Code] [Project]
    links = []
    if paper_url:
        links.append(f"[Paper]({paper_url})")
    else:
        # If no paper URL, skip Paper link
        pass
    if code_url:
        links.append(f"[Code]({code_url})")
    if project_url:
        links.append(f"[Project]({project_url})")

    if links:
        lines.append("  " + " ".join(links))

    # Tags line
    if tags:
        tag_str = " ".join(f"`{tag}`" for tag in tags)
        lines.append("  " + tag_str)

    # Summary line
    if summary:
        lines.append("  " + summary)

    return "\n".join(lines)


def generate_papers_section(papers):
    """Generate the full papers section markdown."""
    grouped = group_papers(papers)

    lines = []
    lines.append(START_MARKER)
    lines.append("")

    # Generate Contents
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

    # Generate each category
    for cat in CATEGORY_ORDER:
        if cat not in grouped:
            continue

        subcats = grouped[cat]
        subcat_order = SUBCATEGORY_ORDER.get(cat, [])

        # Category heading
        lines.append(f"## {cat}")
        lines.append("")

        # Check if there are papers without subcategory
        if "" in subcats and subcats[""]:
            for paper in subcats[""]:
                lines.append(format_paper_entry(paper))
                lines.append("")

        # Subcategories
        for subcat in subcat_order:
            if subcat not in subcats or not subcats[subcat]:
                continue

            lines.append(f"### {subcat}")
            lines.append("")

            for paper in subcats[subcat]:
                lines.append(format_paper_entry(paper))
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

    print(f"README.md updated successfully.")


def main():
    print("=" * 60)
    print("README Generator for Awesome Autonomous Driving World Models")
    print("=" * 60)
    print()

    # Load papers
    papers = load_papers(PAPERS_YAML)
    print()

    # Generate section
    print("Generating papers section...")
    papers_section = generate_papers_section(papers)

    # Count papers per category
    grouped = group_papers(papers)
    for cat in CATEGORY_ORDER:
        if cat not in grouped:
            continue
        total = sum(len(papers) for papers in grouped[cat].values())
        print(f"  {cat}: {total} papers")

    subcat_counts = 0
    for cat in grouped:
        for subcat in grouped[cat]:
            if subcat:
                subcat_counts += len(grouped[cat][subcat])
    print()

    # Update README
    print("Updating README.md...")
    update_readme(README_MD, papers_section)
    print()

    print("Done!")


if __name__ == "__main__":
    main()

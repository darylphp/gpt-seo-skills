#!/usr/bin/env python3
"""Package checks for the AI Search Visibility Skill.

Reads files in this skill folder only. No network calls. Prints a JSON report
with a SHA-256 manifest of the runtime files and exits 1 if any check fails.
"""
from io import BytesIO
from pathlib import Path
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "ai-search-visibility"
STATUSES = [
    "Ready for review: Visibility plan",
    "Ready for review: Control decision",
    "Checks open: Provisional findings",
    "Urgent: Possible unintended exclusion",
    "Blocked: Confirm the scope",
    "Blocked: Supply the evidence",
]
CONTROL_LINES = [
    "Search generative AI control: Include, verified",
    "Search generative AI control: Exclude, verified",
    "Search generative AI control: Mixed by property, verified",
    "Search generative AI control: Not verified",
]
APPROVAL = "Report approval: Awaiting approval"
NO_CHANGE = "This report changes no setting, file or page, and promises no AI visibility, citation or traffic."
SOURCE_ID = r"(?:G-\d{3}|X-\d{2})"
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


# Frontmatter
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
front = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
check(front is not None, "SKILL.md: missing YAML frontmatter")
if front:
    keys = re.findall(r"^(\w+):", front[1], re.M)
    values = dict(re.findall(r"^(name|description): (.+)$", front[1], re.M))
    check(keys == ["name", "description"], "SKILL.md: frontmatter keys must be name and description only")
    check(values.get("name") == ROOT.name == NAME, "SKILL.md: name and folder must both be " + NAME)
    check(len(values.get("name", "")) <= 64, "SKILL.md: name over 64 characters")
    description = values.get("description", "")
    check(0 < len(description) <= 200, f"SKILL.md: description is {len(description)} characters (limit 200)")

# Runtime files
runtime = [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]
check(len(runtime) == 11, f"Expected SKILL.md and ten references, found {len(runtime)} files")

# Source register IDs
register = (ROOT / "references" / "source-register.md").read_text(encoding="utf-8")
registered = set(re.findall(r"^\| (" + SOURCE_ID + r") \|", register, re.M))
check(bool(registered), "Source register has no IDs")

for path in sorted(ROOT.rglob("*")):
    if path.suffix not in {".md", ".yaml", ".py"} or not path.is_file():
        continue
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    check("\u2014" not in text, f"Em dash: {rel}")
    check("\u2013" not in text, f"En dash: {rel}")
    if path.suffix != ".md":
        continue
    for link in re.findall(r"\[[^\]]+\]\(([^)\s]+)\)", text):
        if re.match(r"^[a-z]+:", link) or link.startswith("#"):
            continue
        target = (path.parent / link.split("#")[0]).resolve()
        check(target.exists(), f"Broken local link: {rel} -> {link}")
    for group in re.findall(r"\[(" + SOURCE_ID + r"(?:, " + SOURCE_ID + r")*)\]", text):
        for ident in group.split(", "):
            check(ident in registered, f"Unregistered source {ident} in {rel}")
    if path in runtime:
        check(not re.search(r"\bTODO\b|\[insert |\[needs confirmation\]|\[needs platform verification\]", text, re.I),
              f"Unfinished runtime instruction: {rel}")

# Statuses and fixed lines named in SKILL.md
for status in STATUSES:
    check(f"**{status}**" in skill, f"SKILL.md does not define status: {status}")
for line in [APPROVAL, NO_CHANGE, *CONTROL_LINES]:
    check(f"`{line}`" in skill, f"SKILL.md does not define line: {line}")

# Template and examples
template = (ROOT / "references" / "output-template.md").read_text(encoding="utf-8")
expected = re.findall(r"^## (\d+)\.", template, re.M)
check(expected == [str(n) for n in range(1, 11)], "Template must have sections 1 to 10 in order")
outputs = sorted((ROOT / "examples").glob("*output.md"))
check(len(outputs) == 3, f"Expected three example outputs, found {len(outputs)}")
for path in outputs:
    text = path.read_text(encoding="utf-8")
    name = path.name
    check(re.findall(r"^## (\d+)\.", text, re.M) == expected, f"Example section order: {name}")
    found = [s for s in STATUSES if re.search(r"^\*\*" + re.escape(s) + r"\*\*$", text, re.M)]
    check(len(found) == 1, f"Example needs exactly one status line: {name}")
    check(len(re.findall(r"^`Report approval: ", text, re.M)) == 1, f"Example approval line: {name}")
    check(len(re.findall(r"^`" + re.escape(NO_CHANGE) + r"`$", text, re.M)) == 1, f"Example no-change line: {name}")
    lines = re.findall(r"^`(Search generative AI control: [^`]+)`$", text, re.M)
    check(len(lines) == 1 and lines[0] in CONTROL_LINES, f"Example control line: {name}")

# Runtime archive layout, built in memory
archive = BytesIO()
with zipfile.ZipFile(archive, "w") as zipped:
    for path in runtime:
        zipped.writestr(f"{NAME}/" + path.relative_to(ROOT).as_posix(), path.read_bytes())
with zipfile.ZipFile(archive) as zipped:
    names = zipped.namelist()
    check(len(names) == len(runtime), "Runtime archive entry count")
    check(all(n.startswith(f"{NAME}/") and ".." not in n.split("/") for n in names), "Runtime archive layout")
    check(f"{NAME}/SKILL.md" in names, "Runtime archive entry point")

manifest = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in runtime}
print(json.dumps({"runtime_sha256": manifest, "errors": errors}, indent=2))
raise SystemExit(1 if errors else 0)

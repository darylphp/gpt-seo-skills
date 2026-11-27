#!/usr/bin/env python3
"""Package checks for the SEO Content Writing Skill.

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
NAME = "seo-content-writing"
DRAFT_STATUSES = [
    "Draft ready for review: C1 editorial pass",
    "Draft with writer queries: Owner answers needed",
    "Blocked: Return to B3",
    "Blocked: Return to B2",
]
PROFILE_STATUSES = [
    "Ready for review: Editorial profile",
    "Blocked: Supply voice sources",
]
DRAFT_HANDOFFS = [
    "QA handoff: Ready for C1 editorial pass",
    "QA handoff: After the writer queries are answered",
    "QA handoff: None, return to the brief",
    "QA handoff: None, return to the evidence",
]
PROFILE_HANDOFFS = [
    "Brief handoff: Profile ready for B3 once approved",
    "Brief handoff: None yet",
]
NO_CLEARANCE = "This output does not clear any content for publication."
# Example outputs and the template each one follows
EXAMPLES = {
    "ready-output.md": "draft",
    "blocked-brief-output.md": "draft",
    "profile-output.md": "profile",
}
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def sections(text):
    return re.findall(r"^## (\d+)\.", text, re.M)


# Frontmatter
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
front = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
check(front is not None, "SKILL.md: missing YAML frontmatter")
description = ""
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
check(len(runtime) == 9, f"Expected SKILL.md and eight references, found {len(runtime)} files")

# Source register IDs
register = (ROOT / "references" / "source-register.md").read_text(encoding="utf-8")
registered = set(re.findall(r"^\| (C\d{2}) \|", register, re.M))
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
    for group in re.findall(r"\[(C\d{2}(?:, C\d{2})*)\]", text):
        for ident in group.split(", "):
            check(ident in registered, f"Unregistered source {ident} in {rel}")
    if path in runtime:
        check(not re.search(r"\bTODO\b|\[insert |\[needs confirmation\]|\[needs platform verification\]", text, re.I),
              f"Unfinished runtime instruction: {rel}")

# Statuses and lines named in SKILL.md
for status in DRAFT_STATUSES + PROFILE_STATUSES:
    check(f"**{status}**" in skill, f"SKILL.md does not define status: {status}")
for handoff in DRAFT_HANDOFFS + PROFILE_HANDOFFS:
    check(f"`{handoff}`" in skill, f"SKILL.md does not define handoff: {handoff}")
check(f"`{NO_CLEARANCE}`" in skill, "SKILL.md does not define the no-clearance line")

# Templates and examples
templates = {
    "draft": sections((ROOT / "references" / "output-template.md").read_text(encoding="utf-8")),
    "profile": sections((ROOT / "references" / "profile-template.md").read_text(encoding="utf-8")),
}
check(templates["draft"] == [str(n) for n in range(1, 10)], "Draft template must have sections 1 to 9 in order")
check(templates["profile"] == [str(n) for n in range(1, 9)], "Profile template must have sections 1 to 8 in order")
outputs = sorted(p.name for p in (ROOT / "examples").glob("*output.md"))
check(outputs == sorted(EXAMPLES), f"Expected example outputs {sorted(EXAMPLES)}, found {outputs}")
for name, mode in EXAMPLES.items():
    path = ROOT / "examples" / name
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    statuses = DRAFT_STATUSES if mode == "draft" else PROFILE_STATUSES
    handoffs = DRAFT_HANDOFFS if mode == "draft" else PROFILE_HANDOFFS
    approval = "Draft approval: " if mode == "draft" else "Profile approval: "
    check(sections(text) == templates[mode], f"Example section order: {name}")
    found = [s for s in statuses if re.search(r"^\*\*" + re.escape(s) + r"\*\*$", text, re.M)]
    check(len(found) == 1, f"Example needs exactly one status line: {name}")
    check(len(re.findall(r"^`" + re.escape(approval), text, re.M)) == 1, f"Example approval line: {name}")
    check(len(re.findall(r"^`" + re.escape(NO_CLEARANCE) + r"`$", text, re.M)) == 1, f"Example no-clearance line: {name}")
    lines = re.findall(r"^`((?:QA|Brief) handoff: [^`]+)`$", text, re.M)
    check(len(lines) == 1 and lines[0] in handoffs, f"Example handoff line: {name}")

# Ready draft example: every claim marker in the draft is a permitted claim
ready = (ROOT / "examples" / "ready-output.md").read_text(encoding="utf-8")
fixture = (ROOT / "examples" / "ready-input.md").read_text(encoding="utf-8")
permitted = re.search(r"Permitted: (.+?)\. Do not use", fixture)
check(permitted is not None, "Ready input: permitted claim list not found")
draft = re.search(r"## 3\. Draft\n(.*?)\n## 4\.", ready, re.S)
check(draft is not None, "Ready output: section 3 not found")
if permitted and draft:
    allowed = set(re.findall(r"CL-\d{2}", permitted[1]))
    used = set(re.findall(r"CL-\d{2}", draft[1]))
    check(bool(used) and used <= allowed, f"Ready output uses claims outside the permitted list: {sorted(used - allowed)}")

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
print(json.dumps({"description_length": len(description), "runtime_sha256": manifest, "errors": errors}, indent=2))
raise SystemExit(1 if errors else 0)

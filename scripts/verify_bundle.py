"""Check the bundle without executing skill helpers or contacting services."""

import ast
import hashlib
import json
from pathlib import Path
import re
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    skills = root / "skills"
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    expected_names = {
        "adaptive-ui-workflow", "context7-mcp", "frontend-design-codex",
        "frontend-ui-standards", "guided-learning-tutor", "ui-ux-pro-max",
        "mew-spec", "writing-skills", "anthropic-skill-creator",
    }
    directories = {path.name for path in skills.iterdir() if path.is_dir()}
    errors = []
    if directories != expected_names or manifest["skill_count"] != 9:
        errors.append("Expected exactly nine skill directories")
    for name in sorted(expected_names):
        entry = skills / name / "SKILL.md"
        if not entry.is_file():
            errors.append(f"Missing entry {name}")
            continue
        text = entry.read_text(encoding="utf-8")
        metadata = re.match(r"\A---\r?\n(.*?)\r?\n---", text, re.S)
        if not metadata:
            errors.append(f"Missing frontmatter {name}")
            continue
        declared = re.search(r"(?m)^name:\s*([^\r\n]+)", metadata[1])
        if not declared or declared[1].strip().strip('"\'') != name:
            errors.append(f"Name mismatch {name}")
        if not re.search(r"(?m)^description:\s*\S", metadata[1]):
            errors.append(f"Missing description {name}")
    actual = set()
    for path in skills.rglob("*"):
        if path.is_symlink():
            errors.append(f"Unexpected symlink {path.relative_to(root)}")
            continue
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        relative = path.relative_to(root).as_posix()
        actual.add(relative)
        record = manifest["files"].get(relative)
        if not record or hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
            errors.append(f"Manifest mismatch {relative}")
        if path.suffix == ".py":
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=relative)
            except SyntaxError as error:
                errors.append(f"Python syntax error {relative}: {error}")
    for missing in set(manifest["files"]) - actual:
        errors.append(f"Manifest file missing {missing}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: 9 unique skills, {len(actual)} file hashes, Python syntax")
    return 0


if __name__ == "__main__":
    sys.exit(main())

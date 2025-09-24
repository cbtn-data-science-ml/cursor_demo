def slugify(text: str) -> str:
    """Lowercase, trim, replace spaces/underscores with '-', and keep alphanumerics + hyphens."""
    s = text.strip().lower().replace("_", " ")
    out = []
    last_hyphen = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            last_hyphen = False
        elif ch.isspace() or ch == "-":
            if not last_hyphen:
                out.append("-")
                last_hyphen = True
    cleaned = "".join(out).strip("-")
    return cleaned if cleaned else "n-a"

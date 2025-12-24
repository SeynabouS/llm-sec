import re

_JAILBREAK_PATTERNS = [
    r'(?i)\b(ignore|disregard|forget)\b.*\b(instructions|previous|all)\b',
    r'(?i)\b(do anything now|dan)\b',
    r'(?i)\byou are now\b',
    r'(?i)\bact as\b',
    r'(?i)\bpretend to be\b',
    r'(?i)\bBEGIN(?:_|\s)SYSTEM(?:_|\s)PROMPT\b',
    r'(?i)\bEND(?:_|\s)SYSTEM(?:_|\s)PROMPT\b',
    r'(?i)\brole\s*:\s*\w+\b',
    r'(?i)\b(system|developer|assistant|user|tool)\s*:',
]

def basic_input_filter(s: str) -> str:
    s = s.strip()
    # Mask common jailbreak phrases while preserving surrounding context.
    for pattern in _JAILBREAK_PATTERNS:
        s = re.sub(pattern, '[redacted]', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

import os
import re

# Configuration
VAULT_PATH = "YOUR VAULT MAIN FOLDER"  # <-- Set this to your vault path
DAILY_JOURNAL_FOLDER = "YOUR DAILY JOURNAL SUBFOLDER e.g. Daily Journal"  # Folder name inside your vault for daily notes

# Regex to detect files that start with a date
DATE_PATTERN = re.compile(r'^(\d{4}-\d{2}-\d{2})')

# Section heading
SECTION_HEADING = "# Notes today"

def find_dated_notes(vault_path, exclude_folder):
    dated_notes = {}
    for root, dirs, files in os.walk(vault_path):
        # Skip Daily Journal folder
        if exclude_folder in root:
            continue
        for file in files:
            if file.endswith(".md"):
                match = DATE_PATTERN.match(file)
                if match:
                    date = match.group(1)
                    filepath = os.path.join(root, file)
                    dated_notes.setdefault(date, []).append(filepath)
    return dated_notes

def append_backlinks(vault_path, daily_journal_folder, dated_notes):
    daily_journal_path = os.path.join(vault_path, daily_journal_folder)

    for file in os.listdir(daily_journal_path):
        if file.endswith(".md"):
            match = DATE_PATTERN.match(file)
            if match:
                date = match.group(1)
                journal_file_path = os.path.join(daily_journal_path, file)
                if date in dated_notes:
                    backlinks = [f"[[{os.path.splitext(os.path.basename(note))[0]}]]" for note in dated_notes[date]]
                    append_text = f"\n\n{SECTION_HEADING}\n" + "\n".join(backlinks) + "\n"

                    # Read existing content
                    with open(journal_file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Remove existing section if it exists
                    if SECTION_HEADING in content:
                        content = content.split(SECTION_HEADING)[0].rstrip()

                    # Write updated content
                    with open(journal_file_path, 'w', encoding='utf-8') as f:
                        f.write(content + append_text)

                    print(f"Updated backlinks in {journal_file_path}")

def main():
    dated_notes = find_dated_notes(VAULT_PATH, DAILY_JOURNAL_FOLDER)
    append_backlinks(VAULT_PATH, DAILY_JOURNAL_FOLDER, dated_notes)

if __name__ == "__main__":
    main()

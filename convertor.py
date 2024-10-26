import sys
import re

def extract_file_id(url):
  """Extracts the file ID from a Google Drive URL.

  Args:
    url: The Google Drive URL.

  Returns:
    The extracted file ID, or None if not found.
  """

  pattern = r"d/([^/]+)"
  match = re.findall(pattern, url)
  return match[0] if match else None

if __name__ == "__main__":
  # Check if at least one argument is provided (excluding the script name)
  if len(sys.argv) < 2:
    print("Usage: python file.py <URL>")
    sys.exit(1)

  url = sys.argv[1]
  file_id = extract_file_id(url)

  if file_id:
    print(f'{file_id}')
  else:
    print("Invalid Google Drive URL")

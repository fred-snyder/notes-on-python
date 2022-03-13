# airtable-to-markdown

Create a markdown file from Airtable base rows. In other words: convert JSON data to a Markdown blog-post.

Note: The code structure of this (old) project needs lots of improvements
- [ ] Finish this project using a more modular approach (e.g. classes)

```bash
# create a new virtual environment
python -m venv .venv
python3 -m venv .venv

# load the venv
source .venv/bin/activate

# install the dependencies
pip install -r requirements.txt
pip3 install -r requirements.txt

# copy .env_example to .env
# and edit and replace the API keys
mv .env_example .env

# IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# EXCLUDE .env from Git

```

## Todo's (old)

- [ ] Fix imports
- [ ] Validate Airtable data
  - publish_state value
  - verify airtable field names
- [ ] Compare JSON data with existing/previous JSON
  - only process changes/diffs (perhaps split the records?)
- [ ] Process JSON (extract_data_from_json.py)
  - [ ] Create folder if doesn't exist
  - [ ] Download images/attachments
  - [ ] Create a markdown file

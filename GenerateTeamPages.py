import os
import json
from jinja2 import Environment, FileSystemLoader

# Setup environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Create output folder
os.makedirs("TeamHTMLFiles", exist_ok=True)

# Folder with JSON data
data_folder = "TeamInformation"

# Loop through all JSON files in data folder
for filename in sorted(os.listdir(data_folder)):
    if filename.endswith(".json"):
        team_num = filename.replace("team", "").replace(".json", "")
        team_path = os.path.join(data_folder, filename)

        with open(team_path, "r", encoding="utf-8") as f:
            team_data = json.load(f)

        # Render HTML using the template
        rendered_html = template.render(**team_data)

        # Write to output
        output_filename = f"TeamHTMLFiles/team{int(team_num):02}.html"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(rendered_html)

        print(f"Generated {output_filename}")

import os
import json
from jinja2 import Environment, FileSystemLoader

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
team_template = env.get_template('template.html')
home_template = env.get_template('HomePageTemplate.html')  # NEW: for the homepage

# Create output folder
os.makedirs("TeamHTMLFiles", exist_ok=True)

# Folder with JSON data
data_folder = "TeamInformation"

# Store data for homepage
homepage_teams = []

# Generate individual team pages
for filename in sorted(os.listdir(data_folder)):
    if filename.endswith(".json"):
        team_num = filename.replace("team", "").replace(".json", "")
        team_path = os.path.join(data_folder, filename)

        with open(team_path, "r", encoding="utf-8") as f:
            team_data = json.load(f)

        # Render individual team HTML
        rendered_html = team_template.render(**team_data)

        output_filename = f"TeamHTMLFiles/team{int(team_num):02}.html"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(rendered_html)

        print(f"Generated {output_filename}")

        # Collect info for homepage
        homepage_teams.append({
            "Team_Name": team_data["Team_Name"],
            "Team_Number": team_data["Team_Number"],
            "Prototype_Image": f"./TeamPrototypes/{team_data['Team_Number']}.png",
            "Page_Link": f"./TeamHTMLFiles/team{int(team_num):02}.html"
        })

# Render homepage
homepage_html = home_template.render(teams=homepage_teams)
with open("HomePage.html", "w", encoding="utf-8") as f:
    f.write(homepage_html)

print("Generated HomePage.html")

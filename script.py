import csv
import json

def csv_to_json(csv_filename, json_filename):
  """
  Reads a CSV file and creates a JSON file in the given format.

  Args:
    csv_filename: The name of the CSV file.
    json_filename: The name of the JSON file to create.
  """

  data = []
  with open(csv_filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    i = 0
    for row in reader:
      # Extract data from each row
      i = i+1
      id = i  # Assuming Timestamp is in DD/MM/YYYY format
      name = row['Name']
      pic = row['Photo (1:1 aspect ratio)']
      linkedin = row['Linkedin link']
      insta = row['Instagram link']
      desc = row['Quirky one liner about yourself']
      desig = ""  # Add an empty string for designation

      # Create a dictionary with the extracted data
      data.append({
          "id": id,
          "name": name,
          "pic": pic,
          "linkedin": linkedin,
          "insta": insta,
          "desc": desc,
          "desig": desig
      })

  # Write the data to a JSON file
  with open(json_filename, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

# Replace 'your_csv_file.csv' and 'your_json_file.json' with the actual file names
csv_to_json('team.csv', 'team_data.json')

print("CSV to JSON conversion complete!")

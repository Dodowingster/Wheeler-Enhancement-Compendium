import os
import json
import html

def generate_json(directory, output_file):
    data = []

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check for gif or png files
            if file.endswith(('.gif', '.png')):
                # Extract class name dynamically from the folder name
                class_name = os.path.basename(root)

                # Determine the type of file
                file_extension = file.split('.')[-1].lower()
                if file_extension == "gif":
                    file_type = "gif"
                elif file_extension == "png":
                    file_type = "png"
                else:
                    file_type = "unknown"

                # Validate that the folder name matches the file type
                if class_name.lower() == "gifs" and file_extension != "gif":
                    print(f"Warning: File '{file}' in folder '{class_name}' does not match the folder type.")
                    continue  # Skip this file if it doesn't match
                elif class_name.lower() == "images" and file_extension != "png":
                    print(f"Warning: File '{file}' in folder '{class_name}' does not match the folder type.")
                    continue  # Skip this file if it doesn't match

                # Extract prefix from GIF filenames
                reskin_prefix = None
                reskin_path = None
                if file_extension == "gif" and "_Wheeler" in file:
                    reskin_prefix = file.split('_Wheeler')[0]
                    # Construct the Reskin folder path with "Reskin" appended
                    reskin_path = os.path.join("Reskins", f"{reskin_prefix} Reskin\\SKSE\\Plugins\\wheeler\\resources\\icons")

                # Add the entry to the data list
                entry = {
                    "class": class_name,
                    file_type: os.path.join(root, file)
                }
                if reskin_prefix:
                    entry["Reskin"] = reskin_prefix
                    entry["ReskinPath"] = reskin_path  # Add the Reskin folder path

                data.append(entry)

    # Write the data to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def generate_html(template_file, json_file, output_file):
    # Read the template HTML
    with open(template_file, 'r', encoding='utf-8') as file:
        template_html = file.read()

    # Read the JSON data
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Group entries by class (e.g., "Gifs" or "Images")
    grouped_data = {}
    for item in data:
        class_name = item["class"]
        if class_name not in grouped_data:
            grouped_data[class_name] = []
        grouped_data[class_name].append(item)

    # Generate HTML entries
    html_entries = ""
    for class_name, items in grouped_data.items():
        # Add a section header for each class
        html_entries += f'<h2 class="mt-5 mb-3">{html.escape(class_name)}</h2><div class="row g-4">'

        for item in items:
            # Generate HTML for GIFs
            if class_name.lower() == "gifs":
                # Find the corresponding image for the GIF
                corresponding_image = next(
                    (img for img in grouped_data.get("Images", []) if item.get("Reskin", "").lower() in img["png"].lower()),
                    None
                )

                # Add the GIF and its corresponding image
                html_entries += f"""
                <div class="col-md-6">
                    <div class="card">
                        <img src="{item['gif']}" class="card-img-top half-resolution" alt="{html.escape(item.get('Reskin', 'GIF'))}">
                        <div class="card-body">
                            <h5 class="card-title">{html.escape(item.get('Reskin', 'Unknown'))}</h5>
                        </div>
                    </div>
                </div>
                """
                if corresponding_image:
                    html_entries += f"""
                    <div class="col-md-6">
                        <div class="card">
                            <img src="{corresponding_image['png']}" class="card-img-top half-resolution" alt="Image for {html.escape(item.get('Reskin', 'Unknown'))}">
                        </div>
                    </div>
                    """

                # Add SVGs if available
                if "ReskinPath" in item and os.path.exists(item["ReskinPath"]):
                    svg_cards = ""
                    for svg_file in os.listdir(item["ReskinPath"]):
                        if svg_file.endswith(".svg"):
                            svg_cards += f"""
                            <div class="col-md-4">
                                <div class="card">
                                    <img src="{os.path.join(item['ReskinPath'], svg_file).replace('\\', '/')}" class="card-img-top svg-icon" alt="{html.escape(svg_file)}">
                                    <div class="card-body">
                                        <h5 class="card-title">{html.escape(svg_file)}</h5>
                                    </div>
                                </div>
                            </div>
                            """
                    if svg_cards:
                        html_entries += f'<div class="row row-cols-1 row-cols-md-3 g-4 mt-2">{svg_cards}</div>'

        html_entries += "</div>"  # Close the row for this class

    # Insert the generated HTML into the template
    output_html = template_html.replace("<!-- implement here -->", html_entries)

    # Write the final HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_html)

if __name__ == "__main__":
    # Specify the directory to scan, the template file, and the output files
    directory_to_scan = "./"  # Change this to your target directory
    output_json_file = "output.json"
    template_file = "template.html"
    output_html_file = "index.html"

    # Generate JSON and HTML
    generate_json(directory_to_scan, output_json_file)
    generate_html(template_file, output_json_file, output_html_file)
    print(f"HTML file generated: {output_html_file}")
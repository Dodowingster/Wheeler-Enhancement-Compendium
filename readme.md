# Wheeler of Enhancement Compendium

The **Wheeler of Enhancement Compendium** is a showcase and resource collection for various reskins and enhancements for the Skyrim Special Edition modding community. This project organizes and displays reskins, icons, and animations in an interactive HTML format, making it easier for users to explore and utilize the available assets.

## Features

- **Dynamic HTML Showcase**: Automatically generates an interactive HTML page to display images, GIFs, and SVG icons for each reskin.
- **Reskin Organization**: Reskins are categorized into folders (e.g., `DDDM`, `Fighter`, `Mage`, `Rogue`) with corresponding styles and resources.
- **JSON Data Generation**: Scans the project directory to generate a JSON file (`output.json`) containing metadata for all assets.
- **Bootstrap Integration**: Uses Bootstrap for responsive and visually appealing layouts.
- **SVG Icon Support**: Displays SVG icons for each reskin, dynamically linked from their respective directories.

## Project Structure

### Key Files

- **`generate_html.py`**: Python script to generate `output.json` and `index.html` dynamically.
- **`output.json`**: JSON file containing metadata for all images, GIFs, and reskin paths.
- **`index.html`**: The generated HTML file showcasing all assets.
- **`template.html`**: HTML template used by the Python script to generate the final `index.html`.
- **`Styles.ini`**: Configuration files for each reskin, defining styling and animation properties.

## Usage

### Prerequisites

- Python 3.x
- Bootstrap (linked via CDN in `template.html`)

### Steps to Generate the Showcase

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Wheeler-Enhancement-Compendium
   ```

2. **Run the Python Script**:
    Execute the generate_html.py script to generate output.json and index.html
    ```bash
    python generate_html.py
    ```

3. **Open the Showcase**: 
    Open index.html in your browser to view the interactive showcase.

## Customization

### Adding New Reskins

1. Create a new folder under `Reskins/` with the format `<Reskin Name> Reskin`.
2. Add the required `Styles.ini` and resources (e.g., icons, textures) in the appropriate subdirectories.
3. Add corresponding GIFs and images in the `Images/` directory.

### Updating the Template

Modify `template.html` to change the layout or styling of the showcase.

## JSON Structure

The `output.json` file contains metadata for all assets. Example structure:

```json
[
    {
        "class": "Images",
        "png": "./Images\\DDDM.png"
    },
    {
        "class": "Gifs",
        "gif": "./Images\\Gifs\\DDDM_Wheeler.gif",
        "Reskin": "DDDM",
        "ReskinPath": "Reskins\\DDDM Reskin\\SKSE\\Plugins\\wheeler\\resources\\icons"
    }
]
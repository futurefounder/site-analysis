import pandas as pd
from urllib.parse import urlparse
from datetime import datetime

# Load the CSV file
df = pd.read_csv("2024-11-15_11-41-50_subcategories_with_hierarchy.csv")  # Replace with your actual CSV filename

# Specify the correct column name for URLs
url_column = "Full URL"

# Function to extract the unique category path from a URL
def get_category_path(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    # Remove trailing slashes and page-specific elements
    path_parts = path.strip("/").split("/")
    if path_parts[-1].endswith(".html"):  # Remove .html pages
        path_parts.pop()
    return "/".join(path_parts)  # Join back to get the unique path

# Apply the function to get unique category paths
df["Category Path"] = df[url_column].apply(get_category_path)

# Remove duplicates based on "Category Path"
df_unique = df.drop_duplicates(subset="Category Path")

# Drop the helper "Category Path" column if it's not needed
df_unique = df_unique.drop(columns=["Category Path"])

# Create a timestamped filename
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{current_time}_unique_subcategories.csv"

# Save the deduplicated DataFrame to a new CSV
df_unique.to_csv(filename, index=False)

print(f"Deduplicated categories saved to '{filename}'")

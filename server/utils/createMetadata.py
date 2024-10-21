import os

def create_meta_file(content, filename="test.txt"):
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Navigate to the FastAPI_Template directory (assuming utils is in app directory)
    fastapi_template_dir = os.path.dirname(os.path.dirname(current_dir))
    
    # Construct the path to the contracts directory
    contracts_dir = os.path.join(fastapi_template_dir, 'client', 'ipfs')
    
    # Ensure the contracts directory exists
    os.makedirs(contracts_dir, exist_ok=True)
    
    # Create the full file path
    file_path = os.path.join(contracts_dir, filename)
    
    # Write the content to the file
    with open(file_path, "w") as file:
        file.write(content)
    
    print(f"File '{filename}' has been created successfully at: {file_path}")
    return file_path

if __name__ == "__main__":
    text_string = "Na adicha Thanga Maaten"
    created_file_path = create_meta_file(text_string)
    print(f"File created at: {created_file_path}")
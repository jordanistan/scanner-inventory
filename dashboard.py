import streamlit as st
import pandas as pd
import os

def load_inventory(file_path):
    """Loads the inventory CSV file from the given file path."""
    return pd.read_csv(file_path)

def get_inventory_files():
    """Gets the list of inventory CSV files from the output directory."""
    output_dir = "output"
    if not os.path.exists(output_dir):
        st.error("Output directory not found!")
        return []
    
    files = [f for f in os.listdir(output_dir) if f.startswith("directory_inventory_") and f.endswith(".csv")]
    if not files:
        st.error("No inventory files found!")
    return files

# Streamlit App Title
st.title("📂 File Inventory Dashboard")

# Get list of inventory files
inventory_files = get_inventory_files()

if inventory_files:
    # Dropdown menu to select inventory file
    selected_file = st.sidebar.selectbox("Select Inventory File", inventory_files)
    
    # Load Data
    data = load_inventory(os.path.join("output", selected_file))

    if data is not None:
        st.sidebar.header("Filters")
        
        # Dropdown for selecting output files
        selected_filter_file = st.sidebar.selectbox("View Output Files", inventory_files, index=inventory_files.index(selected_file))
        
        # File Name Search
        search_term = st.sidebar.text_input("Search File Name")
        if search_term:
            data = data[data["Item Name"].str.contains(search_term, case=False, na=False)]
        
        # File Size Filter
        min_size, max_size = st.sidebar.slider("File Size Range (Bytes)", int(data["File Size (Bytes)"].min()), int(data["File Size (Bytes)"].max()), (0, int(data["File Size (Bytes)"].max())))
        data = data[(data["File Size (Bytes)"] >= min_size) & (data["File Size (Bytes)"] <= max_size)]
        
        # Display Data
        st.subheader(f"Inventory from: {selected_file}")
        st.write("Total files scanned:", len(data))
        st.dataframe(data)
        
        # MD5 Hash Analysis
        st.subheader("MD5 Hash Analysis")
        duplicate_hashes = data[data.duplicated("MD5 Hash", keep=False)]
        if not duplicate_hashes.empty:
            st.warning("Duplicate files detected based on MD5 hashes!")
            st.dataframe(duplicate_hashes)
        else:
            st.success("No duplicate files detected.")
        
        # File Type Distribution
        st.subheader("File Type Distribution")
        data["File Extension"] = data["Item Name"].apply(lambda x: os.path.splitext(x)[1] if '.' in x else "No Extension")
        file_type_counts = data["File Extension"].value_counts()
        st.bar_chart(file_type_counts)

        # Recent Files
        st.subheader("Recently Modified Files")
        data_sorted = data.sort_values(by="Date Modified", ascending=False).head(10)
        st.dataframe(data_sorted)

    else:
        st.warning("No data available. Run the inventory script first.")
else:
    st.warning("No inventory files available.")

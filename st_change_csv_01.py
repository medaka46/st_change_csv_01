import streamlit as st
import pandas as pd
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize session state if not exists
if 'data' not in st.session_state:
    # CSVファイルのパス
    csv_file_path = os.path.join(script_dir, 'test.csv')
    
    # CSVファイルを読み込む
    if os.path.exists(csv_file_path):
        st.session_state.data = pd.read_csv(csv_file_path)
    else:
        # Create empty DataFrame if file doesn't exist
        st.session_state.data = pd.DataFrame(columns=['A', 'B', 'C'])

# データを表示
st.write("Current Data:")
st.dataframe(st.session_state.data)

# データの編集
edited_df = st.data_editor(st.session_state.data)

# 保存ボタン
if st.button("Save Changes"):
    try:
        # Get the path to the original CSV file
        csv_file_path = os.path.join(script_dir, 'test.csv')
        
        # Save directly to the original CSV file
        edited_df.to_csv(csv_file_path, index=False)
        
        # Update session state
        st.session_state.data = edited_df
        st.success("Changes saved successfully to test.csv!")
        
    except Exception as e:
        st.error(f"Error saving changes: {str(e)}")

# Read CSVボタン
if st.button("Read CSV"):
    try:
        # Get the path to the CSV file
        csv_file_path = os.path.join(script_dir, 'test.csv')
        
        # Read the CSV file
        if os.path.exists(csv_file_path):
            st.session_state.data = pd.read_csv(csv_file_path)
            st.success("CSV file read successfully!")
        else:
            st.error("CSV file not found!")
            
    except Exception as e:
        st.error(f"Error reading CSV file: {str(e)}")
import streamlit as st
import pandas as pd

# CSVファイルのパス
csv_file_path = 'test.csv'

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path)

# データを表示
st.write("Current Data:")
st.dataframe(df)

# データの編集
edited_df = st.data_editor(df)

# 保存ボタン
if st.button("Save Changes"):
    edited_df.to_csv(csv_file_path, index=False)
    st.success("Changes saved successfully!")
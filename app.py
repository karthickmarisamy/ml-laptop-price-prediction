import streamlit as st
import pickle
import pandas as pd

# Create a Streamlit form
st.title("Laptop Data Submission Form")

# Define the columns in the dataset
with st.form("laptop_form"):
    st.subheader("Enter Laptop Specifications")

    # Dropdowns for categorical data
    cpu_company = st.selectbox("CPU Company", ["Intel", "AMD", "Samsung"])
    gpu_company = st.selectbox("GPU Company", ["Nvidia", "AMD", "Intel", "ARM"])
    company = st.selectbox("Laptop Brand", ["Dell", "Lenovo", "HP", "Asus", "Acer", "MSI", "Toshiba", "Apple", "Samsung", "Razer", "Mediacom", "Microsoft", "Xiaomi", "Vero", "Chuwi", "Google", "Fujitsu", "LG", "Huawei"])
    typename = st.selectbox("Type Name", ["Notebook", "Gaming", "Ultrabook", "2 in 1 Convertible", "Workstation", "Netbook"])
    opsys = st.selectbox("Operating System", ["Windows 10", "No OS", "Linux", "Windows 7", "Chrome OS", "macOS", "Mac OS X", "Windows 10 S", "Android"])

    # Inputs for numerical data
    inches = st.number_input("Screen Size (Inches)", min_value=10.0, max_value=20.0, value=15.6, step=0.1)
    cpu_frequency = st.number_input("CPU Frequency (GHz)", min_value=0.0, value=3.5, step=0.1)
    ram = st.number_input("RAM (GB)", min_value=2, max_value=64, value=16, step=1)
    weight = st.number_input("Weight (kg)", min_value=0.5, value=2.5, step=0.1)
    screen_x_size = st.number_input("Screen Width (Pixels)", min_value=800, value=1920, step=1)
    screen_y_size = st.number_input("Screen Height (Pixels)", min_value=600, value=1080, step=1)
    touch_screen = st.selectbox("Touch Screen", [0, 1], format_func=lambda x: "Yes" if x else "No")
    ips = st.selectbox("IPS Panel", [0, 1], format_func=lambda x: "Yes" if x else "No")
    full_hd = st.selectbox("Full HD", [0, 1], format_func=lambda x: "Yes" if x else "No")
    ultra_hd = st.selectbox("4K Ultra HD", [0, 1], format_func=lambda x: "Yes" if x else "No")
    quad_hd = st.selectbox("Quad HD", [0, 1], format_func=lambda x: "Yes" if x else "No")
    screen_resolution_na = st.selectbox("Screen Resolution NA", [0, 1], format_func=lambda x: "Yes" if x else "No")
    ssd = st.number_input("SSD (GB)", min_value=0, value=512, step=1)
    hdd = st.number_input("HDD (GB)", min_value=0, value=0, step=1)
    flash_storage = st.number_input("Flash Storage (GB)", min_value=0, value=0, step=1)

    # Submit button
    submitted = st.form_submit_button("Submit")

# If the form is submitted, process and display the data
if submitted:
    data = {
        "CPU_Company": [cpu_company],
        "GPU_Company": [gpu_company],
        "Inches": [inches],
        "CPU_Frequency (GHz)": [cpu_frequency],
        "RAM (GB)": [ram],
        "Weight (kg)": [weight],
        "screen_x_size": [screen_x_size],
        "screen_y_size": [screen_y_size],
        "Touch_screen": [touch_screen],
        "IPS": [ips],
        "Full_HD": [full_hd],
        "4k_Ultra_HD": [ultra_hd],
        "Quad_HD": [quad_hd],
        "Screen_Resolution_NA": [screen_resolution_na],
        "SSD": [ssd],
        "HDD": [hdd],
        "Flash_Storage": [flash_storage],
        "Company": [company],
        "TypeName": [typename],
        "OpSys": [opsys],
    }

    # Create a DataFrame from the submitted data
    df = pd.DataFrame(data)
    st.subheader("Submitted Data")
    
    with open('preprocessor.pkl', 'rb') as file:
        preprocessor = pickle.load(file)

    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    data_transformed = preprocessor.transform(df)
    st.write(f"The price of laptop is EURO {model.predict(data_transformed)}")
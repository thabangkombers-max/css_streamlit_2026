import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Kombesi Thabang | Materials Physics & Spintronics",
    layout="wide"
)

# --------------------------------------------------
# Sidebar navigation
# --------------------------------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "Materials Data Explorer", "Contact"],
)

# --------------------------------------------------
# Materials / Spintronics-related datasets
# --------------------------------------------------
mnpt_properties = pd.DataFrame({
    "Property": [
        "Lattice parameter a (Å)",
        "Lattice parameter c (Å)",
        "Magnetic ordering",
        "Bulk modulus (GPa)",
        "Shear modulus (GPa)",
        "Formation energy (eV/atom)"
    ],
    "Value": [
        3.98,
        3.71,
        "Antiferromagnetic",
        215,
        98,
        -0.62
    ]
})

elastic_constants = pd.DataFrame({
    "Elastic Constant": ["C11", "C33", "C44", "C66", "C12", "C13"],
    "Value (GPa)": [310, 290, 95, 88, 140, 120]
})

magnetic_data = pd.DataFrame({
    "Composition": ["MnPt", "MnPt (AFM)", "MnPt (FM)"],
    "Magnetic Moment (μB/Mn)": [3.4, 3.2, 3.8],
    "Relative Energy (meV/atom)": [0, 0, 45]
})

# --------------------------------------------------
# Researcher Profile
# --------------------------------------------------
if menu == "Researcher Profile":
    st.title("Researcher Profile")

    name = "Kombesi Thabang"
    field = "Computational Materials Physics"
    research_focus = (
        "First-principles (DFT) investigation of L1₀ MnPt alloys "
        "for spintronic and magnetic data storage applications."
    )

    st.write(f"**Name:** {name}")
    st.write(f"**Field:** {field}")
    st.write("**Research Focus:**")
    st.write(research_focus)

    st.subheader("Research Interests")
    st.markdown("""
    - Density Functional Theory (DFT)
    - L1₀ MnPt antiferromagnets
    - Spintronics and magnetic data storage
    - Mechanical and thermodynamic stability
    - Elastic, electronic, and magnetic properties of alloys
    """)

# --------------------------------------------------
# Publications
# --------------------------------------------------
elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    uploaded_file = st.file_uploader(
        "Upload a CSV file (Title, Authors, Journal, Year)",
        type="csv"
    )

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        keyword = st.text_input("Filter by keyword (title, journal, authors)")
        if keyword:
            filtered = publications[
                publications.apply(
                    lambda row: keyword.lower() in row.astype(str).str.lower().values,
                    axis=1
                )
            ]
            st.subheader(f"Filtered Results for '{keyword}'")
            st.dataframe(filtered)

        if "Year" in publications.columns:
            st.subheader("Publication Trend by Year")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
    else:
        st.info("Upload your publications CSV to display and analyze.")

# --------------------------------------------------
# Materials Data Explorer
# --------------------------------------------------
elif menu == "Materials Data Explorer":
    st.title("Materials Data Explorer")
    st.sidebar.header("Dataset Selection")

    data_option = st.sidebar.selectbox(
        "Choose a dataset",
        [
            "MnPt Structural & Thermodynamic Properties",
            "Elastic Constants",
            "Magnetic Configurations"
        ]
    )

    if data_option == "MnPt Structural & Thermodynamic Properties":
        st.subheader("L1₀ MnPt Properties")
        st.dataframe(mnpt_properties)

    elif data_option == "Elastic Constants":
        st.subheader("Elastic Constants of L1₀ MnPt")
        st.dataframe(elastic_constants)

        st.bar_chart(
            elastic_constants.set_index("Elastic Constant")
        )

    elif data_option == "Magnetic Configurations":
        st.subheader("Magnetic Configurations of MnPt")
        st.dataframe(magnetic_data)

        st.bar_chart(
            magnetic_data.set_index("Composition")["Relative Energy (meV/atom)"]
        )

# --------------------------------------------------
# Contact
# --------------------------------------------------
elif menu == "Contact":
    st.title("Contact Information")
    st.write("📧 **Email:** (202005520@myturf.ul.ac.za)")
    st.write("🔬 **Research Area:** Computational Materials Physics & Spintronics")

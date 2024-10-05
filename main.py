import pandas as pd
import numpy as np
import streamlit as st
import preprocessor as pre
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Reading the data
df = pd.read_csv('Shark Tank India Dataset.csv')

# Creating Industry Column
df['Industry'] = df['idea'].map(pre.industry_dict)

# Dealing with error of str and float:
df.at[105, 'Industry'] = 'Not Found'

# Add an image to the sidebar
image_path ="logo.jpeg"
st.sidebar.image(image_path, use_column_width=True)



# Checkbox function
def multiselect(title, unique_value):
    select_all = st.sidebar.checkbox('Select All', value=False, key=title)  # Set value to False
    if select_all:
        selected_values = unique_value  #.tolist()  # Convert to list if unique_value is a Series
    else:
        selected_values = st.sidebar.multiselect(title, unique_value)  # Provide options for multiselect
    return selected_values

# Creating Filters for some features:
st.sidebar.title('Filter')

# Filter for Episodes
selected_episode = multiselect('Episode Filter', df['episode_number'].unique())
if len(selected_episode) > 0:
    df = df[df['episode_number'].isin(selected_episode)]

# Filter for Industry
sorted_industries = sorted(df['Industry'].unique())
selected_industry = multiselect('Industry Filter', sorted_industries)
if len(selected_industry) > 0:
    df = df[df['Industry'].isin(selected_industry)]


# Title for the Streamlit application
# Attractive title for the Streamlit application
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #333;  /* Dark gray color for text */
        font-weight: bold;
        font-size: 48px;  /* Font size */
        background-color: #ffffff;  /* White background */
        padding: 20px;  /* Padding for the title */
        border-radius: 10px;  /* Rounded corners */
        border: 2px solid #007BFF;  /* Blue border */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Subtle shadow effect */
        margin-bottom: 20px;  /* Space below the title */
        transition: transform 0.3s ease; /* Smooth scaling effect */
    }

    .title:hover {
        transform: scale(1.05); /* Scale up on hover */
    }
    </style>
    <div class="title">Shark Tank Data Analysis</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)



# Define custom CSS styles for the dashboard
st.markdown(
    """
    <style>
    .reportview-container {
        background: black;
    }
    .custom-subheader {
        font-size: 20px;  /* Adjust font size */
        font-weight: bold;
        color: white; 
        text-align: center;  
        margin-bottom: 20px;  /* Adjust margin */
        border-bottom: 2px solid #ddd;  /* Add a border */
    }
    .kpi-container {
        text-align: center;
        padding: 10px;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .kpi-label {
        font-size: 16px;
        font-weight: normal;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .kpi-value {
        font-size: 24px;
        font-weight: bold;
        color: black;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Create a custom sub-header for KPIs
st.markdown("<div class='custom-subheader'>Key Performance Indicators (KPIs)</div>", unsafe_allow_html=True)


# Create columns for input filters
col1, col2 = st.columns(2)

# Column for KPI calculations
col3, col4, col5 = st.columns(3)

with col3:
    # Total Pitches Made
    total_pitches = len(df)

    # Total Investment Amount
    total_investment = df['deal_amount'].sum()

    # Total Deals Closed
    total_deals = df['deal'].sum()

with col4:
    # Overall Success Rate
    success_rate = (total_deals / total_pitches * 100) if total_pitches > 0 else 0

    # Highest Investment Amount in a Single Deal
    highest_investment_deal = df['deal_amount'].max()

    # Average Deal Valuation
    avg_deal_valuation = df['deal_valuation'].mean()

with col5:
    # Highest Ask Valuation
    highest_ask_valuation = df['ask_valuation'].max()

    # Most Active Shark
    sharks = ['ashneer_present', 'anupam_present', 'aman_present', 'namita_present', 'vineeta_present', 'peyush_present']
    shark_display_names = ['Ashneer', 'Anupam', 'Aman', 'Namita', 'Vineeta', 'Peyush'] 
    shark_deals = df[sharks].apply(lambda x: x > 0).sum()
    most_active_shark = shark_deals.idxmax() if not shark_deals.empty else None

    # Most Invested Industry
    investment_by_industry = df.groupby('Industry')['deal_amount'].sum()
    most_invested_industry = investment_by_industry.idxmax() if not investment_by_industry.empty else None

# Define the KPIs for display using the styled layout
kpis = [
    {"label": "Total Pitches Made", "value": total_pitches},
    {"label": "Total Deals Closed", "value": total_deals},
    {"label": "Overall Success Rate (%)", "value": f"{success_rate:.2f}%"},
    {"label": "Total Investment (Cr)", "value": f"₹{total_investment:.2f}"},
    {"label": "Most Invested Industry", "value": most_invested_industry if most_invested_industry else 'N/A'},
    {"label": "Highest Investment in a Single Deal (Cr)", "value": highest_investment_deal},
    {"label": "Highest Ask Valuation (Cr)", "value": highest_ask_valuation},
    {"label": "Average Deal Valuation (Cr)", "value": f"₹{avg_deal_valuation:.2f}"},
    {"label": "Most Active Shark", "value": shark_display_names[sharks.index(most_active_shark)] if most_active_shark else 'N/A'},
]

# Create 3 columns for the KPIs
num_columns = 3
chunks = [kpis[i:i + num_columns] for i in range(0, len(kpis), num_columns)]  # Divide KPIs into chunks of 3

# CSS styles for hover effect
st.markdown("""
    <style>
    .kpi-container {
        background-color: #f9f9f9; /* Light background for KPI containers */
        border: 1px solid #007BFF; /* Blue border */
        border-radius: 8px; /* Rounded corners */
        padding: 15px; /* Padding inside the container */
        margin: 10px; /* Space around the container */
        transition: background-color 0.3s ease, transform 0.3s ease; /* Smooth transition */
    }

    .kpi-container:hover {
        background-color: #e0f7fa; /* Change background on hover */
        transform: scale(1.05); /* Slightly enlarge on hover */
        cursor: pointer; /* Pointer cursor on hover */
    }

    .kpi-label {
        font-size: 18px; /* Font size for KPI labels */
        color: #333; /* Dark text color */
        font-weight: bold; /* Bold text */
    }

    .kpi-value {
        font-size: 24px; /* Font size for KPI values */
        color: #007BFF; /* Blue color for KPI values */
    }
    </style>
""", unsafe_allow_html=True)

# Create KPI display
for chunk in chunks:
    cols = st.columns(num_columns)  # Create 3 columns in each row
    for col, kpi in zip(cols, chunk):
        with col:
            st.markdown(f"""
                <div class='kpi-container'>
                    <div class='kpi-label'>{kpi['label']}</div>
                    <div class='kpi-value'>{kpi['value']}</div>
                </div>
                """, unsafe_allow_html=True)

# Create two columns for the graphs
col6, col7 = st.columns(2)

with col6:
    # Create a bar chart for total investments and number of deals by each shark
    total_investments_by_sharks = {shark: df[df[shark] > 0]['deal_amount'].sum() for shark in sharks}

    # Number of deals closed by each shark
    deals_closed_by_sharks = df[sharks].apply(lambda x: x > 0).sum()
    # You can then visualize this data using a suitable plotting library (e.g., matplotlib, seaborn)


# Visualization for Total Investments by Industry:
# Create the figure and axes
fig1, ax1 = plt.subplots(figsize=(8, 5))
# Set the background color of the entire figure
fig1.set_facecolor('black')
# Set the background color of the axes (plot area)
ax1.set_facecolor('black')
# Create the bar plot with Seaborn
sns.barplot(x='deal_amount', y='Industry', data=df, ax=ax1, palette='viridis')

# Set title and axis labels with white text to match the dark theme
ax1.set_title('Total Investments by Industry', color='white')
ax1.set_xlabel('Total Investment Amount (Cr)', color='white')
ax1.set_ylabel('Industry', color='white')

# Change the tick label color to white for both axes
ax1.tick_params(colors='white')

# Change the color of the spines (borders of the plot area) to white
for spine in ax1.spines.values():
    spine.set_edgecolor('white')


# Visualization for Deals Closed by Each Shark
deals_closed_by_sharks = df[sharks].apply(lambda x: x > 0).sum()

fig2, ax2 = plt.subplots(figsize=(5, 5))
# Set the figure background to black
fig2.set_facecolor('black')
# Set the axes background to black
ax2.set_facecolor('black')
# Create the pie chart
wedges, texts, autotexts = ax2.pie(deals_closed_by_sharks, 
                                   labels=shark_display_names, 
                                   autopct='%1.1f%%', 
                                   startangle=90, 
                                   textprops={'color': 'white'})  # Set label text color to white
# Ensure the pie is drawn as a circle
ax2.axis('equal')
# Set the color of the percentage labels (autotexts) to white for better visibility
for autotext in autotexts:
    autotext.set_color('white')
# Set the color of the pie chart's labels (shark names) to white
for text in texts:
    text.set_color('white')

# Doing required changes in graph:
st.markdown(
    """
    <style>
    .reportview-container {
        background: black;
    }
    .custom-subheader {
        font-size: 20px;  /* Adjust font size */
        font-weight: bold;
        color: white; 
        text-align: center;  
        margin-bottom: 20px;  /* Adjust margin */
        border-bottom: 2px solid #ddd;  /* Add a border */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Display the figures one below the other

st.markdown("<div class='custom-subheader'>Total Investments by Industry</div>", unsafe_allow_html=True)
st.pyplot(fig1)

st.markdown("<div class='custom-subheader'>Proportion of Deals Closed by Each Shark</div>", unsafe_allow_html=True)
st.pyplot(fig2)


# Visualization for Investments Over Time (using Episode)
if 'episode_number' in df.columns:
    # Group data by episode_number and calculate total deal amounts
    investments_over_time = df.groupby('episode_number')['deal_amount'].sum().reset_index()
    # Display the subheader
    st.markdown("<div class='custom-subheader'>Investments Over Time</div>", unsafe_allow_html=True)
    # Create figure and axes
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    # Set the background color of the entire figure to black
    fig3.set_facecolor('black')
    # Set the background color of the axes (plot area) to black
    ax3.set_facecolor('black')
    # Create the line plot with a marker
    sns.lineplot(x='episode_number', y='deal_amount', data=investments_over_time, ax=ax3, marker='o', color='cyan')
    # Set the title and labels with white text to match the dark theme
    ax3.set_title('Total Investments Over Episodes', color='white')
    ax3.set_xlabel('Episode Number', color='white')
    ax3.set_ylabel('Total Investment Amount (Cr)', color='white')
    # Change tick label colors to white
    ax3.tick_params(colors='white')
    # Change the color of the spines (plot borders) to white for better visibility
    for spine in ax3.spines.values():
        spine.set_edgecolor('white')
    # Display the plot in Streamlit
    st.pyplot(fig3)


# Visualization for Distribution of Deal Amounts
# Check if the 'episode_number' column is in the DataFrame
if 'episode_number' in df.columns:
    st.markdown("<div class='custom-subheader'>Distribution of Deal Amounts</div>", unsafe_allow_html=True)
    # Create the figure and axes
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    # Set the figure background to black
    fig4.set_facecolor('black')
    # Set the axes background to black
    ax4.set_facecolor('black')
    # Create the histogram plot
    sns.histplot(df['deal_amount'], bins=20, kde=True, ax=ax4)
    # Set the title and axis labels with white text for the dark theme
    ax4.set_title('Distribution of Deal Amounts', color='white')
    ax4.set_xlabel('Deal Amount (Cr)', color='white')
    ax4.set_ylabel('Frequency', color='white')
    # Change the tick label color to white for both axes
    ax4.tick_params(colors='white')
    # Change the color of the spines (borders of the plot area) to white
    for spine in ax4.spines.values():
        spine.set_edgecolor('white')
    # Display the figure in Streamlit
    st.pyplot(fig4)





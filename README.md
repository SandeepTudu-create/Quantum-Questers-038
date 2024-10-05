
# Quantum Questers-038

## Introduction

This project focuses on creating a comprehensive data analytics dashboard that visualizes the "Top Investments in Shark Tank India Dataset." The primary objective is to analyze and showcase key trends and insights from the investment deals made on the popular television show *Shark Tank India*. 

## Project Type
Backend | Frontend

## Deplolyed App
https://streamlit.io/cloud

## Directory Structure
my-dashboard-app/Quantum Questers-038  
├─ data/Shark Tank India Dataset.csv                                     
├─ main.py  
├─ preprocessor.py           
├─ requirements.txt    
├─ README.md           
├─ dashboard.py 

## Walkthrough of the project
The dashboard provides an intuitive interface for entrepreneurs, investors, and researchers to explore critical aspects of the Indian startup ecosystem. By presenting Key Performance Indicators (KPIs) such as Total Investment, Highest Deal, Most Active Shark, and Industry Insights, it offers a data-driven perspective on the success of pitches, the distribution of investments across industries, and the role of individual investors ("Sharks").

Core functionalities include interactive graphs, filters for episode and industry type, and an analysis of investment trends over time. This project highlights the diversity of startups that received funding, solving the challenge of understanding where and how venture capital flows within India's dynamic entrepreneurial landscape.

## Walkthrough of the codebase
### Walkthrough of the Codebase

1. **Imports and Setup**:
   The code starts by importing necessary libraries such as `pandas` for data manipulation, `numpy` for numerical operations, `streamlit` for building the dashboard, and visualization libraries like `matplotlib` and `seaborn`. A custom module (`preprocessor`) is imported for preprocessing tasks like mapping ideas to their respective industries. Warnings are suppressed to keep the output clean.

2. **Reading the Dataset**:
   The dataset, which contains investment details from *Shark Tank India*, is read into a pandas DataFrame. A new column, "Industry," is created by mapping the 'idea' field to the appropriate industry using a predefined dictionary. An error in one specific entry is handled manually by assigning "Not Found" to an industry field that had an issue.

3. **Sidebar and Filter Setup**:
   The Streamlit app's sidebar includes a project logo, followed by filters for selecting episodes and industries. These filters allow users to refine the data displayed on the dashboard. A custom `multiselect` function is used to enable multi-selection of episodes and industries with a "Select All" option.

4. **Dashboard Styling and Layout**:
   The dashboard is designed to be visually appealing with custom CSS styles. This includes a center-aligned, bold title, and a background color for the entire dashboard. Key performance indicators (KPIs) are also styled to ensure they are presented in a clean and engaging way.

5. **KPIs Calculation**:
   The dashboard displays key performance indicators (KPIs), such as:
   - Total number of pitches made.
   - Total investment amount.
   - Number of successful deals.
   
   Other KPIs include the overall success rate, the highest deal amount, average deal valuation, the most active shark (by number of deals), and the industry with the highest total investment. These KPIs are calculated from the dataset and displayed in a structured layout.

6. **Graphs and Visualizations**:
   Multiple visualizations are created to analyze the dataset:
   - A **bar chart** to show total investments by industry.
   - A **pie chart** to display the proportion of deals closed by each shark.
   - A **line plot** that tracks investments over time (by episode).
   - A **histogram** that shows the distribution of deal amounts.

   These visualizations use a consistent dark theme with white text for titles, axes labels, and tick marks. They provide a clear and intuitive way for users to explore the data.

7. **Responsive Layout**:
   The code uses Streamlit's `columns` feature to organize KPIs and graphs. This makes the dashboard responsive, ensuring it adapts to various screen sizes and devices, offering a good user experience across platforms.

8. **Final Visualizations**:
   Each visualization is displayed with clear headers and appropriate styling. The code ensures that the visualizations appear one below the other, creating a smooth flow of information on the dashboard.

## Features

- **Interactive Filters:** Apply episode and industry filters to customize the data view.
- **KPI Overview:** Quick insights into total investments, deals closed, success rates, and more.
- **Data Visualizations:** Bar charts, pie charts, and line plots to explore investment trends.
- **Top Performers:** Identify the most active shark and the industry with the highest investment.
- **Responsive Design:** Optimized layout for seamless use across devices.

## Usage
1. **Installation**: Clone the repository and navigate to the project directory. Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Running the Dashboard**: Start the Streamlit application with the following command:
   ```bash
   streamlit run app.py
   ```

3. **Interacting with Filters**: Use the sidebar to select specific episodes and industries. The data displayed will update based on your selections.

4. **Viewing KPIs**: Key performance indicators will be shown on the dashboard, providing insights into investment trends.

5. **Exploring Visualizations**: Scroll through the graphs to analyze total investments by industry, deals closed by each shark, and the distribution of deal amounts. 

## Technology Stack
- pandas
- numpy
- streamlit
- streamlit.io/cloud
- matplotlib
- seaborn
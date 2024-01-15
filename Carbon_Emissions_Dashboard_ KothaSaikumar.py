import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
def load_data():
    # Replace with the path to your dataset
    return pd.read_excel('C:/Users/Harish Sriramoju/Assessments/Ice Mortgage/emissions.xlsx')

# Main function for the Streamlit app
def main():
    st.set_page_config(
        page_title="Carbon Emissions Dashboard",
        page_icon="🌍",
        layout="wide",
    )

    # Load data
    df = load_data()

    # Streamlit page layout
    st.title("Carbon Emissions Dashboard")
    st.write("Welcome to the Carbon Emissions Dashboard. Explore the data interactively!")



    st.header("Emissions Intensity Data Overview")

    summary_table = df.groupby(['Year', 'Disclosure.Scope.12.Category']).agg(
        Median_Scope_1_2=('Intensity.Accepted.Scope.1.2', 'median'),
        Max_Scope_1_2=('Intensity.Accepted.Scope.1.2', 'max'),
        Min_Scope_1_2=('Intensity.Accepted.Scope.1.2', 'min'),
        Median_Scope_3=('Intensity.Accepted.Scope.3', 'median'),
        Max_Scope_3=('Intensity.Accepted.Scope.3', 'max'),
        Min_Scope_3=('Intensity.Accepted.Scope.3', 'min')
    ).reset_index()
    # st.dataframe(summary_table)

    # st.markdown("""

    #         **The summary table** provides a comprehensive overview of the emissions intensity data, categorized by **year** and the **'Disclosure.Scope.12.Category'.** 
    #         For each category, key statistical metrics — median, maximum, and minimum — are calculated for both **'Intensity.Accepted.Scope.1.2'** and **'Intensity.Accepted.Scope.3'.**

    # Notably, in **2013**, the median intensity for Scope 1.2 across all categories hovered around **418.28**, with maximum values reaching up to approximately **16,462.39** and 
    # minimum values as **low as 53.33**. Similarly, the **median intensity** for Scope 3 in the same year was consistently around **531.72**, 
    # with **maximum** values peaking at around **8,120.15** and **minimum** values at **71.44**. 
    # By contrast, in 2015, there was a significant increase in both median and maximum values for Scope 1.2 and Scope 3 intensities. The median values for Scope 1.2 jumped to 55,601.35, with maximum values skyrocketing to over 8.77 million, indicating a substantial increase in emissions intensity for some entities. The Scope 3 intensities also saw a dramatic rise, with median values around 7.39 million and maximum values exceeding 10 billion.

    # These figures suggest a notable escalation in emissions intensity in 2015 compared to 2013, across all disclosure categories. This increase could be indicative of changes in industrial activities, reporting practices, or environmental policies. The stark difference between the median and maximum values, especially in 2015, highlights significant disparities in emissions intensity among different entities. This data underscores the importance of targeted environmental strategies and interventions, particularly for high-emitting sectors or regions.


    #     """)


    # Create two columns for the side by side layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Summary Table")
        # Assuming 'df' is your DataFrame and the summary_table has already been created as per your code
        # Display the summary table dataframe
        st.dataframe(summary_table)

    with col2:
        # st.subheader("Emissions Intensity Summary")
        # Display the markdown text summary
        st.markdown("""
            **The summary table** provides a comprehensive overview of the emissions intensity data, categorized by **year** and the **'Disclosure.Scope.12.Category'.** 
            For each category, key statistical metrics — median, maximum, and minimum — are calculated for both **'Intensity.Accepted.Scope.1.2'** and **'Intensity.Accepted.Scope.3'.**
            
            Notably, in **2013**, the median intensity for Scope 1.2 across all categories hovered around **418.28**, with maximum values reaching up to approximately **16,462.39** and 
            minimum values as **low as 53.33**. Similarly, the **median intensity** for Scope 3 in the same year was consistently around **531.72**, 
            with **maximum** values peaking at around **8,120.15** and **minimum** values at **71.44**. 
            By contrast, in 2015, there was a significant increase in both median and maximum values for Scope 1.2 and Scope 3 intensities. The median values for Scope 1.2 jumped to 55,601.35, with maximum values skyrocketing to over 8.77 million, indicating a substantial increase in emissions intensity for some entities. The Scope 3 intensities also saw a dramatic rise, with median values around 7.39 million and maximum values exceeding 10 billion.
            
            These figures suggest a notable escalation in emissions intensity in 2015 compared to 2013, across all disclosure categories. This increase could be indicative of changes in industrial activities, reporting practices, or environmental policies. The stark difference between the median and maximum values, especially in 2015, highlights significant disparities in emissions intensity among different entities. This data underscores the importance of targeted environmental strategies and interventions, particularly for high-emitting sectors or regions.
        """)

    # Emissions Intensity Analysis Section
    st.header("Emissions Intensity Analysis")
    st.subheader("KDE Plots for Outlier Analysis and Considerations")
    
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    sns.kdeplot(df['Intensity.Accepted.Scope.1.2'], color='blue', fill=True, ax=ax[0])
    ax[0].set_title('KDE of Intensity.Accepted.Scope.1.2')
    ax[0].set_xlabel('Intensity.Accepted.Scope.1.2')
    ax[0].set_ylabel('Density')

    sns.kdeplot(df['Intensity.Accepted.Scope.3'], color='green', fill=True, ax=ax[1])
    ax[1].set_title('KDE of Intensity.Accepted.Scope.3')
    ax[1].set_xlabel('Intensity.Accepted.Scope.3')
    ax[1].set_ylabel('Density')

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown(""" **Based on the KDE plots:**

* **Intensity.Accepted.Scope.1.2 (Blue Curve):** If the plot shows a significant skewness or is not symmetric, it suggests that the data does not follow a normal distribution closely. In such cases, the IQR method is generally more appropriate because it is less sensitive to skewed data and extreme values.
* **Intensity.Accepted.Scope.3 (Green Curve):** Similar reasoning applies here. If the distribution is skewed or not bell-shaped, the IQR method would be a better choice. """)
    
    st.markdown("""

        **Why Choose IQR Over Z-Score in Skewed Distributions?**

* The Z-score method is based on the assumption of a normal distribution of data. It identifies outliers as points that are a certain number of standard deviations away from the mean. This method can be misleading if the data is not normally distributed, especially if there are skewness and extreme values, as it relies heavily on the mean and standard deviation.

* The IQR method, on the other hand, uses the median and quartiles, which are more robust to skewness and extreme values. It defines outliers based on the range between the first and third quartiles, making it more suitable for data that isn't normally distributed.

    
    So, as plotted KDE's indicate that the data for Intensity.Accepted.Scope.1.2 and/or Intensity.Accepted.Scope.3 are skewed or not normally distributed, the IQR method would be the more appropriate choice for outlier detection.

     """)

    # Histograms
    st.header("Histograms for Emission Intensities")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Intensity.Accepted.Scope.1.2")
        fig1 = px.histogram(df, x='Intensity.Accepted.Scope.1.2', color_discrete_sequence=['indianred'])
        st.plotly_chart(fig1)

    with col2:
        st.write("Intensity.Accepted.Scope.3")
        fig2 = px.histogram(df, x='Intensity.Accepted.Scope.3', color_discrete_sequence=['skyblue'])
        st.plotly_chart(fig2)

    st.markdown(""" **Histograms for Emission Intensities:**

* **Intensity.Accepted.Scope.1.2:** The histogram colored in Indian red suggests a distribution pattern for the emission intensity under Scope 1 and 2. This scope generally covers direct emissions from owned or controlled sources and indirect emissions from the generation of purchased energy.
* **Intensity.Accepted.Scope.3:** The histogram in sky blue portrays the distribution for Scope 3 emission intensity. Scope 3 includes all other indirect emissions that occur in a company's value chain.

* Interpreting these results, it becomes evident that the distribution and range of emission intensities vary significantly between scopes and among companies. 
These visualizations are instrumental in identifying trends, outliers, and the overall environmental impact of different sectors and geographies. 
They offer valuable insights for stakeholders and policymakers focusing on sustainability and carbon footprint reduction. 
The data, particularly Scope 3 emissions, underline the importance of considering the entire value chain in environmental impact assessments. 
This comprehensive view aids in formulating more effective strategies for emission reduction and sustainable practices.

""")

    # Box Plots
    st.header("Box Plots for Emission Intensities")
    col3, col4 = st.columns(2)
    with col3:
        fig3 = px.box(df, y='Intensity.Accepted.Scope.1.2', color_discrete_sequence=['purple'])
        st.plotly_chart(fig3)

    with col4:
        fig4 = px.box(df, y='Intensity.Accepted.Scope.3', color_discrete_sequence=['green'])
        st.plotly_chart(fig4)

    st.markdown(""" **Box Plots for Emission Intensities:**

* **Intensity.Accepted.Scope.1.2:** The box plot in purple provides insights into the central tendency and variability of Scope 1 and 2 emission intensities, indicating the range, quartiles, and potential outliers.
* **Intensity.Accepted.Scope.3:** Similarly, the box plot in green for Scope 3 emissions offers a visual summary of this data's distribution, highlighting variations and outliers.""")

    # Correlation Heatmap
    st.header("Correlation Heatmap")
    col1, col2 = st.columns(2)
    
    new_df = df.select_dtypes(include=['float64', 'int64'])
    correlation = new_df.corr()
    with col1:
        fig5 = px.imshow(correlation, text_auto=True)
        st.plotly_chart(fig5)
    with col2:
        st.markdown(""" 

        
        * Notably, there is a strong positive correlation of approximately 0.89 between **'Intensity.Accepted.Scope.1.2'** and **'Intensity.Accepted.Scope.3'**, indicating that these two emission intensity measures tend to increase or decrease together, suggesting a common influence or shared factors affecting both scopes of emission intensities. 
        This high degree of correlation underscores the interconnected nature of different emission scopes and could reflect the integrated environmental impact strategies employed by the companies.

        """)

    # Emissions by Sector
    st.header("Emissions by Sector")

    col1, col2 = st.columns(2)
    with col1:
        fig6 = px.pie(df, names='Sector', title='Emissions by Sector')
        st.plotly_chart(fig6)

    with col2:
        st.markdown(""" 


* The **pie chart** vividly delineates the proportional impact of various sectors on emissions, offering a clear visual narrative of the industrial landscape's contribution to environmental footprint. 
The **Financial sector** is shown as the most significant contributor, occupying over a quarter of the chart with **26.3%**, underscoring the extensive operational scale and indirect impact of financial services on greenhouse gas emissions. 
**Industrials** follow closely, illustrating the sector's inherent energy-intensive processes. On the other end of the spectrum, the **Utilities and Media & Communications sectors** contribute the **least**, 
combined accounting for less than **1% of emissions**, reflecting either their smaller scale, higher efficiency, or less carbon-intensive operations. This distribution encapsulates the varying responsibilities sectors have in the drive towards sustainability and the necessity for targeted strategies that address the unique emission profiles of each sector. 
The pie chart becomes a stark visual call to action, compelling stakeholders across sectors to marshal their resources towards more sustainable industrial practices.


        """)

    # Scatter Plot
    st.header("Scatter Plot of Intensity.Accepted.Scope.1.2 vs Intensity.Accepted.Scope.3")
    col1, col2 = st.columns(2)
    with col1:
        fig7 = px.scatter(df, x='Intensity.Accepted.Scope.1.2', y='Intensity.Accepted.Scope.3', color='Sector')
        st.plotly_chart(fig7)

    with col2:
        st.markdown(""" 


* The **scatter plot** provides a granular analysis of the **relationship between 'Intensity.Accepted.Scope.1.2' and 'Intensity.Accepted.Scope.3' across various sectors.** 
The **majority of sectors** cluster near the origin, suggesting low emission intensities for both scopes, with Financials and Media & Communications sectors being notable exceptions, depicting significantly higher values in Scope 1.2 emissions. 
There's a visible outlier in the **Media & Communications** sector with an exceedingly high Scope 3 intensity, which could indicate a substantial indirect carbon footprint, possibly due to extensive supply chains or distribution networks. 
This plot emphasizes the variability in emission intensity both within and across sectors, highlighting the importance of sector-specific strategies for emission reduction. 
It also accentuates the need for a nuanced approach to sustainability, considering both direct and indirect emissions to fully grasp and effectively manage the environmental impact of different industries. 
The scatter plot serves not just as a data visualization but as a revelation of the multi-faceted nature of corporate emissions, encapsulating the complexities of environmental stewardship in the commercial world.


        """)

    # Create two columns for the side by side charts
    col1, col2 = st.columns(2)

    # First column for 'Intensity.Accepted.Scope.1.2'
    with col1:
        st.subheader("Intensity Accepted Scope 1.2")
        fig8 = px.line(df, x='Year', y='Intensity.Accepted.Scope.1.2', color='Country')
        st.plotly_chart(fig8)

    # Second column for 'Intensity.Accepted.Scope.3'
    with col2:
        st.subheader("Intensity Accepted Scope 3")
        fig9 = px.line(df, x='Year', y='Intensity.Accepted.Scope.3', color='Country')
        st.plotly_chart(fig9)


    st.markdown(""" 

        * The **Time series charts** elegantly depict the evolving narrative of **'Intensity.Accepted.Scope.1.2'** versus **'Intensity.Accepted.Scope.3'** emissions across a suite of countries from **2013 to 2015**. On the left, the Scope 1.2 graph reveals a relatively gentle upward trend for most countries, signifying a gradual increase in direct and energy indirect emissions over time. 
        In stark contrast, the Scope 3 chart on the right shows a more pronounced and steep increase for several countries, especially Kuwait and South Africa, which may indicate a burgeoning indirect emissions footprint, possibly from increased value chain activities such as goods and services procurement, business travel, and waste disposal. 
        Together, these charts illuminate the disparate paces at which different facets of emissions are expanding, offering a dual perspective that highlights the need for nuanced approaches to managing and mitigating various emission sources as part of a comprehensive climate strategy.
        """)


    # Emissions Intensity Comparison
    st.header("Emissions Intensity Comparison by Country")

    # Create two columns for the side by side charts
    col1, col2 = st.columns(2)

    # First column for 'Intensity.Accepted.Scope.1.2'
    with col1:
        st.subheader("Intensity Accepted Scope 1.2")
        fig8 = px.line(df, x='Country', y='Intensity.Accepted.Scope.1.2', color='Country')
        st.plotly_chart(fig8)

    # Second column for 'Intensity.Accepted.Scope.3'
    with col2:
        st.subheader("Intensity Accepted Scope 3")
        fig9 = px.line(df, x='Country', y='Intensity.Accepted.Scope.3', color='Country')
        st.plotly_chart(fig9)


    st.markdown(""" 



        * The **dual bar charts** present a compelling side-by-side comparison of 'Intensity.Accepted.Scope.1.2' and 'Intensity.Accepted.Scope.3' emissions by country, offering an illustrative snapshot of each country's relative contribution to global emissions. 
        The left chart shows that for Scope 1.2, the United States, Malaysia, and China have relatively moderate emission intensities, whereas Kuwait and South Africa exhibit dramatically higher values, indicating significant direct emissions from owned or controlled sources. 
        On the right, the Scope 3 chart reveals that the United States and China have vastly increased their indirect emissions, potentially signifying an extensive impact from their broader economic activities. Together, these charts underscore the multi-dimensional nature of emissions, with some countries exhibiting high direct emissions while others have more significant indirect emissions, highlighting the complex challenge faced by each in addressing their overall carbon footprint. 
        This visual juxtaposition serves as a stark reminder of the varied strategies needed to mitigate climate change on a per-country basis, taking into account the distinct characteristics of their emissions profiles.

        """)


    # Group data by Year and Sector, and calculate mean intensity for Scope 1.2 and Scope 3
    sector_grouped = df.groupby(['Year', 'Sector']).agg(
        Mean_Scope_1_2=('Intensity.Accepted.Scope.1.2', 'mean'),
        Mean_Scope_3=('Intensity.Accepted.Scope.3', 'mean')
    ).reset_index()

    # Group data by Year and Country, and calculate mean intensity for Scope 1.2 and Scope 3
    country_grouped = df.groupby(['Year', 'Country']).agg(
        Mean_Scope_1_2=('Intensity.Accepted.Scope.1.2', 'mean'),
        Mean_Scope_3=('Intensity.Accepted.Scope.3', 'mean')
    ).reset_index()


    # Plotting the Sector chart for Scope 1.2 and Scope 3
    st.header("Emissions Intensity by Sector")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Intensity Accepted Scope 1.2 by Sector")
        fig_sector_scope_1_2 = px.line(sector_grouped, x='Year', y='Mean_Scope_1_2', color='Sector', title='Yearly Intensity Scope 1.2 by Sector')
        st.plotly_chart(fig_sector_scope_1_2)

    with col2:
        st.subheader("Intensity Accepted Scope 3 by Sector")
        fig_sector_scope_3 = px.line(sector_grouped, x='Year', y='Mean_Scope_3', color='Sector', title='Yearly Intensity Scope 3 by Sector')
        st.plotly_chart(fig_sector_scope_3)

    st.markdown(""" 


    * The paired line charts depict the escalating narrative of emission intensities across various sectors, drawing a stark comparison between 'Intensity.Accepted.Scope.1.2' and 'Intensity.Accepted.Scope.3'. In the first chart, the steady ascent of lines for sectors such as Consumer Discretionary and Energy reflects a consistent increase in direct and indirect emissions from 2013 to 2015, suggesting a growing environmental impact tied to these sectors' operations. The second chart, however, unfolds a more dramatic story for Scope 3 emissions, with certain sectors like Financials displaying a steep trajectory that dwarfs others, highlighting a significant rise in all other indirect emissions that occur within the value chain. These visual trends underscore the pressing need for sector-specific emission mitigation strategies and intensify the call for sustainable practices that can curb the environmental impact as economic activities expand. 
The charts serve as a visual testament to the challenges and progress within each sector, providing a clear indication of where focused efforts on sustainability are most urgently needed.

        """)

    # Plotting the Country chart for Scope 1.2 and Scope 3
    st.header("Emissions Intensity by Country")
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Intensity Accepted Scope 1.2 by Country")
        fig_country_scope_1_2 = px.line(country_grouped, x='Year', y='Mean_Scope_1_2', color='Country', title='Yearly Intensity Scope 1.2 by Country')
        st.plotly_chart(fig_country_scope_1_2)

    with col4:
        st.subheader("Intensity Accepted Scope 3 by Country")
        fig_country_scope_3 = px.line(country_grouped, x='Year', y='Mean_Scope_3', color='Country', title='Yearly Intensity Scope 3 by Country')
        st.plotly_chart(fig_country_scope_3)

    st.markdown(""" 

        * Each line represents a country's journey over time, with a general upward trajectory in emission intensities from 2013 to 2015. The 'Intensity.Accepted.Scope.1.2' chart shows a more compressed range of intensities, suggesting that direct and energy indirect emissions are increasing but at a steadier, more uniform rate among the countries. In contrast, the 'Intensity.Accepted.Scope.3' chart exhibits a starkly different pattern, with some countries, like China and India, showing a steep climb in intensities, indicating a surge in all other indirect emissions. This divergence highlights the varied impact of each country's economic activities on their carbon footprint, with some nations facing a rapidly growing challenge in mitigating their indirect emissions. 
        These insights are crucial for understanding the global landscape of carbon emissions, signaling where international efforts and support may be most needed to address the escalating environmental impacts.

        """)




    st.markdown(""" 

        **The Carbon Emissions Dashboard encapsulates a wealth of data, articulating the multifaceted dynamics of global emissions with clarity and precision. 
        Through an array of statistical analyses and visualizations, it exposes the stark contrasts and trends in emissions intensities across different scopes, sectors, and countries. 
        From the median trends to the alarming spikes in the intensity data, the dashboard narrates the unfolding story of our global industrial footprint, where the financial and industrial sectors emerge as dominant contributors, and countries like Kuwait and South Africa are pinpointed as notable for their surging emission intensities. The varied pace of emissions growth—moderate in Scope 1.2 but steep in Scope 3—underscores the urgency for nuanced mitigation strategies tailored to specific industrial activities and national circumstances. The comprehensive suite of charts—from KDE plots to scatter and time series graphs—doesn't just visualize data; it reveals the layered complexity of the climate challenge, urging stakeholders to engage with the data in crafting targeted and effective responses to the pressing issue of climate change. 
        This dashboard is not merely a tool for observation but a call to action, presenting a compelling case for a collaborative and informed approach to reducing carbon emissions on a global scale.**

        """)


    st.markdown(""" 


        The Carbon Emissions Dashboard, with its comprehensive array of data visualizations, underscores a pressing global narrative: a need for immediate, targeted interventions to mitigate the rising trend in carbon emissions. The increasing trajectories of 'Intensity.Accepted.Scope.1.2' and 'Intensity.Accepted.Scope.3' across sectors and countries from 2013 to 2015 highlight a universal challenge but also a differentiated one; each sector and country contributes uniquely to the global carbon footprint, with some—like the Financials and Energy sectors, and countries like China and India—markedly more so.

**Conclusions:**

* **Sector-Specific Strategies:** Financials and Energy sectors demonstrate significant emission intensities, calling for industry-specific carbon reduction policies. Sectors with lower emissions should not be complacent, as their collective impact is still substantial.
* **National Emissions Management:** Countries like China and India show alarming increases in Scope 3 emissions, necessitating national strategies that target the entire value chain, from production to waste management.
* **Data-Driven Policy Making:** The strong correlation between Scope 1.2 and Scope 3 emissions suggests that policies addressing one are likely to affect the other. This interconnection should be leveraged to create holistic environmental policies.

**Recommendations:**

* **Global Collaboration:** High-emitting countries may benefit from shared technology and best practices from lower-emitting nations, fostering a collaborative approach to emission reduction.
* **Invest in Sustainability:** Investment in sustainable technologies and practices should be prioritized, especially in high-impact sectors and countries, to decouple economic growth from environmental degradation.
* **Enhance Reporting Mechanisms:** The disparities in emission intensities within the data call for improved and standardized reporting mechanisms, ensuring that data accurately reflects the environmental impact and aids in tracking progress.
* **Incentivize Green Practices:** Introduce incentives for companies and sectors that successfully reduce their carbon footprint, encouraging innovation and sustainable development.
The Carbon Emissions Dashboard serves as a crucial tool for stakeholders at all levels to comprehend the magnitude of the challenge ahead. It is imperative that this data informs not just awareness but action, translating into concrete, effective strategies and policies that can steer global industries and nations towards a more sustainable future.



        """)

# Run the main function
if __name__ == "__main__":
    main()

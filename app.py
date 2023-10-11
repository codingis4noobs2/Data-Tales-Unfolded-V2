import streamlit as st
import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from PIL import Image
from st_animation import typing_animation_html, typing_animation_css, typing_animation_js
from quotes import quotes
import random
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components
import re
from df_to_csv_conv import convert_df


favicon = Image.open("favicon.ico")
st.set_page_config(
    layout="wide", 
    page_icon=favicon,
    page_title="Data Tales Unfolded"
)

def home_page():
    st.markdown(
        typing_animation_html + typing_animation_css + typing_animation_js, 
        unsafe_allow_html=True
    )
    st.write(f"<h3 style='text-align: center;'>{random.choice(quotes)}</h3>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("<h5>Data Tales Unfolded is a project aimed at visualizing world university rankings data for the years 2011-2023. The project seeks to make it easy for anyone to access and compare university rankings data, allowing for a better understanding of how universities around the world are performing over time.</h5>", unsafe_allow_html=True)
    st.write("Let's first talk about what are the factors that actually affect the standing of a university 🏫 on such a Competitive scale where everyone wants to be on Top 👇🏼")
    st.write("<h6>Wondering what is this all, read statements below to get more know more about them</h6>", unsafe_allow_html=True)
    st.write("* **Teaching** is a measure of the learning experience and quality at a university. It is based on the reputation among academics, and statistics about staff, students and research.")
    st.write("* **Research** is a measure of both the quality and quantity of research output, based on reputation, research income and productivity.")
    st.write("* **Citations** measures how influential that research is, and counts the number of times work published by academics at the university is cited in other papers.")
    st.write("* **International Outlook** measures the environment and attitude with respect to international students, staff and research. It is based on international-to-domestic ratios across staff, students and research collaborations.")
    st.write("* **Innovation or Industry Income** is a measure of innovation at a university, based on how much the university earns from its inventions and industrial work.")


def learning_the_process():
    def display_message(text, is_user='Ash'):
        if is_user == 'Ash':
            avatar_url = "https://i.ibb.co/PZ9KYmr/ash.png"
            message_alignment = "flex-end"
            message_bg_color = "linear-gradient(135deg, #00B2FF 0%, #006AFF 100%)"
            avatar_class = "user-avatar"
            st.write(
                f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                    <div style="background: {message_bg_color}; color: white; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 14px; border: 1px solid #ccc;">
                        {text}
                    </div>
                    <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.caption(
                f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                    <div style="color: white; margin-right: 5px;">Ash</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            avatar_url = "https://i.ibb.co/C0tZHdd/may.png"
            message_alignment = "flex-start"
            message_bg_color = "#71797E"
            avatar_class = "bot-avatar"

            st.write(
                f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                    <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
                    <div style="background: {message_bg_color}; color: white; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 14px; border: 1px solid #ccc;">
                        {text}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.caption(
                f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                    <div style="color: white; margin-right: 5px;">May</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("<h2 style='text-align: center;'>Chitchat💬</h2>", unsafe_allow_html=True)
    st.write("")
    display_message("Hey May! I heard you wanted to learn about data analysis?", "Ash")
    display_message("Yes, Ash! I've heard a lot about it but never got into the details. Where do we start?", "May")
    display_message("Great! At its core, data analysis is about examining, cleaning, transforming, and interpreting data to discover useful information.", "Ash")
    display_message("Sounds interesting! What's the first step?", "May")
    display_message("The first step is always data collection. You gather data from various sources, could be surveys, databases, or even the web.", "Ash")
    display_message("Here are some websites where you can get dataset to start practicing", 'Ash')
    display_message("Google Dataset Search, Kaggle, Datahub, UCI Machine Learning Repository", 'Ash')
    display_message("And after collecting data?", "May")
    display_message("Next step is to load the data into our program, This is where Pandas come into picture", "Ash")
    display_message("Pandas provides many methods to read the dataset, as the dataset is not a csv file everytime", "Ash")
    display_message("Here is a simple example of how you can use pd.read_csv() to read the csv file", "Ash")
    tab1, tab2 = st.tabs(["Code", "Result"])
    with tab1:
        code_sample = """
        import pandas as pd

        # Read dataset
        df = pd.read_csv("https://raw.githubusercontent.com/aiplanethub/Datasets/master/titanic_data.csv")

        # Displays the first five rows by default, can be overridden if provided with a value
        df.head()
        """
        st.code(code_sample)
    with tab2:
        df = pd.read_csv("https://raw.githubusercontent.com/aiplanethub/Datasets/master/titanic_data.csv")
        st.dataframe(df.head())
    display_message("That's great Ash, But is it neccesary to use links, or can we use our own data?", "May")
    display_message("We can use both links and personal data, let me show you", "Ash")
    tab1, tab2 = st.tabs(["Code", "Result"])
    with tab1:
        code_sample = """
            import pandas as pd

            # Sample data
            data = {
                'Name': ['Alice', 'Bob', 'Charlie'],
                'Age': [24, 28, 22],
                'City': ['New York', 'London', 'Sydney']
            }

            # Create dataframe
            df = pd.DataFrame(data)
            """
        st.code(code_sample)
    with tab2:
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [24, 28, 22],
            'City': ['New York', 'London', 'Sydney']
        }
        df = pd.DataFrame(data)
        st.dataframe(df)
    display_message("Alright May, when working with `pandas`, you'll primarily come across two main data structures: `DataFrame` and `Series`.", "Ash")
    display_message("A `DataFrame` is a 2D labeled data structure with columns that can be of different types, just like a spreadsheet or a SQL table. It is the most commonly used pandas object.", "Ash")
    tab1, tab2 = st.tabs(["Code", "Result"])
    with tab1:
        code_dataframe = """
        # Sample DataFrame
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [24, 28, 22],
            'City': ['New York', 'London', 'Sydney']
        }

        df = pd.DataFrame(data)
        """
        st.code(code_dataframe)
    with tab2:
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [24, 28, 22],
            'City': ['New York', 'London', 'Sydney']
        }
        df = pd.DataFrame(data)
        st.dataframe(df)
    display_message("So, it's like a table with rows and columns, right?", "May")
    display_message("Exactly, May! Now, a `Series`, on the other hand, is a one-dimensional labeled array. It can hold any data type. If you extract one column from a DataFrame, it becomes a Series.", "Ash")
    tab1, tab2 = st.tabs(["Code", "Result"])
    with tab1:
        code_series = """
        # Extracting 'Name' column from the DataFrame
        name_series = df['Name']
        """
    with tab2:
        name_series = df['Name']
        st.dataframe(name_series)
    st.code(code_series)
    display_message("So, a DataFrame is a collection of Series?", "May")
    display_message("You've got it! Each column in a DataFrame is essentially a Series. They both have indices, which makes data retrieval efficient. But remember, while a DataFrame can have multiple columns of different data types, a Series is just a single column.", "Ash")
    display_message("That makes sense. So, I can think of a DataFrame like a full table and a Series as just one column of that table, both having indices for referencing.", "May")
    display_message("Precisely! And both these structures come with a plethora of methods to manipulate, analyze, and visualize data. Pandas makes it quite intuitive.", "Ash")
    display_message("Once we have the data loaded in the dataframe, First we have to analyze the structure of the dataframe")
    tab1, tab2 = st.tabs(["Code", "Result"])
    with tab1:
        code_sample = """
        import pandas as pd

        # Read dataset
        df = pd.read_csv("https://raw.githubusercontent.com/aiplanethub/Datasets/master/titanic_data.csv")

        # Get raw information about the dataframe
        df.info()
        """
        st.code(code_sample)
    with tab2:
        df = pd.read_csv("https://raw.githubusercontent.com/aiplanethub/Datasets/master/titanic_data.csv")
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
    display_message("Wow, that's a lot of information! How do I interpret this?", "May")
    display_message("Good question, May! The `info()` method provides a concise summary of the DataFrame. It tells you the number of non-null values in each column, and each column's data type.", "Ash")
    display_message("So, it's a quick way to check for missing values and to see the type of data we are dealing with?", "May")
    display_message("Exactly. Now, to get a statistical overview of numerical columns, you can use the `describe()` method.", "Ash")
    tab1, tab2 = st.tabs(["Code", "Result"])
    with tab1:
        code_sample = """
        import pandas as pd

        # Read dataset
        df = pd.read_csv("https://raw.githubusercontent.com/aiplanethub/Datasets/master/titanic_data.csv")

        # Get statistical summary
        df.describe()
        """
        st.code(code_sample)
    with tab2:
        df = pd.read_csv("https://raw.githubusercontent.com/aiplanethub/Datasets/master/titanic_data.csv")
        st.dataframe(df.describe())
    display_message("This is cool, Ash! It provides count, mean, standard deviation, and other statistics for the numerical columns.", "May")
    display_message("Yes, May! And for columns with non-numerical data, `describe()` provides other kinds of summaries, like the number of unique values.", "Ash")
    display_message("This gives a good preliminary understanding of the data. What's next?", "May")

def analysis():
    import pandas as pd

    filenames = [
        "2011_rankings.csv", 
        "2012_rankings.csv", 
        "2013_rankings.csv", 
        "2014_rankings.csv", 
        "2015_rankings.csv", 
        "2016_rankings.csv", 
        "2017_rankings.csv", 
        "2018_rankings.csv", 
        "2019_rankings.csv", 
        "2020_rankings.csv", 
        "2021_rankings.csv", 
        "2022_rankings.csv", 
        "2023_rankings.csv"
    ]
    dfs = {}      

    for filename in filenames:
        key = filename.split(".")[0]
        df = pd.read_csv(filename)
        dfs[key] = df    # Stores filename as key which can be further used to retrieve data

    st.write("<h1 style='text-align: center;'>Basic Analysis</h1>", unsafe_allow_html=True)
    st.write("---")

    univ_names = []
    for key, df in dfs.items():
        univ_names.extend(df['name'].unique())

    univ_names = list(set(univ_names))    # This will make sure that univ_names only contain unique values
    univ_names.sort()    # Sorts university names in alphabetical order
    univ_names.insert(0, 'Select University')    # Inserts 'Select University' at index 0, as this needs to be our first element

    st.write("<h2 style='text-align: center;'>Indiviual University Stats 📊📈📉</h2>", unsafe_allow_html=True)
    univ_name = st.selectbox('Select University, (or Alternatively you can type your desired university, it will display if it will be present in the dataset)', univ_names)
    plot_color = st.color_picker('Pick Plot Color', '#000000')

    if univ_name != 'Select University':
        visibility = True
        years = []
        teaching_ranks = []
        research_ranks = []
        citations_ranks = []    
        international_outlook_ranks = []
        industry_income_ranks = []
        overall_ranks = []
        ranks = []

        for key, df in dfs.items():
            univ_df = df[df['name'] == univ_name]

            if not univ_df.empty:
                country = univ_df['location'].iloc[0]
                year = key.split("_")[0]
                teaching_rank = univ_df['scores_teaching_rank'].iloc[0]
                research_rank = univ_df['scores_research_rank'].iloc[0]
                citations_rank = univ_df['scores_citations_rank'].iloc[0]
                international_outlook_rank = univ_df['scores_international_outlook_rank'].iloc[0]
                industry_income_rank = univ_df['scores_industry_income_rank'].iloc[0]
                overall_rank = univ_df['scores_overall_rank'].iloc[0]
                rank = univ_df['rank'].iloc[0]
                rank = str(rank)
                rank = re.findall(r'\d+', rank)    # extracting integer values out of the range

                if rank == []:
                    st.warning("😔 Rank Undefined, Pls select other University")
                    visibility = False
                
                if visibility:
                    rank = rank[0]
                    years.append(year)
                    teaching_ranks.append(int(teaching_rank))
                    research_ranks.append(int(research_rank))
                    citations_ranks.append(int(citations_rank))
                    international_outlook_ranks.append(int(international_outlook_rank))
                    industry_income_ranks.append(int(industry_income_rank))
                    overall_ranks.append(int(overall_rank))
                    ranks.append(int(rank))

        if visibility:
            col1, col2 = st.columns(2)
            with col1:
                relationships = (
                    'Teaching Rank vs Year', 
                    'Research Rank vs Year', 
                    'Citations Rank vs Year', 
                    'International Outlook Rank vs Year', 
                    'Industry Income Rank vs Year', 
                    'Rank vs Year', 
                    'Overall Rank vs Year'
                )
                relationship = st.selectbox('Choose Relation', relationships)
                
                if relationship == "Teaching Rank vs Year":
                    fig, ax = plt.subplots()
                    ax.plot(years, teaching_ranks, color=plot_color)
                    ax.invert_yaxis()
                    plt.xlabel('Year')
                    plt.ylabel('Teaching Rank')
                    plt.title(univ_name + f" ({country})")
                    st.pyplot(fig)
                elif relationship == "Research Rank vs Year":
                    fig, ax = plt.subplots()
                    ax.plot(years, research_ranks, color=plot_color)
                    ax.invert_yaxis()
                    plt.xlabel('Year')
                    plt.ylabel('Research Rank')
                    plt.title(univ_name + f" ({country})")
                    st.pyplot(fig)
                elif relationship == "Citations Rank vs Year":
                    fig, ax = plt.subplots()
                    ax.plot(years, citations_ranks, color=plot_color)
                    ax.invert_yaxis()
                    plt.xlabel('Year')
                    plt.ylabel('Citations Rank')
                    plt.title(univ_name + f" ({country})")
                    st.pyplot(fig)
                elif relationship == "International Outlook Rank vs Year":
                    fig, ax = plt.subplots()
                    ax.plot(years, international_outlook_ranks, color=plot_color)
                    ax.invert_yaxis()
                    plt.xlabel('Year')
                    plt.ylabel('International Outlook Rank')
                    plt.title(univ_name + f" ({country})")
                    st.pyplot(fig)
                elif relationship == "Industry Income Rank vs Year":
                    fig, ax = plt.subplots()
                    ax.plot(years, industry_income_ranks, color=plot_color)
                    ax.invert_yaxis()
                    plt.xlabel('Year')
                    plt.ylabel('Industry Income Rank')
                    plt.title(univ_name + f" ({country})")
                    st.pyplot(fig)
                elif relationship == "Rank vs Year":
                    fig, ax = plt.subplots()
                    ax.plot(years, ranks, color=plot_color)
                    ax.invert_yaxis()
                    plt.xlabel('Year')
                    plt.ylabel('Rank')
                    plt.title(univ_name + f" ({country})")
                    st.pyplot(fig)
                elif relationship == "Overall Rank vs Year":
                    fig, ax = plt.subplots()
                    ax.plot(years, overall_ranks, color=plot_color)
                    ax.invert_yaxis()
                    plt.xlabel('Year')
                    plt.ylabel('Overall Rank')
                    plt.title(univ_name + f" ({country})")
                    st.pyplot(fig)

            with col2:
                st.write(f"<h3 style='text-align: center;'>{univ_name}'s Data</h3>", unsafe_allow_html=True)
                data = { 
                    'Year': years, 
                    'Teaching Rank':teaching_ranks, 
                    'Research Rank':research_ranks, 
                    'Citations Rank':citations_ranks, 
                    'International Outlook Rank':international_outlook_ranks, 
                    'Industry Income Rank':industry_income_ranks, 
                    'Rank': ranks,
                    'Overall Rank':overall_ranks
                }
                df = pd.DataFrame(data)
                df_styled = df.style.format({'Year': '{:^}', 'Rank': '{:^}', 'Overall Rank': '{:^}', 'Teaching Rank': '{:^}', 'International Outlook Rank': '{:^}', 'Research Rank': '{:^}', 'Citations Rank': '{:^}', 'Industry Income Rank':'{:^}'}).set_properties(**{'text-align': 'center'}).set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}])
                st.table(df_styled)
                st.write('Additionally you can download this data from here')
            
                csv_data = convert_df(df)
                st.download_button(
                    label="Download data as CSV",
                    data=csv_data,
                    file_name=f'{univ_name}_data.csv',
                    mime='text/csv',
                )
                plt.savefig('fig.png')

                with open('fig.png', "rb") as file:
                    st.download_button(
                        label="Download Plot",
                        data=file,
                        file_name=f'{univ_name}_plot.png',
                        mime='image/png',
                    )
            
            st.write("---")
            st.write(f"<h2 style='text-align: center;'>{univ_name}'s Stats</h2>", unsafe_allow_html=True)

            if 1 <= int(np.mean(ranks)) <= 10:
                st.write("<h3 style='text-align: center;'>Reputation: Global Superstar</h3>", unsafe_allow_html=True)
            if 10 <= int(np.mean(ranks)) <= 50:
                st.write("<h3 style='text-align: center;'>Reputation: Highly prestigious university with a global reputation</h3>", unsafe_allow_html=True)
            if 50 <= int(np.mean(ranks)) <= 100:
                st.write("<h3 style='text-align: center;'>Reputation: Internationally recognized university with a strong reputation</h3>", unsafe_allow_html=True)
            if 100 <= int(np.mean(ranks)) <= 200:
                st.write("<h3 style='text-align: center;'>Reputation: Well-regarded university with a broad range of academic strengths</h3>", unsafe_allow_html=True)
            if 200 <= int(np.mean(ranks)) <= 500:
                st.write("<h3 style='text-align: center;'>Reputation: Established university with a strong regional reputation and international outlook</h3>", unsafe_allow_html=True)
            
            rank_type = [ 
                'Teaching Rank', 
                'Research Rank', 
                'Citations Rank', 
                'International Outlook Rank', 
                'Industry Income Rank', 
                'Rank', 
                'Overall Rank'
            ]
            ranks_achieved = [
                int(np.mean(teaching_ranks)),
                int(np.mean(research_ranks)), 
                int(np.mean(citations_ranks)),
                int(np.mean(international_outlook_ranks)), 
                int(np.mean(industry_income_ranks)),
                int(np.mean(ranks)), 
                int(np.mean(overall_ranks))
            ]
            years_of_lowest_ranking = [
                df.loc[df['Teaching Rank'] == max(teaching_ranks), 'Year'].max(),
                df.loc[df['Research Rank'] == max(research_ranks), 'Year'].max(), 
                df.loc[df['Citations Rank'] == max(citations_ranks), 'Year'].max(),
                df.loc[df['International Outlook Rank'] == max(international_outlook_ranks), 'Year'].max(), 
                df.loc[df['Industry Income Rank'] == max(industry_income_ranks), 'Year'].max(),
                df.loc[df['Rank'] == max(ranks), 'Year'].max(),
                df.loc[df['Overall Rank'] == max(overall_ranks), 'Year'].max() 
            ]
            years_of_highest_ranking = [
                df.loc[df['Teaching Rank'] == min(teaching_ranks), 'Year'].max(),
                df.loc[df['Research Rank'] == min(research_ranks), 'Year'].max(), 
                df.loc[df['Citations Rank'] == min(citations_ranks), 'Year'].max(),
                df.loc[df['International Outlook Rank'] == min(international_outlook_ranks), 'Year'].max(), 
                df.loc[df['Industry Income Rank'] == min(industry_income_ranks), 'Year'].max(),
                df.loc[df['Rank'] == min(ranks), 'Year'].max(), 
                df.loc[df['Overall Rank'] == min(overall_ranks), 'Year'].max()            
            ]
            highest_ranks = [
                min(teaching_ranks),
                min(research_ranks), 
                min(citations_ranks),
                min(international_outlook_ranks), 
                min(industry_income_ranks),
                min(ranks),
                min(overall_ranks)
            ]
            lowest_ranks = [
                max(teaching_ranks),
                max(research_ranks), 
                max(citations_ranks),
                max(international_outlook_ranks), 
                max(industry_income_ranks), 
                max(ranks),
                max(overall_ranks)
            ]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("<h4 style='text-align: center;'>Average Ranking</h4>", unsafe_allow_html=True)
                data_for_avg_stats = {'Type': rank_type, 'Rank Acheived': ranks_achieved}
                df_for_avg_ranking = pd.DataFrame(data_for_avg_stats)
                st.table(df_for_avg_ranking)
            
                csv_data = convert_df(df_for_avg_ranking)
                st.download_button(
                    label="Download data as CSV",
                    data=csv_data,
                    file_name=f'{univ_name}_avg_stats_data.csv',
                    mime='text/csv',
                )
            with col2:
                st.write("<h4 style='text-align: center;'>Highest Rankings Achieved</h4>", unsafe_allow_html=True)
                data_for_highest_ranking = { 'Type': rank_type, 'Year':years_of_highest_ranking, 'Rank Acheived': highest_ranks}
                df_for_highest_ranking = pd.DataFrame(data_for_highest_ranking)
                st.table(df_for_highest_ranking)

                csv_data = convert_df(df_for_highest_ranking)
                st.download_button(
                    label="Download data as CSV",
                    data=csv_data,
                    file_name=f'{univ_name}_highest_ranking_data.csv',
                    mime='text/csv',
                )
            with col3:
                st.write("<h4 style='text-align: center;'>Lowest Rankings Achieved</h4>", unsafe_allow_html=True)
                data_for_lowest_ranking = { 'Type': rank_type, 'Year':years_of_lowest_ranking, 'Rank Acheived': lowest_ranks}
                df_for_lowest_ranking = pd.DataFrame(data_for_lowest_ranking)
                st.table(df_for_lowest_ranking)

                csv_data = convert_df(df_for_lowest_ranking)
                st.download_button(
                    label="Download data as CSV",
                    data=csv_data,
                    file_name=f'{univ_name}_lowest_ranking_data.csv',
                    mime='text/csv',
                )
    else:
        st.warning('⚠️ To Get Started, Please select a university from the dropdown menu')

    st.write("---")
    st.write("<h2 style='text-align: center;'>Compare 2 Universities Stats ⚔️</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    visibility_of_c1 = True
    visibility_of_c2 = True

    with col1:
        univ1 = st.selectbox("Select First University, (or Alternatively you can type your desired university, it will display if it will be present in the dataset)", univ_names)
        if univ1 == "Select University":
            st.warning('⚠️ To Get Started, Please select a university from the dropdown menu')
        else:
            univ1_years = []
            univ1_teaching_ranks = []
            univ1_research_ranks = []
            univ1_citations_ranks = []
            univ1_international_outlook_ranks = []
            univ1_industry_income_ranks = []
            univ1_ranks = []
            univ1_overall_ranks = []
            for key, df in dfs.items():
                univ_df1 = df[df['name'] == univ1]
                if not univ_df1.empty:
                    country1 = univ_df1['location'].iloc[0]
                    year1 = key.split("_")[0]
                    teaching_rank1 = univ_df1['scores_teaching_rank'].iloc[0]
                    research_rank1 = univ_df1['scores_research_rank'].iloc[0]
                    citations_rank1 = univ_df1['scores_citations_rank'].iloc[0]
                    international_outlook_rank1 = univ_df1['scores_international_outlook_rank'].iloc[0]
                    industry_income_rank1 = univ_df1['scores_industry_income_rank'].iloc[0]
                    rank1 = univ_df1['rank'].iloc[0]
                    overall_rank1 = univ_df1['scores_overall_rank'].iloc[0]
                    rank1 = str(rank1)
                    rank1 = re.findall(r'\d+', rank1)
                    
                    if rank1 == []:
                        st.warning("😔 Rank Undefined, Pls select other University")
                        visibility_of_c1 = False
                    
                    if visibility_of_c1:
                        rank1 = rank1[0]
                        univ1_years.append(year1)
                        univ1_teaching_ranks.append(int(teaching_rank1))
                        univ1_research_ranks.append(int(research_rank1))
                        univ1_citations_ranks.append(int(citations_rank1))
                        univ1_international_outlook_ranks.append(int(international_outlook_rank1))
                        univ1_industry_income_ranks.append(int(industry_income_rank1))
                        univ1_ranks.append(int(rank1))
                        univ1_overall_ranks.append(int(overall_rank1))

    with col2:
        univ2 = st.selectbox("Select Second University, (or Alternatively you can type your desired university, it will display if it will be present in the dataset)", univ_names)
        
        if univ2 == "Select University":
            st.warning('⚠️ To Get Started, Please select a university from the dropdown menu')
        
        else:
            univ2_years = []
            univ2_teaching_ranks = []
            univ2_research_ranks = []
            univ2_citations_ranks = []
            univ2_international_outlook_ranks = []
            univ2_industry_income_ranks = []
            univ2_ranks = []
            univ2_overall_ranks = []
            for key, df in dfs.items():
                univ_df2 = df[df['name'] == univ2]
                if not univ_df2.empty:
                    country2 = univ_df2['location'].iloc[0]
                    year2 = key.split("_")[0]
                    rank2 = univ_df2['rank'].iloc[0]
                    overall_rank2 = univ_df2['scores_overall_rank'].iloc[0]
                    teaching_rank2 = univ_df2['scores_teaching_rank'].iloc[0]
                    international_outlook_rank2 = univ_df2['scores_international_outlook_rank'].iloc[0]
                    industry_income_rank2 = univ_df2['scores_industry_income_rank'].iloc[0]
                    research_rank2 = univ_df2['scores_research_rank'].iloc[0]
                    citations_rank2 = univ_df2['scores_citations_rank'].iloc[0]
                    rank2 = str(rank2)
                    rank2 = re.findall(r'\d+', rank2)
                    
                    if rank2 == []:
                        st.warning("😔 Rank Undefined, Please select other University")
                        visibility_of_c2 = False
                    
                    if visibility_of_c2:
                        rank2 = rank2[0]
                        univ2_years.append(year2)
                        univ2_teaching_ranks.append(int(teaching_rank2))
                        univ2_research_ranks.append(int(research_rank2))
                        univ2_citations_ranks.append(int(citations_rank2))
                        univ2_international_outlook_ranks.append(int(international_outlook_rank2))
                        univ2_industry_income_ranks.append(int(industry_income_rank2))
                        univ2_ranks.append(int(rank2))
                        univ2_overall_ranks.append(int(overall_rank2))

    col1, col2 = st.columns(2)
    if univ1 != "Select University" and univ2 != "Select University":
        if univ1 == univ2:
            st.write("<h4 style='text-align: center;'>Oops, You selected same Universities 😆</h4>", unsafe_allow_html=True)
        else:
            with col1:
                if visibility_of_c1:
                    st.write(f"<h4>{univ1} ({country1})</h4>", unsafe_allow_html=True)
                    st.write("<h4>➡️Average Ranking</h4>", unsafe_allow_html=True)
                    st.write(f"<h5>Teaching Rank: {int(np.mean(univ1_teaching_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Research Rank: {int(np.mean(univ1_research_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Citations Rank: {int(np.mean(univ1_citations_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>International Outlook Rank: {int(np.mean(univ1_international_outlook_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Industry Income Rank: {int(np.mean(univ1_industry_income_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Rank: {int(np.mean(univ1_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Overall Rank: {int(np.mean(univ1_overall_ranks))}</h5>", unsafe_allow_html=True)
                    
                    st.write("<h4>➡️Highest Rankings Achieved</h4>", unsafe_allow_html=True)
                    st.write(f"<h5>Teaching Rank Achieved: {min(univ1_teaching_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Research Rank Achieved: {min(univ1_research_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Citations Rank Achieved: {min(univ1_citations_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>International Outlook Rank Achieved: {min(univ1_international_outlook_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Industry Income Rank Achieved: {min(univ1_industry_income_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Rank Achieved: {min(univ1_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Overall Rank Achieved: {min(univ1_overall_ranks)}</h5>", unsafe_allow_html=True)
            
            with col2:
                if visibility_of_c2:
                    st.write(f"<h4>{univ2} ({country2})</h4>", unsafe_allow_html=True)
                    st.write("<h4>➡️Average Ranking</h4>", unsafe_allow_html=True)
                    st.write(f"<h5>Teaching Rank: {int(np.mean(univ2_teaching_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Research Rank: {int(np.mean(univ2_research_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Citations Rank: {int(np.mean(univ2_citations_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>International Outlook Rank: {int(np.mean(univ2_international_outlook_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Industry Income Rank: {int(np.mean(univ2_industry_income_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Rank: {int(np.mean(univ2_ranks))}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Overall Rank: {int(np.mean(univ2_overall_ranks))}</h5>", unsafe_allow_html=True)

                    st.write("<h4>➡️Highest Rankings Achieved</h4>", unsafe_allow_html=True)
                    st.write(f"<h5>Teaching Rank Achieved: {min(univ2_teaching_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Research Rank Achieved: {min(univ2_research_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Citations Rank Achieved: {min(univ2_citations_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>International Outlook Rank Achieved: {min(univ2_international_outlook_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Industry Income Rank Achieved: {min(univ2_industry_income_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Rank Achieved: {min(univ2_ranks)}</h5>", unsafe_allow_html=True)
                    st.write(f"<h5>Overall Rank Achieved: {min(univ2_overall_ranks)}</h5>", unsafe_allow_html=True)
    
    st.write("---")
    country_counts = {}
    for year, df in dfs.items():
        country_counts[year] = df['location'].value_counts().to_dict()

    # Aggregating the counts over the years
    aggregated_counts = {}
    for counts in country_counts.values():
        for country, count in counts.items():
            if country not in aggregated_counts:
                aggregated_counts[country] = 0
            aggregated_counts[country] += count

    # Sorting the countries by the number of top-ranked universities
    sorted_countries = sorted(aggregated_counts.items(), key=lambda x: x[1], reverse=True)
    countries = [item[0] for item in sorted_countries]
    counts = [item[1] for item in sorted_countries]

    st.write("<h3 style='text-align: center;'>Countries with the Highest Number of Top-Ranked Universities (2011-2023)</h3>", unsafe_allow_html=True)

    # Plotting the results
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.bar(countries, counts, color='skyblue')
    ax.set_xticks(countries)
    ax.set_xticklabels(countries, rotation=45, ha='right')
    ax.set_title('Countries with the Highest Number of Top-Ranked Universities (2011-2023)')
    ax.set_xlabel('Country')
    ax.set_ylabel('Number of Top-Ranked Universities')
    fig.tight_layout()
    st.pyplot(fig)

    st.write("---")

    st.write("<h3 style='text-align: center;'>Top 10 Countries with the Highest Number of Top-Ranked Universities vs Year</h3>", unsafe_allow_html=True)
    year = st.slider('Choose A Year', 2011, 2023, 2011)
    years = {
        2011: '2011_rankings',
        2012: '2012_rankings',
        2013: '2013_rankings',
        2014: '2014_rankings',
        2015: '2015_rankings',
        2016: '2016_rankings',
        2017: '2017_rankings',
        2018: '2018_rankings',
        2019: '2019_rankings',
        2020: '2020_rankings',
        2021: '2021_rankings',
        2022: '2022_rankings',
        2023: '2023_rankings'
    }
    latest_data = dfs[years[year]]
    country_counts = latest_data['location'].value_counts().head(10)
    countries = country_counts.index.tolist()
    counts = country_counts.values.tolist()
    fig = go.Figure(data=[go.Bar(x=countries, y=counts)])
    fig.update_layout(
        title=f'Top 10 Countries with the Highest Number of Top-Ranked Universities ({year})',
        xaxis_title='Country',
        yaxis_title='Number of Universities'
    )
    st.plotly_chart(fig)


def dataset_report():
    @st.cache_data
    def generate_report(df):
        profile = ProfileReport(df, title="Profiling Report")
        return profile.to_html()

    df_2011 = pd.read_csv('2011_rankings.csv')
    df_2012 = pd.read_csv('2012_rankings.csv')
    df_2013 = pd.read_csv('2013_rankings.csv')
    df_2014 = pd.read_csv('2014_rankings.csv')
    df_2015 = pd.read_csv('2015_rankings.csv')
    df_2016 = pd.read_csv('2016_rankings.csv')
    df_2017 = pd.read_csv('2017_rankings.csv')
    df_2018 = pd.read_csv('2018_rankings.csv')
    df_2019 = pd.read_csv('2019_rankings.csv')
    df_2020 = pd.read_csv('2020_rankings.csv')
    df_2021 = pd.read_csv('2021_rankings.csv')
    df_2022 = pd.read_csv('2022_rankings.csv')
    df_2023 = pd.read_csv('2023_rankings.csv')
    combined_df = pd.concat([df_2011, df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022, df_2023], ignore_index=True)
    components.html(generate_report(combined_df), height=800, width=800, scrolling=True)

def chat_with_dataset():
    from langchain.agents import AgentType
    from langchain.agents import create_pandas_dataframe_agent
    from langchain.callbacks import StreamlitCallbackHandler
    from langchain.chat_models import ChatOpenAI
    import streamlit as st
    import pandas as pd
    import os


    file_formats = {
        "csv": pd.read_csv,
        # ... other file formats
    }

    def clear_submit():
        """
        Clear the Submit Button State
        Returns:

        """
        st.session_state["submit"] = False

    @st.cache_data
    def load_data(file_name):
        """
        Load data from the selected file.
        """
        try:
            return pd.read_csv(file_name)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            return None

    st.title("Chat with your dataset")
    st.info("Asking one question at a time will result in a better output")

    # Generate file names based on the years 2011 to 2023
    available_files = [f"{year}_rankings.csv" for year in range(2011, 2024)]

    # Dropdown for selecting a file
    selected_file = st.selectbox("Select a Data file", available_files, help="Choose a file", on_change=clear_submit)

    df = load_data(selected_file)  # Load the selected file

    if df is None:  # Check if df is None before proceeding
        st.warning("No data file selected or there was an error in loading the data.")
        return  # Exit the function early if df is None

    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    
    # st.sidebar.info("If you face a KeyError: 'content' error, Press the clear conversation history button")
    if "messages" not in st.session_state or st.sidebar.button("Clear conversation history"):
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    
    # Display previous chat messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder="What is this data about?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        # Check if OpenAI API key is provided
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        llm = ChatOpenAI(
            temperature=0, model="gpt-3.5-turbo-0613", openai_api_key=openai_api_key, streaming=True
        )

        pandas_df_agent = create_pandas_dataframe_agent(
            llm,
            df,
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
            handle_parsing_errors=True,
        )

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = pandas_df_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)


page_names_to_funcs = {
    "Home Page": home_page,
    "Learn the Process": learning_the_process,
    "Analysis": analysis,
    "Dataset Report": dataset_report,
    "Chat with Dataset": chat_with_dataset,
}

page_name = st.sidebar.selectbox("Choose a Page to visit", page_names_to_funcs.keys())
page_names_to_funcs[page_name]()
st.sidebar.success("Select a Page to visit")

with st.sidebar:
    with st.expander("See Datasets"):
        chosen_year = st.selectbox("Choose a Year", [year for year in range(2011, 2024)])
        dataset_file = f"{chosen_year}_rankings.csv"
        dataset = pd.read_csv(dataset_file)  # Load the data into a DataFrame
        st.dataframe(dataset)
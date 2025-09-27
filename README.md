# Data Science, AI & ML Job Salaries (2020–2025)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GdodakisEmmanouil/Data-Science-AI-ML-Job-Salaries-2020-2025/blob/main/Data-Science-AI-ML-Job-Salaries-2020-2025/eda.ipynb)

This project explores job salaries in the fields of Data Science, Artificial Intelligence, and Machine Learning using real-world data.

The dataset was compiled through a combination of market research and publicly available sources, including the AIJobs salary survey (CC0 license), 365DataScience, Payscale, KDnuggets, ZipRecruiter, and others. It reflects real-world compensation trends from around the globe. 

The dataset contains a structured table of salary-related information for jobs in Data Science, Artificial Intelligence (AI), and Machine Learning (ML) from 2020 to 2025. Each row represents a single job record with the following fields:

📅 `work_year` :
 The year in which the salary was paid.

🎓 `experience_level` :
 The experience level of the employee during the year:
- EN: Entry-level / Junior
- MI: Mid-level / Intermediate
- SE: Senior-level / Expert
- EX: Executive-level / Director

💼 `employment_type` :
 Type of employment for the role:
- PT: Part-time  
- FT: Full-time  
- CT: Contract  
- FL: Freelance  

🧑‍💻 `job_title` :
 The title or role held during the year.

💰 `salary` :
 Total gross salary paid for the year (in original currency).

💱 `salary_currency` :
 ISO 4217 currency code of the original salary (e.g., USD, EUR, INR).

💵 `salary_in_usd` :
 Salary converted to USD based on average exchange rate for the respective year. Source: BIS and central banks.

🌍 `employee_residence` :
 Country code (ISO 3166) of the employee's primary residence during the work year.

🏠 `remote_ratio` :
 The amount of work done remotely:
- 0: No remote work (<20%)
- 50: Hybrid / Partially remote
- 100: Fully remote (>80%)

🗺️ `company_location` :
 ISO 3166 country code of the employer's main office or contracting branch.

🏢 `company_size` :
 Company size based on number of employees:
- S: Small (fewer than 50 employees)
- M: Medium (50–250 employees)
- L: Large (more than 250 employees)

## 📂 Project Structure
- `eda.ipynb`: Jupyter notebook with exploratory data analysis.
- `functions.py`: Functions that we created.
- `requirements.txt`: List of Python packages our project needs to run.
- `data`:
  - `salaries.csv`: The original dataset.
  - `cleaned_salaries_data.csv` : The data we used for the analysis.

## 📊 Goals
The primary objective of this analysis is to uncover evolving salary patterns and identify key factors that influence earnings within these rapidly growing technology fields.

Through this analysis, we aim to extract meaningful insights such as:
- Assess salary variations across different factors such as company size, geographic location, employment type, and experience level.
- Identify the highest-paying roles within the AI/ML and Data Science job markets.
- Evaluate the impact of remote work on salary levels,
- Explore salary trends over time (2020–2025) to highlight emerging patterns, market shifts, and the evolution of compensation across the industry.

These insights will help job seekers, employers, and industry analysts better understand the dynamics of compensation in the AI/ML and data science job market.



---
## 🧠 Author
Created by [Gdontakis Emmanouil] 

<img width="15" height="15" alt="image" src="https://github.com/user-attachments/assets/629cee0b-55c0-4c44-8abb-ac62fe5d296e" /> [LinkedIn](https://linkedin.com/in/gdodakis-emmanouil)  

[GitHub](https://github.com/GdodakisEmmanouil)

Student at Athens University of Economics and Business (AUEB), Statistics

# **Comprehensive Statistical Analysis of Cavy Lifetime Dataset** 🦦

## **Project Structure** 📂
- `analysis/`: Contains the Jupyter notebook with the analysis.
    - `analysis.ipynb`: The Jupyter notebook containing the analysis workflow.
    - `config.py`: The Python script containing configuration variables used in the notebook.
- `dataset/`: This directory contains the dataset file used in the analysis.
    - `cavy-dataset.csv`: The CSV file with the cavy lifetime data.
- `venv/`: A directory for the virtual environment containing project-specific Python packages.
- `README.md`: The Markdown file providing an overview of the project.

## **Project Overview** 🔎
This university project is dedicated to the statistical analysis of lifetime data of two groups of cavies (guinea pigs): 
a ***control group*** and a ***bacilli-infected group***. The purpose is to understand the impact of bacilli infection on 
the lifetimes of the subjects and draw meaningful conclusions from the data.

## **Objectives** 📚
- **Data Exploration** 📂: Understand the basic structure and distribution of the data.
- **Statistical Analysis** 📊: Apply various statistical tests to compare the two groups and understand the characteristics of their lifetimes.
- **Distribution Fitting** 📈: Fit different distributions to the data and visualize them to understand the underlying patterns.
- **Hypothesis Testing** 🧮: Conduct hypothesis tests to statistically infer the impact of bacilli on cavy lifetimes.

## **Tools and Libraries Used** 🛠
- **`Python`** 🐍: The main programming language used for analysis.
- **`Pandas`** 🐼: For data manipulation and analysis.
- **`NumPy`** 🔢: For numerical operations.
- **`Matplotlib`** 📉: For creating static, interactive, and animated visualizations in Python.
- **`SciPy`** 🎓: For scientific and technical computing.

## **Analysis Tasks and Descriptions** 📝
1. 💾 Load the data file and separate the observed variable into the respective two observed groups. 
Briefly describe the data and the problem under investigation. Estimate the mean, variance, and median of 
the respective distributions separately for each group.
2. 📊 Estimate the density and distribution function for each group separately using histograms and the 
empirical distribution function.
3. 📈 Find the closest distribution for each group separately: estimate the parameters of the normal, 
exponential, and uniform distributions. Enter the corresponding densities with the estimated parameters 
into the histogram charts. Discuss which of the distributions best matches the observed data.
4. 🗂️ Generate a random sample of 100 values from the distribution you have chosen as the closest for each 
group separately, with the parameters estimated in the previous point. Compare the histogram of simulated 
values with the observed data.
5. 🧮 Calculate a two-sided 95% confidence interval for the mean separately for each group.
6. 🖋️ Test the hypothesis at the 5% significance level for each group separately to see if the mean value is 
equal to the value K (parameter of the task), against a two-sided alternative. You may use either the 
result from the previous point or the output from the respective built-in function of your software.
7. 🔍 Test at the 5% significance level whether the observed groups have the same mean. Choose the type of 
test and alternatives to best correspond with the nature of the problem under investigation.

## **Conclusions and Reflections** 🌟
This project was an extensive exploration of both basic and advanced concepts in statistical analysis. 
Throughout the analysis, we have:
- 📄 Explored and visualized the data, providing a clear understanding of its structure and distribution.
- 🧮 Applied various statistical methods to estimate key parameters such as mean, variance, and median.
- 📊 Fitted different distributions to the data to identify underlying patterns and selected the best-fitting models.
- 🤔 Conducted hypothesis tests to draw meaningful inferences about the impact of bacilli infection on cavy lifetimes.
- 📐 Generated confidence intervals and performed comparative analysis between the control and bacilli-infected groups.

Through this project, we gained hands-on experience with essential statistical tools and libraries in Python, such as `Pandas`, `NumPy`, `Matplotlib`, and `SciPy`. 
We also developed a deeper understanding of statistical concepts and their practical applications in real-world data analysis scenarios.
Overall, this project provided a comprehensive learning experience, enhancing our ability to perform detailed statistical analyses and draw significant conclusions from complex datasets.
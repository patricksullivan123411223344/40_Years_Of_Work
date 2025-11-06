40 Years of Work

Author: Patrick Sullivan
Project Type: Independent Research / Data Visualization

Overview:
This project is an independent economic cisualization exploring the divergence between worker compensation, productivity, and executive pay across the post-WWII era. It began as a personal deep-dive into long-term labor data, built from scratch using publicly available sources and entirely coded, merged, and cleaned by hand. 

The purpose: To visualize how the American economy's growth and proudctivity have evolved relative to wages and corporate profit distribution, turning decades of raw numbers into a readable story. 

Data Sources:
All datasets are authentic and publicly available:

1. Federal Reserve Economic Data (FRED)
    - Demographic & Macroeconomic wage/productivity metrics
    - 1980 - Present
2. Economic Policy Institute (EPI)
    - Net productivity, real hourly compensation, CEO-to-worker pay ratio
    - 1948 - Present
3. Bureau of Labor Statistics (BLS)
    - Supplemental workforce & employment data
    - 1980 - Present

Each dataset was standardized to consistent date formats and units, merged on a shared time index, and verified for continuity. 

Tech Stack:
- Python 3.14, pandas, numpy, matplotlib, plotly
- Juypter Notebook for analysis and visualization
- Git + GitHub for version control

Data Processing:
1. Raw CSVs imported directly from FRED/EPI endpoints.
2. Columns normalized, commas removed, numeric types casted. 
3. Missing values handled via forwar-fill/interpolation.
4. Time indicies unified to yearly intervals. 
5. Validation against published aggregates. 

Visualizations: 
- Wages vs. Productivity Gap (1948-2025)
- CEO-to-Worker Ratio Trendline
- Decade-by-Decade Productivity Output Per Hour
- Demographic and Real Compensation Overlay

Interactive plots (plotly) coming soon. 

Purpose:
This isn't coursework but instead personal research designed to bridge technical data analysis with macroeconomic storytelling. The goal is to build a visually rich, historically accurate model of labor dynamics that can be expanded into formal lab-grade work or future academic publication. 
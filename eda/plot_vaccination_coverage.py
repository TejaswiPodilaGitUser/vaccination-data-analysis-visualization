import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_vaccination_coverage(coverage_df, ax=None):
    if ax is None:
        ax = plt.gca()  # Get current axis if no axis is provided
    
    # Extract the year from the datetime column (if it's in datetime64 format)
    coverage_df['year'] = pd.to_datetime(coverage_df['year']).dt.year

    # Sort the data by year
    coverage_df = coverage_df.sort_values(by='year')

    # Plot the data
    sns.barplot(x='year', y='coverage_percentage', data=coverage_df, ax=ax)

    # Set title and labels
    ax.set_title('Vaccination Coverage by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Coverage Percentage')

    # Rotate x-axis labels to avoid overlap
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    # Explicitly set the ticks to fix the warning
    ax.set_xticks(range(len(coverage_df['year'].unique())))
    ax.set_xticklabels(coverage_df['year'].unique(), rotation=45, ha='right')

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

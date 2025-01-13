import seaborn as sns
import matplotlib.pyplot as plt

def plot_region_disparities(coverage_df, users_df, ax=None):
    if ax is None:
        ax = plt.gca()

    # Merging the data correctly
    merged_df = coverage_df.merge(users_df[['user_id', 'region']], on='user_id', how='left')
    
    # Group by region and calculate mean coverage
    region_coverage = merged_df.groupby('region')['coverage_percentage'].mean().reset_index()
    
    # Sort regions by average coverage percentage
    region_coverage = region_coverage.sort_values(by='coverage_percentage', ascending=False)

    # Debugging information
    print("Region coverage data (sorted):", region_coverage.head())

    # Create the plot with a different color palette
    sns.barplot(
        x='region', 
        y='coverage_percentage', 
        data=region_coverage, 
        ax=ax, 
        palette='Set3',  # Using a different palette
        legend=False     # Suppress legend to avoid future warnings
    )
    
    # Ensure that the ticks are explicitly set
    ax.set_xticks(range(len(region_coverage['region'])))
    ax.set_xticklabels(region_coverage['region'], rotation=45, ha='right')

    ax.set_title('Vaccination Coverage by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Average Coverage Percentage')

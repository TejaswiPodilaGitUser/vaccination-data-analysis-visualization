import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(df, ax=None):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    
    # Calculate the correlation matrix
    correlation_matrix = numeric_df.corr()
    
    # Plot the heatmap
    if ax is None:
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
        plt.title('Correlation Heatmap')

        # Rotate the tick labels for both axes
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=45)
    else:
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True, ax=ax)
        ax.set_title('Correlation Heatmap')

        # Rotate the tick labels for both axes
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        ax.set_yticklabels(ax.get_yticklabels(), rotation=45)


import seaborn as sns
import matplotlib.pyplot as plt

def plot_disease_incidence(incidence_df, ax=None):
    if ax is None:
        ax = plt.gca()

    # Plotting disease incidence (for example, over time or by region)
    sns.lineplot(x='year', y='incidence_rate', data=incidence_df, ax=ax)

    ax.set_title('Disease Incidence Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Incidence Rate')

    # Rotate x-axis labels to avoid overlap
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    # Adjust layout to prevent label cutoff
    plt.tight_layout()


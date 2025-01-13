import matplotlib.pyplot as plt
from data.cleaned.data_cleaning import clean_data
from eda.plot_vaccination_coverage import plot_vaccination_coverage
from eda.plot_disease_incidence import plot_disease_incidence
from eda.plot_region_disparities import plot_region_disparities
from eda.plot_correlation_heatmap import plot_correlation_heatmap

def main():
    # Clean data
    users_df, coverage_df, incidence_df, reported_cases_df = clean_data()

    # Create a figure and axes for subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # EDA Visualizations
    plot_vaccination_coverage(coverage_df, ax=axes[0, 0])
    plot_disease_incidence(incidence_df, ax=axes[0, 1])
    plot_region_disparities(coverage_df, users_df, ax=axes[1, 0])
    plot_correlation_heatmap(coverage_df, ax=axes[1, 1])

    # Set the window title
    fig.canvas.manager.set_window_title("Vaccination Data Analysis Dashboard")

    # Set the overall figure title
    fig.suptitle("Vaccination Data Analysis", fontsize=18, fontweight="bold", y=0.95)

    # Adjust layout for better spacing
    plt.subplots_adjust(top=0.88, hspace=0.35, wspace=0.35)

    # Display the plots
    plt.show()

if __name__ == "__main__":
    main()

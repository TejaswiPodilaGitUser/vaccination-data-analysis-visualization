# List of predefined descriptions for antigen, coverage, and disease
antigen_descriptions = [
    "Diphtheria Toxoid", "Hepatitis B Vaccine", "Measles, Mumps, Rubella",
    "Poliovirus Vaccine", "Haemophilus Influenzae Type B", "Tetanus Toxoid",
    "Rotavirus Vaccine", "Influenza Vaccine", "Yellow Fever Vaccine",
    "Meningococcal Vaccine", "Human Papillomavirus Vaccine", "Pneumococcal Vaccine",
    "BCG Vaccine", "Hepatitis A Vaccine", "Typhoid Vaccine",
]

coverage_descriptions = [
    "Fully administered as per protocol", "Partially administered due to limited stock",
    "Administered as emergency vaccination", "Administered in targeted high-risk areas",
    "Routine vaccination in general population", "Campaign-based vaccination",
    "Vaccination during outbreaks", "Administered with awareness program",
    "Administered at community health centers", "Administered with mobile vaccination units",
    "Vaccination for border health management", "Routine vaccination for children under 5",
    "Administered with additional boosters", "Emergency vaccination for travelers",
    "Vaccination for health workers",
]

disease_descriptions = [
    "Cholera", "Diphtheria", "Measles", "Polio", "Yellow Fever", "Meningitis", "Malaria",
    "Typhoid", "Tuberculosis", "Hepatitis A", "Hepatitis B", "Pneumonia", "Rotavirus Diarrhea",
    "HIV/AIDS", "Tetanus",
]
# Define the constant for 'South Korea'
SOUTH_KOREA = 'South Korea'
SRILANKA = 'Sri Lanka'
NEWZELAND = 'New Zealand'
HONGKONG = 'Hong Kong'
UK = 'United Kingdom'

# Now use the constant instead of the literal string
regions = [
    'North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania',
    'India', 'Japan', 'Australia', 'China', 'Singapore', 
    'Malaysia', 'Indonesia', 'Philippines', 'Russia'
]


# Update affected countries as well to use the constant
affected_countries = {
    'North America': ['USA', 'Canada', 'Mexico'],
    'Europe': ['Italy', 'Spain', 'United Kingdom', 'Germany', 'France', 'Russia', 'Sweden', 'Belgium'],
    'Asia': ['India', 'China', 'Japan', SOUTH_KOREA, 'Indonesia', 'Bangladesh', 'Pakistan', 'Turkey'],
    'South America': ['Brazil', 'Argentina', 'Chile', 'Peru', 'Colombia'],
    'Africa': ['South Africa', 'Nigeria', 'Kenya', 'Egypt', 'Morocco'],
    'Oceania': ['Australia', 'New Zealand', 'Papua New Guinea'],
    'India': ['India'],
    'Japan': ['Japan'],
    'Australia': ['Australia'],
    'China': ['China'],
    SOUTH_KOREA: [SOUTH_KOREA],
    'Singapore': ['Singapore'],
    'Malaysia': ['Malaysia'],
    'Thailand': ['Thailand'],
    'Vietnam': ['Vietnam'],
    'Nepal': ['Nepal'],
    SRILANKA: [SRILANKA],
    'Bangladesh': ['Bangladesh'],
    NEWZELAND: [NEWZELAND],
    'Indonesia': ['Indonesia'],
    'Philippines': ['Philippines'],
    HONGKONG: [HONGKONG],
    'Taiwan': ['Taiwan'],
    'Mongolia': ['Mongolia'],
    UK: [UK],
    'Germany': ['Germany'],
    'France': ['France'],
    'Italy': ['Italy'],
    'Spain': ['Spain'],
    'Russia': ['Russia'],
    'Greece': ['Greece'],
    'Portugal': ['Portugal']
}


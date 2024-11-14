
# Immo Eliza Deployment

This repository hosts the deployment of a real estate price prediction model for Immo Eliza. The application uses Streamlit for the user interface, allowing users to interact with the model and obtain predictions based on real estate data.

## Repository Structure

- **app.py**: The main application file. This script runs the Streamlit app locally, allowing users to interact with the model for predicting property prices.
- **price_stats.json**: A JSON file containing statistical data on real estate prices, used to enhance prediction insights.
- **random_forest_model.joblib**: The trained Random Forest model, saved in joblib format for loading and predictions.
- **requirements.txt**: A list of Python dependencies required to run the app, including Streamlit and other libraries for model loading and data processing.

## Getting Started

### Prerequisites

Ensure you have Python 3.7 or later installed, along with `pip` for managing dependencies.

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/IzaMacBor/immo-eliza-deployment.git
    cd immo-eliza-deployment
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To start the Streamlit app locally, run:

```bash
streamlit run app.py
```

This will launch a local server. Open the provided URL (typically `http://localhost:8501`) in your web browser to interact with the application.

## Usage

- **Price Prediction**: Enter relevant real estate details to get an estimated price based on the trained Random Forest model.
- **Statistics**: View additional pricing statistics for insights into the model's predictions.

## File Descriptions

- **app.py**: Hosts the Streamlit app for user input, model predictions, and result visualization.
- **price_stats.json**: Stores supporting statistical data for context in predictions.
- **random_forest_model.joblib**: Serialized Random Forest model file for predictions.
- **requirements.txt**: Dependencies required to run the app smoothly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

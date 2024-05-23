


# 🎬 Movie Recommendation System using Machine Learning

Welcome to the Movie Recommendation System! This project demonstrates a content-based recommendation model using machine learning, hosted with Streamlit.

## Overview

This project aims to recommend movies based on the content of previously watched movies. It uses a content-based filtering approach to suggest movies that are similar to the ones you have liked before.

## Features

- **Interactive User Interface**: Powered by Streamlit, allowing users to easily select movies and get recommendations.
- **Content-Based Filtering**: Recommends movies based on their content (e.g., genre, director, cast).
- **Real-Time Recommendations**: Provides instant movie recommendations as you select different movies.

## Installation

### Prerequisites

Ensure you have Python 3.9 or higher installed on your system. You also need to have `pip` for package management.

### Setup

1. **Clone the Repository**

  
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system


2. **Create a Virtual Environment**

 
   python -m venv myenv
  

3. **Activate the Virtual Environment**

   - **Windows**

    
     myenv\Scripts\activate
     

   - **macOS/Linux**

     
     source myenv/bin/activate
     

4. **Install Dependencies**

  
   pip install -r requirements.txt


## Usage

1. **Run the Streamlit App**


   streamlit run app.py


2. **Open the Web Application**

   Once the app is running, open your web browser and navigate to `http://localhost:8501`.

3. **Interact with the App**

   - Select a movie from the dropdown menu.
   - The app will display the recommended movies based on the selected movie.

## Project Structure


movie-recommendation-system/
├── artificats/
│   ├── movie_list.pkl
│   └── similarity.pkl
├── myenv/
├── app.py
├── requirements.txt
└── README.md


- `artificats/`: Contains the pickled files for the movie list and similarity matrix.
- `app.py`: The main Streamlit application.
- `requirements.txt`: Lists all the dependencies required for the project.
- `README.md`: This file.

## Data

The data used for this project includes a list of movies and their features (e.g., genres, directors). This data is preprocessed and stored in `movie_list.pkl` and `similarity.pkl`.

## Dependencies

- **Streamlit**: For creating the web interface.
- **Pandas**: For data manipulation.
- **Pickle**: For loading the preprocessed data.

## Acknowledgements

This project was inspired by various machine learning and recommendation system tutorials available online. Special thanks to the open-source community for their invaluable resources and support.

## License

This project is licensed under the MIT License.

---

Feel free to contribute to this project by submitting issues or pull requests. Happy coding! 🎉
```


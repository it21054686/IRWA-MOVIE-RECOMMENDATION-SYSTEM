import pickle
import streamlit as st
import requests

# add stylings
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# poster

def poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e29500185edb84e31a6780b0c7c0f7dc&language=en-US&page=1".format(
        movie_id)
    d = requests.get(url)
    d = data.json()
    poster_path = data['poster_path']  # this will only a part form the path
    # to define the full path
    path = "https://image.tmdb.org/t/p/w500/" + poster_path
    
    return path

# recommend function

def rec(movie):
    indx = movies[movies['title'] == movie].indx[0]
    distances = sorted(
        list(enumerate(similarity[indx])), reverse=True, key=lambda x: x[1])
    RecMovieNames = []
    RecMoviePoster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        RecMoviePoster.append(fetch_poster(movie_id))
        RecMovieNames.append(movies.iloc[i[0]].title)
    return RecMovieNames, RecMoviePoster


st.header("Movie Recommendation System")

movies = pickle.load(
    open('C:/Users/DELL/Downloads/movieR/artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(
    open('C:/Users/DELL/Downloads/movieR/artifacts/similarity.pkl', 'rb'))


MovieList = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    MovieList
)

if st.button('Show recommendations'):
    RecMovieNames, RecMoviePoster = recommend(
        selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(RecMoviePoster[0])
        st.text(RecMovieNames[0])

    with col2:
        
        st.image(RecMoviePoster[1])
        st.text(RecMovieNames[1])

    with col3:
        
        st.image(RecMoviePoster[2])
        st.text(RecMovieNames[2])

    with col4:
        
        st.image(RecMoviePoster[3])
        st.text(RecMovieNames[3])

    with col5:
        
        st.image(RecMoviePoster[4])
        st.text(RecMovieNames[4])
        
else:
    st.write("No Movies are visible Yet")







# dictionary to store movie feedback
movie_feedback = {}
st.markdown(
    """
<style>
    .stApp {
        background-color: #f0f0f0;
    }
    .stTitle {
        color: #333;
    }
    .stTextInput input {
        background-color: black;
    }
    .stTextArea textarea {
        background-color: black;
    }
    .stButton button {
        background-color: #0074cc;
        color: white;
    }
    .stButton button:hover {
        background-color: #0056a0;
    }
</style>
    """,
    unsafe_allow_html=True,
)
 

# Streamlit app title
st.title("Movie Feedback ")

 

# Input for movie name
movie_name = st.text_input("Enter the movie name:")

 

# Input for feedback
feedback = st.text_area("Provide your feedback:")

slider_value = st.slider("Select a value:", 0, 10, 5)

 

# Button to submit feedback
if st.button("Submit Feedback"):
    if movie_name and feedback:
        movie_feedback[movie_name] = feedback
        st.success("Feedback submitted successfully!")
    else:
        st.warning("Please enter both movie name and feedback.")

 

# Display all feedback
st.header("Feedback for Movies")
for movie, user_feedback in movie_feedback.items():
    st.subheader(movie)
    st.write(user_feedback)
    st.write(f"You rated the recommendations as: {slider_value}")
    st.subheader("Thank you for your feedback! 👍")



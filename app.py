import streamlit as st
import datetime

# Set the title of the app
st.title("Fitness Planner")

# Get user input
st.header("User Information")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120, value=25)
weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=70)
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)

# Get fitness goals
st.header("Fitness Goals")
goal = st.selectbox("Select your fitness goal", ["Lose Weight", "Build Muscle", "Improve Stamina", "Maintain Fitness"])
workout_days = st.multiselect("Days you can work out", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
start_date = st.date_input("Start Date", datetime.date.today())

# Get additional preferences
st.header("Preferences")
preferred_workout = st.multiselect("Preferred Workout Type", ["Cardio", "Strength Training", "HIIT", "Yoga", "Pilates"])
dietary_restrictions = st.text_area("Any dietary restrictions?")

# Submit button
if st.button("Generate Fitness Plan"):
    st.subheader("Your Fitness Plan")
    st.write(f"*Name:* {name}")
    st.write(f"*Age:* {age}")
    st.write(f"*Weight:* {weight} kg")
    st.write(f"*Height:* {height} cm")
    st.write(f"*Goal:* {goal}")
    st.write(f"*Workout Days:* {', '.join(workout_days)}")
    st.write(f"*Start Date:* {start_date}")
    st.write(f"*Preferred Workout Type:* {', '.join(preferred_workout)}")
    st.write(f"*Dietary Restrictions:* {dietary_restrictions}")

    # Simple fitness plan output
    st.subheader("Recommended Plan")
    if goal == "Lose Weight":
        st.write("Focus on Cardio exercises and maintain a calorie deficit.")
    elif goal == "Build Muscle":
        st.write("Focus on Strength Training exercises and maintain a calorie surplus.")
    elif goal == "Improve Stamina":
        st.write("Incorporate a mix of Cardio and HIIT exercises.")
    elif goal == "Maintain Fitness":
        st.write("Maintain a balanced workout routine with a mix of Cardio and Strength Training.")

    st.write("Ensure to stay hydrated and follow a balanced diet according to your dietary restrictions.")

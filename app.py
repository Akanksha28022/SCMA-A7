import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the Streamlit app
st.title('Fitness Planner')

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'Create Workout Plan', 'Track Progress', 'Visualize Progress'])

# Initialize session state for workout data
if 'workouts' not in st.session_state:
    st.session_state.workouts = []

# Home Page
if page == 'Home':
    st.header('Welcome to Fitness Planner')
    st.write('Use this app to create and manage your workout routines, track your progress, and visualize improvements over time.')

# Create Workout Plan Page
elif page == 'Create Workout Plan':
    st.header('Create Workout Plan')

    with st.form(key='workout_form'):
        name = st.text_input('Workout Name')
        date = st.date_input('Date')
        exercises = st.text_area('Exercises (separate each exercise with a comma)')
        duration = st.number_input('Duration (minutes)', min_value=1)

        submit_button = st.form_submit_button(label='Add Workout')

        if submit_button:
            workout = {
                'name': name,
                'date': date,
                'exercises': exercises.split(','),
                'duration': duration
            }
            st.session_state.workouts.append(workout)
            st.success('Workout added successfully!')

    st.write('### Current Workout Plan')
    st.dataframe(pd.DataFrame(st.session_state.workouts))

# Track Progress Page
elif page == 'Track Progress':
    st.header('Track Progress')

    if not st.session_state.workouts:
        st.write('No workouts added yet.')
    else:
        st.write('### Completed Workouts')
        for workout in st.session_state.workouts:
            st.write(f"**{workout['name']}** on {workout['date']}")
            st.write(f"Exercises: {', '.join(workout['exercises'])}")
            st.write(f"Duration: {workout['duration']} minutes")
            st.write('---')

# Visualize Progress Page
elif page == 'Visualize Progress':
    st.header('Visualize Progress')

    if not st.session_state.workouts:
        st.write('No workouts added yet.')
    else:
        df = pd.DataFrame(st.session_state.workouts)
        df['date'] = pd.to_datetime(df['date'])

        # Plot total duration over time
        st.write('### Total Duration Over Time')
        fig, ax = plt.subplots()
        df.groupby('date')['duration'].sum().plot(ax=ax)
        plt.xlabel('Date')
        plt.ylabel('Total Duration (minutes)')
        plt.title('Total Workout Duration Over Time')
        st.pyplot(fig)

        # Plot number of workouts over time
        st.write('### Number of Workouts Over Time')
        fig, ax = plt.subplots()
        df.groupby('date').size().plot(ax=ax)
        plt.xlabel('Date')
        plt.ylabel('Number of Workouts')
        plt.title('Number of Workouts Over Time')
        st.pyplot(fig)

        # Display exercise frequency
        st.write('### Exercise Frequency')
        all_exercises = [exercise for workout in st.session_state.workouts for exercise in workout['exercises']]
        exercise_counts = pd.Series(all_exercises).value_counts()
        st.bar_chart(exercise_counts)

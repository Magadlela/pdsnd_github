'''
Project Name: Bikashare
Code by: Magadlela Thato
Udacity third draft 
'''
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input('Enter the Valid name of the city you want to analyze[Chicago,New York city, Washington] : ').lower()
        if city in CITY_DATA:
            return
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the valid name of the month you want to analyze or enter all  [january, febuary, ..., june]:  ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june'] or month == 'all':
            return
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the valid day of the week you want to analyze or enter all[monday, tuesday, ..., sunday]: ').lower()
        if day in ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ] or day == 'all':
            return
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month =  month.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    initial_time = time.time()
    # display the most common month
    print("The most common month is : {}".format(df['month'].value_counts().max()))

    # display the most common day of week
    print("The most common day of week is : {}".format(df['day_of_week'].value_counts().max()))

    # display the most common start hour
    print("The most common start hour is :".format(df['hour'].value_counts().max()))
    
    print("\nThis took %s seconds." % (time.time() - initial_time))
    print('-'*40)
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    initial_time = time.time()

   # display most commonly used start station
    print("The most commonly used start station : {}".format(df['Start Station'].value_counts().max()))

    #display most commonly used end station
    print("The most commonly used end station : {} ".format(df['End Station'].value_counts().max()))

    #display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].max()
    print("The most commonly used start station and end station : {} and {}".format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - initial_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    initial_time = time.time()

    # display total travel time
    print('The total travel time : {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('The mean travel time : {}'.format(df['Trip Duration'].mean()))

    print('\nThis took %s seconds.' % (time.time() - initial_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    initial_time = time.time()

    # Display counts of user types
    print('The number of different user types is : {} '.format(df['User Type'].value_counts()))

    # Display counts of gender
    print('Counts of gender : {}'.format(df['Gender'].value_counts()))

    # Display earliest, most recent, and most common year of birth
    print('The earliest year of birth is : {}'.format(df['Birth Year'].min()))
    print('The most recent year of birth is : {}'.format(df['Birth Year'].max()))
    print('The common year of birth is : {}'.format(df['Birth Year'].mode()))
    print("\nThis took %s seconds." % (time.time() - initial_time))
    print('-'*40)

def display_data(df):
    """Displays raw bikeshare data to the user."""
    print('***'*20)
    print(df.head())
    i = 0
    while True:
        view_data = input('Would you like to view next five row of raw data? [yes or no] : ').lower()
        if view_data != 'yes':
            return
        i += 5
        print(df.iloc[i:i+5])
    

def main():
    '''Calls all other functions to bind them together to complete project'''
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if city == 'washington':
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df) 

        while True:
            view_data = input('Would you like to view first five row of raw data? [yes or no] : ').lower()
            if view_data != 'yes':
                return
            display_data(df)
            return

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            return

if __name__ == "__main__":
	main()
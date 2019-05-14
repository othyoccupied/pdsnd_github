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
    print('Hello! Let\'s explore some US bikeshare data! \n .')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\n Please type in the city you would like to filter the data by.\n 1. Chicago \n 2. New York City \n 3. Washington \n\n").title()
        if city not in ('New York City', 'Washington', 'Chicago'):
            print("Sorry, invalid city. Try again.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n Please type in the month to filter the data by, or type 'All' for no filter.\n 1. January \n 2. February \n 3. March \n 4. April \n 5. May \n 6. June \n 7. All \n\n").title()
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print("Sorry, invalid month. Try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nAre you looking for a specific day? If so, please type one of the options below to filter the data by or type 'all' for no filter.\n 1. Sunday \n 2. Monday \n 3. Tuesday \n 4. Wednesday \n 5. Thursday \n 6. Friday \n 7. Saturday \n 8. All \n\n").title()
        if day not in ('Sunday', 'Monday' , 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
            print("Sorry, invalid day. Try again.")
            continue
        else:
            break
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
    df = pd.read_csv(CITY_DATA[city.lower()])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'All':
        months = ['January','February','March','April','May','June']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('The most popular month is: ', popular_month)

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print("The most popular day of the week is: ", popular_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular start hour is: ", popular_hour)


    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('The most popular start station is: ', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('The most popular end station is: ',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End_Combo'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Start_End_Combo'].value_counts().idxmax()
    print('The most popular trip was: ',popular_trip)


    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time is: ', total_travel_time/86400, ' Days')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: ', mean_travel_time/60, 'Minutes')

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('User Types:')
    print(count_user_types)


    # TO DO: Display counts of gender
    try:
        count_gender_types = df['Gender'].value_counts()
        print('\nGender Types:')
        print(count_gender_types)
    except KeyError:
        print('\nGender Types:\nNo data available for this month.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year is:', earliest_year)
    except KeyError:
        print('\nEarliest Year:\nNo data available for this month.')

    try:
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year is:', most_recent_year)
    except KeyError:
        print('\nMost Recent Year:\nNo data available for this month.')

    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('Most Common Year is:',most_common_year)
    except KeyError:
        print('\nMost Common Year:\nNo data available for this month.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, choice):
    start_index = 0
    end_index = 5

    while True:
        if choice == 'Yes':
            print(df.iloc[start_index : end_index],'\n')
            start_index += 5
            end_index += 5
            choice = input('Would you like to see 5 more rows of raw data? Please enter "Yes" or "No"\n').title()
        elif (choice == 'No'):
            break
        else:
            choice = input('Not a valid input. Please enter "Yes" or "No"\n').title()

def main():
    while True:
        city, month, day = get_filters()
        print('The filters you chose are:\n\nCity - {}\nMonth - {}\nDay - {}'.format(city, month, day))
        df = load_data(city, month, day)
        print('-'*40)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        user_choice = input('Would you like to see the raw data? Please enter "Yes" or "No"\n').title()
        if user_choice == 'Yes':
            raw_data = pd.read_csv(CITY_DATA[city.lower()])
            display_data(raw_data, user_choice)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

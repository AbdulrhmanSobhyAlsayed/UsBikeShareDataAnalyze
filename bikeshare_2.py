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

    cities= ['chicago', 'new york city', 'washington']
    months=['all','january', 'february', 'march', 'april', 'may', 'june']
    days=['all','monday','tuesday','thursday','friday','saturday','sunday']
    city=''
    month=''
    day=''

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("please choose one of these cities ({}): ".format(",".join(cities))).lower()
        if city in cities:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month=input("please choose one of these months or all option ({}): ".format(",".join(months))).lower()
        if month in months:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("please choose one of these days or all option ({}): ".format(",".join(days))).lower()
        if day in days:
            break


    print('-'*40)
    return city, month, day

def display_data(df):
    """Displays lines of data"""
    
    num_of_row=0

    isDisplay=input("\nDo you Want To display 5 lines Of Data? Enter yes or no\n").lower()
    
    while isDisplay == 'yes':
        print(df.iloc[num_of_row*5:(num_of_row+1)*5,:])
        isDisplay=input("\nDo you Want To display Other 5 lines Of Data? yes or no\n").lower()
        num_of_row=num_of_row+1


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days=['monday','tuesday','thursday','friday','saturday','sunday']
        day=days.index(day)
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month

    popular_month = df['month'].mode()[0]

    print('Most Popular Month:', popular_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()

    popular_day_week = df['day_of_week'].mode()[0]

    print('Most Popular Day Of Week:', popular_day_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_end_station)


    # display most frequent combination of start station and end station trip
    popular_comb_station = (df['Start Station'] + ' ' + df['End Station']).mode()[0]

    print('Most Popular combination of Start Station and End Station:', popular_comb_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print('Total Travel Time:', total)

    # display mean travel time
    mean = df['Trip Duration'].mean()
    print('mean Travel Time:', mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print('Counts of User Types:',user_types)


    try:
        # Display counts of gender
        user_genders = df['Gender'].value_counts()

        print('Counts of Gender:',user_genders)


        # Display earliest, most recent, and most common year of birth
        min_year = df['Birth Year'].min()

        print('Min of Birth Year:',min_year)

        max_year = df['Birth Year'].max()

        print('Max of Birth Year:',max_year)

        mode_year = df['Birth Year'].mode()[0]

        print('Most Popular  Birth Year:',mode_year)

    except KeyError:
        print("There isn't a [Gender or Birth Year] column in this spreedsheet!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

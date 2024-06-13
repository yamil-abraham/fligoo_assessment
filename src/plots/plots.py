import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

def plot_reservations_by_hotel(df: DataFrame):
    """Plot the number of reservations by hotel"""
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    _, ax = plt.subplots(figsize=(8, 5))
    
    reservations_by_hotel = df['hotel'].value_counts()
    sns.barplot(x=reservations_by_hotel.index, y=reservations_by_hotel.values, ax=ax, hue=reservations_by_hotel.index, palette="viridis", legend=False)
    ax.set_title('Number of Reservations by Hotel')
    ax.set_xlabel('Hotel')
    ax.set_ylabel('Number of Reservations')
    
    plt.show()

def plot_daily_rate_hist(df: DataFrame):
    """Plot a histogram of the average daily rate"""
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    _, ax = plt.subplots(figsize=(8, 5))
    
    sns.histplot(data=df, x='average_daily_rate', bins=50, ax=ax, kde=True, color='darkblue')
    ax.set_title('Distribution of Average Daily Rate')
    ax.set_xlabel('Daily Rate (USD)')
    ax.set_ylabel('Frequency')
    
    plt.show()

def plot_lead_time_vs_rate(df: DataFrame):
    """Plot a scatter plot of lead time vs. average daily rate"""
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    _, ax = plt.subplots(figsize=(8, 5))
    
    sns.regplot(data=df, x='lead_time', y='average_daily_rate', ax=ax, color='darkgreen', line_kws={"color":"red"})
    ax.set_title('Relationship between Lead Time and Daily Rate')
    ax.set_xlabel('Lead Time (days)')
    ax.set_ylabel('Daily Rate (USD)')
    
    plt.show()

def plot_reservations_with_children(df: DataFrame):
    """Plot a pie chart of the percentage of reservations with and without children"""
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    _, ax = plt.subplots(figsize=(8, 5))
    
    reservations_with_children = df[df['children'] != 'none'].shape[0]
    reservations_without_children = df[df['children'] == 'none'].shape[0]
    
    labels = ['With Children', 'Without Children']
    sizes = [reservations_with_children, reservations_without_children]
    colors = ['#ff9999','#66b3ff']
    
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    ax.set_title('Percentage of Reservations with and without Children')
    
    plt.show()

def plot_reservations_by_market_segment(df: DataFrame):
    """Plot the number of reservations by market segment and hotel"""
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    _, ax = plt.subplots(figsize=(12, 6))
    
    sns.countplot(data=df, x='market_segment', hue='hotel', palette=['#1f77b4', '#ff7f0e'], ax=ax)
    
    ax.set_title('Number of Reservations by Market Segment and Hotel', fontsize=18, fontweight='bold')
    ax.set_xlabel('Market Segment', fontsize=14)
    ax.set_ylabel('Number of Reservations', fontsize=14)
    
    plt.legend(title='Hotel', loc='upper right', title_fontsize=12)
    
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.show()

def plot_daily_rate_by_room_type(df: DataFrame):
    """Plot a box plot of the daily rate by reserved room type"""
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    _, ax = plt.subplots(figsize=(12, 6))
    
    sns.boxplot(data=df, x='reserved_room_type', y='average_daily_rate', palette='viridis', ax=ax)
    
    ax.set_title('Daily Rate by Reserved Room Type', fontsize=18, fontweight='bold')
    ax.set_xlabel('Reserved Room Type', fontsize=14)
    ax.set_ylabel('Daily Rate (USD)', fontsize=14)
    
    plt.xticks(rotation=45)
    
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.show()

def plot_avg_daily_rate_by_country(df: DataFrame):
    """Plot a bar chart of the average daily rate by country of origin"""
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    # Ajustar el tamaño de la figura para que las etiquetas sean más legibles
    _, ax = plt.subplots(figsize=(20, 10))
    
    avg_rate_by_country = df.groupby('country')['average_daily_rate'].mean().sort_values(ascending=False)
    
    sns.barplot(x=avg_rate_by_country.index, y=avg_rate_by_country.values, palette='rocket', ax=ax)
    
    ax.set_title('Average Daily Rate by Country of Origin', fontsize=18, fontweight='bold')
    ax.set_xlabel('Country', fontsize=14)
    ax.set_ylabel('Average Daily Rate (USD)', fontsize=14)
    
    # Rotar las etiquetas del eje x y ajustar el tamaño de la fuente
    plt.xticks(rotation=90, fontsize=10)
    
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df: DataFrame):
    """Plot a correlation heatmap of the numeric variables"""
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    _, ax = plt.subplots(figsize=(12, 10))
    
    corr = df.select_dtypes(include='number').corr()
    
    sns.heatmap(corr, annot=True, cmap='coolwarm', square=True, linewidths=0.5, annot_kws={'fontsize': 12}, ax=ax)
    
    ax.set_title('Correlation Heatmap of Numeric Variables', fontsize=18, fontweight='bold')
    
    plt.tight_layout()
    plt.show()

def plot_avg_nights_by_customer_type(df: DataFrame):
    """Plot a bar chart of the average number of nights stayed by customer type"""
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    _, ax = plt.subplots(figsize=(10, 6))
    
    df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
    avg_nights_by_customer = df.groupby('customer_type')['total_nights'].mean()
    
    sns.barplot(x=avg_nights_by_customer.index, y=avg_nights_by_customer.values, palette='deep', ax=ax)
    
    ax.set_title('Average Number of Nights Stayed by Customer Type', fontsize=18, fontweight='bold')
    ax.set_xlabel('Customer Type', fontsize=14)
    ax.set_ylabel('Average Number of Nights', fontsize=14)
    
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.show()

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

def plot_avg_booking_changes_by_deposit_type(df: DataFrame):
    """Plot a bar chart of the average number of booking changes by deposit type"""
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    _, ax = plt.subplots(figsize=(10, 6))
    
    avg_changes_by_deposit = df.groupby('deposit_type')['booking_changes'].mean()
    
    sns.barplot(x=avg_changes_by_deposit.index, y=avg_changes_by_deposit.values, palette='magma', ax=ax)
    
    ax.set_title('Average Number of Booking Changes by Deposit Type', fontsize=18, fontweight='bold')
    ax.set_xlabel('Deposit Type', fontsize=14)
    ax.set_ylabel('Average Number of Changes', fontsize=14)
    
    # Agregar etiquetas de valores en la parte superior de cada barra
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom', fontsize=12)
    
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.show()

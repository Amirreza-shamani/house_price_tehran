import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

df = pd.read_csv(r"archive (1)\housePrice.csv")

# region clean data

# We have someting in Area (Dtype is object)
df["Area"] = pd.to_numeric(df["Area"], errors="coerce", downcast="integer")

# We have some none in address and Area I delet them
df = df.dropna()

# The Area dtype is float and i turned into init
df["Area"] = df["Area"].apply(lambda x: int(x))
# endregion

# region plot

mod = df["Address"].mode()
df_same_Address = df[df["Address"] == mod[0]]

# region room

def hat_graph(ax, xlabels, values, group_labels):

    def label_bars(heights, rects):
        for height, rect in zip(heights, rects):
            ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4), textcoords='offset points', ha='center', va='bottom')

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
        rects = ax.bar(x - spacing/2 + i * width, heights - heights0,
                       width, bottom=heights0, label=group_label, **style)
        label_bars(heights, rects)


fig, (ax1,ax2) = plt.subplots(2,1)
xlabels1 = np.arange(df["Room"].max()+1)
maximum1 = np.array(df.groupby("Room")["Price"].max().values/1000000)
minimum1 = np.array(df.groupby("Room")["Price"].min().values/1000000)
hat_graph(ax1, xlabels1, [maximum1, minimum1], ['maximum', 'minimum'])

ax1.set_xlabel('Room')
ax1.set_ylabel("price × 1'000'000")
ax1.set_title('(maximum & minimum) by room in Tehran', fontsize=20)
ax1.legend()
ax1.set_ylim(-5000, 110000)
fig.tight_layout()


xlabels2 = np.array(df_same_Address.groupby("Room")["Price"].max().index)
maximum2 = np.array(df_same_Address.groupby("Room")["Price"].max().values/1000000)
minimum2 = np.array(df_same_Address.groupby("Room")["Price"].min().values/1000000)
hat_graph(ax2, xlabels2, [maximum2, minimum2], ['maximum', 'minimum'])


ax2.set_xlabel('Room')
ax2.set_ylabel("price × 1'000'000")
ax2.set_title('(maximum & minimum) by room in Punak', fontsize=20)
ax2.legend()
ax2.set_ylim(500, 14000)
fig.tight_layout()

plt.show()

# endregion

# region parking warehouse elevator

def value(df, column):
    """_summary_

    Args:
        df (data frame): data frame you use
        column (str): column name

    Returns:
        data frame: df1 , df2
    """

    df1 = df[df[column] == True].sort_values("Area")
    df2 = df[df[column] != True].sort_values("Area")
    return df1, df2

def draw(ax, df1, df2, label):
    """_summary_

    Args:
        ax : ax[0,0] ax[0,1]
        df1 (dataframe): data frame 1
        df2 (dataframe): data frame 1
        label (str): label for legend 
    """

    ax.scatter(df1["Area"], df1["Price"]/1000000,
               label=f"+{label}", color="g", s=10)
    ax.scatter(df2["Area"], df2["Price"]/1000000,
               label=f"-{label}", color="r", s=10)
    ax.legend()


fig, ax = plt.subplots(2, 3, figsize=(10, 7))
fig.suptitle('Draw a Chart Bassed on ( Parking, Warehouse, Elevator )', fontsize=20)

df1, df2 = value(df, "Parking")
draw(ax[0, 0], df1, df2, "parking")
ax[0, 0].set_ylabel("price × 1,000,000")

df1, df2 = value(df, "Warehouse")
draw(ax[0, 1], df1, df2, "Warehouse")
ax[0, 1].set_title('In The Tehran', fontsize=16)

df1, df2 = value(df, "Elevator")
draw(ax[0, 2], df1, df2, "Elevator")

######## same address

df1, df2 = value(df_same_Address, "Parking")
draw(ax[1, 0], df1, df2, "parking")

df1, df2 = value(df_same_Address, "Warehouse")
draw(ax[1, 1], df1, df2, "Warehouse")
ax[1, 1].set_title(f'The Same Address ({mod[0]})', fontsize=16)

df1, df2 = value(df_same_Address, "Elevator")
draw(ax[1, 2], df1, df2, "Elevator")

plt.show()

# endregion

# region highst & lowest price in each Address

values = tuple(zip((df.groupby("Address")["Price"].max().values/1000000),
(df.groupby("Address")["Price"].min().values/1000000),
(df.groupby("Address")["Price"].max().index)
))

values = sorted(values, key = lambda i: i[0])
maxi,mini,cities = zip(*values)

# find minimum in the data
index = mini.index(min(mini))

fig, ax = plt.subplots(figsize =(13,6))
ax.plot(cities, maxi, "g-", label="maximum price")
ax.plot(cities, mini, "r-", label="minimum price")
ax.scatter(cities[-1], maxi[-1], color = "g", s = 7, label = f"max price:{cities[-1]}")
ax.scatter(cities[index], mini[index], color = "r", s =25, label = f"min price:{cities[index]}")
ax.set_title("The Price Of Each Address (119)", fontsize = 20)
ax2.set_ylabel("price × 1'000'000")
ax2.set_xlabel('cities')
ax.legend()
ax.grid()

plt.show()

# endregion

#region average price

df_avrage = df
avrage_price = np.average(df_avrage["Price"].values)
std = np.std(df_avrage["Price"].values)

def draw_chart(df, df1, df2, std, avrage_price):
    plt.scatter(df["Price"].index, df["Price"], color ="g", s=10, label="Normal Data")
    plt.scatter(df1["Price"].index, df1["Price"], color ="r", s=10, label="Outlier Data ")
    plt.scatter(df2["Price"].index, df2["Price"], color ="r", s=10)
    plt.plot([0, df["Price"].index[-1]], [avrage_price +(2*std), avrage_price +(2*std)], color='r', label="std line")
    plt.plot([0, df["Price"].index[-1]], [avrage_price -(2*std), avrage_price -(2*std)], color='r')
    plt.plot([0, df["Price"].index[-1]], [avrage_price , avrage_price], color='b', label="avrage line")
    plt.ylabel("Price")
    plt.xlabel("Index")
    plt.legend()
    plt.title("Delet Outlier Data for Avrage", fontsize=16)
    plt.show()

while True:

    num1 = df_avrage[df_avrage["Price"]>avrage_price +(2*std)]
    
    if (num1.empty):
        num2 = df_avrage[df_avrage["Price"]<avrage_price -(2*std)]
    else:
        num2 = num1
    
    if ((num1.empty) and (num2.empty)):
        break
    
    draw_chart(df_avrage, num1, num2, std, avrage_price) 
    df_avrage = df_avrage[df_avrage["Price"].between(avrage_price -(2*std), avrage_price +(2*std))]
    avrage_price = np.average(df_avrage["Price"].values)
    std = np.std(df_avrage["Price"].values)




df_avrage = df_avrage[df_avrage["Price"].between(avrage_price -(2*std), avrage_price +(2*std))]
avrage_price = np.average(df_avrage["Price"].values)
std = np.std(df_avrage["Price"].values)

plt.scatter(np.arange(len(df_avrage["Price"])), df_avrage["Price"], color ="g", s=10)
plt.plot([0, len(df_avrage["Price"])], [avrage_price, avrage_price], color='b', label = f"avrage line")
plt.plot([0, len(df_avrage["Price"])], [avrage_price +(2*std), avrage_price +(2*std)], color='r', label=f"std line")
plt.plot([0, len(df_avrage["Price"])], [avrage_price -(2*std), avrage_price -(2*std)], color='r')
plt.legend(loc="upper left")
plt.ylabel("Price")
plt.xlabel("Numbers")
plt.title(f"Avrage Price in Tehran\n avrage price : {avrage_price}", fontsize=16)

plt.show()



#endregion

# endregion


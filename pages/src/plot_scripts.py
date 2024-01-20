import pandas as pd

import matplotlib.pyplot as plt
from highlight_text import fig_text

from mplsoccer import PyPizza


def plot_pizza_chart_comparison(df, player1, player2, params=None, params_offset=None) -> PyPizza:
    # parameter and values list
    if params:
        params = params
    else:
        params = [
            'Potential', 'Growth', 'Acceleration', 'SprintSpeed', 'Agility', 'Pace', 'Physicality',
            'Shooting', 'Passing', 'Dribbling', 'Finishing', 'BallControl', 'Defending', 'Crossing',
        ]

    values = [v for v in df[df.Name.str.contains(player1)][params].values[0]]
    values_2 = [v for v in df[df.Name.str.contains(player2)][params].values[0]]

    # pass True in that parameter-index whose values are to be adjusted
    # here True values are passed for "\nTouches\nper Turnover" and "pAdj\nPress Regains" params
    params_offset = [True if abs(values[i] - values_2[i]) < 7 else False for i in range(len(values))]

    # instantiate PyPizza class
    baker = PyPizza(
        params=params,  # list of parameters
        background_color="#EBEBE9",  # background color
        straight_line_color="#222222",  # color for straight lines
        straight_line_lw=1,  # linewidth for straight lines
        last_circle_lw=1,  # linewidth of last circle
        last_circle_color="#222222",  # color of last circle
        other_circle_ls="-.",  # linestyle for other circles
        other_circle_lw=1  # linewidth for other circles
    )

    # plot pizza
    fig, ax = baker.make_pizza(
        values,  # list of values
        compare_values=values_2,  # comparison values
        figsize=(12, 12),  # adjust figsize according to your need
        kwargs_slices=dict(
            facecolor="#1A78CF", edgecolor="#222222",
            zorder=2, linewidth=1
        ),  # values to be used when plotting slices
        kwargs_compare=dict(
            facecolor="#FF9300", edgecolor="#222222",
            zorder=2, linewidth=1,
        ),
        kwargs_params=dict(
            color="#000000", fontsize=12,
            va="center"
        ),  # values to be used when adding parameter
        kwargs_values=dict(
            color="#000000", fontsize=12,
            zorder=3,
            bbox=dict(
                edgecolor="#000000", facecolor="cornflowerblue",
                boxstyle="round,pad=0.2", lw=1
            )
        ),  # values to be used when adding parameter-values labels
        kwargs_compare_values=dict(
            color="#000000", fontsize=12,
            zorder=3,
            bbox=dict(edgecolor="#000000", facecolor="#FF9300", boxstyle="round,pad=0.2", lw=1)
        ),  # values to be used when adding parameter-values labels
    )

    # adjust text for comparison-values-text
    baker.adjust_texts(params_offset, offset=-25.0, adj_comp_values=True)

    # add title
    fig_text(
        0.515, 0.99, f"<{player1}> vs <{player2}>", size=17, fig=fig,
        highlight_textprops=[{"color": '#1A78CF'}, {"color": '#EE8900'}],
        ha="center",
        color="#000000"
    )

    # add subtitle
    fig.text(
        0.515, 0.942,
        "Season 2022-23",
        size=15,
        ha="center",
        color="#000000"
    )

    # add credits
    CREDIT_1 = "data: Fifa 23 from kaggle"
    CREDIT_2 = "inspired by: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"

    fig.text(
        0.99, 0.005, f"{CREDIT_1}\n{CREDIT_2}", size=9,
        color="#000000",
        ha="right"
    )
    plt.savefig('comparison_chart.png')

    plt.show()


def plot_player_info(df, player, params=None):
    df = df[df.Name.str.contains(player)]

    # parameter and values list
    if params:
        params = params
    else:
        params = [
            'Potential', 'Growth', 'Acceleration', 'SprintSpeed', 'Agility', 'Pace', 'Physicality',
            'Shooting', 'Passing', 'Dribbling', 'Finishing', 'BallControl', 'Defending', 'Crossing',
        ]

    values = [v for v in df[params].values[0]]

    # color for the slices and text
    slice_colors = ["#1A78CF"] * 7 + ["#FF9300"] * 5 + ["#D70232"] * 2
    text_colors = ["#F2F2F2"] * 14

    if len(values) != len(slice_colors):
        physics = int(input('Tape physics stats number: '))
        attacking = int(input('Tape attacking stats number: '))
        defending = int(input('Tape defending stats number: '))

        slice_colors = ["#1A78CF"] * physics + ["#FF9300"] * attacking + ["#D70232"] * defending
        total = physics + attacking + defending
        text_colors = ["#F2F2F2"] * total

    # instantiate PyPizza class
    baker = PyPizza(
        params=params,  # list of parameters
        background_color="#222222",  # background color
        straight_line_color="#000000",  # color for straight lines
        straight_line_lw=1,  # linewidth for straight lines
        last_circle_color="#000000",  # color for last line
        last_circle_lw=1,  # linewidth of last circle
        other_circle_lw=0,  # linewidth for other circles
        inner_circle_size=20  # size of inner circle
    )

    # plot pizza
    fig, ax = baker.make_pizza(
        values,  # list of values
        figsize=(8, 8.5),  # adjust the figsize according to your need
        color_blank_space="same",  # use the same color to fill blank space
        slice_colors=slice_colors,  # color for individual slices
        value_colors=text_colors,  # color for the value-text
        value_bck_colors=slice_colors,  # color for the blank spaces
        blank_alpha=0.4,  # alpha for blank-space colors
        kwargs_slices=dict(
            edgecolor="#000000", zorder=2, linewidth=1
        ),  # values to be used when plotting slices
        kwargs_params=dict(
            color="#F2F2F2", fontsize=11,
            va="center"
        ),  # values to be used when adding parameter labels
        kwargs_values=dict(
            color="#F2F2F2", fontsize=11,
            zorder=3,
            bbox=dict(
                edgecolor="#000000", facecolor="cornflowerblue",
                boxstyle="round,pad=0.2", lw=1
            )
        )  # values to be used when adding parameter-values labels
    )

    # add title
    fig.text(
        0.515, 0.975, f"{df['Name'].values[0]} - {df['Club'].values[0]}", size=16,
        ha="center", color="#F2F2F2"
    )

    # add subtitle
    fig.text(
        0.515, 0.955,
        "Season 2022-23",
        size=13,
        ha="center",
        color="#F2F2F2"
    )

    # add credits
    CREDIT_1 = "data: FiFa 23 kaggle"
    CREDIT_2 = "inspired by: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"

    fig.text(
        0.99, 0.02, f"{CREDIT_1}\n{CREDIT_2}", size=9,
        color="#F2F2F2",
        ha="right"
    )

    # add text
    fig.text(
        0.34, 0.93, "Physics        Attacking       Defending", size=14,
        color="#F2F2F2"
    )

    # add rectangles
    fig.patches.extend([
        plt.Rectangle(
            (0.31, 0.9225), 0.025, 0.021, fill=True, color="#1a78cf",
            transform=fig.transFigure, figure=fig
        ),
        plt.Rectangle(
            (0.462, 0.9225), 0.025, 0.021, fill=True, color="#ff9300",
            transform=fig.transFigure, figure=fig
        ),
        plt.Rectangle(
            (0.632, 0.9225), 0.025, 0.021, fill=True, color="#d70232",
            transform=fig.transFigure, figure=fig
        ),
    ])

    plt.savefig('info.png')

    plt.show()

    return plt.show()
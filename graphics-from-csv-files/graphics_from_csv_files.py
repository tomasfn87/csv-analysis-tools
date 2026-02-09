import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import re
import matplotlib.colors as mcolors

def validate_and_parse_args():
    raw_args = sys.argv[1:]

    if len(raw_args) < 5 or (len(raw_args) - 2) % 3 != 0:
        print("Usage: python script.py <WxH> <Weightpx> <file1> <title1> <color1> ...")
        print("Example: python script.py 1200x600 2px data.csv 'Sales' 'royalblue'")
        return None

    dim_match = re.match(r"^(\d+)x(\d+)$", raw_args[0])
    weight_match = re.match(r"^(\d+(\.\d+)?)px$", raw_args[1])

    if not dim_match or not weight_match:
        print("Error: Invalid dimension or weight format.")
        return None

    width_in, height_in = int(dim_match.group(1)) / 100, int(dim_match.group(2)) / 100
    line_weight = float(weight_match.group(1))

    valid_colors = mcolors.CSS4_COLORS.keys()
    triplets = []

    for i in range(2, len(raw_args), 3):
        file_path = raw_args[i]
        metric_title = raw_args[i+1]
        color_val = raw_args[i+2].lower()
        if not os.path.isfile(file_path):
            print(f"Error: File '{file_path}' not found.")
            return None
        if color_val not in valid_colors:
            print(f"Error: '{color_val}' is not a valid color.")
            print("\nAccepted colors include standard names like:")
            print(", ".join(list(valid_colors)[:20]) + " ... and many more.")
            print("Full list: https://matplotlib.org/stable/gallery/color/named_colors.html")
            return None

        triplets.append({"file": file_path, "title": metric_title, "color": color_val})

    return {
        "width": width_in,
        "height": height_in,
        "weight": line_weight,
        "triplets": triplets
    }

def generate_graphics():
    config = validate_and_parse_args()
    if not config: return

    dataframes = []
    all_starts, all_ends = [], []
    sns.set_theme(style="whitegrid")
    os.makedirs("output_plots", exist_ok=True)

    for item in config["triplets"]:
        try:
            df = pd.read_csv(item['file'])
            date_col, val_col = df.columns[0], df.columns[1]
            df[date_col] = pd.to_datetime(df[date_col])
            df = df.sort_values(by=date_col)

            dataframes.append({'df': df, 'title': item['title'], 'color': item['color']})
            all_starts.append(df[date_col].min())
            all_ends.append(df[date_col].max())

            plt.figure(figsize=(config["width"], config["height"]))
            sns.lineplot(data=df, x=date_col, y=val_col, linewidth=config["weight"], color=item['color'])
            plt.title(f"Metric: {item['title']}")
            plt.xticks(rotation=30)
            plt.tight_layout()
            plt.savefig(f"output_plots/Individual_{item['title'].replace(' ', '_')}.png", dpi=300)
            plt.close()
        except Exception as e:
            print(f"Error processing {item['file']}: {e}"); return

    common_start, common_end = max(all_starts), min(all_ends)
    summary_list = []
    color_map = {}

    for item in dataframes:
        df = item['df']
        date_col, val_col = df.columns[0], df.columns[1]
        mask = (df[date_col] >= common_start) & (df[date_col] <= common_end)
        sync_df = df.loc[mask].copy()
        sync_df = sync_df.rename(columns={val_col: 'Measurement'})
        sync_df['Metric'] = item['title']
        summary_list.append(sync_df)
        color_map[item['title']] = item['color']

    if summary_list:
        master_df = pd.concat(summary_list, ignore_index=True)
        plt.figure(figsize=(config["width"], config["height"]))

        ax = sns.lineplot(
            data=master_df, x=master_df.columns[0], y='Measurement',
            hue='Metric', palette=color_map, linewidth=config["weight"]
        )

        if ax.get_legend():
            ax.get_legend().remove()

        plt.title(f"Synced Comparison", pad=25)
        plt.xlabel("Timeline", labelpad=15)
        plt.legend(title="Metrics", loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=1)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("output_plots/00_Combined_Comparison.png", dpi=300, bbox_inches='tight')
        plt.close()
        print(f"\nSuccess! Used custom color mapping for {len(config['triplets'])} metrics.")

if __name__ == "__main__":
    generate_graphics()
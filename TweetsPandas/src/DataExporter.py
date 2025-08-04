import json

def export_to_csv(df, file_name):
    df.to_csv(f"../results/{file_name}.csv", index=False)


def export_to_json(dic, file_name):
    with open(f"../results/{file_name}.json", "w", encoding="utf-8") as f:
        json.dump(dic, f, indent=4)
import json

def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def summarize(record):
    if not record:
        return "暂无数据"
    total =sun(r.get("score",0) for r in records)
    avg =total / len(records)
    return f"共{len(records)}条,平均分{avg:1f}"

if __name__ == "__main__":
    data = load_data("scores.json")
    print(summarize(data))
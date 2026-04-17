import csv

sample = [
    ["name","age","score","city"],
    ["Ravi","25","85","Bengaluru"],
    ["Priya","23","92","Mumbai"],
    ["Arjun","27","67","Delhi"],
    ["Sneha","24","78","Bengaluru"],
    ["Kiran","26","55","Chennai"],
    ["Meera","22","91","Mumbai"],
]

with open("students_data.csv","w", newline="") as f:
    csv.writer(f).writerows(sample)

class DataSet:

    def __init__(self, filepath):
        self.filepath = filepath
        self.rows = []
        self._load()

    def _load(self):
        try:

            with open(self.filepath, 'r')as f:
                reader = csv.DictReader(f)
                self.rows = [dict(row) for row in reader]
            print(f"Loaded {len(self.rows)} rows from '{self.filepath}'")

        except FileNotFoundError:
            print(f"Error: {self.filepath} not found")
        except Exception as e:
            print(f"Error loading file: {e}")

    def summary(self):
        if not self.rows:
            print("No data loaded")
            return
        
        print(f"\nRows : {len(self.rows)}")
        print(f"columns : {list(self.rows[0].keys())}")

    def column_stats(self, col):
        try:
            values = [float(row[col]) for row in self.rows]
            print(f"\nStats for '{col}' : ")
            print(f" Mean : {sum(values) / len(values):.2f}")
            print(f"Min : {min(values)}")
            print(f" Max : {max(values)}")

        except KeyError:
            print(f"Column '{col} not found")
        except ValueError:
            print(f"column '{col}' is not found")

    def filter_rows(self, col, value):
        result = [r for r in self.rows if r.get(col) == value]
        print(f"\nRows where {col} = {value}")
        for r in result:
            print(f" {r}")
        return result
        
    def __len__(self):
        return len(self.rows)
        
    def __str__(self):
        return f"DataSet('{self.filepath}', {len(self.rows)} rows)"
    

#use the class

ds = DataSet("students_data.csv")
print(ds)

ds.summary()
ds.column_stats("score")
ds.column_stats("age")
ds.filter_rows("city","Bengaluru")
ds.filter_rows("city","Mumbai")

#testing error handling

bad = DataSet("does_not_exist.csv")
ds.column_stats("name") #not a numeric
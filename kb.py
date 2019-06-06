import pandas as pd
import numpy as np


class Canada():
    def __init__(self, path=None, n=15):
        self.df = self.read(path)
        self.n = n

    def read(self, path):
        df = pd.read_excel(path)
        new_names = df.iloc[0]
        for index, name in enumerate(df.columns):
            # renaming the columns
            df.rename(columns={name: new_names[index]}, inplace=True)
        df.drop(0, inplace=True)
        df.dropna(inplace=True)
        df["Estimated average cost"] = df["Estimated average cost"].apply(
            lambda x: float(x))
        return df

    def search(self, operation_or_condition=None, age=40, budget=np.math.inf):
        indices = []
        for index, row in self.df["Case Mix Group (description)"].items():
            if operation_or_condition not in row:
                indices.append(int(index))
        # finding the correct operation
        whole_operation = self.df.drop(indices)
        age_sub_group = ""
        if age in range(1, 8):
            age_sub_group += "1–7 years (pediatric)"
        elif age in range(18, 60):
            age_sub_group += "18–59 years (adult)"
        else:
            age_sub_group += "60–79 years (adult)"
        flight_cost = 0
        budget += flight_cost
        operation = whole_operation[whole_operation["Age group"]
                                    == age_sub_group]
        operation = operation[operation["Estimated average cost"] <= budget]
        smallest = operation.rename(columns={"Estimated average cost": "Cost",
                                             "Jurisdiction": "Location", "Case Mix Group (description)": "Description"})
        if self.n >= smallest["Cost"].count():
            return smallest
        return smallest.nsmallest(self.n, "Cost")[["Description", "Cost", "Location"]]


class GreatBritain():
    def __init__(self, path=None, n=15):
        self.df = self.read(path)
        self.n = n

    def read(self, path):
        df = pd.read_excel(path)
        df["Unit Cost "] = df["Unit Cost "].apply(lambda x: float(x) * 1.27)
        df.dropna(inplace=True)
        return df

    def search(self, operation_or_condition=None, budget=np.math.inf):
        indices = []
        for index, row in self.df["Currency Description"].items():
            if operation_or_condition not in row:
                indices.append(int(index))
        # finding the correct operation
        whole_operation = self.df.drop(indices)
        operation = whole_operation[whole_operation["Unit Cost "] <= budget]
        operation = operation.rename(
            columns={"Unit Cost ": "Cost", "Currency Description": "Description"})
        if self.n >= operation["Cost"].count():
            return operation
        return operation.nsmallest(self.n, "Cost")[["Description", "Cost"]]


class Generic():
    def __init__(self, path, n):
        self.df = self.read(path)
        self.n = n
        self.path = path

    def read(self, path):
        df = pd.read_excel(path)
        df.dropna()
        return df

    def search(self, operation_or_condition, budget=np.math.inf):
        self.df["Cost"] = self.df["Cost"].apply(lambda x: float(
            "".join("".join(str(x).split(",")).split("$"))))
        operation = self.df[self.df["Cost"] <= budget]
        indices = []
        for index, row in operation["Description"].items():
            if operation_or_condition.lower() not in row.lower():
                indices.append(int(index))
        operation.drop(indices, inplace=True)
        if self.n >= operation["Cost"].count():
            return operation
        return operation.nsmallest(self.n, "Cost")


class KB():
    def __init__(self, paths, n):
        self.canada = Canada(paths[0], n)
        self.gb = GreatBritain(paths[1], n)
        self.generics = [Generic(path, n) for path in paths[2:]]

    def search(self, operation_or_condition=None, age=40, urgency_flight_data=None, sliders=[3, 3, 3], budget=np.math.inf):
        results = []
        results_canada = self.canada.search(
            operation_or_condition, age, budget)
        results_gb = self.gb.search(operation_or_condition, budget)
        results_generics = [generic.search(
            operation_or_condition, budget) for generic in self.generics]
        cities = ["Greater London", "Buckinghamshire", "Cambridgeshire", "Durham", "East Riding of Yorkshire", "East Sussex ",
                  "Essex", "Gloucestershire", "Greater Manchester", "Halton", "Hampshire", "Hartlepool",
                  "Herefordshire", "Oxfordshire", "Rutland", "Shropshire", "Slough", "Somerset"]
        for index in results_canada.index:
            results.append({"Location": f"{results_canada['Location'][index]}, Canada", "Description": results_canada["Description"][index], "Cost": round(
                results_canada["Cost"][index], 0)})
        ctr = 0
        for index in results_gb.index:
            results.append({"Location": f"{cities[ctr]}, England", "Description": results_gb["Description"][index], "Cost": round(
                results_gb["Cost"][index], 0)})
            ctr += 1
        for result in results_generics:
            for index in result.index:
                results.append({"Location": result["Location"][index], "Description": result["Description"][index], "Cost": round(
                    result["Cost"][index], 0)})
        return results

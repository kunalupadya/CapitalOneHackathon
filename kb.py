import pandas as pd
import numpy as np
import json

class Canada():
    def __init__(self, path = None, n = 15):
        self.df = self.read(path)
        self.n = n
    
    def read(self, path):
        df = pd.read_excel(path)
        df.dropna(inplace = True)
        names = df.iloc[0]
        for index, column in enumerate(df.columns):
            df = df.rename(columns = {column:names[index]})
        df.drop([0], inplace=True)
        print(df)
        df["Estimated average cost"] = df["Estimated average cost"].apply(lambda x: float(x))
        return df
    
    def search(self, operation_or_condition = None, age = 40, budget = np.math.inf):
        indices = []
        for index, row in self.df["Case Mix Group (description)"].items():
            if operation_or_condition.lower() not in row.lower():
                indices.append(int(index))
        whole_operation = self.df.drop(indices) # finding the correct operation
        age_sub_group = ""
        if age in range(1,8):
            age_sub_group += "1–7 years (pediatric)"
        elif age in range(18,60):
            age_sub_group += "18–59 years (adult)"
        else:
            age_sub_group += "60–79 years (adult)"
        operation = whole_operation[whole_operation["Age group"] == age_sub_group]
        # operation["Estimated average cost"] = operation["Estimated average cost"].apply(float)
        operation = operation[operation["Estimated average cost"] <= float(budget)]
        smallest = operation.rename(columns = {"Estimated average cost": "Cost", "Jurisdiction": "Location", "Case Mix Group (description)":"Description"})
        if self.n >= smallest["Cost"].count():
            return smallest
        return smallest.nsmallest(self.n, "Cost")[["Description", "Cost", "Location"]]

class GreatBritain():
    def __init__(self, path = None, n = 15):
        self.df = self.read(path)
        self.n = n
    
    def read(self, path):
        df = pd.read_excel(path)
        df["Unit Cost "] = df["Unit Cost "].apply(lambda x: float(x) * 1.27)
        df.dropna(inplace = True)
        return df
    
    def search(self, operation_or_condition = None, budget = np.math.inf):
        indices = []
        for index, row in self.df["Currency Description"].items():
            if operation_or_condition.lower() not in row.lower():
                indices.append(int(index))
        whole_operation = self.df.drop(indices) # finding the correct operation
        operation = whole_operation[whole_operation["Unit Cost "] <= float(budget)]
        operation = operation.rename(columns = {"Unit Cost ": "Cost", "Currency Description":"Description"})
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
    
    def search(self, operation_or_condition, budget = np.math.inf):
        self.df["Cost"] = self.df["Cost"].apply(lambda x : float("".join("".join(str(x).split(",")).split("$"))))
        self.df['Location'] = self.df["Location"].apply(lambda x: ", ".join("".join(str(x).split("\xa0")).split(",")))
        operation = self.df[self.df["Cost"] <= float(budget)]
        indices = []
        for index, row in operation["Description"].items():
            if operation_or_condition.lower() not in row.lower():
                indices.append(int(index))
        operation.drop(indices, inplace = True)
        if self.n >= operation["Cost"].count():
            return operation
        return operation.nsmallest(self.n, "Cost")
class FlightCosts():
    def __init__(self, path):
        self.df = pd.read_excel(path)
    def search(self, city, days):
        df = self.df
        for index, row in self.df["City"].items():
            if city.lower() not in row.lower():
                df = df.drop(index)
        df = df[df["Days Out"] < float(days)]
        df["Price"] = df['Price'].apply(lambda x : float("".join("".join(str(x).split(",")).split("$"))))
        return df["Price"].mean()
        
        
class KB():
    def __init__(self, paths, costs, n):
        self.costs = [FlightCosts(path) for path in costs]
        self.canada = Canada(paths[0], n)
        self.gb = GreatBritain(paths[1], n)
        self.generics = [Generic(path, n) for path in paths[2:]]
    
    def search(self, operation_or_condition, age = 40, urgency = 100, budget = np.math.inf):
        results = []
        urgency = float(urgency)
        results_canada = self.canada.search(operation_or_condition, age, budget)
        results_gb = self.gb.search(operation_or_condition, budget)
        results_generics = [generic.search(operation_or_condition, budget) for generic in self.generics]
        cities = ["Greater London", "Buckinghamshire", "Cambridgeshire", "Durham", "East Riding of Yorkshire", "East Sussex ",
                    "Essex", "Gloucestershire", "Greater Manchester","Halton", "Hampshire", "Hartlepool", 
                 "Herefordshire", "Oxfordshire", "Rutland", "Shropshire", "Slough", "Somerset"]
        for index in results_canada.index:
            city = f"{results_canada['Location'][index].lower().title()}, Canada"
            description = results_canada["Description"][index].lower().title()
            results.append({"Location": f"{city}, Canada", "Description": description, "Cost": round(float(results_canada["Cost"][index]) + self.costs[1].search(city, urgency),0)})
        ctr = 0
        for index in results_gb.index:
            city = f"London, England"
            description = results_gb["Description"][index].lower().title()
            results.append({"Location": f"{cities[ctr]}, England", "Description": description, "Cost": round(float(results_gb["Cost"][index]),0) + 2000})
            ctr += 1
        for result in results_generics:
            for index in result.index:
                city = result["Location"][index].lower().title()
                print(float(result["Cost"][index]))
                description = result["Description"][index].lower().title()
                results.append({"Location": city, "Description": description, "Cost": round(float(result["Cost"][index]),0)})
        return results
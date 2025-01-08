'''using lambda(),filter(),map(),process a list of dictionary to extract and transform a specific value
lst=[{"name":"kiran","age":25},{"name":"mantu","age":23},{"name":"arun","age":50}]
task:extract the names of the people older then 25 in upper case'''

lst = [{"name": "kiran", "age": 25}, {"name": "mantu", "age": 26}, {"name": "arun", "age": 50}]
result = list(map(lambda person: person["name"].upper(), filter(lambda person: person["age"] > 25, lst)))

print(result)

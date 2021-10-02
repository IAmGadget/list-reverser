list_items = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for idx, key in enumerate(list_items):
  new_list.insert(key, len(list_items) - idx)
  print(key, idx)
print(f"""
{'#'*20} New List {'#'*20}
    {new_list}
{'#' * (40 + len(' New list'))}""")

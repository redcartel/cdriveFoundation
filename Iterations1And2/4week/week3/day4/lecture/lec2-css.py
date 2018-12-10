"""

soup.find finds elements that match css selectors
always returns a list

css selectors:

#idname
.class_name
parent_selector > immediate_child_selector
parent_selector > descendent_selector
[attribute]  (just has the attribute
[attribute='value']
"""

soup.select("div.wrapper div.content")


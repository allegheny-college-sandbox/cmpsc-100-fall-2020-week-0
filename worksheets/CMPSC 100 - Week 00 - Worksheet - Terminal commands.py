#!/usr/bin/env python
# coding: utf-8

# # CMPSC 100: `TITLE`
# 
# ---
# 
# The following worksheet asks you to participate in a programming-based number trick based on the following topics:
# 
# * ...
# * ...
# * ...
# 
# Portions of the worksheet `will require you to reference values calculated as the answers in previous questions, so be sure to follow the instructions and use the variable name suggested.
# 
# * The `Activity` portion of the worksheet outlines the programming work that you need to complete. 
#   * Think of this section as *how* you do something in Python.
# * The `Q & A` portion asks a few questions for you to think about and answer.
#   * This portion underscores *why* you might do something while programming in Python.
# 
# 
# ## Table of Contents
# 
# * [Activity](#Activity)
#   * [Final Check](#Final-check)
# * [Q&A](#Q-&-A)

# ## Activity

# ### 1. If `foo`, does `foo["bar"]` `baz`?

# In[1]:


foo = {}
foo["bar"] = "baz"

# Evaluate foo["bar"] to see if baz

for val in foo:
    try:
        if foo[val] == "baz" and val == "bar":
            print(True)
    except KeyError:
        print("There's no bar in a foo to baz!")


# ### Final check

# In[ ]:


# Implement some final check to ensure to allow for a find of "exit ticket"?


# ## Q & A

# `A short series of questions (no more than 5) to provide notes for review when returning from activity break`

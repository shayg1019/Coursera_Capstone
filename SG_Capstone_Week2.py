#!/usr/bin/env python
# coding: utf-8

# ## Using UK Government Road Accident Data to Discern Which Features Make an Accident More Likely, and to Predict Accident Severity

# ### Introduction

# In 2018 (the last year for which there are complete annual records), there were 1,784 reported road deaths and 25,511 serious injuries in car accidents in the United Kingdom. This level is similar to that of all 6 years since 2012 and, although there was a decline in the first decade of the 21st century, deaths have stabilised around this mark. 
# 
# Although the decline that occurred from 2000 to 2012 is overwhelmingly positive, 1,784 road deaths and 25,511 serious injuries is still too many. These incidents cause untold emotional damage to those surrounding the casualties, as well as a significant amount of damage to the economy of the United Kingdom. Indeed, a report from Fonesca Law (a solicitors firm in the UK) in 2014 (when road deaths were roughly the same as they were in 2018) argues that road accidents cost the national economy almost £15 billion, partially due to vehicle and property damages, police costs and insurance costs.
# 
# The aim of this project, therefore, is to perform data analysis and visualisation which indicates the features which make a road accident more likely, and to build a machine learning model which can predict accident severity. 
# 
# Having observed the analysis and used the model, it is hoped that drivers will consequently be able to change their driving habits accordingly, and thus be less likely to have an accident. If there is sufficient uptake of the model, it might be possible to reduce the number of road deaths and road injuries per year by a significant margin. However, even if just a few people observe the data analysis and use the model, and change their behaviour, leading to higher levels of safety on the UK’s roads, this would be justification enough for this project. 
# 

# ### Data

# Data on the subject of road accidents is readily available through the UK government. Indeed, each year the Department for Transport releases information on road accidents and road casualties, downloadable in CSV format. Each annual accident dataset tends to include around 120,000 observations (rows) and exactly 32 attributes (columns). For each accident that occurs, the Department records accident severity, the number of vehicles involved, the number of casualties, the day of the week, the time, road classes (i.e. motorway, A-road etc.) of each road involved, road type (roundabout, one-way street, dual carriageway etc.), the speed limit, details regarding the junction, the type of controls at the junction (traffic lights, none etc.), the light conditions, the weather conditions, the road surface conditions, whether there were any hazards on the carriageway, and whether the accident occurred in an urban or rural (or unassigned) area. The 120,000 observations from a single year should be more than enough for effective data analysis and the construction of a good machine learning model. 
# 
# Though the data is readily available, it is formatted in such a way that is not conducive to immediate analysis. There are many missing values (coded as various things, from -1 to 6 depending on the attribute), variables whose datatype is not conducive to analysis, unnecessary attributes (such as ‘Did_Officer_Attend_Scene_of_Accident’) and variables which should not be used because they might unfairly affect the model (for instance, using ‘Number_of_Casualties’ as a predictor for accident severity would be unwise, since it is something which one cannot know before one actually has an accident, and because it would lead to a less useful model). As a consequence, a large amount of data pre-processing will have to occur before anything can be done.
# 
# That said, I am optimistic about the results of using this dataset, and I look forward to observing the results of this project.
# 

# In[ ]:





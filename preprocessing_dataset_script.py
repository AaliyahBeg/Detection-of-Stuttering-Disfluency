# %% [markdown]
# Import Pandas

# %%
import pandas as pd

# %% [markdown]
# Make Dataframe

# %%
df=pd.read_csv('SEP-28k_labels.csv')

# %% [markdown]
# Print Dataframe

# %%
df

# %% [markdown]
# Columns corresponding to types of stuttering

# %%
df.iloc[:,5:]

# %%
df1=df.drop(['Show'],axis=1)
df1=df1.drop(['EpId'],axis=1)
df1=df1.drop(['Start'],axis=1)
df1=df1.drop(['Stop'],axis=1)
df1=df1.drop(['ClipId'],axis=1)

# %%
df1

# %% [markdown]
# The total number of votes given

# %%
Sum=[]
for index, row in df1.iterrows():
    rowsum=row.sum()
    print(row)
    print(rowsum)
    Sum.append(rowsum)


# %%
Sum

# %%
# df1['Sum']=Sum

# %%
df1

# %% [markdown]
# The number of audio files in each types when in the case of max present in more than one type label, all occurence considered

# %%
count ={}
count['Block']=0
count['DifficultToUnderstand']=0
count['Interjection']=0
count['Music']=0
count['NaturalPause']=0
count['NoSpeech']=0
count['NoStutteredWords']=0
count['PoorAudioQuality']=0
count['Prolongation']=0
count['SoundRep']=0
count['Unsure']=0
count['WordRep']=0


# %% [markdown]
# Create a dictionary with the other occurence of max value for each row

# %%
type = []
multi ={}
for index, row in df1.iterrows():
    max_label = row.idxmax()
    max_value = row[max_label]
    labels = [label for label, value in row.items() if value == max_value]
    for v in labels:
        count[v]=count[v]+1
    if (len(labels)>1) :
        labels.pop(0)
        multi[index]=labels
    type.extend(labels)


# %%
print(count['Block'])
print(count['DifficultToUnderstand'])
print(count['Interjection'])
print(count['Music'])
print(count['NaturalPause'])
print(count['NoSpeech'])
print(count['NoStutteredWords'])
print(count['PoorAudioQuality'])
print(count['Prolongation'])
print(count['SoundRep'])
print(count['Unsure'])
print(count['WordRep'])



# %%
print(count['Block']+count['DifficultToUnderstand']+count['Interjection']+count['Music']+count['NaturalPause']+count['NoSpeech']+count['NoStutteredWords']
+count['PoorAudioQuality']
+count['Prolongation']
+count['SoundRep']
+count['Unsure']
+count['WordRep'])

# %%
print(multi)

# %%
print(len(multi))

# %%
print(type)

# %%
# type=[]
# for index, row in df1.iterrows():
#     type.append(row.idxmax())

# %%
# df['Type']=type #error coming for multiple values handling 

# %%
# # Create an empty column 'Type'
# df['Type'] = ''

# # Iterate over the rows of df1 DataFrame and assign values to the 'Type' column
# for index, row in df1.iterrows():
#     df.at[index, 'Type'] = row.idxmax()
    

# %%
# Create an empty column 'Type'
df['Type'] = ''
# type=[]
# Iterate over the rows of df1 DataFrame and assign values to the 'Type' column
for index, row in df1.iterrows():
    df.at[index, 'Type'] = row.idxmax()
    # type.append(row.idxmax())

# %% [markdown]
# The number of audio files in each types when in the case of max present in more than one type label, first occurence considered 

# %%

# # Create a pandas Series from the list
# series = pd.Series(type)

# # Count the occurrences of each value in the Series
# value_counts = series.value_counts()

# # Print the count of each value
# print(value_counts)

# %%
types=df['Type'].unique()
for ty in types:
    print(ty)
    print(df[df['Type']==ty]['Type'].count())


# %%
# df[(df['Show']=='WomenWhoStutter') & (df['EpId']==0) & (df['ClipId']==223)]

# %%
print(df['EpId'].nunique())

# %%
# for index, row in df.iterrows():
#   i=row['EpId']
#   print(i)
#   if (i/100)<1:
#     i=str(i)
#     i=str('0'+i)
#     print(f"->{i}")
#     # i=int(i)
#     # df.loc[df['EpId'] ==i,'EpId']=i
#     row['EpId']=i
#     print(row['EpId'])
#     df.at[index,'EpId']=i


# %%
print(df['EpId'].nunique())

# %%
df

# %%
print(df['EpId'].nunique)

# %%
import pathlib
from pathlib import Path

# %% [markdown]
# Making folder structure as per types (FluencyBank)

# %%
# for ind in df.index:
#   # print(files)
#   folder_id=df['EpId'][ind] #folder
#   print(folder_id)
#   file_id=df['ClipId'][ind] #file
#   audio_type=df['Type'][ind]
#   print(file_id)
#   folder_path = Path(r'C:\Users\aaliy\OneDrive\Desktop\Speech Processing Lab IIITH\ml-stuttering-events-dataset\[CLIP_DIR]_fluencybank\content\[CLIP_DIR]\FluencyBank\{folderid}'.format(folderid=folder_id))
#   file_name="FluencyBank_{folderid}_{fileid}.wav".format(folderid=folder_id, fileid=file_id)
#   file_path_dest = Path(r'C:\Users\aaliy\OneDrive\Desktop\Speech Processing Lab IIITH\ml-stuttering-events-dataset\Type_fluencybank\{audiotype}\{filename}'.format(audiotype=audio_type,filename=file_name))
#   # file_name="FluencyBank_"+files['EpId']+"_"+files['ClipId']


#   file_path = folder_path / file_name

#   if file_path.is_file():
#     # File exists
#     with file_path.open('rb') as file:
#         # Read the contents of the file
#         contents = file.read()
#         # print(contents)# Save the content to the file
#         with file_path_dest.open('wb') as file_dest:
#           file_dest.write(contents)

#         print(f"File '{file_path}' has been saved.")
#   else:
#     # File does not exist
#     print(f"File '{file_name}' does not exist in the folder '{folder_path}'.")


# %%

# Create a DataFrame
data = {'EpId': [1, 2, 3], 'Name': ['Episode 1', 'Episode 2', 'Episode 3']}
df_try = pd.DataFrame(data)

# Accessing the value using df['EpId'][key]
value = df_try['EpId'][1]
value2 =df_try.iloc[1]['EpId']
print(value)  # Output: 2
print(value2)
print(df_try)

# %% [markdown]
# Making folder structure as per types (SEP-28K)

# %%
# for ind in df.index:
#   # print(files)
#   folder_id=df['EpId'][ind] #folder
#   print(folder_id)
#   file_id=df['ClipId'][ind] #file
#   audio_type=df['Type'][ind]
#   print(file_id)
#   show_name=df['Show'][ind]
#   folder_path = Path(r'C:\Users\aaliy\OneDrive\Desktop\Speech Processing Lab IIITH\ml-stuttering-events-dataset\[CLIP_DIR]_sep28k\content\[CLIP_DIR]\{showname}\{folderid}'.format(showname=show_name,folderid=folder_id))
#   file_name="{showname}_{folderid}_{fileid}.wav".format(showname=show_name,folderid=folder_id, fileid=file_id)
#   file_path_dest = Path(r'C:\Users\aaliy\OneDrive\Desktop\Speech Processing Lab IIITH\ml-stuttering-events-dataset\Type_sep28k\{audiotype}\{filename}'.format(audiotype=audio_type,filename=file_name))
#   # file_name="FluencyBank_"+files['EpId']+"_"+files['ClipId']


#   file_path = folder_path / file_name

#   if file_path.is_file():
#     # File exists
#     with file_path.open('rb') as file:
#         # Read the contents of the file
#         contents = file.read()
#         # print(contents)# Save the content to the file
#         with file_path_dest.open('wb') as file_dest:
#           if file_path_dest.is_file():
#             print(f"File '{file_name}' already exist in the destination folder.")
#           else :
#             file_dest.write(contents)

#         print(f"File '{file_path}' has been saved.")
#   else:
#     # File does not exist
#     print(f"File '{file_name}' does not exist in the folder '{folder_path}'.")


# %%
for k in multi:
    print(k)
    print(df.iloc[k]['EpId'])
    print(multi[k])

# %% [markdown]
# Adding the remaining occurence to the folder structure as per types (SEP-28K)

# %%
# for key in multi:
#   # print(files)
#   folder_id=df['EpId'][key] #folder
#   print(folder_id)
#   file_id=df['ClipId'][key] #file
#   print(file_id)
#   for audio_type in multi[key]:
#     print(audio_type)
#     # print(file_id)
#     show_name=df['Show'][ind]
#     print(show_name)
#     folder_path = Path(r'C:\Users\aaliy\OneDrive\Desktop\Speech Processing Lab IIITH\ml-stuttering-events-dataset\[CLIP_DIR]_sep28k\content\[CLIP_DIR]\{showname}\{folderid}'.format(showname=show_name,folderid=folder_id))
#     file_name="{showname}_{folderid}_{fileid}.wav".format(showname=show_name,folderid=folder_id, fileid=file_id)
#     file_path_dest = Path(r'C:\Users\aaliy\OneDrive\Desktop\Speech Processing Lab IIITH\ml-stuttering-events-dataset\Type_sep28k\{audiotype}\{filename}'.format(audiotype=audio_type,filename=file_name))
#     # file_name="FluencyBank_"+files['EpId']+"_"+files['ClipId']


#     file_path = folder_path / file_name

#     if file_path.is_file():
#       # File exists
#       with file_path.open('rb') as file:
#         # Read the contents of the file
#         contents = file.read()
#         # print(contents)# Save the content to the file
#         with file_path_dest.open('wb') as file_dest:
#           if file_path_dest.is_file():
#             print(f"File '{file_name}' already exist in the destination folder.")
#           else :
#             file_dest.write(contents)
             
#         print(f"File '{file_path}' has been saved.")
#     else:
#     # File does not exist
#       print(f"File '{file_name}' does not exist in the folder '{folder_path}'.")




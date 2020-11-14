
#  Applicant tracking systems

import docx2txt


resume = docx2txt.process('myresume.docx')
resume


job_description = docx2txt.process("job_description.docx")
job_description


text = [resume, job_description]


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(text)


from sklearn.metrics.pairwise import cosine_similarity


# Print the Similarity scores
print ( "\n Similarity Scores: ")
print (cosine_similarity(count_matrix))



# get the match percentage
matchpercentage = cosine_similarity(count_matrix)[0][1]*100
matchpercentage = round (matchpercentage, 2)
print ("Your resume matches about " + str (matchpercentage) + "% of the job description")








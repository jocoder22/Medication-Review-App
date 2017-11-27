
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import MedCategory, Base, MedList, User

engine = create_engine("sqlite:///medication.db")
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won"t be persisted into the database until you call
# session.commit(). If you"re not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# add_entry will add new medication to the medication database
def add_entry(query):
    session.add(query)
    session.commit()

# Add the first user to the database
user1 = User(name="Okigbo Joshua", email="okigbookey@gmail.com",
             picture='/static/pharm1.jpg')
add_entry(user1)


# Add Antibacterial category
category1 = MedCategory(category="Antibacterial", user=user1)
add_entry(category1)

med1 = MedList(name="Cephalexin",
    description="Cephalexin is a first generation cephalosporin antibiotic that kills bacteria. it is use to treat many infections caused by bacteria in the body such as urinary and respiratory infections",
    adverseEffect="diarrhea, headaches, stomach pain, joint pain",
    pregnancyCategory="B",
    medcategory=category1,user=user1)
add_entry(med1)

med2 = MedList(name = "Cefazolin",
    description = "cefazolin is a first generation cephalosporin antibiotic that kills bacteria. it is use to prevent and treat many infections caused by bacteria in the body such as  bone and ear infections",
    adverseEffect = "nausea, diarrhea, dizziness, dark urine",
    pregnancyCategory = "B",
    medcategory = category1, user=user1)
add_entry(med2)

med3 = MedList(name = "Ampicillin",
    description = "Ampicillin is aminopenicillin that kills bacteria by inhibiting the formation of bacteria cell wall. it is use to prevent and treat many infections, such as skin, upper and lower respiratory infections, urinary tract infections caused by bacteria in the body",
    adverseEffect = "nausea, diarrhea, vomiting, skin rash",
    pregnancyCategory = "B",
    medcategory = category1, user=user1)
add_entry(med3)

med4 = MedList(name = "Amoxicillin ",
    description = "Amoxicillin is aminopenicillin that kills bacteria by inhibiting the synthesis of bacteria cell wall. it is use to treat many infections, such as pneumonia, bronchits, and tonsillitis caused by bacteria in the body",
    adverseEffect = "nausea, diarrhea, dizziness, black stool, stomach pains",
    pregnancyCategory = "B",
    medcategory = category1, user=user1 )
add_entry(med4)



category1 = MedCategory(category = "Antiviral", user=user1)
add_entry(category1)

med1 = MedList(name = "Ritonavir",
    description = "Ritonavir is a protease inhibitor synthetic antiviral medication that hinder the action of HIV-1 protease enzyme. Ritonavir is use to treat many infection caused HIV and AIDS",
    adverseEffect = "headaches, sweating, dizziness, constipation",
    pregnancyCategory = "C",
    medcategory = category1, user=user1)
add_entry(med1)

med2 = MedList(name = "Acyclovir",
    description = "Acyclovir is an antiviral medication that slow herpes viral growh in the body.  it is use to treat many infection caused by herpes viruses in the body  cold sores and genital herpes",
    adverseEffect = "stomach pains, tiredness, vomiting, nausea",
    pregnancyCategory = "B",
    medcategory = category1, user=user1)
add_entry(med2)

med3 = MedList(name = "Nevirapine",
    description = "Nevirapine is a Non-nucleoside reverse transcriptase inhibitor (NNRTI) that inhibit the HIV-1 reverse transcriptase enzyme.  it is use to treat many infection caused is use to treat many infection caused HIV and AIDS",
    adverseEffect = "diarrhea, dark urine, black stool, skin rash",
    pregnancyCategory = "B",
    medcategory = category1, user=user1)
add_entry(med3)



category1 = MedCategory(category = "Antipyschotics", user=user1)
add_entry(category1)
med1 = MedList(name = "Olanzapine",
    description = "Olanzapine is an atypical second generation antipyschotics used in the treatment and management of schizophrenia, bipolar disorder and depression. It is indicated for people who are resistant to first generation antipyschotics and those experiencing major side effects from use of first generation antipyschotics",
    adverseEffect = "slurred speech, restlessness, mask-like face, impaired vision",
    pregnancyCategory = "B",
    medcategory = category1, user=user1)
add_entry(med1)


med2 = MedList(name = "Clozapine",
    description = "Clozapine is an atypical antipyschotics used in the management of severe resistant schizophrenia with or without suicidal ideation",
    adverseEffect = "low white cell count, high sugar levels, irregular heart beats, confusion",
    pregnancyCategory = "B",
    medcategory = category1, user=user1)
add_entry(med2)


med5 = MedList(name = "Lithium",
    description = "Lithium is antipyschotics used in treatment of major depression disorder and manic episodes of bipolar disorder",
    adverseEffect = "confusion, frequent urination, restlessness, tremor, hypothyroidism, weight gain",
    pregnancyCategory = "None",
    medcategory = category1, user=user1)
add_entry(med5)


category1 = MedCategory(category = "Antihypertensives", user=user1)
add_entry(category1)
med1 = MedList(name = "Lisinopril",
    description = "Lisinopril is an angiotensin converting enzyme (ACE) inhibitor use in the treatment of heart failure, hypertension",
    adverseEffect = "dry cough, hypotension, dizziness, high potassium level",
    pregnancyCategory = "None",
    medcategory = category1, user=user1)
add_entry(med1)


med2 = MedList(name = "Spironolactone",
    description = "Spironolactone is an aldosterone receptor antagonists, works by blocking the effect of aldosterone on body organs such as  kidneys, sweat glands and colon. It is a potassium-sparing diuretic medication. Spironolactone is used in the treatment of hypertension, congestive heart failure, nephrotic syndrome and liver cirrhosis.",
    adverseEffect = "high potassium, nausea, vomiting, chest pain, muscle pain.",
    pregnancyCategory = "C",
    medcategory = category1, user=user1)
add_entry(med2)

med3 = MedList(name = "Nifedipine",
    description = "Nifedipine is a calcium channel blocker that blocks the entry of calcium into smooth muscle cell resulting in the relaxation of blood vessel and decrease in blood pressure",
    adverseEffect = "cough, headaches, muscle pains, dizziness",
    pregnancyCategory = "C",
    medcategory = category1, user=user1)
add_entry(med3)




category1 = MedCategory(category = "Antidiabetes", user=user1)
add_entry(category1)
med1 = MedList(name = "Insulin",
    description = "Insulin is the hormone that produce in the body in the normal state by is lacking in peopel with diabetes. Insulin is hormone replacement therapy in people with type 1 diabetes",
    adverseEffect = "hypoglycemia, blurred vision, confusion, convulsions, nausea, nightmares",
    pregnancyCategory = "B",
    medcategory = category1, user=user1)
add_entry(med1)

med2 = MedList(name = "Metformin",
    description = "Metformin is used in type 2 diabetes especially in overweight people becasue Metformin is not associted with increase or weight gain",
    adverseEffect = "nausea, diarrhea, stomach pains",
    pregnancyCategory = "B",
    medcategory = category1, user=user1)
add_entry(med2)

med3 = MedList(name = "Pioglitazone",
    description = "Pioglitazone is used in management of type 2 diabetes. Pioglitazone is used alone or combine with other medication in management of type 2 diabetes",
    adverseEffect = "bladder tumor, chest pains, weight gian",
    pregnancyCategory = "None",
    medcategory = category1, user=user1)
add_entry(med3)

med4 = MedList(name = "Pramlintide",
    description = "Pramlintide is an Amylin analog, a polypeptide hormone produced by the body. Pramlintide help the insulin in the body to control glucose metabolism",
    adverseEffect = "slurred speech, headaches, blurred vision, dizziness",
    pregnancyCategory = "C",
    medcategory = category1, user=user1)
add_entry(med4)



category1 = MedCategory(category = "Immunoactives", user=user1)
add_entry(category1)
med1 = MedList(name = "Pegfilgrastim",
    description = "Pegfilgrastim is a colony stimulating factor glycoprotein that enhance the  production of blood cells. Pegfilgrastim is used in the treatment of patient with suppression due to chemotherapy.",
    adverseEffect = "fever, sore throat, chest pain, cough",
    pregnancyCategory = "C",
    medcategory = category1, user=user1)
add_entry(med1)


med2 = MedList(name = "Aldesleukin",
    description = "Aldesleukin is an interleukin, a cytokine produced by cells such as lymphocytes, monocytes that performs regulatory functions in the immune systme. Aldesleukin is used in the treatment of kidney cancer and skin cancer",
    adverseEffect = "dizziness, nausea, vomiting, confusion, agitation",
    pregnancyCategory = "C",
    medcategory = category1, user=user1)
add_entry(med2)


med3 = MedList(name = "Interferon beta-1a",
    description = "Interferon beta-1a are produced by recombinant DNA technology. Interferon beta-1a works by activating cells in the immune system aiding destruction of invading pathogens in the body. It is used in the treatment of multiple sclerosis",
    adverseEffect = "necrosis at injection site, muscle pain, fever, headaches",
    pregnancyCategory = "C",
    medcategory = category1, user=user1)
add_entry(med3)






category1 = MedCategory(category = "Hormones", user=user1)
add_entry(category1)
med1 = MedList(name = "Dexamethasone",
    description = "Dexamethasone is a synthetic glucocorticoid hormone used for its antiinflammatory effects. Dexamethasone is used in treatment of ulcerative colitis, arthrits and lupus psoriasis",
    adverseEffect = "anxiety, aggressive behavior, dizziness, headaches, irritability, weight gain",
    pregnancyCategory = "C",
    medcategory = category1, user=user1)
add_entry(med1)


med2 = MedList(name = "Fludrocortisone",
    description = "Fludrocortisone is a mineralocorticoid hormone used for its salt and water regulatory effects. Fludrocortisone is used in the treatment of addison\"s disease",
    adverseEffect = "muscle weakness, sodium and water retention",
    pregnancyCategory = "C",
    medcategory = category1, user=user1)
add_entry(med2)

med3 = MedList(name = "Desmopressin",
    description = "Desmopressin is a synthetic antidiuretic hormone that acts on the kidneys to enhance reabsorption of water causing retention of water. Desmopressin is used in the treatment of diabetes insipidus, hemophilia and von willebrand disease",
    adverseEffect = "confusion, convulsions, dizziness, headaches, muscle pains",
    pregnancyCategory = "B",
    medcategory = category1, user=user1)
add_entry(med3)

med4 = MedList(name = "Somatropin",
    description = "Somatropin is a recombinant form of human growth hormone use in the treatment of growth deficiency.",
    adverseEffect = "bloody urine, confusion, changes in skin color",
    pregnancyCategory = "C",
    medcategory = category1, user=user1)
add_entry(med4)



print ("added medications to database!")


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_setup import MedCategory, Base, MedList

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



# Add Antibacterial category
category1 = MedCategory(category="Antibacterial")
add_entry(category1)

med1 = MedList(name="Cephalexin",
    description="Cephalexin is a first generation cephalosporin antibiotic that kills bacteria. it is use to treat many infections caused by bacteria in the body such as urinary and respiratory infections",
    adverseEffect="diarrhea, headaches, stomach pain, joint pain",
    pregnancyCategory="B",
    medcategory=category1)
add_entry(med1)

med2 = MedList(name = "Cefazolin",
    description = "cefazolin is a first generation cephalosporin antibiotic that kills bacteria. it is use to prevent and treat many infections caused by bacteria in the body such as  bone and ear infections",
    adverseEffect = "nausea, diarrhea, dizziness, dark urine",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med2)

med3 = MedList(name = "Ampicillin",
    description = "Ampicillin is aminopenicillin that kills bacteria by inhibiting the formation of bacteria cell wall. it is use to prevent and treat many infections, such as skin, upper and lower respiratory infections, urinary tract infections caused by bacteria in the body",
    adverseEffect = "nausea, diarrhea, vomiting, skin rash",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med3)

med4 = MedList(name = "Amoxicillin ",
    description = "Amoxicillin is aminopenicillin that kills bacteria by inhibiting the synthesis of bacteria cell wall. it is use to treat many infections, such as pneumonia, bronchits, and tonsillitis caused by bacteria in the body",
    adverseEffect = "nausea, diarrhea, dizziness, black stool, stomach pains",
    pregnancyCategory = "B",
    medcategory = category1 )
add_entry(med4)

med5 = MedList(name = "Tetracycline",
    description = "Tetracycline is an antibiotic that prevent bacteria growth by hindering protein synthesis by the bacteria. it is use to prevent and treat many infection caused by bacteria in the body such as  bone and ear infections",
    adverseEffect = "sensitivity to sunlight, nausea, vomiting, stomach pains",
    pregnancyCategory = "D",
    medcategory = category1)
add_entry(med5)

med6 = MedList(name = "Ciprofloxacin",
    description = "Ciprofloxacin is a synthetic antibiotic that kills bacteria by inhibiting enzymes that is very important for the bacteria multiple. it is use to prevent and treat many infections, such as anthrax and plague caused by bacteria in the body.",
    adverseEffect = "tearing or swelling of tendons, nausea, diarrhea, headaches, hearing loss",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med6)

med7 = MedList(name = "Erythromycin",
    description = "Erythromycin is an antibiotic that slow and prevent bacteria growth by hindering protein synthesis by the bacteria. it is use to prevent and treat many infection caused by bacteria in the body such as  bone and ear infections",
    adverseEffect = "nausea, diarrhea, chest pains, headaches",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med7)

med8 = MedList(name = "Vancomycin",
    description = "Vancomycin is a gylcopeptide antibiotics that kills bacteria by hindering the synthesis of bacteria cell wall.  it is use to treat many infection caused by resistant bacteria in the body such as  methicillin-resistant staphylococcus aureus (MRSA) infections",
    adverseEffect = "bloody urine, convulsions, muscle pains, nausea",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med8)




category1 = MedCategory(category = "Antiviral")
add_entry(category1)

med1 = MedList(name = "Ritonavir",
    description = "Ritonavir is a protease inhibitor synthetic antiviral medication that hinder the action of HIV-1 protease enzyme. Ritonavir is use to treat many infection caused HIV and AIDS",
    adverseEffect = "headaches, sweating, dizziness, constipation",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med1)

med2 = MedList(name = "Acyclovir",
    description = "Acyclovir is an antiviral medication that slow herpes viral growh in the body.  it is use to treat many infection caused by herpes viruses in the body  cold sores and genital herpes",
    adverseEffect = "stomach pains, tiredness, vomiting, nausea",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med2)

med3 = MedList(name = "Nevirapine",
    description = "Nevirapine is a Non-nucleoside reverse transcriptase inhibitor (NNRTI) that inhibit the HIV-1 reverse transcriptase enzyme.  it is use to treat many infection caused is use to treat many infection caused HIV and AIDS",
    adverseEffect = "diarrhea, dark urine, black stool, skin rash",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med3)




category1 = MedCategory(category = "Anthelmintics")
add_entry(category1)
med1 = MedList(name = "Mebendazole",
    description = "Mebendazole is used in treatment of many worm infections such as  pinworm infection, ascariasis, guinea worm infection ",
    adverseEffect = "convulsions, dark urine, nausea, vomiting, fever",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med1)


med2 = MedList(name = "Praziquantel",
    description = "Praziquantel is a medication that kills worm such as  roundworms and tapeworms in the body. It is used in treatment of schistosomiasis, tapeworm infection, cysticercosis and hydatid disease",
    adverseEffect = "stomach pains, nausea, joint pains, dizziness",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med2)

med3 = MedList(name = "Pyrantel",
    description = "Pyrantel is used in the treatment of worm infections such as  pinworm infection, ascariasis, hookworm infections",
    adverseEffect = "dizziness, nausea, headaches",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med3)




category1 = MedCategory(category = "Antimalaria")
add_entry(category1)
med1 = MedList(name = "Chloroquine",
    description = "Chloroquine is a quinolines antimalaria medication used in the prevention and treatment of malaria",
    adverseEffect = "blurred vision. chest pains, confusion, black stool",
    pregnancyCategory = "None",
    medcategory = category1)
add_entry(med1)

med2 = MedList(name = "Quinine",
    description = "Quinine is a quinolines antimalaria medication used in the treatment of  severe malaria or resistant malaria",
    adverseEffect = "ringing in the ear, blurred vision, headaches",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med2)

med3 = MedList(name = "Artesunate",
    description = "Artesunate is a artemisinin derivative antimalaria  mostly used in combination with other antimalaria in the treatment of severe and resistant malaria.",
    adverseEffect = "dizziness, low red and white blood counts",
    pregnancyCategory = "None",
    medcategory = category1)
add_entry(med3)

med4 = MedList(name = "Halofantrine",
    description = "Halofantrine is mostly used in treatment of severe and resistant malaria",
    adverseEffect = "vomiting, diarrhea, rash, stomach pains, headaches",
    pregnancyCategory = "None",
    medcategory = category1)
add_entry(med4)




category1 = MedCategory(category = "Antipyschotics")
add_entry(category1)
med1 = MedList(name = "Olanzapine",
    description = "Olanzapine is an atypical second generation antipyschotics used in the treatment and management of schizophrenia, bipolar disorder and depression. It is indicated for people who are resistant to first generation antipyschotics and those experiencing major side effects from use of first generation antipyschotics",
    adverseEffect = "slurred speech, restlessness, mask-like face, impaired vision",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med1)


med2 = MedList(name = "Clozapine",
    description = "Clozapine is an atypical antipyschotics used in the management of severe resistant schizophrenia with or without suicidal ideation",
    adverseEffect = "low white cell count, high sugar levels, irregular heart beats, confusion",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med2)

med3 = MedList(name = "Chlorpromazine",
    description = "Chlorpromazine is an typical first generation antipyschotics used in the treatment and management of schizophrenia and mania",
    adverseEffect = "parkinson\"s-like symptoms, restlessness, tardive dyskinesia, tremor, rigidity, dry mouth, amenorrhea, weight gain, dizziness",
    pregnancyCategory = "None",
    medcategory = category1)
add_entry(med3)

med4 = MedList(name = "Fluphenazine",
    description = "Fluphenazine is an typical first generation antipyschotics used in the treatment and management of schizophrenia",
    adverseEffect = "parkinson\"s-like symptoms, restlessness, tardive dyskinesia, tremor, rigidity, weight gain",
    pregnancyCategory = "None",
    medcategory = category1)
add_entry(med4)


med5 = MedList(name = "Lithium",
    description = "Lithium is antipyschotics used in treatment of major depression disorder and manic episodes of bipolar disorder",
    adverseEffect = "confusion, frequent urination, restlessness, tremor, hypothyroidism, weight gain",
    pregnancyCategory = "None",
    medcategory = category1)
add_entry(med5)


category1 = MedCategory(category = "Antihypertensives")
add_entry(category1)
med1 = MedList(name = "Lisinopril",
    description = "Lisinopril is an angiotensin converting enzyme (ACE) inhibitor use in the treatment of heart failure, hypertension",
    adverseEffect = "dry cough, hypotension, dizziness, high potassium level",
    pregnancyCategory = "None",
    medcategory = category1)
add_entry(med1)


med2 = MedList(name = "Spironolactone",
    description = "Spironolactone is an aldosterone receptor antagonists, works by blocking the effect of aldosterone on body organs such as  kidneys, sweat glands and colon. It is a potassium-sparing diuretic medication. Spironolactone is used in the treatment of hypertension, congestive heart failure, nephrotic syndrome and liver cirrhosis.",
    adverseEffect = "high potassium, nausea, vomiting, chest pain, muscle pain.",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med2)

med3 = MedList(name = "Nifedipine",
    description = "Nifedipine is a calcium channel blocker that blocks the entry of calcium into smooth muscle cell resulting in the relaxation of blood vessel and decrease in blood pressure",
    adverseEffect = "cough, headaches, muscle pains, dizziness",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med3)


category1 = MedCategory(category = "Antidiabetes")
add_entry(category1)
med1 = MedList(name = "Insulin",
    description = "Insulin is the hormone that produce in the body in the normal state by is lacking in peopel with diabetes. Insulin is hormone replacement therapy in people with type 1 diabetes",
    adverseEffect = "hypoglycemia, blurred vision, confusion, convulsions, nausea, nightmares",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med1)

med2 = MedList(name = "Metformin",
    description = "Metformin is used in type 2 diabetes especially in overweight people becasue Metformin is not associted with increase or weight gain",
    adverseEffect = "nausea, diarrhea, stomach pains",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med2)


med3 = MedList(name = "Pioglitazone",
    description = "Pioglitazone is used in management of type 2 diabetes. Pioglitazone is used alone or combine with other medication in management of type 2 diabetes",
    adverseEffect = "bladder tumor, chest pains, weight gian",
    pregnancyCategory = "None",
    medcategory = category1)
add_entry(med3)


med4 = MedList(name = "Pramlintide",
    description = "Pramlintide is an Amylin analog, a polypeptide hormone produced by the body. Pramlintide help the insulin in the body to control glucose metabolism",
    adverseEffect = "slurred speech, headaches, blurred vision, dizziness",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med4)




category1 = MedCategory(category = "Antineoplastics")
add_entry(category1)
med1 = MedList(name = "Cyclophosphamide",
    description = "Cyclophosphamide is an alkylating antineoplastics medication works by incorporating alkyl group to DNA protein, causing the DNA to break. This hinder the cell ability to replicate and grow. Cyclophosphamide is used in the treatment of cancers like leukemia, breast cancer, small cell lung cancer and multiple myeloma",
    adverseEffect = "vomiting, bladder bleeding, low white cell counts",
    pregnancyCategory = "D",
    medcategory = category1)
add_entry(med1)


med2 = MedList(name = "Chlorambucil",
    description = "Chlorambucil is an alkylating antineoplastics medication works by incorporating alkyl group to DNA protein, this hinder the cell ability to replicate and grow. Chlorambucil is used in the treatment of cancers like chronic lymphocytic leukemia, Hodgkin lymphoma, and non-Hodgkin lymphoma",
    adverseEffect = "infertility, chest pain, bone marrow suppression, black stool, painful urination",
    pregnancyCategory = "D",
    medcategory = category1)
add_entry(med2)


med3 = MedList(name = "Fluorouracil",
    description = "Fluorouracil is an antimetabolite and pyrimidine analog antineoplastics that works by preventing DNA synthesis by hindering the activities of thymidylate synthase. Fluorouracil is used in the treatment of breast cancer, pancreatic cancer, cervical cancer and colon cancer",
    adverseEffect = "low blood cell counts, diarrhea, sore mouth and lips",
    pregnancyCategory = "D",
    medcategory = category1)
add_entry(med3)


med4 = MedList(name = "Methotrexate",
    description = "Methotrexate is an antimetabolite antifolate antineoplastics that works by preventing DNA and RNA synthesis by hindering the activities of dihydrofolate reductase. Methotrexate is used in the treatment of lymphoma, lung cancer, breast cancer and leukemia",
    adverseEffect = "liver damanage, nausea, low white cell count, skin rashes",
    pregnancyCategory = "X",
    medcategory = category1)
add_entry(med4)


med5 = MedList(name = "Doxorubicin",
    description = "Doxorubicin is an Antineoplastics antibiotic by inhibiting DNA replication. Doxorubicin is used in treatment of lymphoma, breast cancer and bladder cancer",
    adverseEffect = "joint pains, back pains, fever, cough, irregular heat beats",
    pregnancyCategory = "D",
    medcategory = category1)
add_entry(med5)



category1 = MedCategory(category = "Cardioactives")
add_entry(category1)
med1 = MedList(name = "Nitroglycerin",
    description = "Nitroglycerin is a nitrate antianginal medication that causes relaxation of smooth muscle of blood vessels and opens the blood vessels for blood to flow easily. Nitroglycerin is used in the treatment of heart attack, heart failure and hypertension",
    adverseEffect = "low blood pressure, headaches, dizziness, redness of skin",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med1)


med2 = MedList(name = "Atenolol",
    description = "Atenolol is a beta-selective medication that blocks the stimulation of the beta-1 adrenergic sympathetic nervous system. This blockage of stimulation causes reduces heart rate, heart activities and systolic blood pressure. Atenolol is used in the treatment of angina and hypertension",
    adverseEffect = "blurred vision, confusion, dizziness, postural hypotension",
    pregnancyCategory = "D",
    medcategory = category1)
add_entry(med2)


med3 = MedList(name = "Amiodarone",
    description = "Amiodarone is a group III antiarrhythmic medication that blocks potassium channels in cell membrane. This action prolong the repolarization of the cell membrane help restoree the heart rhythm. Amiodarone is used in the treatment of ventricular tachycardia and ventricular fibrillation",
    adverseEffect = "nausea, vomiting, dizziness, insomnia",
    pregnancyCategory = "None",
    medcategory = category1)
add_entry(med3)


category1 = MedCategory(category = "Immunoactives")
add_entry(category1)
med1 = MedList(name = "Pegfilgrastim",
    description = "Pegfilgrastim is a colony stimulating factor glycoprotein that enhance the  production of blood cells. Pegfilgrastim is used in the treatment of patient with suppression due to chemotherapy.",
    adverseEffect = "fever, sore throat, chest pain, cough",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med1)


med2 = MedList(name = "Aldesleukin",
    description = "Aldesleukin is an interleukin, a cytokine produced by cells such as lymphocytes, monocytes that performs regulatory functions in the immune systme. Aldesleukin is used in the treatment of kidney cancer and skin cancer",
    adverseEffect = "dizziness, nausea, vomiting, confusion, agitation",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med2)


med3 = MedList(name = "Interferon beta-1a",
    description = "Interferon beta-1a are produced by recombinant DNA technology. Interferon beta-1a works by activating cells in the immune system aiding destruction of invading pathogens in the body. It is used in the treatment of multiple sclerosis",
    adverseEffect = "necrosis at injection site, muscle pain, fever, headaches",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med3)






category1 = MedCategory(category = "Hormones")
add_entry(category1)
med1 = MedList(name = "Dexamethasone",
    description = "Dexamethasone is a synthetic glucocorticoid hormone used for its antiinflammatory effects. Dexamethasone is used in treatment of ulcerative colitis, arthrits and lupus psoriasis",
    adverseEffect = "anxiety, aggressive behavior, dizziness, headaches, irritability, weight gain",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med1)


med2 = MedList(name = "Fludrocortisone",
    description = "Fludrocortisone is a mineralocorticoid hormone used for its salt and water regulatory effects. Fludrocortisone is used in the treatment of addison\"s disease",
    adverseEffect = "muscle weakness, sodium and water retention",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med2)

med3 = MedList(name = "Desmopressin",
    description = "Desmopressin is a synthetic antidiuretic hormone that acts on the kidneys to enhance reabsorption of water causing retention of water. Desmopressin is used in the treatment of diabetes insipidus, hemophilia and von willebrand disease",
    adverseEffect = "confusion, convulsions, dizziness, headaches, muscle pains",
    pregnancyCategory = "B",
    medcategory = category1)
add_entry(med3)

med4 = MedList(name = "Somatropin",
    description = "Somatropin is a recombinant form of human growth hormone use in the treatment of growth deficiency.",
    adverseEffect = "bloody urine, confusion, changes in skin color",
    pregnancyCategory = "C",
    medcategory = category1)
add_entry(med4)



print ("added medications to database without users!")

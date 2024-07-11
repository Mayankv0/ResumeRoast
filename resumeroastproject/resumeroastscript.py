import os
import PyPDF2
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key file
cred = credentials.Certificate("resume-roaster-55d49-firebase-adminsdk-4cexo-9fc4c84cd7.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Set up Gemini API key
genai.configure(api_key="AIzaSyB150f5rLA5guP325uGNJi5zNVVhqZZ8BA")


def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file"""
    try:
        with open(pdf_file, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None


def analyze_resume(resume_text, parameters):
    """Analyze the resume based on the provided parameters"""
    try:
        prompt = f"""
        You will be given a resume text and some parameters to analyze the resume.
        Based on these parameters, provide a detailed analysis of the resume, highlighting areas for improvement.

        Parameters to evaluate:
        1. Impact:
           - Evaluate the quantification of impact using metrics and numbers.
           - Check for repetition of action verbs and suggest avoiding them.
           - Identify weak action verbs and recommend their removal.

        2. Brevity:
           - Assess if the resume's word count is appropriate.
           - Evaluate the use of bullet points.
           - Determine if there are too many bullet points.
           - Check the length of bullet points and ensure they are not too lengthy.

        3. Style:
           - Identify any weak buzzwords or clichés.
           - Ensure the dates are formatted correctly.
           - Check if the contact and personal details are appropriately included.
           - Evaluate the overall readability of the resume.
           - Identify the use of personal pronouns and suggest their removal.
           - Look for passive voice and recommend replacing it with active voice.
           - Identify any inconsistencies in punctuation.

        4. Sections:
           - Ensure the resume includes essential sections such as Work Experience, Awards and Achievements, Projects, and Positions of Responsibility.
           - Check if the Education section is present and correctly formatted.
           - Verify that the Experience section is listed before the Education section.
           - Evaluate the Skills section for completeness and relevance.
           - Ensure there are no unnecessary or outdated sections in the resume.

        Resume text:
        {resume_text}
        """

        response = genai.GenerativeModel(
            model_name="gemini-1.5-flash"
        ).generate_content([prompt])
        return response.text
    except Exception as e:
        print(f"Error analyzing resume: {e}")
        return None


def roast_resume(analysis, resume_text):
    """Roast the resume based on the analysis"""
    try:
        prompt = f"""
        You have been given the analysis of a resume. Now, based on this analysis, roast the resume creatively. Use a funky, corny, edgy, and slightly offensive tone to point out areas that need improvement. Make the roast humorous and engaging to make the other person feel a bit embarrassed. Use the provided examples as inspiration.

        Analysis:
        {analysis}

        Resume text:
        {resume_text}

        Here are some examples of roasts:
                Here are some resumes and their roasts:
        resume of mayank verma:
        MAYANK VERMA
 +91 9650724783  2021uee0147@iitjammu.ac.in  in/mayankv0  Mayankv0  mayankv0.in
EDUCATION
Course Institute Year of Passing Result
B.Tech (EE) IIT Jammu Expected 2025 7.60 CGPA (Till 6th Semester)
12th Standard Blue Bells Model School 2021 93%
10th Standard Blue Bells Model School 2019 94.2%
SCHOLASTIC ACHIEVEMENTS
Secured 99.5 percentile in JEE Advanced (2021)
Attained 34th rank in DUET out of more than 40,000 appearing candidates (2021)
WORK EXPERIENCE
Knoldus Inc
Software Development Engineer Intern, AI-ML Team, Noida (Jun 2024 - Present)
Established scalable client-server connection for real-time sensor data acquisition through Raspberry Pi.
Developed and deployed a DNN-based ML model for sensor data using Vertex AI and joblib with 95% accuracy.
Researched multi-camera tracking with NVIDIA Metropolis, and explored EdgeX Foundry for IoT data management.
Multigraphics Group
Software Development Intern, Delhi (May 2023 - Jun 2023)
Created OMR Sheet gen/scanning app using Flutter, Dart, Python (OpenCV, PIL), and Firebase for data storage.
Slashed educational costs by 80% for 200+ teachers and 5000+ students through mobile-based OMR processing.
Used tech Stack: Flutter, Dart, Python (OpenCV, PIL)
PROJECTS
Self Driving Car Simulator 2.0 
Programmed a self-driving car using JavaScript and neural network technology which can be refined within 5 iterations.
Developed highly accurate DNNs from scratch for object detection, and obstacle avoidance, achieving 100% accuracy.
Virtual World Creator 2.1 
Utilized JavaScript to integrate lifelike 3D effects for road rendering and visualization.
Empowered users to interactively design and customize road layouts within the application, slashing sketch time by 90%.
Engineered procedural generation for rapid automatic creation of trees and houses, achieving a 70% speed improvement.
SketchWiz 1.0 
Developed SketchWiz, a web app utilizing KNN, ANNs, DNNs to recognize hand-drawn sketches in 0.2 seconds.
Optimized model accuracy by extracting features such as roundness and elongation, achieving a 93% recognition rate.
Employed JavaScript and Python to seamlessly integrate machine learning algorithms trained on 2200*8 drawings.
SKILLS
Programming Language C/C++, Python, Javascript, SQL
Web Development HTML, CSS, Tailwind, Bootstrap, Django, React Js
Machine Learning Scikit Learn, TensorFlow, Numpy, Pandas, Matplotlib, NLP
Miscellaneous Git, VS Code, Data Structures and Algorithms, Arduino
ADDITIONAL DETAILS
Awards
2nd runner up in, IRC-9 International, Moscow, Russia and 1st position in IRC-9 Nationals, Gurugram, Haryana.
Secured 4th position in Inter IIT held at IIT Bombay.
Coding Profile: Leetcode, Codeforces
Position of Responsibility
Team Lead in Inter IIT Tech meet (team of 10)
Class representative for four consecutive semesters.

here is the roast of the resume
Mayank Verma, your resume looks like it ended before it even started. do you have nothign to show uh uh(written this because resume is short)
you scored 99.5 percentile in JEE advanced, the toughest exam of India, still can't make it to IIT-Delhi ( written this because IIT-Delhi/Mumbai are the top IITs of the country)
you have only two achievements in your resume, seems like you are not much of an achiever right? (written this because ideally 4-5 achivment shoudl be there)
you have used big buzzwords in your resume, ATS will definately give you a high score, just that you will fall flat in interviews
you have impressive projects hope some of them work too(written because they are interactive projects)
your skill section looks like it is copied from TOP SKILLS IN THE COUNTRY BLOG (because these are very commmon)
you have good position of responsibility or should I say you didnt study and were only performing responsibilities

here is the content of another resume:
Chaitanya Arora
Roll no. | chaitanya21033@iiitd.ac.in
DOB:
Github
Education
Indraprastha Institute of Information Technology
B.Tech Honors (CSE) Minor in Entrepreneurship (2021 - present)
CGPA: 8.48
(Till 6th semester)
Mata Nand Kaur Public School, Delhi
CBSE, Standard 12 (2019-2021)
Percentage : 92.25%
Delhi Public School Maruti Kunj, Gurgaon
CBSE, Standard 10 (2017 - 2019)
Percentage : 94.8%
Technical Skills
Expertise Area: Competitive Programming | Object-Oriented Programming | Data Structures and Algorithms | Databases | Firebase | App Development | Computer Networks | Cryptography.
Programming
Languages:
C/C++ | Java | Python | Assembly | SQL
Tools and
Technologies:
Flask | Flutter | Dask | MySQL | NoSQL | OpenCV | Pickel | NumPy | gRPC | ZeroMQ
| RabbitM | Linux | Google Cloud | Windows | Arduino | Cuda | Android Studio
Technical Electives: Object-Oriented Programming(A+) | Foundations of Computer Security(A+) | Computer Organization(A-) | Operating Systems(A-) | Algorithm Design and Analysis(A-)
| Network Security (A-) | Computer Networks(A-) | Databases Management(B) | Distributed Systems Concepts and Designs(B)
Soft Skills: Result oriented | Continuous Improvement | Reading Documentation | Platform Agnostic | Data driven.
Work Experience
Human Computer Interaction, HCI (Research Intern) (Jan, 24 - Apr, 24)
• Conducted study on Large Language Models (LLMs), examining dataset of 4000+ student interactions with LLM Tools like ChatGPT, Gemini, Github Copilot in CSE530: DSCD course.
• Contributed to discussions on integrating LLMs in Computing Education.
• Paper Submitted in ICER’2024. Link to Paper Guide: Dr. Dhruv Kumar
Network and System Security Lab (Research Intern) (Jul, 23 - Present)
• Developed Traitor Tracing Protocol for video piracy using FFmpeg, Python, Digital Fingerprinting and OpenCV, achieving 96% efficiency in imperceptible user-information embedding.
• Deployed Modified Real Time Streaming Protocol on Google Cloud Platform for mimicking
real-world CDN. Guide: Dr. Sambuddho (HoD CSE) and Dr. A V Subramaniam
Multigraphics Group (Software Development Intern) (May, 23 - Jun, 23)
• Developed Mobile Application and Software for OMR Sheet generation and scanning using Flutter, Dart,
and Python (OpenCV, PIL). Integrated Firebase for data storage.
• Reduced costs for educational institutions by 80%, benefiting 200+ teachers and 5000+ students with
affordable mobile-based OMR processing. Tech Stack: Flutter, Dart, Python (OpenCV, PIL)
Projects
Modified Raft Consensus Algorithm for Geo-Distributed Databases (Mar, 2024 - Apr, 2024)
GitHub Project Link
• Optimized read latency by 30% while maintaining strong consistency in leader leases.
• Implemented gRPC for node-to-node communication and designed fault-tolerant architecture.
• Enhanced leader election, log replication, and node failure recovery. Deployed on Google Cloud Platform. Team Size: 3. Guide: Dr. Dhruv Kumar
Global Human Migration Patterns Analysis
GitHub Project Link (Jan, 2024 - Apr, 2024)
• Created application analyzing global human migration patterns, processing 100000+ data points.
• Utilized Information Retrieval techniques: Boolean Retrieval, Phrase Query Retrieval, Probabilistic Retrieval, BM25 to create RAG-Based Model.
• Integrated OpenAI API, improving query interpretation accuracy by 40%. Team Size: 5. Guide:
Dr. Rajiv Ratan Shah
25acres: Escrow Service
GitHub Project Link (Aug, 2023 - Nov, 2023)
• Innovated Real Estate Aggregator Platform, improved transaction security using 256-bit encryption.
• Implemented SSL, HTTPS, PKI, OTP, SQLite, Nginx, e-signature, reducing fraud incidents by 85%.
Team Size: 4. Guide: Prof. Arun Balaji Buduru
BidMyRide: Cab Booking (Jan, 2023 - Apr, 2023)
GitHub Project Link
• Collaborated MySQL database for cab booking service, optimizing for efficient data handling and concurrent transactions.
• Implemented SQL triggers and OLAP queries, along with transaction management protocols for
concurrency. Team Size: 2. Guide: Dr. Vikram Goel
Positions of Responsibility
Branch Representative, Placement Committee: Aided in conducting placement drives
for companies on campus, liaised between students and recruiters for successful placements.
(2024 – Present)
Student Mentor, Dean of Student Affairs: Mentored 5 students, improving academic
performance by average of 10% and helped achieve academic excellence.
(Oct 2023 – Present)
Event Management: Organized Blind Dating event at Odyssey’24, managed 800 participants and increased event satisfaction by 25%.
(Oct, 23 - Jan, 24)
Served as President and Vice-President of Discipline Council for DPS-DLF school,
promoted decorum and discipline amongst 2000 students.
(Apr, 17 - Mar, 19)
Awards and Achievements
Secured Global Rank 128 (AIR 20) amongst 30000 participants in Codeforces Round 952. Standings.
Secured Global Rank 131 out of 32000+ participants in Leetcode Weekly contest 405. Standings.
Maintained Rating of 2121 on Leetcode(Knight). ChaitanyaArora. Amongst Top 1.75% users globally.
Google Kickstart Round-A 2023: Achieved All India Rank (AIR) of 1655 amongst 10000 participants.
Codeforces Specialist: Maintained specialist rating on Codeforces with profile rating of 1507: Chaitanya30.
ICPC Mathura Contest: Secured rank of 550, showcasing algorithmic and programming proficiency in team.
Achieved highest Words-Per-Minute of 114 WPM on monkeytype.
National French Olympiad: Achieved 2nd Rank in 2018 and awarded laptop for outstanding performance.
Interests and Hobbies
• Playing Squash and Competitive Chess.
• Reading Books and Journals.
Declaration: The above information is correct to the best of my knowledge.
Chaitanya Arora
Date: July 07, 2024

here is the roast for it:

roast:
Chaitanya, get a life, having a high 8.48 CGPA and so many skills that can fill a newspaper.( Because a cgpa more than 8 is considered high also there are more than 15 skills which is a high number of skills)Can you even use these skills?(Having large number of skills makes it less likely to be an expert in one field ) Why do you need skills as fillers in such a lengthy resume?(The resume word count is very high and even then he's putting too many fillers). You must touch the grass sometimes. ( Because of the high number of work experience and projects as a fresher). Hey, do you know the meaning of expertise, every project of yours has a different tech stack.( Projects in the same tech stack would increase expertise in a particular skill).
What's wrong with your position of responsibilities, you mentored five students and their academic performance increases by only 10% if it was someone who was not organizing blind dates your students would have improved a lot more.( The duration of blind date and student mentor is clashing) you are a shame as ex president of the discipline council, bring some discipline in your life.(Because he is clashing all timelines)


go through the above examples carefully and meticulosly and then write the roast for the resume provided in the prompt

        Example 1:
        Oh no, chaitanyaarora30, it seems like you're stuck in the easies of LeetCode! With only 74 hard problems solved, I'm starting to think you're just hiding under the "Knight" badge, afraid to get your armor tarnished. Your 536 total problems solved is impressive, but what's with the 144 total active days? Are you really only using LeetCode during nap time? And don't even get me started on your 78-day streak - I'm pretty sure that's just because you're too scared to click "submit" and face the crushing disappointment of not solving another easy problem.

        Example 2:
        The illustrious Jeetaksh! A grand total of 161 hard problems solved? That's like me conquering a Snorlax on a lazy Sunday afternoon! And don't even get me started on the sheer mediocrity that is your 1881 total problems solved. You've had 191 active days, but I'm pretty sure that's just because you're trying to make up for lost time (aka being a beginner). And those badges? Congrats, you've mastered the art of showing up regularly! *cracks open a can of disappointment*

        Example 3:
        Suppose that a resume is too long then you can say that I thought you were writing a book about yourself.

        Example 4:
        If a resume is too short then you can say that the resume ended before even starting.

        Now, use similar creativity to roast the resume based on the provided analysis.
        """

        response = genai.GenerativeModel(
            model_name="gemini-1.5-flash"
        ).generate_content([prompt])
        return response.text
    except Exception as e:
        print(f"Error roasting resume: {e}")
        return None


def store_resume(resume_text, analysis, roasted_resume):
    try:
        doc_ref = db.collection("resumes").add(
            {"resume_text": resume_text, "analysis": analysis, "roast": roasted_resume}
        )
        # print(f"Resume stored with ID: {doc_ref.id}")
    except Exception as e:
        print(f"Error storing resume: {e}")


def main():
    # Path to the PDF file
    pdf_file = "resume.pdf"

    # Extract text from the PDF file
    resume_text = extract_text_from_pdf(pdf_file)
    if not resume_text:
        print("Failed to extract resume text.")
        return

    # Set up parameters for resume analysis
    parameters = """
    1. Impact:
       - Evaluate the quantification of impact using metrics and numbers.
       - Check for repetition of action verbs and suggest avoiding them.
       - Identify weak action verbs and recommend their removal.

    2. Brevity:
       - Assess if the resume's word count is appropriate.
       - Evaluate the use of bullet points.
       - Determine if there are too many bullet points.
       - Check the length of bullet points and ensure they are not too lengthy.

    3. Style:
       - Identify any weak buzzwords or clichés.
       - Ensure the dates are formatted correctly.
       - Check if the contact and personal details are appropriately included.
       - Evaluate the overall readability of the resume.
       - Identify the use of personal pronouns and suggest their removal.
       - Look for passive voice and recommend replacing it with active voice.
       - Identify any inconsistencies in punctuation.

    4. Sections:
       - Ensure the resume includes essential sections such as Work Experience, Awards and Achievements, Projects, and Positions of Responsibility.
       - Check if the Education section is present and correctly formatted.
       - Verify that the Experience section is listed before the Education section.
       - Evaluate the Skills section for completeness and relevance.
       - Ensure there are no unnecessary or outdated sections in the resume.
    """

    # Step 1: Analyze the resume
    analysis = analyze_resume(resume_text, parameters)
    if not analysis:
        print("Failed to analyze resume.")
        return

    # Step 2: Roast the resume based on the analysis
    roasted_resume = roast_resume(analysis, resume_text)
    if roasted_resume:
        print(roasted_resume)
    else:
        print("Failed to roast resume.")

    # Step 3: Store resume, analysis, and roast in Firebase
    store_resume(resume_text, analysis, roasted_resume)


if __name__ == "__main__":
    print("current working directory: ", os.getcwd())
    main()
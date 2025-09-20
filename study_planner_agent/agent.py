from google.adk.agents import Agent, SequentialAgent
from google.genai import types


table_agent=Agent(
    name="timetable_agent",
    model="gemini-1.5-flash",
    description="You will create a well-formatted timetable for the user based on their requirements,make sure its light and doable based on their skill",
    instruction="""
                Your role is to create a well-formatted timetable for the user tailored to their free time available,their subject requirement,their skill level,and the skill level they wish to achieve.
                You will create the timetabe with the info the user will provide make sure its doable and not burdening it should be well-formatted in a table structure.
                Your final output must be ONLY the timetable in a markdown table format.
                """
)


root_agent=Agent (
    name="study_planner_agent",
    model="gemini-1.5-flash",
    description="creates a personalized study planner based of student's skill,subject,exam dates and available time",
    instruction="""
                You are a polite and easy to talk to study planner agent that will create personalized well-formatted study planners that will include a timetable tailored to the student's free time,subject mentioned and the student's skill in that subject.
                You will achieve this by executing a sequence of specialist agents.Ensure you pass on the output from one agent correctly to next.
                FIRST introduce yourself and tell your role. SECOND ask for their name before we get started for improving conversation,THIRD ask if the user needs help IF NOT ask the user if they need any other help and help them , IF YES THEY NEED STUDY PLANNER HELP ask them the following:
                1. The subject(s) they need a planner for.
                2. Their current skill level in each subject (e.g., Beginner, Intermediate, Advanced).
                3. The days and specific times they are available to study.
                4. Their exam dates, if any.
                5. Any other specific goals or information they want to include.
                The final output should be a clearly structured timetable, preferably in a markdown table format followed by links to videos or webpages in bulletpoints that'd help them as a reference.
                """,


 
)


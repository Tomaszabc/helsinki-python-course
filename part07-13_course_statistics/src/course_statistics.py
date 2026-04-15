import urllib.request
import json

def retrieve_all():
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats/api/courses")
    course_data = json.loads(request.read())
    courses = []
    for course in course_data:
        if not course['enabled']:
            continue

        exercises = 0
        for exercise in course['exercises']:
            if exercise:
                exercises += exercise

        courses.append((course['fullName'], course['name'], course['year'], exercises))

    return courses

def retrieve_course(course_name: str):
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats/api/courses/{course_name}/stats")
    course_weeks = json.loads(request.read())
    students = 1
    exercises = 0
    hours = 0
    for no, week, in course_weeks.items():
        if week['students'] > students:
            students = week['students']
        hours += week['hour_total']
        exercises += week['exercise_total']

    return {
        "weeks": len(course_weeks),
        "students": students,
        "hours": hours,
        "hours_average": hours//students,
        "exercises": exercises,
        "exercises_average": exercises//students,
    }

# import urllib.request
# import json
# import ssl

# def retrieve_all():
#     context = ssl._create_unverified_context()
#     url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    
#     response = urllib.request.urlopen(url, context=context)
#     courses = json.load(response)
    
#     result = []
#     for course in courses:
#         if course.get("enabled", False):
#             full_name = course["fullName"]
#             name = course["name"]
#             year = course["year"]
#             exercises_sum = sum(course.get("exercises", []))
#             result.append((full_name, name, year, exercises_sum))
            
#     return result

# def retrieve_course(course_name: str):
#     context = ssl._create_unverified_context()
#     url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    
#     response = urllib.request.urlopen(url, context=context)
#     data = json.load(response)
    
#     # Zamieniamy na listę, żeby tester nie miał problemów z typem dict_values
#     weeks_data = list(data.values())
    
#     weeks = len(weeks_data)
#     students = max(week["students"] for week in weeks_data)
#     hours = sum(week["hour_total"] for week in weeks_data)
#     exercises = sum(week["exercise_total"] for week in weeks_data)
    
#     hours_average = hours // students
#     exercises_average = exercises // students

#     return {
#         "weeks": weeks,
#         "students": students,
#         "hours": hours,
#         "hours_average": hours_average,
#         "exercises": exercises,
#         "exercises_average": exercises_average
#     }

# if __name__ == "__main__":
#     print(retrieve_all())
#     print(retrieve_course("docker2019"))
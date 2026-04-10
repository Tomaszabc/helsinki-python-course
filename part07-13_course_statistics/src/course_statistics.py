import urllib.request
import json
import ssl


def retrieve_all():
    context = ssl._create_unverified_context()
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses", context=context)
    
    courses = json.loads(my_request.read())
    result = []
    for course in courses:
        if course.get("enabled", False):
            full_name = course["fullName"]
            name = course["name"]
            year = course["year"]
            exercises = sum(course.get("exercises", []))
            result.append((full_name, name, year, exercises))

    return result

def retrieve_course(course_name: str):
    context = ssl._create_unverified_context()
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    response = urllib.request.urlopen(url, context=context)
    weeks_data = json.loads(response.read())
    response.close()

    weeks = len(weeks_data)
    students = max(week["students"] for week in weeks_data)
    hours = sum(week["hour_total"] for week in weeks_data)
    exercises = sum(week["exercises"] for week in weeks_data)
    hours_average = hours // students
    exercises_average = exercises // students

      
    return {
        "weeks": weeks,
        "students": students,
        "hours": hours,
        "hours_average": hours_average,
        "exercises": exercises,
        "exercises_average": exercises_average
    }



if __name__ == "__main__":
    active_courses = retrieve_all()
    print(active_courses)

    course = retrieve_course("docker2019")
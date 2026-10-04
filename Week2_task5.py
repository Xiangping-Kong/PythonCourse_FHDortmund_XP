# Step1: Dictionary of Dortmund events, key:event name, value:event date
dortmund_events = {
    "DEW21 Museumsnacht (Night of Museums)": "19-09-2026",
    "Fassaden Mapping at Dortmunder U": "19-09-2026",
    "Jazz Duo at Brauerei-Museum": "19-09-2026",
    "Guided tour at German Football Museum": "19-09-2026",
    "KAMRAD Live Concert at Friedensplatz": "19-09-2026",
    "Dortmund Digital Week Opening": "15-09-2026",
    "Art Exhibition at Museum für Kunst": "27-09-2026"
}

target_date = "19-09-2026"

# Step2: Filter events running during Night of Museums
museums_night_events = []
for event_name, event_date in dortmund_events.items():
    if event_date == target_date:
        museums_night_events.append(event_name)

# Step3: Print result
print("Events running during the Night of Museums in Dortmund on 19th September 2026:")
for event in museums_night_events:
    print(f"- {event}")

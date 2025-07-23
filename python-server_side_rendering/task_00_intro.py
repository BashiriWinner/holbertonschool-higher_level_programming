import os

def generate_invitations(template, attendence):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template


        placeholders = ["name", "event_title", "event_date", "event_location"]
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))

        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing to {output_filename}: {str(e)}")

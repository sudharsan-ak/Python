# ---------------------------------------------------------------------
# Day 9 - Final Mixed Exercise: Conditionals
# Scenario: Python workshop check-in system
# 1. Create a variable called attendee_age and set it to 22
attendee_age = 22

# 2. If attendee_age is greater than or equal to 18, print "Adult attendee"
# Otherwise, print "Minor attendee"
if attendee_age >= 18:
    print("Adult attendee")
else:
    print("Minor attendee")

# 3. Create a variable called has_ticket and set it to True
has_ticket = True

# 4. If attendee_age is greater than or equal to 18 AND has_ticket is True,
# print "Entry approved"
# Otherwise, print "Entry not approved"
if attendee_age >= 18 and has_ticket:
    print("Entry approved")
else:
    print("Entry not approved")

# 5. Create a variable called ticket_type and set it to "vip"
ticket_type = "vip"

# 6. Use if / elif / else:
# If ticket_type is "standard", print "Standard access"
# If ticket_type is "vip", print "VIP access"
# If ticket_type is "speaker", print "Speaker access"
# Otherwise, print "Unknown ticket type"
if ticket_type == "standard":
    print("Standard access")
elif ticket_type == "vip":
    print("VIP access")
elif ticket_type == "speaker":
    print("Speaker access")
else:
    print("Unknown ticket type")

# 7. Ask the user to enter their workshop track
# Store it in workshop_track
# Use strip()
workshop_track = input("Please enter your workshop track: ").strip()

# 8. If workshop_track is empty, print "Workshop track is required"
# Otherwise, print "Workshop track saved"
if not workshop_track:
    print("Workshop track is required")
else:
    print("Workshop track saved")

# 9. Ask the user to enter their preferred language
# Store it in preferred_language
# Use strip()
preferred_language = input("Please enter your preferred language: ").strip()

# 10. If preferred_language is "Python" OR "JavaScript",
# print "Relevant language background"
# Otherwise, print "We will focus on Python basics"
if preferred_language in ["Python", "JavaScript"]:
    print("Relevant language background")
else:
    print("We will focus on Python basics")

# 11. Create a list called completed_topics with:
# "Dictionaries", "Conditionals"
completed_topics = ["Dictionaries", "Conditionals"]

# 12. If completed_topics has items, print "Learning progress found"
# Otherwise, print "No learning progress found"
if completed_topics:
    print("Learning progress found")
else:
    print("No learning progress found")

# 13. Create a dictionary called learner_profile with:
# "name" -> your name
# "current_day" -> 9
# "active" -> True
learner_profile = {
    "name": "Sudharsan",
    "current_day": 9,
    "active": True
}

# 14. If "current_day" exists in learner_profile AND current_day is greater than or equal to 9,
# print "Ready for Day 9 review"
# Otherwise, print "Not ready for Day 9 review"
if "current_day" in learner_profile and learner_profile["current_day"] >= 9:
    print("Ready for Day 9 review")
else:
    print("Not ready for Day 9 review")

# 15. Create a variable called mentor_available and set it to False
mentor_available = False

# 16. Write a nested conditional:
# If has_ticket is True:
#     If mentor_available is True, print "Mentor session confirmed"
#     Otherwise, print "Mentor session unavailable"
# Otherwise, print "Ticket required for mentor session"
if has_ticket:
    if mentor_available:
        print("Mentor session confirmed")
    else:
        print("Mentor session unavailable")
else:
    print("Ticket required for mentor session")

# 17. Create a short-hand conditional variable called final_status:
# "Checked in" if has_ticket is True and workshop_track has a value
# "Check-in incomplete" otherwise
final_status = "Checked in" if has_ticket and workshop_track else "Check-in incomplete"

# 18. Print final_status
print(f"Final status: {final_status}")
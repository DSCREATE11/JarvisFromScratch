import random

def build_huge_dataset(output_filename="training_data.py"):
    # --- Vocabulary Blocks ---
    rooms = ["living room", "bedroom", "kitchen", "office", "basement", "garage", "hallway", "dining room"]
    light_fixtures = ["light", "lamp", "leds", "bulb", "chandelier", "desk light"]
    fan_fixtures = ["fan", "ceiling fan", "cooler", "exhaust fan", "ac fan"]
    
    light_verbs_on = ["turn on", "switch on", "activate", "enable", "power up", "illuminate"]
    light_verbs_off = ["turn off", "switch off", "deactivate", "disable", "power down", "extinguish"]
    fan_verbs_on = ["turn on", "start", "crank up", "activate", "power up", "run"]
    fan_verbs_off = ["turn off", "stop", "shut down", "deactivate", "kill"]

    names = ["Alex", "Sam", "John", "Sarah", "Emily", "David", "Jessica", "Michael", "Boss", "Manager", "Professor"]
    subjects = ["project updates", "meeting notes", "weekly report", "urgent follow up", "schedule shift", "vacation request", "agenda", "invoice details"]
    times = ["at 2 pm", "tomorrow morning", "this Friday at 4", "next Monday", "at noon", "at 9 am tomorrow", "this afternoon"]
    events = ["synch meeting", "dentist appointment", "code review", "lunch catchup", "project presentation", "interview panel"]
    
    search_queries = ["distance to Mars", "how to cook pasta", "Python matrix multiplication", "weather forecast", "latest news updates", "stock market trends", "why is the sky blue"]

    dataset_lines = []

    # --- 1. LIGHTS GENERATION (~1200 lines) ---
    for v in light_verbs_on + light_verbs_off:
        label = 0
        for r in rooms:
            for f in light_fixtures:
                dataset_lines.append((f"{v} the {r} {f}", label))
                dataset_lines.append((f"please {v} the {r} {f}", label))
                dataset_lines.append((f"jarvis {v} the {f} in the {r}", label))

    # --- 2. FANS GENERATION (~1000 lines) ---
    for v in fan_verbs_on + fan_verbs_off:
        label = 1
        for r in rooms:
            for f in fan_fixtures:
                dataset_lines.append((f"{v} the {r} {f}", label))
                dataset_lines.append((f"can you {v} the {f} inside the {r}", label))
                dataset_lines.append((f"hey jarvis {v} the {r} {f} right now", label))

    # --- 3. GOOGLE_MAIL GENERATION (~1000 lines) ---
    mail_templates = [
        "send an email to {name} about {sub}",
        "draft a mail to {name} regarding {sub}",
        "write an email to {name} containing the {sub}",
        "compose a message to {name} covering {sub}",
        "shoot an email to {name} about the {sub}",
        "create a draft for {name} regarding {sub}"
    ]
    for t in mail_templates:
        for name in names:
            for sub in subjects:
                dataset_lines.append((t.format(name=name, sub=sub), 2))
                dataset_lines.append((f"please {t.format(name=name, sub=sub)}", 2))

    # --- 4. GOOGLE_CALENDAR GENERATION (~1000 lines) ---
    cal_templates = [
        "schedule a {event} {time}",
        "book a slot for {event} {time}",
        "add {event} to my calendar {time}",
        "set up a meeting for {event} {time}",
        "create a calendar event for {event} {time}"
    ]
    for t in cal_templates:
        for event in events:
            for time in times:
                dataset_lines.append((t.format(event=event, time=time), 3))
                dataset_lines.append((f"jarvis {t.format(event=event, time=time)}", 3))

    # --- 5. GOOGLE_SEARCH GENERATION (~500 lines) ---
    for q in search_queries:
        for prefix in ["google", "search for", "look up", "can you browse", "find information on", "check google for"]:
            dataset_lines.append((f"{prefix} {q}", 4))
            dataset_lines.append((f"please {prefix} {q}", 4))

    # --- 6. GENERIC GREET GENERATION (~400 lines) ---
    greets = ["hello", "hi", "hey jarvis", "good morning", "good afternoon", "yo", "greetings"]
    followups = ["how are you", "hope you are good", "are you awake", "let's do some work", "wake up"]
    for g in greets:
        dataset_lines.append((g, 5))
        for f in followups:
            dataset_lines.append((f"{g} {f}", 5))
            dataset_lines.append((f"hey {g} {f}", 5))

    # Shuffle to ensure target features are completely distributed during training epochs
    random.seed(42)
    random.shuffle(dataset_lines)

    # Cut off or padding check to make it exactly around 5000 lines
    dataset_lines = dataset_lines[:5100]

    # Write out into training_data.py structure
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("# Automatically generated large corpus dataset for Jarvis RNN\n\n")
        f.write("data = [\n")
        for text, label in dataset_lines:
            # Clean string symbols to prevent string syntax failures
            clean_text = text.replace("'", "").replace('"', "")
            f.write(f"    ('{clean_text}', {label}),\n")
        f.write("]\n")
        
    print(f"File '{output_filename}' generated successfully with {len(dataset_lines)} samples!")

if __name__ == "__main__":
    build_huge_dataset()

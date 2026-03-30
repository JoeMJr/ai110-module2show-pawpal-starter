import streamlit as st
import pawpal_system as pawpal

if "owner" not in st.session_state:
    st.session_state.owner = pawpal.Owner(name="Jordan")

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner = st.session_state.owner
owner_name = st.text_input("Owner name", value=owner.name)
if owner_name != owner.name:
    owner.name = owner_name

st.markdown("### Pets")
new_pet_name = st.text_input("New pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
if st.button("Add pet"):
    owner.add_pet(pawpal.Pet(name=new_pet_name.strip() or "Unnamed pet", species=species))
    st.success(f"Added pet {new_pet_name.strip() or 'Unnamed pet'} the {species}")

pets = owner.get_pets()
if pets:
    st.write("Current pets:")
    st.table([{"name": pet.name, "species": pet.species} for pet in pets])
else:
    st.info("No pets yet. Add one above.")

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

frequency = st.selectbox("Frequency", ["daily", "weekly", "once"], index=0)
selected_day = st.selectbox(
    "Scheduled day",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    index=0,
)
scheduled_time = st.text_input("Scheduled time", value="08:00")

pet_names = [pet.name for pet in owner.get_pets()]
if pet_names:
    selected_pet = st.selectbox("Pet", pet_names)
    if st.button("Add task"):
        new_task = pawpal.Task(
            title=task_title,
            description=f"{task_title} for {selected_pet}",
            duration_minutes=int(duration),
            priority=priority,
            frequency=frequency,
        )
        owner.add_task(new_task, pet_name=selected_pet)
        new_task.schedule(selected_day, scheduled_time)
        st.success(f"Added task '{task_title}' for {selected_pet} on {selected_day} at {scheduled_time}")
else:
    st.warning("Add a pet before adding tasks.")

all_tasks = owner.get_all_tasks()
if all_tasks:
    st.write("Current tasks:")
    st.table([
        {
            "title": task.title,
            "pet": task.pet.name if task.pet else "",
            "day": task.scheduled_day or "",
            "time": task.scheduled_time or "",
            "priority": task.priority,
        }
        for task in all_tasks
    ])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
schedule_day = st.selectbox(
    "Select day to view",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    index=0,
)

scheduler = pawpal.Scheduler(owner)
if st.button("Generate schedule"):
    daily_tasks = scheduler.get_daily_plan(schedule_day)
    if daily_tasks:
        st.write(f"Today's Schedule for {schedule_day}:")
        for task in daily_tasks:
            st.write(
                f"- {task.title} for {task.pet.name if task.pet else 'unknown pet'} "
                f"at {task.scheduled_time} ({task.duration_minutes} min, priority={task.priority})"
            )
    else:
        st.info(f"No tasks scheduled for {schedule_day}.")

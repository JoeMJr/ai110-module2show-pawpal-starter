from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    owner = Owner(name="Jordan")

    dog = Pet(name="Mochi", species="dog")
    cat = Pet(name="Luna", species="cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    task1 = Task(
        title="Morning walk",
        description="Walk the dog around the block.",
        duration_minutes=30,
        priority="high",
        frequency="daily",
        pet=dog,
    )
    task2 = Task(
        title="Feed dinner",
        description="Serve evening meal to the cat.",
        duration_minutes=10,
        priority="medium",
        frequency="daily",
        pet=cat,
    )
    task3 = Task(
        title="Brush fur",
        description="Brush pet fur to reduce shedding.",
        duration_minutes=15,
        priority="low",
        frequency="weekly",
        pet=dog,
    )

    owner.add_task(task1, pet_name="Mochi")
    owner.add_task(task2, pet_name="Luna")
    owner.add_task(task3, pet_name="Mochi")

    scheduler = Scheduler(owner=owner)
    task1.schedule(day="Monday", time="08:00")
    task2.schedule(day="Monday", time="18:30")
    task3.schedule(day="Monday", time="20:00")

    today = "Monday"
    todays_tasks = scheduler.get_daily_plan(today)

    print("Today's Schedule:")
    print(f"Owner: {owner.name}\n")

    for task in todays_tasks:
        pet_name = task.pet.name if task.pet else "Unknown pet"
        print(
            f"- {task.title}: {task.description} "
            f"for {pet_name} at {task.scheduled_time} "
            f"({task.duration_minutes} min, priority={task.priority})"
        )


if __name__ == "__main__":
    main()

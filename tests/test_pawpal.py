from pawpal_system import Pet, Task


def test_task_completion_marks_task_as_completed() -> None:
    pet = Pet(name="Mochi", species="dog")
    task = Task(
        title="Morning walk",
        description="Walk the dog around the block.",
        duration_minutes=30,
        priority="high",
        frequency="daily",
        pet=pet,
    )

    assert task.is_completed is False
    task.mark_completed()
    assert task.is_completed is True


def test_pet_add_task_increases_task_count() -> None:
    pet = Pet(name="Luna", species="cat")
    task = Task(
        title="Feed dinner",
        description="Serve evening meal to the cat.",
        duration_minutes=10,
        priority="medium",
        frequency="daily",
        pet=pet,
    )

    assert len(pet.tasks) == 0
    pet.add_task(task)
    assert len(pet.tasks) == 1
    assert pet.tasks[0] is task
    assert task.pet is pet

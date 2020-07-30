import experiment
import in_memory_store


def main():
    store = in_memory_store.InMemoryStore()
    user_id = 123
    is_perfectionist = True
    num_trial = 5
    problem_type = "anagram"

    exp = experiment.Experiment(user_id, is_perfectionist, num_trial, problem_type, store)
    exp.run()

    print(store.dump())


if __name__ == "__main__":
    main()

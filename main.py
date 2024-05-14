"""Call all functions to simulatete annual accounts process."""
# from classifications.classification import ClassificationsList
# from agregator.agregator import generate_dataset_from_entries, save_dataset


from json import loads
from tools.json_validator import validate
from path import Path

from classifications.classification import ClassificationsList


def main():
    """Run all steps needed for testing."""
    """Load all classifications needed."""
    # cls = ClassificationsList(do_update=True)
    # cls.update_classification_elements()

    """Generate from transactions file a dataset file."""
    # dataset = generate_dataset_from_entries(
    #     "annual_report/tests/entry/modified_entries_list.json", "11308014", "2023-01-01", "2023-12-31")
    # save_dataset(dataset)

    """Validate json file."""
    file_name = "annual_report/agregator/output/11308014-2024-05-13T14:14:07:726.json"
    schema = "annual_report/json_shemas/EE0301020_schema.json"

    if Path(file_name).exists():
        dataset = loads(Path(file_name).read_text())
    result = validate(dataset, schema)

    print(result)


if __name__ == "__main__":
    main()
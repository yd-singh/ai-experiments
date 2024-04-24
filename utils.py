import yaml
def load_config(filename):
    with open(filename, 'r') as file:
        config = yaml.safe_load(file)
    return config

def append_text_to_file(text, resarch_topic_task):
    with open("test.txt", 'a') as file:
        text = "Task: {resarch_topic_task}"
        text = text + '\n' + "Output: {resarch_topic_task}"
        file.write(text + '\n')
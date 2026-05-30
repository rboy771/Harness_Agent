import json
class logger:
    def __init__(self):
        self.entries = []
    def log_step(self, step, observation, action, result):
        self.entries.append({
            'step': step,
            'observation': observation,
            'action': action,
            'result': result
        })

    def save_json(self):
        with open('log.json', 'w') as f:
            json.dump(self.entries, f, indent=2)

    def save_html(self):
        with open('log.html', 'w') as f:
            f.write("<html><body>\n")
            for entry in self.entries:
                f.write(f"<h2>Step {entry['step']}</h2>\n")
                f.write(f"<p><strong>Observation:</strong> {entry['observation']}</p>\n")
                f.write(f"<p><strong>Action:</strong> {entry['action']}</p>\n")
                f.write(f"<p><strong>Result:</strong> {entry['result']}</p>\n")
            f.write("</body></html>\n")
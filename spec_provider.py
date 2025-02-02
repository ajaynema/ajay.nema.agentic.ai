import os
import yaml


class SpecProvider():
    def __init__(self, app_directory):
        self.spec_directory = app_directory+"/specs/"
        self.specs = dict()
        self.load_specs()

    def load_specs(self):
        file_list = os.listdir(self.spec_directory)
        for file_name in file_list:
            file_full_path = self.spec_directory + file_name
            f = open(file_full_path, 'r')
            try:
                spec = yaml.load(f, Loader=yaml.SafeLoader)
                spec_name = spec["name"]
                self.specs[spec_name] = spec
            except:
                print("Something wrong loading file " + file_full_path)
            finally:
                f.close()

    def get_spec(self, spec):
        return self.specs[spec]

    def dump_all(self):
        for spec in self.specs:
            self.dump(spec)

    def dump(self, spec):
        print(self.specs[spec])

    def test(self):
        print("========= Testing SpecProvider in spec_provider.py file ")
        self.dump_all();
        print("========= End Testing ============= ")




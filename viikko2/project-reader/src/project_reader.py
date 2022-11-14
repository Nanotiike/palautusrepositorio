from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_dict=toml.loads(content)

        p_name=toml_dict["tool"]["poetry"]["name"]
        p_description=toml_dict["tool"]["poetry"]["description"]
        p_dependencies=toml_dict["tool"]["poetry"]["dependencies"]
        p_dev_dependencies=toml_dict["tool"]["poetry"]["dev-dependencies"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(p_name, p_description, p_dependencies.keys(), p_dev_dependencies.keys())

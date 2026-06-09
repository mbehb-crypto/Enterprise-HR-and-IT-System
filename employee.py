from typing import Dict, Any, Optional, Set

class Employee:
    # __slots__ optimizes RAM and prevents the creation of __dict__ (dynamic attributes)
    __slots__ = ('_name', '_title')

    # Restrict roles based strictly on company departments
    DEPARTMENT_ROLES: Dict[str, Set[str]] = {
        'Cybersecurity': {'Security Analyst', 'Security Engineer', 'CISO'},
        'Engineering': {'Software Engineer', 'DevOps', 'Architect'},
        'HR': {'HR Manager', 'Recruiter'},
        'Operations': {'Logistics Manager', 'Supply Chain Associate'}
    }

    def __init__(self, name: str, title: str):
        self._name = name
        self.title = title  # Uses title setter for department validation

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        if not new_name or not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Name must be a valid, non-empty string.")
        self._name = new_name.strip()

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, new_title: str):
        valid_titles = {t for titles in self.DEPARTMENT_ROLES.values() for t in titles}
        if new_title not in valid_titles:
            raise ValueError(f"Invalid role '{new_title}'. Must match a valid company department.")
        self._title = new_title

    def to_dict(self) -> Dict[str, str]:
        """ Exports employee to a dictionary structure. """
        return {'name': self.name, 'title': self.title}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Employee':
        """ Pipeline factory method for dictionary or web payload initialization. """
        name = data.get('name', '')
        title = data.get('title', '')
        if not name or not title:
            raise ValueError("Payload missing 'name' or 'title' keys.")
        return cls(name=name, title=title)